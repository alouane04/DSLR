import pandas as pd
import sys
import numpy as np
import cmath
from Selection_Sort import Selection_Sort
from quantile import quantile

# if len(sys.argv) > 1:
#     fileName = sys.argv[1]
# else:
#     print("Error: No csv fileName was given")

# # Load up the csv
# df = pd.read_csv(fileName)
df = pd.read_csv("dataset_train.csv")
print(df.describe())

# Remove NaN values from all rows
df.fillna(0, inplace=True)

# All the required values to Mimic Describe methode
ds_Names = []
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


# This will give you the name for all columns
for column_name in numeric_data:
    print(column_name)

    ds_Names.append(column_name)

    ds_Count.append(df[column_name].size)

    print('Index: ', f"{df[column_name].size:.6f}")
    
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

    # ds_Min = df[column_name].values.min()

    # Init the first one with fist value
    ds_Min = df[column_name].values[0]
    ds_Max = df[column_name].values[0]

    # Search for Min and Max values
    for value in df[column_name].values:
        if value < ds_Min:
            ds_Min = value
        elif value > ds_Max:
            ds_Max = value

    print("Min: ", f"{ds_Min:.6f}")

    print("Max: ", f"{ds_Max:.6f}")

    # Sort a copy of our array values
    sorted_ele = np.array(Selection_Sort(df[column_name].values.copy()))

    ds_25 = quantile(sorted_ele, 0.25)
    ds_50 = quantile(sorted_ele, 0.50)
    ds_75 = quantile(sorted_ele, 0.75)

    print("25%", f"{ds_25:.6f}")
    print("50%", f"{ds_50:.6f}")
    print("75%", f"{ds_75:.6f}")
