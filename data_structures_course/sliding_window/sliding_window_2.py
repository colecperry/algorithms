# find the largest subarray whose sum is less than or equal to a target value

# Ex. 1
    # arr = [1, -2, 7, 2, 3, -10] 
    # target = 8
    # output = 6

# How to solve (Brute Force)
    # max_count tracks the maximum length of the subarray less than or equal to a target value
    # count tracks the count of the current subarray
    # Loop through array
        # Each loop reset the running sum and the count (starting new subarray count)
        # loop through each 

# How to solve (Sliding window)
    # track left pointer (holds left index of current sub array), running sum of the current subarray, and the max count which equals the max sub array we find
    # Iterate through array, and update the running sum
    # If we get to a point where our running sum is larger than the target and the left and right pointers haven't met (while loop)
        # Decrease the running sum by the value at the left pointer and move the left pointer over (shrink window)
    # Update max count of current window and previous max 

# Brute Force solution - O(n^2)
def problem(arr, target):
    max_count = 0 # Track max length of subarray <= target
    count = 0 # Tracks count of current subarray we are looping on

    for i in range(len(arr)): # Loop through array
        running_sum = 0 # Reset sum and count on each outer loop 
        count = 0 # (starting new subarray)
        for j in range(i, len(arr)): # Loop thru ele's starting at j
            running_sum = running_sum + arr[j] # Add ele to sum
            count += 1 # Increase count
            if running_sum <= target: # If sum less than target
                max_count = max(max_count, count) # Update max count
            else: # If we encounter an invalid sum
                break # we stop the count

    return max_count

# Sliding Window - O(n)
def problem2(arr, target):
    left = 0 # Left pointer
    running_sum = 0 # Keep track of sum
    max_length = 0 # Max length of sub array

    for right in range(len(arr)): # Iterate through arr
        running_sum += arr[right] # Update running sum

        # If sum gets bigger than target and don't meet
        while running_sum > target and left <= right: 
            running_sum -= arr[left] # Decrease sum from l
            left += 1 # Increase left pointer
        
        # Update max length (current max length and length of current window)
        max_length = max(max_length, right - left + 1)
    
    return max_length



arr = [1, -2, 7, 2, 3, -10] 
target = 8

print(problem2(arr, target))