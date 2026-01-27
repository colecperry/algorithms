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

from typing import List
    
def maxArea(height: List[int]) -> int:
        """
        TC: O(n) - single pass with two pointers
        SC: O(1) - only tracking pointers and max
        """
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate area: width × height (limited by shorter line)
            width = right - left
            min_height = min(height[left], height[right])
            area = width * min_height
            max_area = max(area, max_area)
            
            # Move the shorter line (value) inward 
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area


print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))
