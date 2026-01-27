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
    """
    TC: O(n) -> loop over each non duplicate number once, and touch each number one more time while counting in another sequence. Each number does not have it's own while loop because their predecessor exists
    SC: O(n) -> hold non duplicate nums from original array
    """
    def longestConsecutive(self, nums):       
        nums_set = set(nums)  # Convert list into a set for O(1) lookup/ eliminate
        maxCount = 0          # dups (we only need to start counting from non-dups)
        
        for num in nums_set: # Look at each num in set (non dups)
            if (num - 1) not in nums_set: # Start counting if the curr num is start of a seq
                count = 0 # Reset count to 0

                while num in nums_set: # Start a while loop using "in" operator for set
                    count += 1 # Increase the count
                    num += 1 # Increment to next num in potential seq
                
                maxCount = max(maxCount, count) # Update maxCount after while loop ends
        
        return maxCount

my_solution = Solution()
print(my_solution.longestConsecutive([100,4,200,1,3,2]))
print(my_solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))