# Selection sort: Think SELECTION -> we select the smallest element on each iteration
    # Big idea: Loop through the array starting at the first element. Track the smallest element (assume it is the first element). If you find something smaller, set that element to the smallest element. Once you finish the loop, swap the new smallest element with the first element if it does not equal the first index still.
    # Find the smallest value: Start by assuming the first element is the smallest.
    # Look through the rest: Use a loop to check every other element in the list.
    # Update the smallest value: If you find something smaller, remember where it is.
    # Swap positions: Once you finish checking, swap the smallest value with the one you're currently looping on
    # Repeat: Move on to the next position in the list and repeat the process.
    
# Tips:
    # Track the min index
    # Loop through the whole list to find min index before swapping
    # Before swapping, check that i is still not min index after loop

# Psuedo code for selection sort not in place
    # Create empty output array
    # Loop through input array, track smallest element
    # When we find the smallest element, add it to the output array
    # Replace the index that held the smallest element in the input array to infinity so we don't keep selecting the same element

# Big O:
    # Worst-case time complexity: O(n²): In the worst case, selection sort makes n passes and performs n comparisons in each pass, leading to a time complexity of O(n²).
    # Best-case time complexity: O(n²): Even if the list is already sorted, selection sort still scans the entire unsorted portion in every pass, resulting in a best-case time complexity of O(n²).
    # Average-case time complexity: O(n²): On average, selection sort performs the same number of comparisons regardless of the input's initial order, yielding an average time complexity of O(n²).

# In place
def selection_sort(array):
    for i in range(len(array) - 1): # Iterate one less b/c of i+1
        min_index = i # Set minimum index to i to track the position in the outer loop
        for j in range(i+1, len(array)): # Iterate through the list again starting with (j= (i + 1)) one index after i until last index
            if array[j] < array[min_index]: # Check if the element you are on is less than the element at the min_index
                min_index = j # Keep looping all the way through to find the min_index
        if i != min_index: # Code for edge case where i is already the min index
            temp = array[i] # After looping all the way through, swap the element on min_index on the outer loop with the element we found that has the minumum value (j)
            array[i] = array[min_index]
            array[min_index] = temp
            
    return array

# Using an output array (not in place)
import math

def selection_sort2(A):
    """
    This version sorts A into a new list B without modifying A directly.
    
    Parameters:
    A (list): The list to be sorted.

    Returns:
    list: A new sorted list B.

    Example:
    A = [3, 1, 4, 1, 5, 9, 2]
    B = selection_sort(A)
    print(B)  # Output: [1, 1, 2, 3, 4, 5, 9]
    """
    B = [0] * len(A)  # Initialize the output list B with the same length as A

    for i in range(len(A)):  # Iterate through all elements of A
        min_ind = 0  # Assume the first element is the minimum
        
        for j in range(1, len(A)):  # Iterate to find the smallest element
            if A[j] < A[min_ind]:  # If we find a smaller element
                min_ind = j # Store that index

        B[i] = A[min_ind]  # Store the smallest element in output array B
        A[min_ind] = math.inf  # Mark the elements "used" in input array A by setting it to infinity
    
    return B  # Return the sorted list




print(selection_sort([4,2,6,5,1,3]))
