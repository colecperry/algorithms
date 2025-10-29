from typing import List

# =============================================================================
# WHAT IS THE SLIDING WINDOW PATTERN?
# =============================================================================
"""
Sliding window is a technique where we maintain a "window" (a contiguous/adjacent subarray or substring) that slides across the data structure. The window can:
    - Expand: Add elements to the right
    - Contract: Remove elements from the left
    - Slide: Move both boundaries together

The pattern transforms O(n²) or O(n*k) brute force solutions into O(n) elegant 
solutions by avoiding redundant recalculations of overlapping subarrays.

-----------------------------------------------------------------------------
Visual Example - FIXED SIZE SLIDING WINDOW (size = 3):

Array: [1, 2, 3, 4, 5, 6, 7, 8]
        [─────]                    Window 1: [1,2,3] sum=6
           [─────]                 Window 2: [2,3,4] sum=9
              [─────]              Window 3: [3,4,5] sum=12
                 [─────]           Window 4: [4,5,6] sum=15
                    [─────]        Window 5: [5,6,7] sum=18
                       [─────]     Window 6: [6,7,8] sum=21

-----------------------------------------------------------------------------
Visual Example - VARIABLE SIZE SLIDING WINDOW (sum ≤ target):

Array: [1, 2, 3, 4, 5]  Target: 5
        ↑              
       left           
       right          Window: [1] sum=1 (expand)

Array: [1, 2, 3, 4, 5]
        ↑──↑        
       left  right    Window: [1,2] sum=3 (expand)

Array: [1, 2, 3, 4, 5]
        ↑─────↑     
       left    right  Window: [1,2,3] sum=6 (contract)

Array: [1, 2, 3, 4, 5]
           ↑──↑     
          left right  Window: [2,3] sum=5 (valid!)
"""

# =============================================================================
# SLIDING WINDOW ADVANTAGE: O(n * k)/O(n^2) BRUTE FORCE vs O(n) SLIDING WINDOW
# =============================================================================
"""
════════════════════════════════════════════════════
SCENARIO 1: FIXED WINDOW SIZE (k given)
════════════════════════════════════════════════════

PROBLEM: Find maximum sum of k=3 consecutive elements
Array: [1, 2, 3, 4, 5]

────────────────────────────────────────────────────
BRUTE FORCE - O(n * k)
────────────────────────────────────────────────────
For EACH of n windows:
    Calculate sum of k elements

Window 1: 1+2+3 = 6     (3 additions)
Window 2: 2+3+4 = 9     (3 additions) ← Recalculating!
Window 3: 3+4+5 = 12    (3 additions) ← Recalculating!

Total: 3 windows x 3 additions = 9 operations
Complexity: O(n * k)

────────────────────────────────────────────────────
SLIDING WINDOW - O(n)
────────────────────────────────────────────────────
Calculate first window once, then slide

Window 1: 1+2+3 = 6     (3 additions)
Window 2: 6-1+4 = 9     (2 ops: remove left, add right)
Window 3: 9-2+5 = 12    (2 ops: remove left, add right)

Total: 3 + 2 + 2 = 7 operations
Complexity: O(n)

Key: Reuse previous sum instead of recalculating!

════════════════════════════════════════════════════
SCENARIO 2: VARIABLE WINDOW SIZE
════════════════════════════════════════════════════

PROBLEM: Find longest subarray with sum ≤ target
Array: [1, 2, 3, 4, 5], target = 7

────────────────────────────────────────────────────
BRUTE FORCE - O(n²)
────────────────────────────────────────────────────
Check ALL possible subarrays with nested loops:

for start in range(n):           # Outer loop: n times
    for end in range(start, n):  # Inner loop: up to n times
        if sum(arr[start:end+1]) <= 7:
            track length

Subarrays checked:
[1] = 1 ≤ 7 ✓ length 1
[1,2] = 3 ≤ 7 ✓ length 2
[1,2,3] = 6 ≤ 7 ✓ length 3
[1,2,3,4] = 10 > 7 ✗
[1,2,3,4,5] = 15 > 7 ✗
[2] = 2 ≤ 7 ✓ length 1
[2,3] = 5 ≤ 7 ✓ length 2
[2,3,4] = 9 > 7 ✗
[2,3,4,5] = 14 > 7 ✗
[3] = 3 ≤ 7 ✓ length 1
[3,4] = 7 ≤ 7 ✓ length 2
[3,4,5] = 12 > 7 ✗
[4] = 4 ≤ 7 ✓ length 1
[4,5] = 9 > 7 ✗
[5] = 5 ≤ 7 ✓ length 1

Total: 15 subarrays checked = O(n²)
Answer: [1,2,3] with length 3

────────────────────────────────────────────────────
VARIABLE SLIDING WINDOW - O(n)
────────────────────────────────────────────────────
Expand right, shrink left when sum exceeds target

left = 0, right = 0, curr_sum = 0, max_len = 0

[1, 2, 3, 4, 5]
 L
 R
Add arr[0]: curr_sum = 1 ≤ 7 ✓, max_len = 1

[1, 2, 3, 4, 5]
 L  R
Add arr[1]: curr_sum = 3 ≤ 7 ✓, max_len = 2

[1, 2, 3, 4, 5]
 L     R
Add arr[2]: curr_sum = 6 ≤ 7 ✓, max_len = 3

[1, 2, 3, 4, 5]
 L        R
Add arr[3]: curr_sum = 10 > 7 ✗
Shrink left: Remove arr[0], curr_sum = 9

[1, 2, 3, 4, 5]
L            R
Still > 7, shrink left: Remove arr[1], curr_sum = 7 ≤ 7 ✓

[1, 2, 3, 4, 5]
    L        R
max_len stays 3

[1, 2, 3, 4, 5]
       L     R
Add arr[4]: curr_sum = 12 > 7 ✗
Shrink left until valid...

Total: Each element visited at most twice (once by right, once by left)
Complexity: O(n)
Answer: length 3

Key: Single pass! Expand right when valid, shrink left when invalid.
    Never recalculate entire subarray sums.

════════════════════════════════════════════════════
COMPLEXITY COMPARISON
════════════════════════════════════════════════════

Array Size | Window Size | Brute Force | Sliding Window
─────────────────────────────────────────────────────────
FIXED WINDOW (k given):
    100    |     10      |   O(n*k)    |     O(n)
                         |    1,000    |      100
  1,000    |     10      |   10,000    |    1,000
 10,000    |  1,000      |10,000,000   |   10,000

VARIABLE WINDOW (any size):
    100    |   varies    |   O(n²)     |     O(n)
                         |   10,000    |      100
  1,000    |   varies    | 1,000,000   |    1,000
 10,000    |   varies    |100,000,000  |   10,000
"""

