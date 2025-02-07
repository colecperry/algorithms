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

# Binary search recursively - > notice no while loop, only recursive call
def binary_search_recursive(array, target, left, right):

    # Base case: If the range is invalid, the target is not in the list
    if left > right:
        return -1

    # Find the middle index
    mid = (left + right) // 2
    mid_value = array[mid]

    # Check if the target is at the middle
    if mid_value == target:
        return mid

    # If the target is smaller than the middle value, search the left half
    if target < mid_value:
        return binary_search_recursive(array, target, left, mid - 1)

    # If the target is larger than the middle value, search the right half
    return binary_search_recursive(array, target, mid + 1, right)


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

    # Example usage
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7

    result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    # Display results
    if result != -1:
        print(f"Target {target} found at index {result}.")
    else:
        print(f"Target {target} not found in the list.")


if __name__ == "__main__":
    main()
