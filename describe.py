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
index = 0

    
# This will give you the name for all columns
for column_name in numeric_datas:

    big_len = 0


    ds_Names.append(column_name)

    if len(column_name) > big_len:
        big_len = len(column_name)
        if "-" in column_name:
            big_len -= 1

    ds_Counts.append(f"{count(df[column_name]):.6f}")

    if len(ds_Counts[index]) > big_len:
        big_len = len(ds_Counts[index])
        if "-" in ds_Counts[index]:
            big_len -= 1
    
    ds_Means.append(f"{find_mean(df[column_name].values):.6f}")

    if len(ds_Means[index]) > big_len:
        big_len = len(ds_Means[index])
        if "-" in ds_Means[index]:
            big_len -= 1

    ds_Stds.append(f"{find_std(df[column_name].values):.6f}")

    if len(ds_Stds[index]) > big_len:
        big_len = len(ds_Stds[index])
        if "-" in ds_Stds[index]:
            big_len -= 1

    ds_Mins.append(f"{find_min(df[column_name].values):.6f}")

    if len(ds_Mins[index]) > big_len:
        big_len = len(ds_Mins[index])
        if "-" in ds_Mins[index]:
            big_len -= 1

    ds_Maxs.append(f"{find_max(df[column_name].values):.6f}")

    if len(ds_Maxs[index]) > big_len:
        big_len = len(ds_Maxs[index])
        if "-" in ds_Maxs[index]:
            big_len -= 1

    ds_25s.append(f"{quantile(df[column_name], 0.25):.6f}")

    if len(ds_25s[index]) > big_len:
        big_len = len(ds_25s[index])
        if "-" in ds_25s[index]:
            big_len -= 1

    ds_50s.append(f"{quantile(df[column_name], 0.50):.6f}")

    if len(ds_50s[index]) > big_len:
        big_len = len(ds_50s[index])
        if "-" in ds_50s[index]:
            big_len -= 1

    ds_75s.append(f"{quantile(df[column_name], 0.75):.6f}")

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
        space = big_len - len(ds_name) + 6
    elif "-" in ds_name:
        space = big_len - len(ds_name) + 1
    else:
        space = big_len - len(ds_name) + 2

    line += " " * space + ds_name

print(line)

#     if ds
# for i in range(len(ds_Names)):
#     big_len = 0

#     if len(ds_Names[i]) > big_len:
#         big_len = ds_Names[i]
#     if len(ds_Counts[i]) > big_len:
#         big_len = ds_Counts[i]
#     if len(ds_Means[i]) > big_len:
#         big_len = ds_Means[i]
#     if len(ds_Stds[i]) > big_len:
#         big_len = ds_Stds[i]
#     if len(ds_Mins[i]) > big_len:
#         big_len = ds_Mins[i]
#     if len(ds_25s[i]) > big_len:
#         big_len = ds_25s[i]
#     if len(ds_50s[i]) > big_len:
#         big_len = ds_50s[i]
#     if len(ds_75s[i]) > big_len:
#         big_len = ds_75s[i]
#     if len(ds_Maxs[i]) > big_len:
#         big_len = ds_Maxs[i]
    
#     # if i is not 0:
#     print(" " * 7)



# for i in 
#     # Print first row
#     print("" * 7)

#           Index    Arithmancy   Astronomy  Herbology  Defense Agai
# count  6.000000      6.000000    6.000000   6.000000      5.000000
# mean   2.500000  43893.166667 -147.531976  -1.857047      2.643934
# std    1.870829  20336.363661  565.765109   6.773587      5.456081
# min    0.000000  21209.000000 -613.687160  -7.820623     -6.977428
# 25%    1.250000  25943.250000 -536.016902  -6.369772      3.660761
# 50%    2.500000  45525.500000 -426.981101  -5.138321      4.878861
# 75%    3.750000  59714.500000  236.062373   3.223086      5.520605
# max    5.000000  67239.000000  697.742809   7.725017      6.136872