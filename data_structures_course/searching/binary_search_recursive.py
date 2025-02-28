# Since the array is sorted, and we know what the middle element is, we know whether our the element we are searching for is before or after the middle, so we can discard half the array on each comparison

# Run Time Complexity: O(log n) -> Each recursive call eliminates half of the elements: If we start with n = 16 and search for an element that isn't there, we continue dividing until we only have one element left, which would be log2 * 16 steps = 4, best case is O(1) -> I is already at the middle element

# Space Complexity: O(1) -> the function does not use any new data structures

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
    
    mid = min + (max - min) // 2  # Calculate middle index (floor)
    
    if I == A[mid]: # If we are looking for is at mid index
        return True  # Element found
    
    if I > A[mid]: # If ele we are looking for is greater than mid index
        return Recursive_bs(A, I, mid + 1, max)  # Search right half (not including middle)
    else: # If ele we are looking for is less than mid index
        return Recursive_bs(A, I, min, mid - 1)  # Search left half (not including middle)



A = [1, 3, 5, 7, 9, 11, 15, 18]
I = 1

# Call the function
result = Recursive_bs(A, I, 0, len(A) - 1)

# Output the result
print(f"Element {I} found:", result)
