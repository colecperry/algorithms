def binary_search(arr, target):
    """
    Perform a binary search on a sorted array to find the target value.

    Time complexity: O(log n) -> works by repeatedly dividing the search interval in half, in each step, the size of the search space is reduced by a factor of two

    Parameters:
        arr (list): The sorted list of elements to search through.
        target (any): The value to search for.

    Returns:
        int: The index of the target value if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Return the index where the target is found
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    
    return -1  # Return -1 if the target is not found


def main():
    """Main function to demonstrate binary search."""
    # Example sorted array and target to search
    arr = [10, 20, 30, 40, 50, 60]
    target = 40

    # Perform binary search
    result = binary_search(arr, target)

    # Display results
    if result != -1:
        print(f"Target {target} found at index {result}.")
    else:
        print(f"Target {target} not found in the list.")


if __name__ == "__main__":
    main()
