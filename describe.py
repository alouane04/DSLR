import pandas as pd
import sys
import numpy as np
import cmath

# if len(sys.argv) > 1:
#     fileName = sys.argv[1]
# else:
#     print("Error: No csv fileName was given")

# # Load up the csv
# df = pd.read_csv(fileName)
df = pd.read_csv("dataset_train2.csv")
print(df.describe())

# Remove NaN values from all rows
df.fillna(0, inplace=True)

# All the required values to Mimic Describe methode
ds_Count = []
ds_Mean = 0
ds_Std = 0
ds_Min = 0
ds_25 = 0
ds_50 = 0
ds_75 = 0
ds_Max = 0


# Filter the numeric columns only
numeric_data = df.select_dtypes(include=[np.number])


# This will give you the count for all columns
for column_name in numeric_data:
    print(column_name)
    print('count: ', float(df[column_name].size))
    
    find_mean = 0
    for value in df[column_name].values:
        find_mean += value

    ds_Mean = find_mean / df[column_name].size
    print('mean is: ', f"{ds_Mean:.6f}")
    
    # or just use this but you know
    # print('mean is: ', f"{df[column_name].mean():.6f}")

    sum_variance = 0
    for value in df[column_name].values:

        # Subtract the mean from the value
        find_std = value - ds_Mean

        # Square it
        Square_std = find_std * find_std

        # Sum it to average it in the next step
        sum_variance += Square_std
    
    # Average the squared deviations (variance)
    variance = sum_variance / (df[column_name].size - 1)

    # Square root it to get out STD final value
    ds_Std =variance ** 0.5

    print('STD: ', f"{ds_Std:.6f}")

    ds_Min = df[column_name].values.min()

    print("Min: ", f"{ds_Min:.6f}")

    ds_Max = df[column_name].values.max()

    print("Max: ", f"{ds_Max:.6f}")

