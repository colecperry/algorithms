# 11. Container With Most Water

# Topics - Array, Two Pointers, Greedy

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# How to solve: (Brute Force)
    # We are trying to maximize the area of the container
    # Loop through every combination of our left pointer and right pointer (nested)
    # Left pointer would start at first index, right pointer would start at second index
    # Calculate max area for each iteration

# How to solve: (Optimal) - Linear time 
    # Use a two pointer technique - initialize a left pointer all the way at the left, and a right pointer all the way to the right
    # Create while loop
    # Calculate area
    # Update left pointer or right pointer (which ever is a lower number)
    # If the pointers are equal, shift which ever one has a larger height coming next
    # Update max area


# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# Brute Force: Gets time limit exceeded
class Solution(object):
    def maxArea(self, height):
        max_area = 0
        for l in range(len(height)): # Create nested loop to check every combination
            for r in range(l + 1, len(height)):
                area = min(height[l], height[r]) * (r - l) # Calculate area
                max_area = max(max_area, area) # update max area
        return max_area
    
# Optimal Solution Uses two pointer
    def maxArea2(self, height):
        max_area = 0 # Create variable to track area
        l, r = 0, len(height) - 1 # Create two pointer at each end of array

        while l < r: # Loop until they meet
            area = min(height[l], height[r]) * (r-l) # Calculate the area
            max_area = max(area, max_area) # Update the max area
            if height[l] < height[r]: # Move on from pointer that has a smaller value
                l += 1                # This maximizes the potential area
            else:
                r -= 1

        return max_area




my_solution = Solution()
print(my_solution.maxArea([1,8,6,2,5,4,8,3,7]))
print(my_solution.maxArea([1,1]))
