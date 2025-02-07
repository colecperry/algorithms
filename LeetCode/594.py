# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

# Topics: Array, HashTable, Sliding Window, Sorting, Counting


# Example 1:
# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation:
# The longest harmonious subsequence is [3,2,2,2,3].

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 2
# Explanation:
# The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

# Example 3:
# Input: nums = [1,1,1,1]
# Output: 0
# Explanation:
# No harmonic subsequence exists.

# How to solve: (Brute Force):
    # Store variables for max length, current length, and boolean variable to track if the current portion of our array is harmonious
    # Iterate twice (i & j), update current length, and only update max length if our variable turns true

# Code:
    # Create a variable to count the max length
    # Iterate through the array starting at 0
        # Create variable to store current harmonious array count from i
        # Create bool var to track if there's at least one number that is equal to i + 1
        # Iterate again with j
            # If the numbers equal each other, increment the current counter
            # If the number at j is one more than i, increment the current counter, and turn the boolean variable True
        # Only update the max length variable if the boolean variable is True

    # Time Complexity: O(n^2) - Iterates over every element i & j
    # Space Complexity: O(1) - Only uses variables such as max_length and count

# How to Solve (hashmap w/ counter):
    # Import counter and to create a hashmap of frequencies of each ele in the array
    # Create a variable to hold the max length of the harmonious array
    # Iterate over the keys of the hashmap  
        # If the key + 1 exists, update the max length by adding the freq's of the key and key + 1

    # Time Complexity: O(n): hashmap stores at most n unique elements
    # Space Complexity: O(1): Constant space only uses variable max_length


# How to Solve (sliding window)
    # Sort the array (which guarentees numbers with a diff of 1 are next to eachother)
    # Create left and right pointers to create a sliding window
    # Matintain a valid sliding window -> 
        # Shrink the window if nums[r] - nums[l] > 1
        # If the window is the valid length, update the max value

    # Time Complexity: O(n log n): sorting takes O(n log n), sliding window is O(n)
    # Space Complexity: O(n) if sorting creates a new list, or O(1) if sorting is in place






from collections import Counter

class Solution(object):
    # Brute Force
    def findLHS(self, nums):
        max_length = 0 # Variable holds max length of harmonious array
        
        for i in range(len(nums)): # Iterate through input array from i
            count = 0 # Count current length of harmonious array from i
            has_pair = False # Tracks if there ia at least one nums[i] + 1

            for j in range(len(nums)): # Iterate again (nested loop)
                if nums[j] == nums[i]: # If the number at j is the same as i
                    count += 1 # We found the same number, increase count
                # Since we are iterating over all possible starting points, we do not need to check nums[j] == nums[i] - 1 because nums[i] - 1 will already be checked when nums[i] takes on a different value later on
                elif nums[j] == nums[i] + 1:  # If the number at j is 1 more than i
                    count += 1 # Increase the count
                    has_pair = True  # Found a valid pair(we found a num j other than i)
                    
            if has_pair: # If we found a num other than i
                max_length = max(max_length, count) # Increase the max length
        
        return max_length
    
    # Solution with counter (Optimal)
    def findLHS2(self, nums):
        freq = Counter(nums)  # Creates a array of integers and their frequencies (by order of insertion)
        max_length = 0 # Holds max length of harmonious array
        
        for key in freq: # Iterate over the keys of the dictionary
            if key + 1 in freq:  # Check if `num+1` exists in the hashmap
                max_length = max(max_length, freq[key] + freq[key + 1]) # Update the max length (bigger of current max length and value of the key and key+1)
        
        return max_length

    # Solution with Sliding Window
    def findLHS3(self, nums):
        nums.sort()  # Sort the array ()
        l = 0  # Left pointer of sliding window
        max_seq = 0  # Store max length of harmonious subsequence
        
        for r in range(len(nums)):
            while nums[r] - nums[l] > 1:  # Shrink window if difference > 1
                l += 1  

            if nums[r] - nums[l] == 1:  # Valid harmonious subsequence
                max_seq = max(max_seq, r - l + 1) # Update the max sequence variable

        return max_seq
    
my_solution = Solution()
nums1 = [1,3,2,2,5,2,3,7]
nums2 = [1,2,3,4]
nums3 = [1,1,1,1]
print(my_solution.findLHS3(nums1))
print(my_solution.findLHS(nums2))
print(my_solution.findLHS(nums3))
