# Insertion Sort:
    # Start with the second item in the list and compare it to the item before
    # If the item at the second index is less than the item at the first index, swap them
    # Move to the third item in the list and compare it to the item before
    # If the item at the third index is less than the item at the second index, swap them
    # Assuming you swapped, now compare the item at the second index to the item in the first index
    # If the second item is less than the first item, swap them

# Big O

def insertion_sort(array):
    for i in range(1, len(array)): # Sort looping through the array on the second item
        temp = array[i] # Store the element at the second element to a variable temp
        j = i - 1 # Set variable j equal to the index before i
        while temp < array[j] and j > -1:
            array[j+1] = array[j] # Move the element on the left over one
            array[j] = temp # Move the element on the right to the left
            j -= 1
    return array







insertion_sort([1, 2, 4, 3, 5, 6])