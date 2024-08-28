# -*- coding: utf-8 -*-

import numpy as np

__all__ = ["mae", "mse", "rmse", "mape", "smape", "mase", 'wape', 'msmape', "mae_norm", "mse_norm", "rmse_norm", "mape_norm", "smape_norm", "mase_norm", 'wape_norm', 'msmape_norm']


def _error(actual: np.ndarray, predicted: np.ndarray, **kwargs):
    """ Simple error """
    return actual - predicted


def _percentage_error(actual: np.ndarray, predicted: np.ndarray, **kwargs):
    """ Percentage error """
    return (actual - predicted) / actual


def mse(actual: np.ndarray, predicted: np.ndarray, **kwargs):
    """ Mean Squared Error """
    return np.mean(np.square(_error(actual, predicted)))


def rmse(actual: np.ndarray, predicted: np.ndarray, **kwargs):
    """ Root Mean Squared Error """
    return np.sqrt(mse(actual, predicted))


def mae(actual: np.ndarray, predicted: np.ndarray, **kwargs):
    """ Mean Absolute Error """

    return np.mean(np.abs(_error(actual, predicted)))


def mase(
    actual: np.ndarray,
    predicted: np.ndarray,
    hist_data: np.ndarray,
    seasonality: int = 2,
    **kwargs
):
    """
    Mean Absolute Scaled Error
    Baseline (benchmark) is computed with naive forecasting (shifted by @seasonality)
    """
    if seasonality == 2:
        return -1
    scale = len(predicted) / (len(hist_data) - seasonality)

    dif = 0
    for i in range((seasonality + 1), len(hist_data)):
        dif = dif + abs(hist_data[i] - hist_data[i - seasonality])

    scale = scale * dif

    return (sum(abs(actual - predicted)) / scale)[0]


def mape(actual: np.ndarray, predicted: np.ndarray, **kwargs):
    """
    Mean Absolute Percentage Error

    Properties:
    + Easy to interpret
    + Scale independent
    - Biased, not symmetric
    - Undefined when actual[t] == 0
    """
    return np.mean(np.abs(_percentage_error(actual, predicted))) * 100


def smape(actual: np.ndarray, predicted: np.ndarray, **kwargs):
    """
    Symmetric Mean Absolute Percentage Error
    """
    return (
        np.mean(
            2.0 * np.abs(actual - predicted) / ((np.abs(actual) + np.abs(predicted)))
        )
        * 100
    )

def wape(actual: np.ndarray, predicted: np.ndarray, **kwargs):
    """Masked weighted absolute percentage error (WAPE)

    :param predicted: Predicted values.
    :param actual: Ground truth labels.
    :return: Masked mean absolute error.
    """
    loss = np.sum(np.abs(actual - predicted)) / np.sum(np.abs(actual)) * 100
    return loss

def msmape(actual: np.ndarray, predicted: np.ndarray, epsilon: float = 0.1, **kwargs):
    """
    Function to calculate series wise smape values

    :param actual: Array of actual values.
    :param predicted: Array of predicted values.
    :param epsilon: Small constant to avoid division by zero.
    :return: Mean symmetric mean absolute percentage error (MSMAPE) as a percentage.
    """

    comparator = np.full_like(actual, 0.5 + epsilon)
    denom = np.maximum(comparator, np.abs(predicted) + np.abs(actual) + epsilon)
    msmape_per_series = np.mean(2 * np.abs(predicted - actual) / denom) * 100
    return msmape_per_series


def _error_norm(actual: np.ndarray, predicted: np.ndarray, scaler: object,  **kwargs):
    """ Simple error """
    return scaler.transform(actual) - scaler.transform(predicted)


def _percentage_error_norm(actual: np.ndarray, predicted: np.ndarray, scaler: object, **kwargs):
    """ Percentage error """
    return (scaler.transform(actual) - scaler.transform(predicted)) / scaler.transform(actual)


def mse_norm(actual: np.ndarray, predicted: np.ndarray, scaler: object, **kwargs):
    """ Mean Squared Error """
    return np.mean(np.square(_error_norm(actual, predicted, scaler)))


def rmse_norm(actual: np.ndarray, predicted: np.ndarray, scaler: object, **kwargs):
    """ Root Mean Squared Error """
    return np.sqrt(mse_norm(actual, predicted, scaler))


def mae_norm(actual: np.ndarray, predicted: np.ndarray, scaler: object, **kwargs):
    """ Mean Absolute Error """

    return np.mean(np.abs(_error_norm(actual, predicted, scaler)))


def mase_norm(
    actual: np.ndarray,
    predicted: np.ndarray,
    scaler: object,
    hist_data: np.ndarray,
    seasonality: int = 2,
    **kwargs
):
    """
    Mean Absolute Scaled Error
    Baseline (benchmark) is computed with naive forecasting (shifted by @seasonality)
    """
    actual = scaler.transform(actual)
    predicted = scaler.transform(predicted)
    hist_data = scaler.transform(hist_data)
    if seasonality == 2:
        return -1
    scale = len(predicted) / (len(hist_data) - seasonality)

    dif = 0
    for i in range((seasonality + 1), len(hist_data)):
        dif = dif + abs(hist_data[i] - hist_data[i - seasonality])

    scale = scale * dif

    return (sum(abs(actual - predicted)) / scale)[0]


def mape_norm(actual: np.ndarray, predicted: np.ndarray, scaler: object, **kwargs):
    """
    Mean Absolute Percentage Error
    Properties:
    + Easy to interpret
    + Scale independent
    - Biased, not symmetric
    - Undefined when actual[t] == 0
    """
    return np.mean(np.abs(_percentage_error_norm(actual, predicted, scaler))) * 100


def smape_norm(actual: np.ndarray, predicted: np.ndarray, scaler: object, **kwargs):
    """
    Symmetric Mean Absolute Percentage Error
    """
    actual = scaler.transform(actual)
    predicted = scaler.transform(predicted)
    return (
        np.mean(
            2.0 * np.abs(actual - predicted) / ((np.abs(actual) + np.abs(predicted)))
        )
        * 100
    )

def wape_norm(actual: np.ndarray, predicted: np.ndarray, scaler: object, **kwargs):
    """
    Masked weighted absolute percentage error (WAPE)

    :param actual: Array of actual values.
    :param predicted: Array of predicted values.
    :param scaler: Object used to scale the actual and predicted values.
    :return: Weighted absolute percentage error (WAPE) as a percentage.
    """
    actual = scaler.transform(actual)
    predicted = scaler.transform(predicted)
    loss = np.sum(np.abs(actual - predicted)) / np.sum(np.abs(actual)) * 100
    return loss

def msmape_norm(actual: np.ndarray, predicted: np.ndarray, scaler: object, epsilon: float = 0.1, **kwargs):
    """
    Function to calculate series wise smape values

    :param actual: Array of actual values.
    :param predicted: Array of predicted values.
    :param scaler: Object used to scale the actual and predicted values.
    :param epsilon: Small constant to avoid division by zero.
    :return: Mean symmetric mean absolute percentage error (MSMAPE) as a percentage.
    """
    actual = scaler.transform(actual)
    predicted = scaler.transform(predicted)
    comparator = np.full_like(actual, 0.5 + epsilon)
    denom = np.maximum(comparator, np.abs(predicted) + np.abs(actual) + epsilon)
    msmape_per_series = np.mean(2 * np.abs(predicted - actual) / denom) * 100
    return msmape_per_series
