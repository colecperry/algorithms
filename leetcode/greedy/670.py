# 670. Maximum Swap

# Topics: Math, Greedy

# You are given an integer num. You can swap two digits at most once to get the maximum valued number.

# Return the maximum valued number you can get.

# Example 1:

# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:

# Input: num = 9973
# Output: 9973
# Explanation: No swap.

"""
BIG PICTURE:
- Given a number, swap at most two digits to get the maximum valued number
- Goal: find the leftmost digit that can be swapped with a larger digit to its right
- Key insight: we want to swap the leftmost small digit with the rightmost large digit

WHY GREEDY WORKS:
- Swapping digits at earlier positions has bigger impact (e.g., swapping at position 0 changes thousands place)
- We want to find the first position where we can upgrade to a larger digit
- Among multiple occurrences of the max digit, choose the rightmost to maximize the result

APPROACH:
1. Build a "max_to_right" array: for each position, store the largest digit from that position to the end by iterating right to left
2. Scan left-to-right to find first position where current digit < max available to its right
3. Find the rightmost occurrence of that max digit and swap
4. Return immediately (only one swap allowed)

EXAMPLE: num = 2736
- max_to_right = [7, 7, 6, 6]
- Position 0: 2 < 7? (Is current digit less than max available to its right?) YES! Find rightmost 7 (index 1), swap
- Result: 7236

TC: O(n) where n = number of digits (two passes through the number)
SC: O(n) for the max_to_right array and string conversion
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num)) # Convert int to string list
        max_to_right = [num[-1]] # Array stores the max # to the right of curr idx, init with last num (max to right of last num in arr is the last num)
        for i in range(len(num) - 2, -1, -1): # Iterate from second to last idx
            max_num = max(num[i], max_to_right[0])  # Find max_num for curr idx by comparing curr with front of max_to_right
            max_to_right.insert(0, max_num) # Insert at front
        
        # Find first position where num[i] < max_to_right[i]
        for i in range(len(num)):
            if num[i] < max_to_right[i]:
                # Find the RIGHTMOST occurrence of max_to_right[i]
                for j in range(len(num) - 1, i, -1): # iterate backwards to i
                    if num[j] == max_to_right[i]:
                        # Swap and return immediately
                        num[i], num[j] = num[j], num[i]
                        return int(''.join(num))
        
        # No swap needed (number is already max)
        return int(''.join(num))

sol = Solution()
print(sol.maximumSwap(2736)) # 7236
print(sol.maximumSwap(9973)) # 9973