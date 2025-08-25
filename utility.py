import pandas as pd
from numba import njit
import numpy as np


@njit
def remove_nan(values):
    clean_data = []

    for value in values:
        if not np.isnan(value):
            clean_data.append(value)
    
    return clean_data


@njit
def count(values):
    n = 0

    for value in values:
        if not np.isnan(value):
            n += 1

    return n


@njit
def find_mean(values):
    total = 0
    n = 0

    for value in values:
        if not np.isnan(value):
            total += value
            n += 1

    return total / n if n > 0 else float("NaN")


@njit
def find_std(values):

    mean = find_mean(values)
    total = 0
    n = 0

    for value in values:

        if not np.isnan(value):

            # Subtract the mean from the value
            find_std = value - mean

            # Square it
            Square_std = find_std * find_std

            # Sum it to average it in the next step
            total += Square_std

            n += 1
    
    if n > 1:
        # Average the squared deviations (variance)
        variance = total / (n - 1)
    else:
        return float("NaN")

    # Square root it to get out STD final value
    return variance ** 0.5 if n > 1 else float("NaN")


@njit
def find_min(values):
    
    if len(values) == 0:
        return float("NaN")

    ds_min = values[0]

    for value in values:
        if not np.isnan(value):
            if value < ds_min:
                ds_min = value
    
    return ds_min


@njit
def find_max(values):
    
    if len(values) == 0:
        return float("NaN")

    ds_max = values[0]

    for value in values:
        if not np.isnan(value):
            if value > ds_max:
                ds_max = value
    
    return ds_max
