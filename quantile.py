import numpy as np

def quantile(data, q):
    
    # Step 1: Get n Len
    n = len(data)

    # Step 2: find position with formula  pos = (n − 1) × q
    pos = (n - 1) * q

    # Step 3: Get lower and upper ex: 1,25 == L = 1, U = 2
    lower = int(np.floor(pos))
    upper = int(np.ceil(pos))

    # This give you the decimal for our ex is 0,25
    fraction = pos - lower   # the "decimal part"

    if lower == upper: # Mean that there is no fraction
        # exact position → just return that value
        return data[int(pos)]
    else:
        # interpolate between data[lower] and data[upper]
        return data[lower] + fraction * (data[upper] - data[lower])
