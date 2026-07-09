"""
=================================================================
SLIDING WINDOW COMPLETE GUIDE
=================================================================

WHAT IS SLIDING WINDOW?
-----------------------
Sliding window is a technique for efficiently computing properties of contiguous
subarrays or substrings. Instead of recomputing each window from scratch, the window
expands by adding one element on the right and contracts by removing one from the left —
reusing previous calculations at each step.

Key characteristics:
- Works on CONTIGUOUS elements (arrays and strings)
- Window boundaries defined by left and right pointers
- Each element enters and exits the window at most once -> O(n)
- Eliminates the need for nested loops (brute force O(n*k) -> O(n))

TIME COMPLEXITY ADVANTAGE:
--------------------------
Example: Max sum of k consecutive elements
- Brute force: sum all k elements for each window -> O(n * k)
- Sliding window: compute first window O(k), then slide n-k times each O(1) -> O(n)

Example: Longest substring with unique characters
- Brute force: check every substring -> O(n^2)
- Sliding window: each char enters/exits window once -> O(n)

Window types:
- Fixed size: window size k is constant (given in problem)
- Variable size: window expands until constraint violated, then contracts

When to use Sliding Window:
- "Contiguous subarray/substring with property X"
- "Longest/shortest window satisfying constraint"
- "Find all windows matching pattern"
- Constraint involves sum, count, frequency, or distinct characters

SLIDING WINDOW CORE PATTERNS
==============================
"""

from typing import List
from collections import Counter

"""
SLIDING WINDOW COMPLEXITY REFERENCE
=====================================

+---------------------------+------------------+------------------+
| Pattern                   | Time             | Space            |
+---------------------------+------------------+------------------+
| Fixed Window Numeric      | O(n)             | O(1)             |
| Fixed Window Frequency    | O(n)             | O(1) [26 letters]|
| Variable Window Maximize  | O(n)             | O(1) or O(k)     |
| Variable Window Minimize  | O(n + m)         | O(m)             |
+---------------------------+------------------+------------------+

n = array/string length, k = window size or char set size, m = pattern length

NOTES:
- Fixed numeric: one add + one subtract per slide -> O(1) per step
- Fixed frequency: Counter comparison is O(26) = O(1) for lowercase letters
- Variable maximize: right expands n times, left contracts at most n times -> O(n) total
- Variable minimize: expand until valid, shrink while valid -> also O(n) total
"""

"""
========================
SLIDING WINDOW PATTERNS
========================
"""

"""
================================================================
PATTERN 1: FIXED WINDOW NUMERIC (AGGREGATE OVER K ELEMENTS)
PATTERN EXPLANATION: Window size k is given. Compute the aggregate (sum, product)
for the first k elements, then slide: subtract the leftmost element and add the
new rightmost element in O(1) per step. Update the result at every position.
No need to re-sum the entire window — reuse the previous window's computation.

Applications: Max/min sum of k elements, average of k elements, max product subarray.
================================================================
"""

