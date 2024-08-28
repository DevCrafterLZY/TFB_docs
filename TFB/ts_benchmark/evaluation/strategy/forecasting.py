# -*- coding: utf-8 -*-
import abc
import traceback
from typing import Any, Optional

import pandas as pd
from sklearn.preprocessing import StandardScaler

from ts_benchmark.data.data_pool import DataPool
from ts_benchmark.evaluation.strategy.constants import FieldNames
from ts_benchmark.evaluation.strategy.strategy import Strategy
from ts_benchmark.models import ModelFactory
from ts_benchmark.utils.data_processing import split_before
from ts_benchmark.utils.random_utils import fix_random_seed


class ForecastingStrategy(Strategy, metaclass=abc.ABCMeta):
    """
    The base class for forecasting strategies
    """

    REQUIRED_CONFIGS = ["seed"]

    def execute(self, series_name: str, model_factory: ModelFactory) -> Any:
        """
        The primary interface to execute a forecasting strategy

        In this method:

        - Random seeds are set;
        - Target series and corresponding meta-info are prepared;
        - Exceptions are handled;

        :param series_name: The name of a series data to evaluate.
        :param model_factory: A model factory that creates a new model with each invocation.
        :return: The results generated by evaluating a model on a series.
        """
        fix_random_seed(self._get_scalar_config_value("seed", series_name))

        data_pool = DataPool().get_pool()
        data = data_pool.get_series(series_name)
        meta_info = data_pool.get_series_meta_info(series_name)

        try:
            single_series_results = self._execute(
                data, meta_info, model_factory, series_name
            )
        except Exception as e:
            log = f"{traceback.format_exc()}\n{e}"
            single_series_results = self.get_default_result(
                **{FieldNames.LOG_INFO: log}
            )

        return single_series_results

    @abc.abstractmethod
    def _execute(
        self,
        series: pd.DataFrame,
        meta_info: Optional[pd.Series],
        model_factory: ModelFactory,
        series_name: str,
    ) -> Any:
        """
        The execution pipeline of forecasting tasks

        Subclasses are expected to overwrite this method, instead of the :meth:`execute` method.

        :param series: Target series to evaluate.
        :param meta_info: The corresponding meta-info.
        :param model_factory: The factory to create models.
        :param series_name: the name of the target series.
        :return: The evaluation results.
        """

    def _get_eval_scaler(
        self, train_valid_data: pd.DataFrame, train_ratio_in_tv: float
    ) -> Any:
        """
        Gets the scaler used in normalized metrics

        Currently, the scaler is trained on the training series (without the validation data).

        NOTE that this scaler is used only in the metrics, which does not affect model
        training and inferencing.

        :param train_valid_data: The train-validation series.
        :param train_ratio_in_tv: The ratio of the training series when performing train-validation split.
        :return: A scaler object.
        """
        train_data, _ = split_before(
            train_valid_data,
            int(len(train_valid_data) * train_ratio_in_tv),
        )
        scaler = StandardScaler().fit(train_data.values)
        return scaler
