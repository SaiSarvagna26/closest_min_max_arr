def smallest_subarray_size(arr):
    maximum = max(arr)
    minimum = min(arr)
    left = None
    right = None
    min_length = float('inf')

    for i in range(len(arr)):
        if arr[i] == maximum:
            left = i
        if arr[i] == minimum:
            right = i
        if left is not None and right is not None:
            length = right - left + 1
            min_length = min(min_length, length)

    return min_length

