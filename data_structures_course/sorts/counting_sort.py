# Counting sort assumes that each of n input elements is an integer in the range O to k. Counting sort determines for each input element x, the number of elements that are less than x, and then uses that information to place element x directly in the position in the output array

# How to solve: (code)
    # Handle edge case where the input array is empty
    # Create variable for min_val and max_val -> determine smallest and largest ele's we need for the count array -> counts frequencies
    # Create variable for range of elements -> determines number of indexes needed for our count freq array, add one to ensure array includes all values from min_val to max_val
    # Create empty output array
    # Create freq count array, loop through each ele in the input array and increment the count of that num corresponding to the index
    # Loop though the count array and make count array into a cumulative count array by adding the count of the prior index
    # Iterate over the input array in reverse order, use the count array to determine the correct position of each element, and place the element in the correct index in the sorted array, then decrement the count array
        # count[num - min_val] tells us how many elements are less than or equal to num, subtract 1 from it to find the correct index in sorted_arr

    # Time complexity: O(n + k) -> two for loops = O(n)
    # Space complexity: O(n + k) -> uses two additional arrays



def counting_sort(arr):
    if len(arr) == 0: 
        return arr

    # Find the range of the input data
    max_val = max(arr) # Determines largest ele in input array, which helps us define the size of the count array
    min_val = min(arr) # Determines the smallest ele in the input array, which helps us define the align the smallest ele with correct index
    range_of_elements = max_val - min_val + 1 # Range of ele's = differece between the max and min values -> defines the size of the count array

    sorted_arr = [0] * len(arr) # Create output arr of correct len

    # Step 0: Create an count array to store # of times each ele appears
    count = [0] * range_of_elements

    # Loop through input array, and with the min_val being at index 0, increment the count of each number 
    for num in arr:
        count[num - min_val] += 1 # ++ the count of num in the count array accounting for the min_val at idx 0

    # Create a cumulative count array: modify count[i] to store number of elements equal to or before that index
    for i in range(1, len(count)): # Start at idx 1
        count[i] += count[i - 1]

    # Iterate though A backwards and place elements in their correct sorted positions: 
    for num in reversed(arr):
        # Find the correct position for the element in the sorted array
        position = count[num - min_val] - 1
        # Place the element in it's sorted position
        sorted_arr[position] = num
        # Decrement the count for the element (to handle duplicates)
        count[num - min_val] -= 1

    return sorted_arr


# Test the function with the given input
A = [4, 1, 2, 2]
sorted_A = counting_sort(A)
print("Sorted array:", sorted_A)

# Step by step (code)
    # max_val = 4, min_val = 1, range_of_elements = 4 -> number of indexes needed for freq array
    # sorted_arr = [0,0,0,0]
    # count = [0,0,0,0]
    # create count array and increment -> [1, 2, 0, 1]
    # create cumulative count array -> each count[i] stores number of elements equal to or before it: [1,3,3,4]
    # Loop through the nums reversed
        # Iteration 1:
            # position = count[2-1] - 1 -> count[1] - 1 -> 2
            # place ele in it's sorted position -> [0,0,2,0]
            # decrement the count for that ele -> count = [1,2,3,4]
        # Iteration 2:
            # position = count[2-1] - 1 -> count[1] - 1 -> 1
            # place ele in sorted position -> [0,2,2,0]
            # decrement count for that ele -> count = [1,1,3,4]
        # Iteration 3:
            # 



