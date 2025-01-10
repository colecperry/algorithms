# QUICK SORT:
# Start with a pivot point (first item)
# Compare each item after the pivot point to see if it greater than or less than
# If the item is less than the pivot point, swap it with the first element in the "greater than" portion of the list
# This will leave us with two portions: all the items less than the pivot point and all items greater than the pivot point
# Next step: Swap the first item (the pivot point) with the last item in the less than portion of the list, now the pivot point is sorted
# Next step: Run quick sort again on the left portion of the list (less than), and the right portion of the list (greater than)
# Keep running quick sort until there is only one item in the list, then it will be sorted

# Big O of Quick Sort -> O (n log n)
# Running pivot is had a for loop that loops through the list -> O(n)
# Recursive call -> O(log n) -> For list of 8, we have to make 2^3 recursive calls
# Worst case -> O (n^2) if you have already sorted data



# Helper function that swaps two indexes
def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

# PIVOT HELPER FUNCTION:
# Sorts the list into two sections, sorts the pivot element, and returns the index of the pivot point
def pivot(my_list, pivot_index, end_index): # Pass pivot a list, pivot index (0) and the last index of the list
    swap_index = pivot_index # Create another variable that is equal to the pivot index (initially at 0)
    for i in range(pivot_index + 1, end_index + 1): # Loop from the second index to the last index (stops before end_index + 1)
        if my_list[i] < my_list[pivot_index]: # Compare first value to the pivot value
            swap_index += 1 # Move swap index over one
            swap(my_list, swap_index, i) # Swap two items
    swap(my_list, pivot_index, swap_index) # Swap items at the pivot index (0) and the swap index (now at the end of the sorted portion of the list less than the pivot item)
    return swap_index

# QUICK SORT
# Use pivot function and recursively run pivot on the left and right sides
def quick_sort_helper(my_list, left, right):
    if left < right: # Base case -> If the left and right indexes equal each other
        pivot_index = pivot(my_list, left, right) # Run pivot to rearrange the list and return the pivot index
        quick_sort_helper(my_list, left, pivot_index - 1) # Recursive calls on left and right side
        quick_sort_helper(my_list, pivot_index + 1, right)
    return my_list # Return for the base case

# Avoids having to pass in first and last indexes
def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)

print(quick_sort([4,6,1,7,3,2,5]))