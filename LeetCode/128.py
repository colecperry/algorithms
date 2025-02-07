# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. # You must write an algorithm that runs in O(n) time.

# How to solve:
    # Convert the list to a set
    # Loop through the set, check if it is the start of a new seq
        # If it is, reset count to 0 and create a pointer for the num we are on
        # If it is not, use "in" operator for a set to see if current is in the set, if it is, increase the count and current variable (next potential num in seq)
    # Update maxCount

    # The "in operator" works with both lists and sets, but for lists it is O(n) because it has to scan the entire list until it reaches the end. For sets, it is O(1) because sets are implemented as hash tables


# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

class Solution(object):
    def longestConsecutive(self, nums):       
        nums_set = set(nums) # Convert list into a set
        maxCount = 0
        
        for n in nums_set:
            if n - 1 not in nums_set: # Only start counting if 'n' is the start of a seq
                count = 0 # Reset count to 0
                current = n # Set current variable to ele at start of seq

                while current in nums_set: # Start a while loop using "in" operator for set
                    count += 1 # Increase the count
                    current += 1 # Increase current (next num in seq after n)
                
                maxCount = max(maxCount, count) # Update maxCount after while loop ends
        
        return maxCount

my_solution = Solution()
print(my_solution.longestConsecutive([100,4,200,1,3,2]))
print(my_solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))