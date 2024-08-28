# -*- coding: utf-8 -*-
"""
This module contains paths and constants used throughout the project.

- ROOT_PATH: The root directory of the project.
- FORECASTING_DATASET_PATH: The path to the dataset for forecasting.
- CONFIG_PATH: The configuration directory.
- THIRD_PARTY_PATH: The directory for third-party libraries.
"""

import os

# Get the root path where the code file is located
ROOT_PATH = os.path.abspath(os.path.join(__file__, "..", "..", ".."))

# Build the path to the dataset folder
FORECASTING_DATASET_PATH = os.path.join(ROOT_PATH, "dataset", "forecasting")

# Profile Path
CONFIG_PATH = os.path.join(ROOT_PATH, "config")

# third-party library path
THIRD_PARTY_PATH = os.path.join(ROOT_PATH, "ts_benchmark", "baselines", "third_party")
