# 1652 - Defuse the Bomb

# Topics - Array, Sliding Window

# You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

# To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

# If k > 0, replace the ith number with the sum of the next k numbers.
# If k < 0, replace the ith number with the sum of the previous k numbers.
# If k == 0, replace the ith number with 0.
# As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

# Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

# Example 1:
# Input: code = [5,7,1,4], k = 3
# Output: [12,10,16,13]
# Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.

# Example 2:
# Input: code = [1,2,3,4], k = 0
# Output: [0,0,0,0]
# Explanation: When k is zero, the numbers are replaced by 0. 

# Example 3:
# Input: code = [2,4,9,3], k = -2
# Output: [12,5,6,13]
# Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.

# How to solve: (Brute Force)
    # Create an output array with all zero's, return if k == 0
    # Iterate from i to len(nums) (Outer loop because at each i we need to add three ele's)
        # If k > 0:
            # Iterate next three elements
                # Add ele in input arr to spot at i in output array (use mod to get correct index)
        # If k < 0:
            # Iterate prev three elements
                # Add ele in input arr to spot at i in output array (use mod to get correct index)

# How to solve: (Sliding Window):
# Big Picture:
    # Initialize starting & ending points of your sliding window, do calculations if needed, and use running variable (usually a sum) to subtract out the value leaving the window, add in the value entering the window, leaving the size of the window correct

# Code: 
    # Create an output array with all zero's, return if k == 0
    # Create variables to initialize the starting point, ending point, and current sum of the window
    # If k < 0, we need to readjust the starting point and ending point indexes
    # Use a for loop to add up the values of the input array from start to end (just do this once for idx 0)
    # Use another for loop starting at the beginning of the output array to:
        # Add the current sum to the output array
        # Subtract the value leaving the window from the sum
        # Add the value coming into the window to the sum
        # Move start and finish pointers forward
    # Return the output array




class Solution(object):
    # Brute Force
    def decrypt(self, code, k):
        N = len(code)
        res = [0] * N # Create output array to store answer

        if k == 0: # If k is zero
            return res # Return all zero's

        for i in range(N):
            if k > 0: # If k is positive, add sum of next k ele's to output arr
                for j in range(i + 1, i + 1 + k): # Iterate from next ele to k elements from next ele
                    res[i] += code[j % N] # Add the next element (mod accounts for circular loop)
            elif k < 0: # If k is negative, add sum of prev k ele's to output arr
                for j in range(i - 1, i - 1 - abs(k), -1): # Iterate from prev ele to prev ele - abs(k)
                    res[i] += code[j % N]
        
        return res
    
    # Sliding Window
    def decrypt2(self, code, k):
        result = [0 for _ in range(len(code))] # Initialize output array
        if k == 0: # Stop code if k == 0
            return result
        # Create pointers for the initial window and initial sum for k > 0 (window will move later)
        start, end, window_sum = 1, k, 0

        # if k < 0, replace the ith number with the sum of the previous k numbers.
        if k < 0: # If k < 0, 
            start = len(code) - abs(k) # The starting point of the window will be before the length - abs(k) 
            end = len(code) - 1 # The ending point of the window will be last index of the array

        for i in range(start, end + 1): # Sum up numbers in the window
            window_sum += code[i]

        # Scan through the code array as i moving to the right, update the window sum.
        for i in range(len(code)):
            result[i] = window_sum # Add the current sum to the result
            window_sum -= code[start % len(code)] # Subtract the value in input array leaving the window 
            window_sum += code[(end + 1) % len(code)] # Add the value coming into window to the sum
            start += 1 # Move pointers forward
            end += 1
        return result





my_solution = Solution()
code1 = [5,7,1,4]
k1 = 3

code2 = [1,2,3,4]
k2 = 0

code3 = [2,4,9,3]
k3 = -2

print(my_solution.decrypt2(code1, k1))
print(my_solution.decrypt2(code2, k2))
print(my_solution.decrypt2(code3, k3))