# =============================================================================
# TIME & SPACE COMPLEXITY
# =============================================================================
"""
Time Complexity Comparison:
────────────────────────────────────────────────────
Brute Force (nested loops):
- Fixed window: O(n * k) where k = window size
- Variable window: O(n²)

Sliding Window:
- Fixed window: O(n) 
- Variable window: O(n)
- Always linear time!

Space Complexity:
────────────────────────────────────────────────────
Fixed Window:
- O(1) - only track window sum/count

Variable Window:
- O(1) - if only tracking numbers
- O(k) - if using hash map for character frequencies
- O(min(k, n)) - bounded by window size or alphabet size
"""
# =============================================================================
# COMMON PROBLEMS
# =============================================================================
"""
────────────────────────────────────────────────────
Fixed Size Window:
- Maximum/minimum sum of k consecutive elements
- Average of subarrays of size k
- First negative in every window of size k

Variable Size Window:
- Longest substring with k distinct characters
- Smallest subarray with sum ≥ target
- Longest substring without repeating characters
- Minimum window substring containing all characters

String Pattern Matching:
- Find all anagrams in a string
- Permutation in string
- Substring with concatenation of words

Optimization Problems:
- Maximum/minimum subarray meeting condition
- Count of subarrays meeting condition
"""

# =============================================================================
# WINDOW TYPE IDENTIFICATION
# =============================================================================
"""
FIXED SIZE WINDOW:
─────────────────────
When you see:
- "Size k" explicitly mentioned
- "Every k consecutive elements"
- "Window of size k"

Example: "Maximum sum of subarray of size k"
Pattern: Right expands to k, then slide (right++, left++)

VARIABLE SIZE WINDOW:
────────────────────────
When you see:
- "Longest/shortest substring/subarray that..."
- "At most K distinct..."
- "Smallest subarray with sum ≥ target"

Example: "Longest substring with at most k distinct characters"
Pattern: Expand until invalid, contract until valid

Contracting Conditions (when to shrink):
- Sum/product exceeds target
- Too many distinct elements
- Duplicate found (if not allowed)
- Condition violated

DON'T use sliding window when:
────────────────────────────────────────────────────────
✗ Need non-contiguous (non-adjacent) elements (use dynamic programming or greedy)
✗ Need to find all subarrays, not just optimal one (might need nested loops)
✗ Problem involves comparing elements far apart (use hash map or two pointers)
✗ Need to track global state across non-adjacent elements
✗ Problem asks for subsequences (non adjacent) instead of subarrays (contiguous)

Example of when NOT to use:
✗ "Maximum sum of non-adjacent elements" → Dynamic Programming
✗ "Longest increasing subsequence" → Dynamic Programming  
✗ "Two sum" → Hash Map or Two Pointers (not sliding window)
✗ "All possible subarrays" → Generate all O(n²) (not optimization problem)

DECISION TREE:
────────────────────────────────────────────────────────

                    Problem involves subarrays/substrings?
                           /              \
                         NO               YES
                         ↓                 ↓
                   Different           Are they CONTIGUOUS?
                    pattern               /          \
                                        NO          YES
                                        ↓            ↓
                                  Subsequence    Fixed or variable size?
                                   problem         /            \
                                              FIXED          VARIABLE
                                                ↓                ↓
                                          Sliding Window    Sliding Window
                                          (Fixed Size)      (Two Pointers)

"""

