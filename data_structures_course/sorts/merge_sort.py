# Merge Sort - Idea : if you have two sorted lists, you can combine them into a new sorted list
# Keep breaking your list into smaller lists until each list only has one element in it
# Then, take each list and compare with another list, sort them, and create a new sorted list
# Keep doing this until you combine it into one sorted list

# Merge - Helper function -> Takes two sorted lists , takes each value, and creates a new combined sorted list
# Loop through each list (pointer i and j), and compare each value
# Whichever is lowest we will add to the new combined list
# Do this until one list is empty, then add the rest of that list to the combined list

# Big O: 
# Time complexity: O(log n) for breaking the list down, O(n) for putting it back together since you have to use the merge function on each element, O(n log n) overall time complexity
# Space complexity: O(n): num of elements being stored equal to list input

def merge_sort(my_list):
    if len(my_list) == 1: # Base case for recursive call merge_sort is if len is 1 (list of 1 is sorted)
        return my_list 
    mid_index = int(len(my_list)/2) # Find the middle index of the list -> int will return the floor 
    left = merge_sort(my_list[:mid_index]) # Create new list "left" starting at index 0 up to before the mid index
    right = merge_sort(my_list[mid_index:]) # Create new list "right" starting at mid idx and ending at the last ele

    return merge(left, right)


def merge(list1, list2): # Pass in two sorted lists
    combined = [] # 
    i = 0 # Pointer for list1 loop
    j = 0 # Pointer for list2 loop
    while i < len(list1) and j < len(list2): # Loop as long as both lists have items in them
        if list1[i] < list2[j]: # If the value at index i first list is less than val at index j in list2
            combined.append(list1[i]) # Append the element in list i
            i += 1 # Move the i pointer over one
        else:
            combined.append(list2[j]) # Append the element in list j
            j += 1 # Move the j pointer over one
    while i < len(list1): # Runs if there are only left over elements in list1
        combined.append(list1[i]) 
        i += 1
    while j < len(list2): # Runs if there are only left over elements in list2
        combined.append(list2[j])
        j += 1
    return combined

original_list = [3,1,4,2]
sorted_list = merge_sort(original_list)

print('Original List:', original_list)
print('\nSorted List:', sorted_list)


# Visual Aid for Recursion in merge_sort([3,1,4,2])

# Initial Call: merge_sort([3,1,4,2])
# ┌───────────────────────────────┐
# │ Call stack -> merge_sort([3,1,4,2])  │
# │ mid_index = 2                        │
# │ Left: merge_sort([3,1])              │
# └───────────────────────────────┘

# ┌───────────────────────────────┐
# │ Call stack -> merge_sort([3,1])       │
# │ mid_index = 1                        │
# │ Left: merge_sort([3])                │
# └───────────────────────────────┘

# ┌───────────────────────────────┐
# │ Call stack -> merge_sort([3])          │
# │ Base case: returns [3]                │
# └───────────────────────────────┘
# Back to: merge_sort([3,1])

# ┌───────────────────────────────┐
# │ Call stack -> merge_sort([3,1])       │
# │ Right: merge_sort([1])               │
# └───────────────────────────────┘

# ┌───────────────────────────────┐
# │ Call stack -> merge_sort([1])          │
# │ Base case: returns [1]                │
# └───────────────────────────────┘
# Back to: merge_sort([3,1])

# ┌───────────────────────────────┐
# │ Call stack -> merge([3], [1])          │
# │ Returns [1,3]                         │
# └───────────────────────────────┘
# Back to: merge_sort([3,1,4,2])

# ┌───────────────────────────────┐
# │ Call stack -> merge_sort([3,1,4,2])  │
# │ Left: [1,3]                         │
# │ Right: merge_sort([4,2])            │
# └───────────────────────────────┘

# ┌───────────────────────────────┐
# │ Call stack -> merge_sort([4,2])       │
# │ mid_index = 1                        │
# │ Left: merge_sort([4])                │
# └───────────────────────────────┘

# ┌───────────────────────────────┐
# │ Call stack -> merge_sort([4])          │
# │ Base case: returns [4]                │
# └───────────────────────────────┘
# Back to: merge_sort([4,2])

# ┌───────────────────────────────┐
# │ Call stack -> merge_sort([4,2])       │
# │ Right: merge_sort([2])               │
# └───────────────────────────────┘

# ┌───────────────────────────────┐
# │ Call stack -> merge_sort([2])          │
# │ Base case: returns [2]                │
# └───────────────────────────────┘
# Back to: merge_sort([4,2])

# ┌───────────────────────────────┐
# │ Call stack -> merge([4], [2])          │
# │ Returns [2,4]                         │
# └───────────────────────────────┘
# Back to: merge_sort([3,1,4,2])

# ┌───────────────────────────────┐
# │ Call stack -> merge_sort([3,1,4,2])  │
# │ Left: [1,3]                         │
# │ Right: [2,4]                        │
# │ Call merge([1,3], [2,4])            │
# └───────────────────────────────┘

# ┌───────────────────────────────┐
# │ Call stack -> merge([1,3], [2,4])     │
# │ Returns [1,2,3,4]                     │
# └───────────────────────────────┘
# Back to the original function call: merge_sort([3,1,4,2])

# Final Result: [1,2,3,4]












