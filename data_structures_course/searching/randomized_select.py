# Randomized select is an algoritm for finding the kth smallest element (order statistics) in an array. It is based on the quickselect algo, which is a modification of quicksort, but instead of sorting the entire array, it selects a pivot and only recurses into one partition (the part that contains the desired element), allowing it to run in O(n).

# Time Complexity:
# - Best/Average Case: O(n)
#   - Each partitioning step reduces the problem size roughly by half on average.
#   - Since we only recurse on one side, the recurrence relation is:
#     T(n) = T(n/2) recursive calls + O(n) (partitioning takes O(n)) - we loop through the whole subarr once to swap elements
#   - Solving this gives O(n) expected time.
#
# - Worst Case: O(n^2)
#   - If we always pick the worst pivot (e.g., smallest or largest element), 
#     one partition is empty, and the other has n-1 elements.
#   - This results in T(n) = T(n-1) recursive calls + O(n) for partitioning, which solves to O(n^2).
#   - Randomization helps avoid this case in practice.

# Space Complexity:
# - O(1) (Iterative Partitioning) or O(log n) (Recursive Calls)
#   - Partitioning is done **in place**, so no extra storage is needed.
#   - The recursion depth is O(log n) on average, leading to O(log n) space.
#   - In the worst case (unbalanced partitions), recursion depth is O(n), leading to O(n) space.


import random

def randomized_select(arr, low, high, i):
    """
    Randomized Select algorithm to find the i-th smallest element in arr[low..high].
    """
    if low == high:
        return arr[low]

    # Partition array with random pivot and return pivot idx
    pivot_index = randomized_partition(arr, low, high)
    
    # Since the pivot is placed in it's correct sorted position, k tells us how many elements are <= to the pivot
    k = pivot_index - low + 1 # rank of pivot in overall arr

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
    pivot = arr[high] # Get val for pivot comparisons
    i = low - 1 # idx to insert ele smaller than pivot
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