# =============================================================================
# SLIDING WINDOW PATTERNS - COMPREHENSIVE GUIDE
# =============================================================================

# ================================================================
# PATTERN 1: FIXED WINDOW - NUMERIC TRACKING (nums/aggregates)
# PATTERN EXPLANATION: Window size k is fixed, slide by removing left element and adding right element.
# Key insight: Reuse previous sum by subtracting outgoing element and adding incoming element.
# Applications: Maximum/minimum sum of k elements, average of k elements, fixed-size operations.
# ================================================================

# PROBLEM 1: LC 643 - Maximum Average Subarray I
# Calculate initial window sum, then slide and track maximum

class Pattern1(object):
    """
    You are given an integer array nums consisting of n elements, and an integer k. Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.

    Example:
    Input: nums = [1,12,-5,-6,50,3], k = 4
    Output: 12.75000
    Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

    TC:
        - Initial sum calculation -> O(k)
        - Sliding window through remaining elements -> O(n - k)
        - Each slide operation -> O(1) (one subtraction, one addition)
        - Total -> O(n)
    SC:
        - O(1) -> only storing window_sum and max_avg variables
        - No additional data structures needed
    """
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k]) # Calculate initial window sum of first k elements
        max_avg = window_sum / float(k) # Calculate initial average

        for r in range(k, len(nums)): # R goes from k to end of arr
            window_sum += nums[r] - nums[r - k] # Slide: add new element, remove leftmost element
            max_avg = max(max_avg, window_sum / float(k)) # Update max average

        return max_avg

solution = Pattern1()
print(solution.findMaxAverage([1,12,-5,-6,50,3], 4))

# ================================================================
# PATTERN 2: FIXED WINDOW - PATTERN/ANAGRAM MATCHING
# PATTERN EXPLANATION: Fixed window size equals pattern length, compare frequency maps while sliding.
# Key insight: Match character frequencies between window and pattern, slide and update frequencies.
# Applications: Find all anagrams, permutation in string, substring matching with character counts.
# ================================================================

# PROBLEM 1: LC 438 - Find All Anagrams in a String
# Slide fixed window, compare frequency maps to find anagrams

class Pattern2(object):
    """
    Given two strings s and p, return an array of all the start indices of p's 
    anagrams in s.

    Example 1:
    Input: s = "cbaebabacd", p = "abc"
    Output: [0,6]
    Explanation: "cba" at index 0 and "bac" at index 6 are anagrams of "abc"

    Example 2:
    Input: s = "abab", p = "ab"
    Output: [0,1,2]
    Explanation: "ab" at 0, "ba" at 1, "ab" at 2 are all anagrams of "ab"

    TC: O(n)
        - Build pattern frequency map: O(m) where m = len(p)
        - Build initial window: O(m)
        - Slide window: O(n-m) iterations, each with O(1) operations
        - Total: O(n + m) = O(n)
    
    SC: O(1)
        - Frequency maps bounded by alphabet size (26 lowercase letters)
        - Constant space regardless of input size
    """
    def findAnagrams(self, s, p):
        if len(p) > len(s):  # Pattern longer than string
            return []
        
        p_count = {}  # Pattern character frequencies for p
        window_count = {}  # Current window character frequencies
        
        # Build pattern frequency map for p
        for char in p:
            p_count[char] = p_count.get(char, 0) + 1
        
        # Build initial window char count
        for i in range(len(p)):
            window_count[s[i]] = window_count.get(s[i], 0) + 1
        
        result = [] # result arr stores indexes
        
        # Check if initial window is anagram
        if window_count == p_count:
            result.append(0)
        
        # Slide window through rest of string p->s
        for right in range(len(p), len(s)):
            # Add new character entering window (right side)
            window_count[s[right]] = window_count.get(s[right], 0) + 1
            
            # Remove character leaving window (left side)
            left = right - len(p) # i leaving window
            window_count[s[left]] -= 1
            if window_count[s[left]] == 0:
                del window_count[s[left]]
            
            # Check if current window matches pattern
            if window_count == p_count:
                result.append(left + 1)  # Starting index of anagram
        
        return result

