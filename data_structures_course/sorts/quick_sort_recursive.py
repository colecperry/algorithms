def quick_sort(arr, p, r):
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
    if p < r:
        # Partition the array and get the pivot index
        q = partition(arr, p, r)

        # Recursively sort elements before and after partition
        quick_sort(arr, p, q - 1)  # Sort the left subarray
        quick_sort(arr, q + 1, r)  # Sort the right subarray


def partition(arr, p, r):
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
    pivot_val = arr[r]  # Choose the last element as the pivot
    i = p - 1  # Pointer for the smaller element

    for j in range(p, r):  # Iterate through the array
        if arr[j] <= pivot_val:  # If current element is smaller than pivot
            i += 1  # Move the pointer forward
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    # Swap pivot element with the first larger element (placing pivot in sorted position)
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    
    return i + 1  # Return the pivot index


# Example Function Calls
if __name__ == "__main__":
    # Test case 1
    arr1 = [10, 7, 8, 9, 1, 5]
    quick_sort(arr1, 0, len(arr1) - 1)
    print("Sorted array:", arr1)  # Output: [1, 5, 7, 8, 9, 10]

    # Test case 2
    arr2 = [3, 6, 2, 7, 4, 1, 5]
    quick_sort(arr2, 0, len(arr2) - 1)
    print("Sorted array:", arr2)  # Output: [1, 2, 3, 4, 5, 6, 7]

    # Test case 3 (already sorted)
    arr3 = [1, 2, 3, 4, 5, 6, 7]
    quick_sort(arr3, 0, len(arr3) - 1)
    print("Sorted array:", arr3)  # Output: [1, 2, 3, 4, 5, 6, 7]

    # Test case 4 (reverse sorted)
    arr4 = [7, 6, 5, 4, 3, 2, 1]
    quick_sort(arr4, 0, len(arr4) - 1)
    print("Sorted array:", arr4)  # Output: [1, 2, 3, 4, 5, 6, 7]
