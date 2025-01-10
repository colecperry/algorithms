def set_based_search(arr, target):
    """
    Perform a hash-based search using a set to find the target value.

    Time Complexity: O(1) average case for lookups.

    Parameters:
        arr (list): The list of elements to search through.
        target (any): The value to search for.

    Returns:
        bool: True if the target value is found, otherwise False.
    """
    hash_set = set(arr)  # Convert the list into a hash-based set
    return target in hash_set


def dict_based_search(arr, target):
    """
    Perform a hash-based search using a dictionary to find the target value.

    Time Complexity: O(1) average case for lookups.

    Parameters:
        arr (list): The list of elements to search through.
        target (any): The value to search for.

    Returns:
        int: The index of the target value if found, otherwise -1.
    """
    hash_dict = {}  # Initialize an empty dictionary
    for index, value in enumerate(arr):  # Populate the dictionary with array values and their indices
        hash_dict[value] = index

    if target in hash_dict:  # Check if the target exists in the dictionary
        return hash_dict[target]
    else:
        return -1


def main():
    """Main function to demonstrate set-based and dict-based hash searches."""
    # Example array and target
    arr = [10, 20, 30, 40, 50, 60]
    target = 40

    # Perform set-based search
    found_in_set = set_based_search(arr, target)
    if found_in_set:
        print(f"[Set-Based Search] Target {target} found in the list.")
    else:
        print(f"[Set-Based Search] Target {target} not found in the list.")

    # Perform dict-based search
    found_in_dict = dict_based_search(arr, target)
    if found_in_dict != -1:
        print(f"[Dict-Based Search] Target {target} found at index {found_in_dict}.")
    else:
        print(f"[Dict-Based Search] Target {target} not found in the list.")


if __name__ == "__main__":
    main()
