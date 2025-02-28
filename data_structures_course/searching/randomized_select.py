# Randomized select is an algoritm for finding the kth smallest element (order statistics) in an array. It is absed on the quickselect algo, which is a modification of quicksort, but instrad of sorting the entire array, it selects a pivot and only recurses into one partition (the part that contains the desired element), allowing it to run in O(n).

import random

def randomized_select(arr, low, high, i):
    """
    Randomized Select algorithm to find the i-th smallest element in arr[low..high].
    """
    if low == high:
        return arr[low]

    # Partition the array around a random pivot
    pivot_index = randomized_partition(arr, low, high)
    
    # Number of elements in the left partition
    k = pivot_index - low + 1

    if i == k:  # The pivot element is the i-th smallest
        return arr[pivot_index]
    elif i < k:  # Look for the i-th smallest in the left partition
        return randomized_select(arr, low, pivot_index - 1, i)
    else:  # Look for the (i-k)-th smallest in the right partition
        return randomized_select(arr, pivot_index + 1, high, i - k)

def randomized_partition(arr, low, high):
    """
    Utility function to partition the array using a randomly chosen pivot.
    """
    # Choose a random pivot index between low and high
    pivot_index = random.randint(low, high)
    # Swap pivot with the last element
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    # Standard partition logic
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # Place the pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage
test_array = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
k = 3  # Find the 3rd smallest element

result = randomized_select(test_array, 0, len(test_array) - 1, k)
print(f"The {k}-th smallest element is: {result}")
