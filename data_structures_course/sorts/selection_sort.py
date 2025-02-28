# Selection Sort is a comparison-based sorting algorithm that works by repeatedly selecting the smallest element from the unsorted portion of the array and placing it into a new sorted array.

# IN PLACE 
    # We iterate through the input list 𝐴, finding the minimum element at each step.
    # Instead of swapping elements within 𝐴, we store the minimum in a new list 𝐵
    # To keep track of used elements, we mark the selected minimum in 𝐴 as infinity (math.inf), ensuring it won't be chosen again.
    # This process continues until all elements from 𝐴 are placed into 𝐵 in sorted order.
    # Since this implementation builds a separate sorted list 𝐵, it does not sort in-place, but follows the fundamental idea of selecting the smallest available element at each step.

# NOT IN PLACE
    # Big idea: Loop through the array starting at the first element. Track the smallest element (assume it is the first element). If you find something smaller, set that element to the smallest element. Once you finish the loop, swap the new smallest element with the first element if it does not equal the first index still. Now that the smallest element is stored at index 1, move onto the next index and repeat the process.
    # Find the smallest value: Start by assuming the first element is the smallest.
    # Look through the rest: Use a loop to check every other element in the list.
    # Update the smallest value: If you find something smaller, remember where it is.
    # Swap positions: Once you finish checking, swap the smallest value with the one you're currently looping on
    # Repeat: Move on to the next position in the list and repeat the process.

# Runtime complexity
# Big O:
    # Worst-case time complexity: O(n²): In the worst case, selection sort makes n passes and performs n comparisons in each pass, leading to a time complexity of O(n²).
    # Best-case time complexity: O(n²): Even if the list is already sorted, selection sort still scans the entire unsorted portion in every pass, resulting in a best-case time complexity of O(n²).
    # Average-case time complexity: O(n²): On average, selection sort performs the same number of comparisons regardless of the input's initial order, yielding an average time complexity of O(n²).

# Space complexity
    # In place - O(1) space (only swaps elements within the original array)
    # Not in place - O(n) because it constructs a seperate list the same size as the original array

import math

# Using an output array (not in place)
def selection_sort(A):
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

# Using one array - In Place
def selection_sort2(array):
    for i in range(len(array) - 1): # Iterate one less b/c of i+1
        min_index = i # Set minimum index to i to track the position in the outer loop
        for j in range(i+1, len(array)): # Iterate through the list again starting with (j= (i + 1)) one index after i until last index
            if array[j] < array[min_index]: # Check if the element you are on is less than the element at the min_index
                min_index = j # Keep updating min_index
        if i != min_index: # Only swap if min_index isn't i
            temp = array[i] # Store variable at index i
            array[i] = array[min_index] # Update var at index i with smallest element found
            array[min_index] = temp # Swap ele that was at index i into ele we found at min_index 
            
    return array


# Example Function Calls
if __name__ == "__main__":
    # Test case 1
    A1 = [3, 1, 4, 1, 5, 9, 2]
    B1 = selection_sort2(A1.copy())  # Use .copy() to prevent modifying the original list
    print("Sorted array:", B1)  # Output: [1, 1, 2, 3, 4, 5, 9]

    # Test case 2
    A2 = [10, 7, 8, 9, 1, 5]
    B2 = selection_sort(A2.copy())
    print("Sorted array:", B2)  # Output: [1, 5, 7, 8, 9, 10]

    # Test case 3 (already sorted)
    A3 = [1, 2, 3, 4, 5, 6, 7]
    B3 = selection_sort(A3.copy())
    print("Sorted array:", B3)  # Output: [1, 2, 3, 4, 5, 6, 7]

    # Test case 4 (reverse sorted)
    A4 = [7, 6, 5, 4, 3, 2, 1]
    B4 = selection_sort(A4.copy())
    print("Sorted array:", B4)  # Output: [1, 2, 3, 4, 5, 6, 7]
