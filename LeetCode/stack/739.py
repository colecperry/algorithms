# 739. Daily Temperatures

# Topics: Array, Stack, Monotonic Stack

# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]

from typing import List

class Solution:
        """
        - TC: O(n) - each index pushed and popped at most once
        - SC: O(n) - stack can store up to n indices
        """
        def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            n = len(temperatures)
            answer = [0] * n 
            stack = []  # Stores indices of days waiting for a warmer day - maintains DECREASING temperature order
            
            for i, temp in enumerate(temperatures):            
                # While current temp is warmer than stack top:
                # Pop those days - they found their answer (today is their warmer day!)
                while stack and temp > temperatures[stack[-1]]:
                    prev_index = stack.pop()
                    answer[prev_index] = i - prev_index  # Days waited = today - that day
                
                # Add current day to stack (it's now waiting for a warmer day)
                stack.append(i)
            
            # Days still in stack never found warmer weather (already 0)
            return answer

sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73])) # [1,1,4,2,1,1,0,0]
print(sol.dailyTemperatures([30,40,50,60])) # [1,1,1,0]
print(sol.dailyTemperatures([30,60,90])) # [1,1,0]