solution = Pattern2()
print(solution.findAnagrams("cbaebabacd", "abc"))  # [0, 6]
print(solution.findAnagrams("abab", "ab"))         # [0, 1, 2]

# ================================================================
# PATTERN 3: VARIABLE WINDOW - CONSTRAINT-BASED (MAXIMIZE/MINIMIZE)
# PATTERN EXPLANATION: Expand window until condition changes, contract based on goal and constraint type.
# Key insight: 
#   - Track state with SET (existence), HASHMAP (frequencies), or VARIABLE (sum/count)
#   - MAXIMIZE window: Shrink ONLY when constraint violated (duplicate found, > k distinct, sum > limit)
#   - MINIMIZE window: Shrink WHILE constraint satisfied (>= target sum, contains all required chars)
# Applications: Longest/shortest substrings with uniqueness, character limits, numeric constraints, or sum conditions
# Time: O(n) - each element enters/exits window at most once
# Space: O(1) for numeric tracking, O(k) for set/hashmap tracking, O(alphabet_size) bounded worst case
# ================================================================

# PROBLEM 1: LC 3 - Longest Substring Without Repeating Characters
# Expand until duplicate, shrink from left until no duplicates

class Pattern3(object):
    """
    Given a string s, find the length of the longest substring without repeating characters.

    Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    TC: O(n)
        - Each character enters set once (right pointer): O(n)
        - Each character leaves set at most once (left pointer): O(n)
        - Set operations (add, remove, in): O(1)
        - Total: O(2n) = O(n)
    
    SC: O(min(n, alphabet_size))
        - Set stores unique characters in current window
        - Worst case: O(n) if all characters unique
        - Bounded by alphabet (e.g., 26 for lowercase, 128 for ASCII)
    """
    def lengthOfLongestSubstring(self, s):
        left = 0  # Left boundary of window
        seen = set()  # Track characters in current window
        longest = 0  # Track max length found
        
        for right in range(len(s)):  # Expand window with R ptr
            # We have a duplicate in our substring
            while s[right] in seen: # Shrink window til dup removed
                seen.remove(s[left]) 
                left += 1 
            
            # Add current character and update max length
            seen.add(s[right])
            longest = max(longest, right - left + 1)
        
        return longest

solution = Pattern3()
print(solution.lengthOfLongestSubstring("abcabcbb"))  # 3
print(solution.lengthOfLongestSubstring("bbbbb"))     # 1

# ================================================================
# PATTERN 4: VARIABLE WINDOW - COUNT ALL VALID SUBSTRINGS
# PATTERN EXPLANATION: For each valid window ending at right, count all substrings within that window.
# Key insight: When window [left, right] is valid, there are (right - left + 1) substrings ending at right.
# Applications: Count subarrays/substrings meeting condition, not just find optimal one.
# ================================================================

# PROBLEM 1: LC 3258 - Count Substrings That Satisfy K-Constraint I
# Count all valid substrings by adding window length at each step

class Pattern4(object):
    """
    You are given a binary string s and an integer k.
    A binary string satisfies the k-constraint if either of the following conditions holds:
    - The number of 0's in the string is at most k.
    - The number of 1's in the string is at most k.
    
    Return an integer denoting the number of substrings of s that satisfy the k-constraint.

    Example 1:
    Input: s = "10101", k = 1
    Output: 12
    Explanation: Every substring except "1010", "10101", and "0101" satisfies k-constraint.

    Example 2:
    Input: s = "1010101", k = 2
    Output: 25

    TC: O(n)
        - Right pointer traverses string once: O(n)
        - Left pointer moves at most n times total: O(n)
        - Each iteration does constant work: O(1)
    
    SC: O(1)
        - Only storing pointers and count variables
    """
    def countKConstraintSubstrings(self, s, k):
        left = 0
        count = 0  # Total valid substrings
        zeros = 0  # Count of 0's in current window
        ones = 0   # Count of 1's in current window
        
        for right in range(len(s)):
            # Expand window: add current character
            if s[right] == '0':
                zeros += 1
            else:
                ones += 1
            
            # Shrink window while invalid (both counts exceed k)
            while zeros > k and ones > k:
                if s[left] == '0':
                    zeros -= 1
                else:
                    ones -= 1
                left += 1
            
            # Current window [left, right] is valid
            # Add all NEW substrings ending at right (no duplicates)
            # Example: Window [a,b,c] ending at right adds 3 substrings: "c", "bc", "abc"
            count += right - left + 1
        
        return count

solution = Pattern4()
print(solution.countKConstraintSubstrings("10101", 1))      # 12
print(solution.countKConstraintSubstrings("1010101", 2))    # 25