class FixedWindowNumeric:
    """
    Problem: Given an integer array nums and integer k, find the contiguous subarray
    of length k with the maximum average value. Return this maximum average.

    Example:
        nums = [1, 12, -5, -6, 50, 3], k = 4
        Windows: [1,12,-5,-6]=2, [12,-5,-6,50]=51, [-5,-6,50,3]=42
        Output: 51/4 = 12.75

    Steps:
    1. Compute sum of first k elements (initial window)
    2. Slide from index k to end:
       a. Add nums[right] (new element entering window)
       b. Subtract nums[right - k] (element leaving window)
       c. Update max_sum
    3. Return max_sum / k
    """
    def findMaxAverage(self, nums: List[int], k: int) -> float:  # LC 643
        """
        TC: O(n) - one pass through array
        SC: O(1) - only window_sum and max_sum variables
        """
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for right in range(k, len(nums)):
            window_sum += nums[right] - nums[right - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k

    # Trace: nums=[1,12,-5,-6,50,3], k=4
    # Initial window [0:3]: 1+12-5-6 = 2, max_sum=2
    # right=4 (50): 2 + 50 - 1 = 51, max_sum=51
    # right=5 (3):  51 + 3 - 12 = 42, max_sum=51
    # Output: 51/4 = 12.75 ✓

sol = FixedWindowNumeric()
print("Max Average:", sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # 12.75


"""
================================================================
PATTERN 2: FIXED WINDOW FREQUENCY (ANAGRAM / PATTERN MATCHING)
PATTERN EXPLANATION: Window size equals the pattern length. Build frequency maps for
the pattern and the initial window. Slide by decrementing the outgoing character count
and incrementing the incoming character count. Match check is O(1) (26-entry comparison).
Delete a key when its count hits zero to keep the Counter clean for equality checks.

Applications: Find all anagrams, permutation in string, repeated DNA sequences.
================================================================
"""

class FixedWindowFrequency:
    """
    Problem: Given strings s and p, return all start indices of p's anagrams in s.
    An anagram of p is any permutation of p's characters.

    Example:
        s = "cbaebabacd", p = "abc"
        "cba" at index 0, "bac" at index 6 -> Output: [0, 6]

    Steps:
    1. Build Counter for pattern p and for first len(p) characters of s
    2. If they match, record index 0
    3. Slide window from len(p) to end:
       a. Increment incoming character (right side)
       b. Decrement outgoing character (left side), remove if count reaches 0
       c. If window Counter matches pattern Counter, record start index
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:  # LC 438
        """
        TC: O(n) - single pass; Counter comparison is O(26) = O(1)
        SC: O(1) - frequency maps bounded by alphabet size (26 letters)
        """
        if len(p) > len(s):
            return []

        p_count = Counter(p)
        window = Counter(s[:len(p)])
        result = []

        if window == p_count:
            result.append(0)

        for right in range(len(p), len(s)):
            left = right - len(p)
            window[s[right]] += 1
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]

            if window == p_count:
                result.append(left + 1)

        return result

    # Trace: s="cbaebabacd", p="abc", p_count={a:1,b:1,c:1}
    # Initial window "cba": {c:1,b:1,a:1} == p_count -> result=[0]
    # Slide to "bae": add 'e', remove 'c' -> {b:1,a:1,e:1} != p_count
    # ...
    # Window at index 6 "bac": {b:1,a:1,c:1} == p_count -> result=[0,6] ✓

sol = FixedWindowFrequency()
print("Anagram Indices:", sol.findAnagrams("cbaebabacd", "abc"))  # [0, 6]
print("Anagram Indices:", sol.findAnagrams("abab", "ab"))         # [0, 1, 2]


"""
================================================================
PATTERN 3: VARIABLE WINDOW MAXIMIZE (LONGEST VALID WINDOW)
PATTERN EXPLANATION: Expand the window by moving right. When the window becomes INVALID,
shrink from the left until it is valid again. After shrinking, always record the window
size (it is always valid at this point). Goal: find the LONGEST window that never violates
the constraint. The while loop for shrinking only removes the minimum needed.

Applications: Longest substring without repeating chars, longest subarray with sum <= k,
longest substring with at most k distinct characters.
================================================================
"""

class VariableMaximize:
    """
    Problem: Find the length of the longest substring without any repeating characters.

    Example:
        s = "abcabcbb"
        Longest: "abc" -> Output: 3

    Steps:
    1. Initialize left=0, empty set for characters in window
    2. For each right:
       a. While s[right] already in window (duplicate): remove s[left], left += 1
       b. Add s[right] to window
       c. Update max_length with current window size (right - left + 1)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:  # LC 3
        """
        TC: O(n) - right visits each char once; left moves at most n times total
        SC: O(min(n, 26)) - set stores at most alphabet_size characters
        """
        left = 0
        seen = set()
        max_length = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

    # Trace: s = "abcabcbb"
    # r=0 'a': seen={a}, max=1
    # r=1 'b': seen={a,b}, max=2
    # r=2 'c': seen={a,b,c}, max=3
    # r=3 'a': 'a' in seen -> remove 'a', left=1; seen={b,c,a}, max=3
    # r=4 'b': 'b' in seen -> remove 'b', left=2; seen={c,a,b}, max=3
    # r=5 'c': 'c' in seen -> remove 'c', left=3; seen={a,b,c}, max=3
    # r=6 'b': 'b' in seen -> remove 'a',left=4; still 'b' -> remove 'b',left=5; seen={c,b}, max=3
    # r=7 'b': 'b' in seen -> remove 'c',left=6; still 'b' -> remove 'b',left=7; seen={b}, max=3
    # Output: 3 ✓

sol = VariableMaximize()
print("Longest Unique:", sol.lengthOfLongestSubstring("abcabcbb"))  # 3
print("Longest Unique:", sol.lengthOfLongestSubstring("bbbbb"))     # 1


"""
================================================================
PATTERN 4: VARIABLE WINDOW MINIMIZE (SHORTEST VALID WINDOW)
PATTERN EXPLANATION: Expand the window until it becomes VALID (satisfies the constraint),
then SHRINK from the left WHILE it remains valid, recording the minimum at each shrink
step. Goal: find the SHORTEST window that satisfies the constraint. The while loop
for shrinking continues as long as the window is still valid — opposite of maximize.

Applications: Minimum window substring, smallest subarray with sum >= k.
================================================================
"""

class VariableMinimize:
    """
    Problem: Given strings s and t, return the minimum window substring of s such that
    every character in t (including duplicates) is included. Return "" if none exists.

    Example:
        s = "ADOBECODEBANC", t = "ABC"
        Minimum window: "BANC" (length 4) -> Output: "BANC"

    Steps:
    1. Build frequency map for t; track required = number of unique chars needed
    2. Expand right: add char to window; if its count matches t's count, increment formed
    3. While window is valid (formed == required): shrink from left
       a. Update minimum window if current is smaller
       b. Remove s[left] from window; if count drops below t's count, decrement formed
       c. left += 1
    4. Return the minimum window found
    """
    def minWindow(self, s: str, t: str) -> str:  # LC 76
        """
        TC: O(n + m) where n = len(s), m = len(t)
        SC: O(m) - frequency maps
        """
        if not s or not t:
            return ""

        t_count = Counter(t)
        window = {}
        required = len(t_count)
        formed = 0
        left = 0
        min_len = float('inf')
        min_left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            if char in t_count and window[char] == t_count[char]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left
                lc = s[left]
                window[lc] -= 1
                if lc in t_count and window[lc] < t_count[lc]:
                    formed -= 1
                left += 1

        return "" if min_len == float('inf') else s[min_left:min_left + min_len]

    # Trace: s="ADOBECODEBANC", t="ABC", t_count={A:1,B:1,C:1}, required=3
    # Expand until A,B,C all in window -> "ADOBEC" (right=5), formed=3
    # Shrink: remove A, formed=2 -> stop; min="ADOBEC" (len=6), min_left=0
    # Continue expanding -> find "BANC" (right=11, left=9) as new minimum
    # Output: "BANC" ✓

sol = VariableMinimize()
print("Min Window:", sol.minWindow("ADOBECODEBANC", "ABC"))  # "BANC"
print("Min Window:", sol.minWindow("a", "a"))                # "a"
