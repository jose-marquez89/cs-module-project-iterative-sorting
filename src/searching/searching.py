from pdb import set_trace as bp


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    if len(arr) < 1:
        return -1

    low = 0
    high = len(arr) - 1

    while low <= high:
        bp()
        middle = (high + low) // 2
        if arr[middle] == target:
            return middle
        else:
            if target > arr[middle]:
                low = middle + 1
            elif target < arr[middle]:
                high = middle - 1

    return -1
