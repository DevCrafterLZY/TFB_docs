# -*- coding: utf-8 -*-
from typing import List

from statsmodels.tsa.stattools import acf
from scipy.signal import argrelextrema
import numpy as np


def find_length(data: np.ndarray) -> int:
    """
    Automatically calculate the appropriate period length for time series data.

    :param data: Time series data.
    :return: The automatically calculated period length.
    """
    if len(data.shape) > 1:
        return 0

    # 取前 20000 个数据点进行计算
    data = data[: min(20000, len(data))]

    base = 3
    auto_corr = acf(data, nlags=400, fft=True)[base:]

    local_max = argrelextrema(auto_corr, np.greater)[0]
    try:
        max_local_max = np.argmax([auto_corr[lcm] for lcm in local_max])
        if local_max[max_local_max] < 3 or local_max[max_local_max] > 300:
            return 125
        return local_max[max_local_max] + base
    except:
        return 125


def get_list_anomaly(labels: np.ndarray) -> List[int]:
    """
    Get a list of anomaly interval lengths from time series labels.

    :param labels: A list of time series labels, where 1 indicates anomaly and 0 indicates normal.
    :return: A list of anomaly interval lengths.
    """
    # results = []
    # start = 0
    # anom = False
    # for i, val in enumerate(labels):
    #     if val == 1:
    #         anom = True
    #     else:
    #         if anom:
    #             results.append(i - start)
    #             anom = False
    #     if not anom:
    #         start = i
    # return results

    end_pos = np.diff(np.array(labels, dtype=int), append=0) < 0
    return np.diff(np.cumsum(labels)[end_pos], prepend=0)

