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

# Filter the numeric columns only
numeric_datas = df.select_dtypes(include=[np.number])

# Remove NaN values from all rows
# df.fillna(0, inplace=True)

# All the required values to Mimic Describe methode
ds_Names = []
ds_Counts = []
ds_Means = []
ds_Stds = []
ds_Mins = []
ds_25s = []
ds_50s = []
ds_75s = []
ds_Maxs = []

big_lens = []
# index = 0

    
# This will give you the name for all columns
for index, column_name in enumerate(numeric_datas):

    big_len = 0
    decimals = 6

    # If it's firt iteration
    if index == 0:
        decimals = 5


    ds_Names.append(column_name)

    if len(column_name) > big_len:
        big_len = len(column_name)
        if "-" in column_name:
            big_len -= 1

    ds_Counts.append(f"{count(df[column_name]):.{decimals}f}")

    if len(ds_Counts[index]) > big_len:
        big_len = len(ds_Counts[index])
        if "-" in ds_Counts[index]:
            big_len -= 1
    
    ds_Means.append(f"{find_mean(df[column_name].values):.{decimals}f}")

    if len(ds_Means[index]) > big_len:
        big_len = len(ds_Means[index])
        if "-" in ds_Means[index]:
            big_len -= 1

    ds_Stds.append(f"{find_std(df[column_name].values):.{decimals}f}")

    if len(ds_Stds[index]) > big_len:
        big_len = len(ds_Stds[index])
        if "-" in ds_Stds[index]:
            big_len -= 1

    ds_Mins.append(f"{find_min(df[column_name].values):.{decimals}f}")

    if len(ds_Mins[index]) > big_len:
        big_len = len(ds_Mins[index])
        if "-" in ds_Mins[index]:
            big_len -= 1

    ds_Maxs.append(f"{find_max(df[column_name].values):.{decimals}f}")

    if len(ds_Maxs[index]) > big_len:
        big_len = len(ds_Maxs[index])
        if "-" in ds_Maxs[index]:
            big_len -= 1

    ds_25s.append(f"{quantile(df[column_name], 0.25):.{decimals}f}")

    if len(ds_25s[index]) > big_len:
        big_len = len(ds_25s[index])
        if "-" in ds_25s[index]:
            big_len -= 1

    ds_50s.append(f"{quantile(df[column_name], 0.50):.{decimals}f}")

    if len(ds_50s[index]) > big_len:
        big_len = len(ds_50s[index])
        if "-" in ds_50s[index]:
            big_len -= 1

    ds_75s.append(f"{quantile(df[column_name], 0.75):.{decimals}f}")

    if len(ds_75s[index]) > big_len:
        big_len = len(ds_75s[index])
        if "-" in ds_75s[index]:
            big_len -= 1

    index += 1
    big_lens.append(big_len)

print('test')

# if "-" in data:
#     index -= 1


# for ds_name, ds_Count, ds_Mean, ds_Std, ds_Min, ds_25, ds_50, ds_75, ds_Max\
#     in ds_Names, ds_Counts, ds_Means, ds_Stds, ds_Mins, ds_25s, ds_50s, ds_75s, ds_Maxs:

line = ""

for ds_name, big_len in zip(ds_Names, big_lens):
    
    # Check if it's the first loop
    if ds_name == ds_Names[0]:
        space = big_len - len(ds_name) + 7
    else:
        space = big_len - len(ds_name) + 2

    line += " " * space + ds_name


line += "\ncount"
for ds_count, big_len in zip(ds_Counts, big_lens):
        
    space = big_len - len(ds_count) + 2

    line += " " * space + ds_count


line += "\nmean"
for ds_mean, big_len in zip(ds_Means, big_lens):

    if ds_mean == ds_Means[0]:
    # 5       9              7    
        space = big_len - len(ds_mean) + 3
    else:
        space = big_len - len(ds_mean) + 2

    line += " " * space + ds_mean


line += "\nstd"
for ds_std, big_len in zip(ds_Stds, big_lens):

    if ds_std == ds_Stds[0]:
    # 5       9              7    
        space = big_len - len(ds_std) + 4
    else:
        space = big_len - len(ds_std) + 2

    line += " " * space + ds_std


line += "\nmin"
for ds_min, big_len in zip(ds_Mins, big_lens):

    if ds_min == ds_Mins[0]:
    # 5       9              7    
        space = big_len - len(ds_min) + 4
    else:
        space = big_len - len(ds_min) + 2

    line += " " * space + ds_min


line += "\n25%"
for ds_25, big_len in zip(ds_25s, big_lens):

    if ds_25 == ds_25s[0]:
    # 5       9              7    
        space = big_len - len(ds_25) + 4
    else:
        space = big_len - len(ds_25) + 2

    line += " " * space + ds_25


line += "\n50%"
for ds_50, big_len in zip(ds_50s, big_lens):

    if ds_50 == ds_50s[0]:
    # 5       9              7    
        space = big_len - len(ds_50) + 4
    else:
        space = big_len - len(ds_50) + 2

    line += " " * space + ds_50


line += "\n25%"
for ds_75, big_len in zip(ds_75s, big_lens):

    if ds_75 == ds_75s[0]:
    # 5       9              7    
        space = big_len - len(ds_75) + 4
    else:
        space = big_len - len(ds_75) + 2

    line += " " * space + ds_75


line += "\nmax"
for ds_max, big_len in zip(ds_Maxs, big_lens):

    if ds_max == ds_Maxs[0]:
    # 5       9              7    
        space = big_len - len(ds_max) + 4
    else:
        space = big_len - len(ds_max) + 2

    line += " " * space + ds_max


print(line)
