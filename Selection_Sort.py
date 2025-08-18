
def Selection_Sort(array):
    n = len(array)

    for i in range(n):
        # Take fist element Assuming It’s the samllest
        small_ele = i
        for j in range(i + 1, n):
            if array[j] < array[small_ele]:
                small_ele = j
        array[i], array[small_ele] = array[small_ele], array[i]
    
    return array
