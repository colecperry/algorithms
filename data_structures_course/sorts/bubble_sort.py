# Bubble sort -> start with the first item in the list, and compare it to the second. If the first item is greater than the second item, switch them. Then take the second item and compare it to the third item, if they don't need to be switched, move to the third item, if not, switch them. If you have n items, you will have n - 1 comparisons

# How to solve:
    # Iterate through the length of the list for the number of elements in the list
    # On each iteration, iterate through again to compare the index you are currently on to the next index
    # If the index you are currently on is greater than the next index, switch, if not, do nothing and move to the next index
    # After each pass, the largest unsorted element will end up in its correct position at the end of the list because it keeps getting swapped with smaller elements as we move through the list. ****

# Big O: 
    # Worst-case time complexity: O(n²). This happens when the list is in reverse order, and every element needs to be compared and swapped multiple times. If you iterate through the list more than twice, the time complexity is still O(n^2)
    # Best-case time complexity: O(n). This occurs when the list is already sorted, and an optimized bubble sort can stop early if no swaps are made during a pass.
    # Average-case time complexity: O(n²). Even though the list may not be in reverse order, in general, a large number of comparisons and swaps are still required.

def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1): # Iterate through the list from length - 1 to zero
        for j in range(i): # Iterate through the list one less time each time
            if my_list[j] > my_list[j+1]: # If the element after is greater:
                temp = my_list[j] # swap the two elements
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
                print(my_list)
    return my_list


# Example of iterating forwards
def bubble_sort_forwards(arr):
    n = len(arr)
    for i in range(n):  # Outer loop (iterates forwards) up to right before the length n
        for j in range(0, n - i - 1):  # Inner loop (iterates forwards)
            print("i: ", i)
            print("j: ", j)
            print("\n")
            if arr[j] > arr[j + 1]:  # Compare adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap if needed


print(bubble_sort([4, 3, 5, 1, 2]))