# 414 - Third Number

# Topics - Array, Sorting

# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

# Example 1:
# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.

# Example 2:
# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.

# Example 3:
# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.

# Note to self: Third max number means third largest number

# How to Solve: (Sorting)
    # Sort the elements from largest to smallest (allows us to compare ele's and count distinct ele's)
    # Start count at 1 (count first element) which counts the number of distinct nums encountered until now
    # Loop and compare ele with prev element
        # If different, increase count, update current distinct num
        # If count gets to 3 (3 distinct nums), return that num
    # Return the first ele if we don't get to 3 distinct ele's

    # Time complexity: O(N log N): Sorting the array takes O(N log N), iterating through the array takes O(n), so the total time complexity is O(N log N + N) = O(N log N)
    # Space complexity: O(1): No extra space

# How to Solve: (Min Heap):
    # Big picture: Use a min heap to ensure smallest of top three numbers is at the root, use a hash set to to track and prevent insertion of already used numbers
    # Code:
        # Initialize a min heap to keep track of the smallest element (root), and a hash set to track inserted numbers to prevent duplicates
        # Loop through nums array
            # If that num is already in the set, it is a duplicate, skip
            # If the heap has three nums in it: (we always want to have three largest nums)
                # Remove min_heap root from hash set, remove root from hash set
                # Add new num into heap, add new num into hash set

            # If the heap does not have three nums in it:
                # Push the current num into the heap
                # Add the current num into the hash set
        
        # After loop ends, if heap:
            # Only has one element -> Return the root of the min heap (which is the max element)
            # Has two elements -> return the child (which would be the max element)
            # Has three or more elements -> Return the root (which is the smallest ele)


import heapq

class Solution(object):
    def thirdMax(self, nums):
        nums.sort(reverse=True) 
        count = 1 # Count the first ele
        distinct_num = nums[0]  # Start with the largest element

        for i in range(1, len(nums)):  # Start from index 1 to avoid OOB
            if nums[i] != nums[i - 1]:  # Compare with previous element
                count += 1 # + count if dif ele's
                distinct_num = nums[i] # Update max num
                if count == 3: # If we find 3 distinct nums
                    return nums[i] # Return that num

        return nums[0]  # Return the max if there is no third max
    
    def thirdMax2(self, nums):
        min_heap = [] # Initialize a min heap
        taken = set() # Initialize a hash set to track nums inserted in the min heap

        for i in range(len(nums)):
            if nums[i] in taken: # If current num already in min heap
                continue # skip

            if len(min_heap) == 3: # If min heap already has three numbers
                if nums[i] > min_heap[0]: # If current num greater than smallest num in min heap (notice there is no "else" here, if we encounter a number smaller than the root we ignore)
                    taken.remove(min_heap[0]) # Remove smallest num from hash set
                    heapq.heappop(min_heap) # Pop off smallest num from heap (root)

                    heapq.heappush(min_heap, nums[i]) # Push new num into heap
                    taken.add(nums[i]) # Add new num into hash set
                    
            # If min heap does not have three numbers we can push it.
            else:
                heapq.heappush(min_heap, nums[i])
                taken.add(nums[i])
        
        # 'nums' has only one distinct element it will be the maximum.
        if len(min_heap) == 1:
            return min_heap[0]
        
        # 'nums' has two distinct elements.
        elif len(min_heap) == 2:
            return min_heap[1]
        
        return min_heap[0]


my_solution = Solution()
print(my_solution.thirdMax2([3,2,1]))
print(my_solution.thirdMax2([1,2]))
print(my_solution.thirdMax2([2,2,3,1]))
print(my_solution.thirdMax2([2, 3, 1, 5, 6, 4]
))