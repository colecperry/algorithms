def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2

        # Recursively sort the left and right halves
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)

        # Merge sorted halves
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    print(f"Merging: {arr[low:mid+1]} and {arr[mid+1:high+1]}")
    
    # Create left and right subarrays
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]

    i = j = 0  # Pointers for left and right arrays
    k = low    # Pointer for main array

    # Merge process
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements from left subarray
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy remaining elements from right subarray
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    print(f"Result after merging: {arr[low:high+1]}")

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print(f"Original Array: {arr}")
merge_sort(arr, 0, len(arr) - 1)
print(f"Sorted Array: {arr}")
