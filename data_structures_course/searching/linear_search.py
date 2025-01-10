def linear_search(arr, target):
    """
    Perform a linear search on the array to find the target value.
    
    Time complexity: O(n)

    Parameters:
        arr (list): The list of elements to search through.
        target (any): The value to search for.

    Returns:
        int: The index of the target value if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the target is found
    return -1  # Return -1 if the target is not found


def main():
    """Main function to demonstrate linear search."""
    # Example array and target to search
    arr = [10, 20, 30, 40, 50, 60]
    target = 40

    # Perform linear search
    result = linear_search(arr, target)

    # Display results
    if result != -1:
        print(f"Target {target} found at index {result}.")
    else:
        print(f"Target {target} not found in the list.")


if __name__ == "__main__":
    main()