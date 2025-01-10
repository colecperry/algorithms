# Insertion Sort:
    # Start with the second item in the list and compare it to the item before
    # If the item at the second index is less than the item at the first index, swap them
    # Move to the third item in the list and compare it to the item before
    # If the item at the third index is less than the item at the second index, swap them
    # Assuming you swapped, now compare the item at the second index to the item in the first index
    # If the second item is less than the first item, swap them

# High level: Think of a deck of cards. You have a sorted portion on the left side and an unsorted portion on the right side. You start with the initial sorted portion (the first card). You keep moving to the next card and slide that card over until it reaches the correct sorted spot.

# Tips:
    # Start at the second index for first loop
    # Need a variable to decrement -> The variable is initialized to i each loop
    # Use a while loop for the second loop
    # Remember edge case for decrementing j -> don't let j go out of bounds

# Big O Analysis of Insertion Sort:
# Worst Case: O(n^2) - Occurs when the array is sorted in reverse order, requiring (n-1) comparisons and shifts for each element.
# Best Case: O(n) - Happens when the array is already sorted, resulting in one comparison per element.
# Average Case: O(n^2) - For a randomly ordered array, each element may need to be compared and shifted about half the time.
# Space Complexity: O(1) - Insertion sort operates in place, using only a constant amount of additional space.


# [2,8,4,6,3]




def insertion_sort(arr):
    for i in range(1, len(arr)): # Start on second index for i, end on last item of arr
        j = i # Set counter j equal to i (number of iterations for second loop)
        while j > 0 and arr[j] < arr[j-1]: 
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr



print(insertion_sort([4, 3, 2, 1]))