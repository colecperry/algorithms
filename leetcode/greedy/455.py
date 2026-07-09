# 455. Assign Cookies

# Topics: Array, Two Pointer, Greedy, Sorting

# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

# Example 1:

# Input: g = [1,2,3], s = [1,1]
# Output: 1
# Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
# And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
# You need to output 1.

# Example 2:

# Input: g = [1,2], s = [1,2,3]
# Output: 2
# Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
# You have 3 cookies and their sizes are big enough to gratify all of the children, 
# You need to output 2.

"""
Problem: Assign Cookies (LeetCode 455)

High-level approach:
    1. Sort children by greed factor (ascending) - satisfy least greedy first
    2. Sort cookies by size (ascending) - use smallest adequate cookie
    3. Use two pointers to greedily match cookies to children
    4. For each child, find the smallest cookie that satisfies them
    5. Move to next child only when current child is satisfied

Greedy strategy works because:
- Always better to satisfy less greedy child with smaller cookie
- Leaves larger cookies available for more greedy children

Time Complexity: O(n log n + m log m)
- Sorting children: O(n log n) where n = len(g)
- Sorting cookies: O(m log m) where m = len(s) 
- Two-pointer traversal: O(n + m)
- Overall: O(n log n + m log m) - dominated by sorting (ignore O(n) and O(m))

Space Complexity: O(1) 
- Only using constant extra space (pointers, counter)
- Sorting is done in-place
- If considering sorting space: O(log n + log m) for recursion stack
"""

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # edge case -> no cookies or kids, return 0
        if not s or not g:
            return 0
        # sort the greed factors (maximize the # of children we can feed)
        # sort the cookies (use a two pointer to match the cookies with the greed efficiently)
        g.sort()
        s.sort()
        # two pointers, i + j, output variable (integer)
        i, j = 0, 0
        kids_satisifed = 0

        while j < len(s) and i < len(g):
            # if the cookie is big enough, increment the output, move both pointers forward
            if s[j] >= g[i]:
                kids_satisfied += 1
                i += 1
                j += 1
            # if cookie is not big enough, move the cookie index forward
            else:
                j += 1
        # return the output variable once we reach end of cookie list
        return kids_satisfied

sol = Solution()
print(sol.findContentChildren([1,2,3], [1,1])) # 1
print(sol.findContentChildren([1,2], [1,2,3])) # 2

