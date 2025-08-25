import numpy as np
from pandas import DataFrame
from Selection_Sort import Selection_Sort
from utility import count, remove_nan
from numba import njit


@njit
def quantile(data: np.ndarray, q):

    # Sort the element and make a copy from the original FataFrame
    sorted_ele = Selection_Sort(data.copy())

    # Remove the nan from the column
    clean_data = remove_nan(sorted_ele)
    
    # Get clean count
    n = count(clean_data)

    # Find position with formula  pos = (n − 1) × q
    pos = (n - 1) * q

    # Get lower and upper for ex: 1,25 == L = 1, U = 2
    lower = int(np.floor(pos))
    upper = int(np.ceil(pos))

    # This give you the decimal for our ex is 0,25
    fraction = pos - lower   # the "decimal part"

    if lower == upper: # Mean that there is no fraction
        # exact position → just return that value
        return clean_data[int(pos)]
    else:
        # interpolate between clean_data[lower] and clean_data[upper]
        return clean_data[lower] + fraction * (clean_data[upper] - clean_data[lower])
