def Recursive_bs(A, I, min, max):
    """
    Performs a recursive binary search to determine if a target value exists in a sorted list.

    Parameters:
    A (list): A sorted list of integers.
    I (int): The target integer to search for.
    min (int): The starting index of the search range.
    max (int): The ending index of the search range.
    """
    if min > max:  # Base case: element not found
        return False
    
    mid = min + (max - min) // 2  # Calculate middle index
    
    if A[mid] == I: # If ele at mid index is ele we are looking for
        return True  # Element found
    
    if A[mid] < I: # If ele at mid index is less than ele we are looking for
        return Recursive_bs(A, I, mid + 1, max)  # Search right half
    else: # If ele at mid index is greater than ele we are looking for
        return Recursive_bs(A, I, min, mid - 1)  # Search left half



A = [1, 3, 5, 7, 9, 11, 15, 18]
I = 1

# Call the function
result = Recursive_bs(A, I, 0, len(A) - 1)

# Output the result
print(f"Element {I} found:", result)