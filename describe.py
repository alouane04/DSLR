import pandas as pd
import sys
import numpy as np
import cmath
from Selection_Sort import Selection_Sort
from quantile import quantile
from utility import find_mean, find_std, count, find_min, find_max


# if len(sys.argv) > 1:
#     fileName = sys.argv[1]
# else:
#     print("Error: No csv fileName was given")

# # Load up the csv
# df = pd.read_csv(fileName)
df = pd.read_csv("dataset_train2.csv")
print(df.describe())

# Remove NaN values from all rows
# df.fillna(0, inplace=True)

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
    # print(column_name)

    ds_Names.append(column_name)

    ds_Count.append(count(df[column_name]))

    # print(ds_Names)
    # print(ds_Count)







    print('Index: ', f"{count(df[column_name]):.6f}")
    
    ds_Mean = find_mean(df[column_name].values)

    print('mean is: ', f"{ds_Mean:.6f}")

    ds_Std = find_std(df[column_name].values)

    print('STD: ', f"{ds_Std:.6f}")

    ds_Min = find_min(df[column_name].values)

    print("Min: ", f"{ds_Min:.6f}")

    ds_Max = find_max(df[column_name].values)

    print("Max: ", f"{ds_Max:.6f}")



    ds_25 = quantile(df[column_name], 0.25)
    ds_50 = quantile(df[column_name], 0.50)
    ds_75 = quantile(df[column_name], 0.75)

    print("25%", f"{ds_25:.6f}")
    print("50%", f"{ds_50:.6f}")
    print("75%", f"{ds_75:.6f}")
