# Selection sort 
    # Find the smallest value: Start by assuming the first element is the smallest.
    # Look through the rest: Use a loop to check every other element in the list.
    # Update the smallest value: If you find something smaller, remember where it is.
    # Swap positions: Once you finish checking, swap the smallest value with the one you're currently looping on
    # Repeat: Move on to the next position in the list and repeat the process.
    
# Tips:
    # Track the min index
    # Loop through the whole list to find min index before swapping
    # Before swapping, check that i is still not min index after loop

# Big O:
    # Worst-case time complexity: O(n²): In the worst case, selection sort makes n passes and performs n comparisons in each pass, leading to a time complexity of O(n²).
    # Best-case time complexity: O(n²): Even if the list is already sorted, selection sort still scans the entire unsorted portion in every pass, resulting in a best-case time complexity of O(n²).
    # Average-case time complexity: O(n²): On average, selection sort performs the same number of comparisons regardless of the input's initial order, yielding an average time complexity of O(n²).

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







print(selection_sort([4,2,6,5,1,3]))
