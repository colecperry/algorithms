# Bubble sort: Think BUBBLE UP -> bubble up (by repeated comparison) to one end of array
# Big Idea : you bubble up the largest element to the end of the array or smallest element to the beginning of the array one at a time. Starting at the beginnig or end of the array, you compare two elements at a time, and swap them depending, moving either the largest or smallest element to the end or beginning of the array on each outer loop.
# Start with the first item in the list, and compare it to the second. If the first item is greater than the second item, switch them. Then take the second item and compare it to the third item, if they don't need to be switched, move to the third item, if not, switch them. If you have n items, you will have n - 1 comparisons

# How to solve:
    # TRICK - Iterate backwards on first loop
    # Iterate through the length, and on each iteration, iterate through again 1 less time (if you start i at (len(arr)-1) on outer loop and iterate backwards, and you iterate inner loop with (j in range(i)), it will naturally decrease by one each time
    # Example:
        # arr = [4,3,5,1,2] i loops 4 times total (4, 3, 2, 1)
        # on first i loop j iterates 4 times
        # on second i loop j iterates 3 times
        # on third i loop j iterates 2 times
        # on fourth i loop j iterates 1 time
    # If the index you are currently on is greater than the next index, switch, if not, do nothing and move to the next index
    # After each pass, the largest unsorted element will end up in its correct position at the end of the list because it keeps getting swapped with smaller elements as we move through the list. ****

# Big O: 
    # Worst-case time complexity: O(n²). This happens when the list is in reverse order, and every element needs to be compared and swapped multiple times. If you iterate through the list more than twice, the time complexity is still O(n^2)
    # Best-case time complexity: O(n). This occurs when the list is already sorted, and an optimized bubble sort can stop early if no swaps are made during a pass.
    # Average-case time complexity: O(n²). Even though the list may not be in reverse order, in general, a large number of comparisons and swaps are still required.

def bubble_sort_backwards(my_list):
    for i in range(len(my_list) - 1, 0, -1): # Iterating backwards allows i to decrease by 1 each 
        for j in range(i): # time from the correct starting length
            if my_list[j] > my_list[j+1]: # If the element after is greater:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list


# Example of iterating forwards
def bubble_sort_forwards(arr):
    for i in range(len(arr) - 1): # iterate from i to len - 1
        for j in range(len(arr) - i - 1): # it from j to len - 1 subtracting 1 each it
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort_backwards([4, 3, 5, 1, 2]))
print(bubble_sort_forwards([1, 2, 3, 4]))