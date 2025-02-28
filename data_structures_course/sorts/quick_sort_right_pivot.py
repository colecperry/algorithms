# Fastest comparison sorting algorithm -> start with a pivot element, and then shift all elements less than the pivot to the left of the pivot, and all the elements greater than the pivot to the right of the pivot

# High level
    # quick_sort function:
        # if l < r we stop because a single element is already sorted
        # otherwise call parition which moves elements smaller than the pivot to the left and larger elements to the right, and the pivot is placed into it's final position, returning q (the index of the pivot)
        # Recursively sort the l half (l to q - 1) and r half (q + 1 to r) -> pivot already in place
    # Partition function
        # the pivot is chosen as the last element
        # initialize a pointer to track the position where the smaller elements should be placed (starts at -1)
        # iterate from l to r
            # if element is less than the pivot, move i forward and swap it into place
        # after looping, swap the pivot with arr[i+1] so it ends up in the correct position
        # return the pivot's index

# Time complexity:
    # Best Case - the pivot divides the array into two equal halves on each step, resulting in balanced partitions which reduces recursive calls. Total partitioning on each level is O(n): we scan all n elements moving them to the correct place before/after pivot, and if we have balanced paritions, the max recursion depth is minimized to log(n) levels. Total: O(n log n)
    # Average Case - random pivot selection -> decently balanced partitions. The recursion depth is not as small as log n (best case), but not as deep as n (worst case). On average, the recursion depth is log n, and with total partitioning on each level being O(n), the total time complexity: O(n log n)
    # Worst Case - pivot is always the smallest or largest element, leading to one partition having n-1 elements and one having zero. Instead of dividing the problem in half each time, we only reduce the array size by one each step. Instead of reaching a recursion depth of log n (like in the best case), we reach n recursive levels, and with O(n) paritioning work at each level, total time complexity -> O(n^2)
    # Already sorted list [1, 2, 3, 4]: if pivot is always chosen as the first or last element, O(n^2), if randomized pivot, O(n log n)
    # Reverse sorted list [4, 3, 2, 1]: if pivot is always the last element, O(n^2), if randomized pivot, O(n log n)
    # If list is parially sorted, quicksort still performs well with the right pivot strategy, and results in O(n log n)


def quick_sort(arr, l, r):
    """
    Recursively sorts an array using the QuickSort algorithm.

    Parameters:
    arr (list): The list to be sorted.
    p (int): The starting index of the partition.
    r (int): The ending index of the partition.

    Returns:
    None (the list is sorted in-place).
    
    Example:
    arr = [10, 7, 8, 9, 1, 5]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)  # Output: [1, 5, 7, 8, 9, 10]
    """
    if l < r: # Keep calling until left = right
        pivot_idx = partition(arr, l, r) # Call partition with left and right most index

        # Recursively sort elements before and after partition
        quick_sort(arr, l, pivot_idx - 1)  # Recursively call left subarray from l to one less than returned pivot
        quick_sort(arr, pivot_idx + 1, r)  # Sort the right subarray with one to the right of the pivot index and r (pivot index already in place)


def partition(arr, l, r):
    """
    Partitions the array by selecting a pivot and placing elements
    smaller than the pivot to its left and greater elements to its right.

    Parameters:
    arr (list): The list to be partitioned.
    p (int): The starting index.
    r (int): The ending index, where the pivot is located.

    Returns:
    int: The final position of the pivot element.
    
    Example:
    arr = [10, 7, 8, 9, 1, 5]
    pivot_index = partition(arr, 0, len(arr) - 1)
    print(arr)  # Example output after partitioning step
    """
    pivot = arr[r]  # Get the value for the pivot (at index r)
    i = l - 1  # track position where smaller elements should be placed

    for j in range(l, r):  # Iterate through the array
        if arr[j] <= pivot:  # If current element is smaller than pivot
            i += 1  # Move the pointer forward
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    # Swap pivot element with the first larger element (placing pivot in sorted position)
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    
    return i + 1  # Return the pivot index


# Example Function Calls
if __name__ == "__main__":
    # Test case 1
    arr1 = [12, 3, 9, 5, 10, 6, 8]
    quick_sort(arr1, 0, len(arr1) - 1)
    print("Sorted array:", arr1)  

    # Test case 2 (Reverse sorted)
    
    arr2 = [5, 4, 3, 2, 1]
    quick_sort(arr2, 0, len(arr2) - 1)
    print(arr2)  
    # Expected Output: Sorted list in ascending order


    # Test case 3 (already sorted)
    arr3 = [1, 2, 3, 4, 5]
    quick_sort(arr3, 0, len(arr3) - 1)
    print("Sorted array:", arr3)  

# Code in detail with example call [4, 2, 7, 1]
    # First call to quick_sort(arr, 0, 3)
        # l = 0, r = 3
        # call partition(arr, 0, 3)
            # intial array = [4, 2, 7, 1], pivot = 1
            # skips all initial swaps
            # swaps pivot 1 with arr[0] -> arr = [1, 2, 7, 4] which puts the pivot ele in correct spot
            # returns i + 1: 0 -> return the pivot index
    # call quick_sort(arr, l, pivot_idx - 1) -> quick_sort(arr, 0, -1): call fn recursively with list left of pivot
        # hit base case
    # call quick_sort(arr, pivot_idx + 1, r) -> quick_sort(arr, 1, 3): call fn recursively with list right of pivot
        # call partition(arr, 1, 3)
            # initial array = [1, 2, 7, 4], pivot = 4
            # swaps -> arr[1] < 4, move i right (i = 1), swap arr[1] with itself b/c j = 1
            # swap pivot 4 with arr[2] -> arr = [1, 2, 4, 7]
            # return i + 1: 2
    # Call quick_sort(arr, l, pivot_idx - 1) -> quick_sort(arr, 1, 1) -> hits base case
    # Call quick_sort(arr, pivot_idx + 1, r) -> quick_sort(arr, 1, 1) -> hits base case
    # final sorted array (no return) = [1, 2, 4, 7]

