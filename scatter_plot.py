from itertools import combinations
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utility import find_mean, find_std, remove_nan
import seaborn as sns


def scatter_plot(df, f1, f2, corr_value):
    plt.figure(figsize=(8,6))
    plt.scatter(df[f1], df[f2], alpha=0.6)

    plt.title(f"Scatter Plot: {f1} vs {f2} (corr={corr_value:.2f})")
    plt.xlabel(f1)
    plt.ylabel(f2)
    plt.tight_layout()
    plt.show()


def align_arrays(x, y):
    aligned_x = []
    aligned_y = []
    for xi, yi in zip(x, y):
        if not (np.isnan(xi) or np.isnan(yi)):
            aligned_x.append(xi)
            aligned_y.append(yi)
    return aligned_x, aligned_y

def find_corr(x, y):

    # Align arrays to same length, drop NaN pairs
    x, y = align_arrays(x, y)

    # Clean data
    # x = remove_nan(x)
    # y = remove_nan(y)

    # Make sure same length
    if len(x) != len(y) or len(x) < 2 or len(y) < 2:
        return np.nan

    # Step 1: Find the mean of x, and the mean of y
    x_mean = find_mean(x)
    y_mean = find_mean(y)

    # Step 2: Subtract the mean of x from every x value
    sum = 0
    for x_1, y_1 in zip(x, y):
        sum += (x_1 - x_mean) * (y_1 - y_mean)
    
    covariance = sum / (len(x) - 1)

    # Step 3: Get STD for X and Y
    std_x = find_std(x)
    std_y = find_std(y)

    if std_x == 0 or std_y == 0 or np.isnan(std_x) or np.isnan(std_y):
        return float("NaN")

    # Person corelation
    return covariance / (std_x * std_y)


if __name__ == "__main__":

    df = pd.read_csv("dataset_train.csv")

    # Remove NaN values from all rows
    # df.fillna(0, inplace=True)

    numeric_cols = df.select_dtypes(include=[np.number])

    best_pair = None
    best_corr = 0.0 # smaller then any corr

    for c1, c2 in combinations(numeric_cols, 2):
        corr = find_corr(numeric_cols[c1].values, numeric_cols[c2].values)

        # corr2 = find_corr(numeric_cols[c1].values, numeric_cols[c2].values)

        print(f"my co: {corr}")

        aabs = abs(corr)
        # aabs2 = abs(corr2)

        if np.isnan(corr):
            continue

        if abs(corr) > abs(best_corr):
            best_corr = corr
            best_pair = (c1, c2)
    
    s1, s2 = best_pair
    print(f"the two similar options are: {s1} and {s2}, with Correlation of: {best_corr}")
    scatter_plot(df, s1, s2, best_corr)
