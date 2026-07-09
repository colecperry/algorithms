# 2379. Minimum Recolors to Get K Consecutive Black Blocks

# Topics: String, Sliding Window

# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

# You are also given an integer k, which is the desired number of consecutive black blocks.

# In one operation, you can recolor a white block such that it becomes a black block.

# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

# Example 1:
# Input: blocks = "WBBWWBBWBW", k = 7
# Output: 3
# Explanation: One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks so that blocks = "BBBBBBBWBW". 
# It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations. Therefore, we return 3.

# Example 2:
# Input: blocks = "WBWBBBW", k = 2
# Output: 0
# Explanation: No changes need to be made, since 2 consecutive black blocks already exist. Therefore, we return 0.

# How to Solve (Sliding Window):
#   - Use a sliding window of size k to scan through the string.
#   - For each window, count how many white blocks (operations)
#     are in that window.
#   - The fewer whites in the window, the fewer recolors are 
#     needed.
#   - Track the minimum number of white blocks across all 
#     windows of size k.

# Steps:
    # 1. Initialize a left pointer at 0 and a running count of 
    #    white blocks in the current window.
    # 2. Loop through the string with a right pointer.
    # 3. For each character:
    #     - If it's 'W', increment the current white count.
    # 4. Once the window size hits k:
    #     - Update the minimum number of white blocks seen so
    #       far.
    #     - Before moving the window, check if the leftmost 
    #       character is 'W' and subtract from the count if 
    #       needed.
    #     - Slide the window forward (increment left pointer).
    # 5. After the loop, return the minimum white count found (i.
    #    e., the minimum number of recolors needed).

# Time Complexity: O(n)
# - Each character is visited once as the window slides through the string.

# Space Complexity: O(1)
# - Only a few integer variables are used for counting and tracking the window.

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        curr_ops = 0 # Current number of operations in the window
        min_ops = float('inf') # Track min number of operations, start at infinity

        for r in range(len(blocks)):
            if blocks[r] == 'W':
                curr_ops += 1

            # When window size reaches k
            if r - l + 1 == k:
                min_ops = min(min_ops, curr_ops) # Update min number of ops for window size k

                # Move left pointer: subtract if it was 'W'
                if blocks[l] == 'W':
                    curr_ops -= 1
                l += 1

        return min_ops

sol = Solution()
print(sol.minimumRecolors("WBBWWBBWBW", 7))
print(sol.minimumRecolors("WBWBBBW", 2))