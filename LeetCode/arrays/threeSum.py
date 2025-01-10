# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# valToIndex - 

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


# Big Idea:
    # Sort the input array so we can compare to the last num in the array to make sure it's not a duplicate
    # Use a Left and Right pointer to solve for the next two elements (since the array is now sorted)
    # If the sum > 0, move the right pointer left (right pointer has bigger numbers)
    # If the sum < 0, move the left pointer right (left pointer has smaller numbers)
    # Make sure the left and right pointers don't move to a duplicate, if it does, shift it again



class Solution(object):
    def threeSum(self, nums):
        nums.sort()  # Sort the array for two-pointer technique
        output_arr = []  # Output list to store unique triplets

        for i in range(len(nums) - 2):
            # Skip duplicate values for `i`
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum > 0:
                    right -= 1  # Move right pointer leftward to reduce the sum
                elif sum < 0:
                    left += 1  # Move left pointer rightward to increase the sum
                else:
                    # Found a triplet
                    output_arr.append([nums[i], nums[left], nums[right]])

                    # Move both pointers and skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move pointers inward after processing a valid triplet
                    left += 1
                    right -= 1

        return output_arr
    
# Neetcode Solution
    def threeSum2(self, nums):
        nums.sort() # Sort the array so we can use a two pointer technique to find pairs
        output_arr = [] # Create an ouput array for the answer

        for i, n in enumerate(nums): # Loop through the nums array
            if i > 0 and n == nums[i - 1]: # If i is on at least the second index and num is equal to the prev num
                continue # Skip this loop and move to next i

            l, r = i + 1, len(nums) - 1 # Set left and right pointers

            while l < r: # Loop until left and right equal each other
                sum = n + nums[l] + nums[r] # Sum the three pointers
                if sum > 0: # If sum is too big
                        r -= 1 # Move the right pointer one left
                elif sum < 0: # If the sum is too small
                        l += 1 # Move the left pointer one right
                else: # If they are equal
                    output_arr.append([n, nums[l], nums[r]]) # Append
                    l += 1 # Move the left pointer over one
                    while nums[l] == nums[l - 1] and l < r: # If the left pointer and left is less than right
                        l += 1 # is equal to the num to the left, increment
        return output_arr



nums1 = [-1,0,1,2,-1,-4]
nums2 = [0,1,1]
nums3 = [0,0,0]


my_solution = Solution()
print(my_solution.threeSum2(nums1))
print(my_solution.threeSum2(nums2))
print(my_solution.threeSum2(nums3))

