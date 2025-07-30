# 228. Summary Ranges

# You are given a sorted unique integer array nums. A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b

# Example 1:
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"

# Example 2:
# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"

# How to Solve (For Loop):
# - Initialize an output list and a variable to track the start of the current range.
# - Iterate through the list from index 1 to the end.
# - If the current number is not consecutive (i.e., not equal to previous + 1), the range ends:
#     - If the range is a single number, add just that number to output.
#     - If it's a range, format it as "start->end".
#     - Update the start to the current number.
# - After the loop, handle the final range similarly since it's not automatically added in the loop.

# Time Complexity (TC):
# - O(n), where n is the length of the input list.
# - Each element is visited exactly once.

# Space Complexity: O(n)
# - In the worst case, each number becomes its own range (e.g., [1, 3, 5, 7])
# - So the output list could have up to n entries

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]: # for loop
        if not nums: # Edge case for empty list
            return []

        output = [] 
        start = nums[0] # Track starting index of each range (initial is first number)

        for i in range(1, len(nums)): # Loop from second number
            if nums[i] != nums[i - 1] + 1: # If curr != prev + 1, reached end of range
                if start == nums[i - 1]: # If range is a single num
                    output.append(str(start))
                else: # If range is multiple numbers
                    output.append(f"{start}->{nums[i - 1]}")
                start = nums[i]  # start new range each loop/time we append

        # Add the final range
        if start == nums[-1]: # If start of range is last number in the arr
            output.append(str(start)) # Append single num
        else:
            output.append(f"{start}->{nums[-1]}") # Append range

        return output
    
    # How to Solve (while loop)
    # 1. Initialize a pointer `i` at the beginning of the list.
    # 2. Use a while loop to traverse the list until `i` reaches the end.
    # 3. For each iteration, mark the start of a new potential range.
    # 4. Use an inner while loop to extend the range as long as the next number is consecutive.
    # 5. When the end of a range is found, format the result:
    #    - If the range is one number, just add it.
    #    - If the range includes multiple numbers, add it in "start->end" format.
    # 6. Move `i` forward and repeat.
    # 7. Return the list of formatted range strings.

    # Time Complexity: O(n)
    # - We visit each element in the list once while building ranges.

    # Space Complexity: O(n)
    # - In the worst case (e.g., no consecutive numbers), we store n individual strings in the output list.

        
    def summaryRanges2(self, nums: List[int]) -> List[str]: # while loop solution
        i = 0 # manual pointer for while loop
        output = []
        while i < len(nums):
            start = i # set starting range
            # Increment i while next index not OOB and current num + 1 == next num
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]: 
                i += 1 
            # Once current num + 1 != next num
            if start == i: # Start == i if only single num in the range
                output.append(str(nums[i])) # Append single num
            else: # If multiple nums in the range
                output.append(f'{nums[start]}->{nums[i]}') # Append range of nums
            i += 1 # Increment i after appending
        return output
    



sol = Solution()
#                        i
#                        S E
print(sol.summaryRanges2([0,1,2,4,5,7])) # ["0->2","4->5","7"]
#                        i
#                        S 
print(sol.summaryRanges2([0,2,3,4,6,8,9])) # ["0","2->4","6","8->9"]