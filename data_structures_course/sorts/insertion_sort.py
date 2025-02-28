# Insertion Sort: 
    # Big Idea: Think of a deck of cards. As you continue to pull out cards, you keep sliding the card over until it is the sorted position (while loop).
    # Start with the second item in the list and compare it to the item before
    # If the item at the second index is less than the item at the first index, swap them
    # Move to the third item in the list and compare it to the item before
    # If the item at the third index is less than the item at the second index, swap them
    # Assuming you swapped, now compare the item at the second index to the item in the first index
    # If the second item is less than the first item, swap them

# High level: Think of a deck of cards. You have a sorted portion on the left side and an unsorted portion on the right side. You start with the initial sorted portion (the first card). You keep moving to the next card and slide that card over until it reaches the correct sorted spot.

# Tips:
    # Start at the second index for first loop
    # Need a pointer variable to move backwards and do comparisons -> The variable j is initialized to i each loop which allows the correct amount of comparisons at each loop
    # Use a while loop for the second loop -> while j >= 0 and ele smaller than prev ele

# Big O Analysis of Insertion Sort:
# Worst Case: O(n^2) - Occurs when the array is sorted in reverse order, requiring (n-1) comparisons and shifts for each element.
# Best Case: O(n) - Happens when the array is already sorted (we don't enter the second while loop)
# Average Case: O(n^2) - For a randomly ordered array, each element may need to be compared and shifted about half the time.
# Space Complexity: O(1) - Insertion sort operates in place, using only a constant amount of additional space.