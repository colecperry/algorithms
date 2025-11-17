"""
=================================================================
SLIDING WINDOW COMPLETE GUIDE
=================================================================

WHAT IS SLIDING WINDOW?
-----------------------
Sliding window is a technique where we maintain a contiguous subarray or substring that slides across the data structure. The window can expand (add elements on right), contract (remove elements from left), or slide (move both boundaries).

Key characteristics:
- Works on arrays and strings (contiguous elements)
- Window boundaries defined by two pointers (left and right)
- Reduces O(n²) or O(n*k) to O(n) by reusing calculations
- Each element enters and exits window at most once
- Must be CONTIGUOUS - elements must be next to eachother (neighbors) in the arr

TIME COMPLEXITY ADVANTAGE:
-------------------------
Brute Force vs Sliding Window:

Example: Find max sum of k consecutive elements in array of size n
- Brute Force: Calculate sum for each k-sized window independently
  TC: O(n * k) - for each of n-k+1 windows, sum k elements
  
- Sliding Window: Calculate first window, then reuse by adding/removing one element
  TC: O(n) - calculate first window O(k), then slide n-k times O(1) each
  
Speedup: O(n*k) → O(n)
For n=1000, k=100: 100,000 operations → 1,000 operations (100x faster!)

Example: Find longest substring with at most k distinct characters
- Brute Force: Check every substring, count distinct chars
  TC: O(n²) - n² substrings, each needs O(n) to count distinct
  
- Sliding Window: Expand/contract window while tracking frequencies
  TC: O(n) - each element added/removed once from frequency map
  
Speedup: O(n³) or O(n²) → O(n)

KEY INSIGHT: Sliding window avoids redundant recalculation by:
1. Reusing previous window's computation
2. Incremental updates (add one, remove one)
3. Each element processed at most twice (enter window, exit window)

Window types:
- Fixed size: Window size k is constant, slide together
- Variable size: Window expands/contracts based on conditions

When to use Sliding Window:
- Problem involves CONTIGUOUS subarrays or substrings
- Need optimal (longest/shortest) or count of valid windows
- Window has constraint (sum, distinct chars, frequencies)
- Problem mentions "consecutive", "subarray", "substring"

When NOT to use Sliding Window:
- Need NON-CONTIGUOUS elements (use DP or hash map)
- Problem asks for subsequences (can skip elements)
- Elements can be far apart (use two pointers or hash map)
- Need all possible subarrays, not optimal (use nested loops)

Common sliding window problem types:
- Maximum/minimum sum of k consecutive elements
- Longest/shortest substring with constraints
- Count subarrays meeting condition
- Pattern matching (anagrams, permutations)
- Character frequency constraints

SLIDING WINDOW CORE TEMPLATES
==============================
"""

from typing import List
from collections import defaultdict, Counter

from collections import Counter, defaultdict

# ================================================================
# FIXED SIZE WINDOW TEMPLATE
# ================================================================
def fixed_window_template(arr, k):
    """
    Template for fixed size sliding window
    
    PROBLEM CONTEXT:
    Find the maximum sum of any contiguous subarray of size k.
    Example: arr = [2,1,5,1,3,2], k = 3
    Subarrays: [2,1,5]=8, [1,5,1]=7, [5,1,3]=9, [1,3,2]=6
    Output: 9 (maximum sum)
    
    TC: O(n) - each element enters and exits window once
    SC: O(1) for numeric tracking, O(k) for frequency tracking
    
    WHEN TO USE:
    - Window size k is given
    - "Every k consecutive elements"
    - "Subarray of size k"
    - "Maximum/minimum of all k-sized windows"
    
    PATTERN:
    1. Calculate initial window (first k elements)
    2. Slide window: remove left, add right
    3. Update result at each position
    4. Return optimal result
    """
    if len(arr) < k:
        return 0
    
    # Step 1: Calculate initial window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Step 2: Slide window across array
    for right in range(k, len(arr)):
        # Remove leftmost element, add new right element
        window_sum += arr[right] - arr[right - k]
        # Update maximum
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Example usage
arr = [2, 1, 5, 1, 3, 2]
k = 3
result = fixed_window_template(arr, k)
print(f"Maximum sum of size {k}: {result}")  # Output: 9


# ================================================================
# VARIABLE SIZE WINDOW TEMPLATE
# ================================================================
def variable_window_template(arr, target):
    """
    Template for variable size sliding window
    
    PROBLEM CONTEXT:
    Find the length of the longest subarray with sum less than or equal to target.
    Example: arr = [1,2,3,4,5], target = 8
    Longest subarray: [1,2,3] (length 3)
    Output: 3
    
    TC: O(n) - right expands n times, left contracts at most n times
    SC: O(1) for numeric, O(k) for hash map tracking
    
    WHEN TO USE:
    - "Longest/shortest substring/subarray that..."
    - "At most K distinct..."
    - "Minimum window containing..."
    - Window size is NOT fixed
    
    PATTERN (for MAXIMIZE - longest valid window):
    1. Expand right to grow window
    2. Update window state
    3. While constraint violated: shrink from left
    4. Track maximum valid window
    
    PATTERN (for MINIMIZE - shortest valid window):
    1. Expand right to grow window
    2. While constraint satisfied: shrink from left
    3. Track minimum valid window
    """
    left = 0
    max_length = 0 # Track the max sub array
    window_sum = 0 # sum must be <= target
    
    for right in range(len(arr)):
        # Step 1: Expand - add element at right
        window_sum += arr[right]
        
        # Step 2: Contract - shrink while constraint violated
        # (for maximize: shrink when invalid)
        while window_sum > target:
            window_sum -= arr[left]
            left += 1
        
        # Step 3: Update result with current valid window
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example usage
arr = [1, 2, 3, 4, 5]
target = 8
result = variable_window_template(arr, target)
print(f"Longest subarray with sum <= {target}: {result}")  # Output: 3


# ================================================================
# FREQUENCY MAP TEMPLATE
# ================================================================
def frequency_window_template(s, pattern):
    """
    Template for sliding window with character frequencies
    
    PROBLEM CONTEXT:
    Find all starting indices of anagrams of pattern in string s.
    Example: s = "cbaebabacd", pattern = "abc"
    Anagrams of "abc": "cba" at index 0, "bac" at index 6
    Output: [0, 6]
    
    TC: O(n) - single pass through string
    SC: O(k) where k = alphabet size or pattern length
    
    WHEN TO USE:
    - Match character frequencies
    - Find anagrams or permutations in string
    - Track distinct characters
    - "Contains all characters of..."
    
    PATTERN:
    1. Build frequency map for target pattern
    2. Build frequency map for sliding window
    3. Slide and update frequencies
    4. Compare maps to check if window is valid
    """
    if len(s) < len(pattern):
        return []
    
    # Step 1: Build target frequency map
    pattern_freq = Counter(pattern)
    window_freq = defaultdict(int)
    result = []
    k = len(pattern)  # Fixed window size
    
    # Step 2: Build initial window
    for i in range(k):
        window_freq[s[i]] += 1
    
    # Check if initial window is anagram of "pattern"
    if window_freq == pattern_freq:
        result.append(0)
    
    # Step 3: Slide window and update frequencies
    for right in range(k, len(s)):
        # Add new character on right
        window_freq[s[right]] += 1
        
        # Remove character on left
        left = right - k
        window_freq[s[left]] -= 1
        if window_freq[s[left]] == 0:
            del window_freq[s[left]]  # Remove if count becomes 0
        
        # Step 4: Check if current window matches pattern
        if window_freq == pattern_freq:
            result.append(left + 1)  # Starting index of anagram
    
    return result

# Example usage
s = "cbaebabacd"
pattern = "abc"
result = frequency_window_template(s, pattern)
print(f"Anagram starting indices: {result}")  # Output: [0, 6]

"""
COMPLEXITY QUICK REFERENCE
==========================

Sliding Window Efficiency:
- Brute force: O(n*k) for fixed, O(n²) for variable
- Sliding window: O(n) for both
- Space: O(1) to O(k) depending on tracking needs

Why Sliding Window is Fast:
- Reuses calculations from previous window
- Each element enters window once (right pointer)
- Each element exits window once (left pointer)
- No redundant recalculation of window properties

Common Time Complexities:
- Fixed window: O(n) - slide through array once
- Variable window: O(n) - right expands n times, left contracts at most n times
- With frequency map: O(n) - map operations are O(1) per character

Space Complexities:
- Numeric tracking (sum, count): O(1)
- Set tracking (distinct chars): O(min(n, alphabet_size))
- Frequency map: O(k) where k = window size or alphabet size
- Result array: O(n) if storing all valid positions

Pattern Time/Space:
1. Fixed - Numeric: O(n) time, O(1) space
2. Fixed - Frequency: O(n) time, O(k) space
3. Variable - Optimize: O(n) time, O(1) to O(k) space
4. Variable - Count All: O(n) time, O(1) to O(k) space

Key Optimization:
- Fixed window: Slide by removing left, adding right (reuse sum)
- Variable window: Each element processed at most twice (expand + contract)
- Both avoid nested loops and redundant calculations

When to Use Each Pattern:
1. Fixed - Numeric: Window size k given, track sum/max/min
2. Fixed - Frequency: Window size k given, match character counts
3. Variable - Optimize: Find longest/shortest, maximize/minimize
4. Variable - Count: Count all valid windows, not just one
"""

"""
SLIDING WINDOW PATTERNS
=======================
"""

# ================================================================
# PATTERN 1: FIXED WINDOW - NUMERIC TRACKING
# PATTERN EXPLANATION: Window size k is fixed and given. Calculate sum/product/aggregate for initial window of k elements, then slide window one position at a time. Remove leftmost element and add new rightmost element, updating aggregate. Avoid recalculating entire window each time by reusing previous result.
#
# TYPICAL STEPS:
# 1. Calculate aggregate for initial window [0, k-1]
# 2. For each position from k to n-1:
#    - Remove element at (right - k) from window
#    - Add element at right to window
#    - Update aggregate
#    - Track optimal result
# 3. Return maximum/minimum aggregate found
#
# Applications: Max sum of k elements, average of k elements, max/min in fixed window.
# ================================================================

class FixedNumericPattern:
    """
    Problem: Given array of integers nums and integer k, find contiguous subarray of length k that has the maximum average value. Return this maximum average.
    
    TC: O(n) - calculate initial window O(k), slide through remaining O(n-k), each slide O(1)
    SC: O(1) - only store window_sum and max_avg variables
    
    How it works:
    1. Calculate sum of first k elements
    2. This is our initial window
    3. Slide window: subtract leftmost, add rightmost
    4. Update max average after each slide
    5. Return maximum average found
    
    Why it's efficient:
    - Initial calculation: O(k)
    - Each slide: O(1) (one subtraction, one addition)
    - Total: O(k + n - k) = O(n)
    - Compare to brute force: O(n * k)
    """
    def findMaxAverage(self, nums: List[int], k: int) -> float: # LC 643
        # Calculate initial window sum
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        # Slide window through rest of array
        for right in range(k, len(nums)):
            # Remove left element, add right element
            window_sum += nums[right] - nums[right - k]
            max_sum = max(max_sum, window_sum)
        
        return max_sum / k

# Example:
# nums = [1,12,-5,-6,50,3], k = 4
#
# Initial window [0:3]: [1,12,-5,-6]
#   window_sum = 1+12-5-6 = 2
#   max_sum = 2
#
# Slide to [1:4]: [12,-5,-6,50]
#   Remove nums[0]=1, add nums[4]=50
#   window_sum = 2 - 1 + 50 = 51
#   max_sum = 51
#
# Slide to [2:5]: [-5,-6,50,3]
#   Remove nums[1]=12, add nums[5]=3
#   window_sum = 51 - 12 + 3 = 42
#   max_sum = 51 (no update)
#
# max_avg = 51 / 4 = 12.75
# Output: 12.75

sol = FixedNumericPattern()
print("Max average:", sol.findMaxAverage([1,12,-5,-6,50,3], 4))  # 12.75
print("Max average:", sol.findMaxAverage([5], 1))  # 5.0


# ================================================================
# PATTERN 2: FIXED WINDOW - FREQUENCY MATCHING
# PATTERN EXPLANATION: Window size equals pattern length. Build frequency maps for both pattern and current window. Slide window while maintaining frequency map - decrement count for outgoing character, increment for incoming character. Compare frequency maps at each position to detect matches (anagrams, permutations).
#
# TYPICAL STEPS:
# 1. Build frequency map for target pattern
# 2. Build frequency map for initial window (first k characters)
# 3. Check if initial window matches pattern
# 4. Slide window through rest of string:
#    - Decrement frequency of outgoing character (left)
#    - Increment frequency of incoming character (right)
#    - Remove character from map if count becomes 0
#    - Check if current window matches pattern
# 5. Return all positions where match occurs
#
# Applications: Find anagrams, permutation in string, pattern matching with frequency.
# ================================================================

class FixedFrequencyPattern:
    """
    Problem: Given strings s and p, return array of all start indices of p's anagrams in s. An anagram is a word formed by rearranging letters.
    
    TC: O(n) where n = len(s)
        - Build pattern map: O(m) where m = len(p)
        - Build initial window: O(m)
        - Slide window: O(n-m) iterations, each O(1)
        - Total: O(n + m) = O(n)
    SC: O(1) - frequency maps bounded by alphabet size (26 lowercase letters)
    
    How it works:
    1. Build frequency map for pattern p
    2. Build frequency map for first k=len(p) characters of s
    3. If maps match, found anagram at index 0
    4. Slide window:
       - Remove outgoing character (decrement count)
       - Add incoming character (increment count)
       - Compare maps to check if current window is anagram
    5. Return all starting indices where anagrams found
    """
    def findAnagrams(self, s: str, p: str) -> List[int]: # LC 438
        if len(p) > len(s):
            return []
        
        # Build frequency maps
        p_count = Counter(p)
        window_count = Counter(s[:len(p)])
        result = []
        
        # Check initial window
        if window_count == p_count:
            result.append(0)
        
        # Slide window through rest of string
        for right in range(len(p), len(s)):
            # Add incoming character (right side)
            window_count[s[right]] += 1
            
            # Remove outgoing character (left side)
            left = right - len(p)
            window_count[s[left]] -= 1
            if window_count[s[left]] == 0:
                del window_count[s[left]]
            
            # Check if current window is anagram
            if window_count == p_count:
                result.append(left + 1)
        
        return result

# Example:
# s = "cbaebabacd", p = "abc"
# Pattern freq: {'a':1, 'b':1, 'c':1}
#
# Window 1 [0:2]: "cba"
#   freq: {'c':1, 'b':1, 'a':1}
#   Matches! Add index 0
#
# Slide to [1:3]: "bae"
#   Remove 'c', add 'e'
#   freq: {'b':1, 'a':1, 'e':1}
#   No match
#
# Slide to [2:4]: "aeb"
#   Remove 'b', add 'b'
#   freq: {'a':1, 'e':1, 'b':1}
#   No match
#
# Continue sliding...
#
# Window at [6:8]: "bac"
#   freq: {'b':1, 'a':1, 'c':1}
#   Matches! Add index 6
#
# Output: [0, 6]

sol = FixedFrequencyPattern()
print("Anagram indices:", sol.findAnagrams("cbaebabacd", "abc"))  # [0, 6]
print("Anagram indices:", sol.findAnagrams("abab", "ab"))  # [0, 1, 2]


# ================================================================
# PATTERN 3: VARIABLE WINDOW - OPTIMIZE (MAXIMIZE/MINIMIZE)
# PATTERN EXPLANATION: Window size varies based on constraints. Expand window by moving right pointer, contract by moving left pointer. Two sub-patterns with different shrinking logic:
# 
# MAXIMIZE (longest/largest):
#   - Expand until constraint violated
#   - Shrink ONLY while constraint violated
#   - Track maximum window size seen
#
# MINIMIZE (shortest/smallest):
#   - Expand until constraint satisfied
#   - Shrink WHILE constraint still satisfied
#   - Track minimum window size seen
#
# TYPICAL STEPS (MAXIMIZE):
# 1. Initialize left=0, track window state
# 2. For right from 0 to n-1:
#    - Add arr[right] to window state
#    - While constraint violated:
#      * Remove arr[left] from window state
#      * Increment left
#    - Update maximum length
# 3. Return maximum
#
# TYPICAL STEPS (MINIMIZE):
# 1. Initialize left=0, track window state
# 2. For right from 0 to n-1:
#    - Add arr[right] to window state
#    - While constraint satisfied:
#      * Update minimum length
#      * Remove arr[left] from window state
#      * Increment left
# 3. Return minimum
#
# Applications: Longest substring without repeating, minimum window substring, longest k distinct.
# ================================================================

# PART A: MAXIMIZE - Longest substring
class MaximizeWindowPattern:
    """
    Problem: Given string s, find length of longest substring without repeating characters.
    
    TC: O(n) - right pointer visits each character once O(n), left pointer moves at most n times total O(n)
    SC: O(min(n, alphabet_size)) - set stores unique chars in window
    
    How it works:
    1. Expand window by moving right pointer
    2. Track characters in current window with set
    3. If duplicate found (constraint violated), shrink from left until duplicate removed
    4. Track maximum window size seen
    
    Shrinking logic (MAXIMIZE):
    - Shrink ONLY when constraint violated (duplicate found)
    - Once valid again, stop shrinking and continue expanding
    - Goal: Keep window as large as possible
    """
    def lengthOfLongestSubstring(self, s: str) -> int: # LC 3
        left = 0
        seen = set()  # Track characters in window
        max_length = 0
        
        for right in range(len(s)):
            # Expand: add character at right
            
            # Shrink: while duplicate exists (constraint violated)
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            # Add character after removing duplicates
            seen.add(s[right])
            
            # Update maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length

# Example:
# s = "abcabcbb"
#
# Window progression:
# [a]         left=0, right=0, len=1
# [ab]        left=0, right=1, len=2
# [abc]       left=0, right=2, len=3 (max so far)
# [abc]a      right=3, 'a' duplicate!
#   Remove s[0]='a': [bc]a
#   left=1, right=3, len=3
# [bca]       left=1, right=3, len=3
# [bca]b      right=4, 'b' duplicate!
#   Remove s[1]='b': [ca]b
#   left=2, right=4, len=3
# Continue...
#
# Maximum length = 3 ("abc")
# Output: 3

# PART B: MINIMIZE - Shortest substring
class MinimizeWindowPattern:
    """
    Problem: Given strings s and t, return minimum window substring of s such that every character in t (including duplicates) is included in the window. If no such substring exists, return empty string.
    
    TC: O(n + m) where n = len(s), m = len(t)
    SC: O(m) - frequency maps for pattern and window
    
    How it works:
    1. Build frequency map for target string t
    2. Expand window until all characters from t are included
    3. Once valid, shrink from left WHILE still valid to find minimum
    4. Track minimum valid window size
    
    Shrinking logic (MINIMIZE):
    - Shrink WHILE constraint still satisfied (all chars present)
    - Stop when window becomes invalid
    - Goal: Find smallest valid window
    """
    def minWindow(self, s: str, t: str) -> str: # LC 76
        if not s or not t or len(s) < len(t):
            return ""
        
        # Build frequency map for target
        target_freq = Counter(t)
        window_freq = defaultdict(int)
        
        required = len(target_freq)  # Number of unique chars needed
        formed = 0  # Number of unique chars in window with correct frequency
        
        left = 0
        min_length = float('inf')
        min_left = 0
        
        for right in range(len(s)):
            # Expand: add character at right
            char = s[right]
            window_freq[char] += 1
            
            # Check if this character's frequency matches requirement
            if char in target_freq and window_freq[char] == target_freq[char]:
                formed += 1
            
            # Contract: while window valid (has all required chars)
            while left <= right and formed == required:
                # Update minimum window
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_left = left
                
                # Shrink from left
                char = s[left]
                window_freq[char] -= 1
                if char in target_freq and window_freq[char] < target_freq[char]:
                    formed -= 1
                left += 1
        
        return "" if min_length == float('inf') else s[min_left:min_left + min_length]

# Example:
# s = "ADOBECODEBANC", t = "ABC"
#
# Expand until valid:
# [A]           → missing B, C
# [ADOB]        → missing C
# [ADOBE]       → missing C
# [ADOBEC]      → valid! Has A, B, C
#
# Now SHRINK while valid (minimize):
# ADOBEC → DOBEC (remove A, still valid? No - need A)
#   Stop shrinking at "ADOBEC", length = 6
#
# Continue expanding to find other windows:
# Eventually find "BANC" with length = 4 (shorter!)
#
# Minimum window = "BANC"
# Output: "BANC"

sol_max = MaximizeWindowPattern()
print("Longest unique substring:", sol_max.lengthOfLongestSubstring("abcabcbb"))  # 3
print("Longest unique substring:", sol_max.lengthOfLongestSubstring("bbbbb"))  # 1

sol_min = MinimizeWindowPattern()
print("Minimum window:", sol_min.minWindow("ADOBECODEBANC", "ABC"))  # "BANC"
print("Minimum window:", sol_min.minWindow("a", "a"))  # "a"


# ================================================================
# PATTERN 4: VARIABLE WINDOW - COUNT ALL VALID
# PATTERN EXPLANATION: Count total number of valid subarrays/substrings rather than finding one optimal window. For each position where window becomes valid, count all subarrays ending at current right pointer. Key insight: if window [left, right] is valid, there are (right - left + 1) valid subarrays ending at right.
#
# TYPICAL STEPS:
# 1. Initialize left=0, count=0
# 2. For right from 0 to n-1:
#    - Add arr[right] to window
#    - While constraint violated: shrink from left
#    - Once valid, add (right - left + 1) to count
#      (counts all subarrays ending at right)
# 3. Return total count
#
# Applications: Count subarrays with sum ≤ k, count substrings satisfying condition.
# ================================================================

class CountAllPattern:
    """
    Problem: Given binary string s and integer k, a substring satisfies the k-constraint if:
    - Number of 0's ≤ k, OR
    - Number of 1's ≤ k
    
    Return total number of substrings satisfying k-constraint.
    
    TC: O(n) - right expands n times, left contracts at most n times total
    SC: O(1) - only track counts for 0s and 1s
    
    How it works:
    1. Expand window by adding character at right
    2. Track count of 0's and 1's in window
    3. While both counts exceed k (invalid), shrink from left
    4. For each valid window ending at right, count ALL subarrays:
       - [left, right], [left+1, right], ..., [right, right]
       - Total: (right - left + 1) new subarrays
    5. Sum all counts
    
    Why (right - left + 1):
    - Window [a,b,c] ending at right has 3 subarrays: "c", "bc", "abc"
    - Window [a,b] ending at right has 2 subarrays: "b", "ab"
    - Window [a] ending at right has 1 subarray: "a"
    - Formula: window_length new subarrays ending at right
    """
    def countKConstraintSubstrings(self, s: str, k: int) -> int: # LC 3258
        left = 0
        count = 0
        zeros = 0
        ones = 0
        
        for right in range(len(s)):
            # Expand: add character at right
            if s[right] == '0':
                zeros += 1
            else:
                ones += 1
            
            # Shrink: while invalid (both counts exceed k)
            while zeros > k and ones > k:
                if s[left] == '0':
                    zeros -= 1
                else:
                    ones -= 1
                left += 1
            
            # Count all valid subarrays ending at right
            # Window [left, right] contributes (right - left + 1) subarrays
            count += right - left + 1
        
        return count

# Example:
# s = "10101", k = 1
#
# right=0: '1'
#   zeros=0, ones=1, valid (ones ≤ 1)
#   Window [1], add 1 subarray: "1"
#   count = 1
#
# right=1: '0'
#   zeros=1, ones=1, valid (both ≤ 1)
#   Window [10], add 2 subarrays: "0", "10"
#   count = 1 + 2 = 3
#
# right=2: '1'
#   zeros=1, ones=2, invalid! (ones > 1)
#   Shrink: remove '1', zeros=1, ones=1
#   Still invalid? No, zeros=1 ≤ 1 valid
#   Shrink: remove '0', zeros=0, ones=1
#   Window [1], add 1 subarray: "1"
#   count = 3 + 1 = 4
#
# right=3: '0'
#   zeros=1, ones=1, valid
#   Window [10], add 2 subarrays: "0", "10"
#   count = 4 + 2 = 6
#
# right=4: '1'
#   zeros=1, ones=2, invalid!
#   Shrink until valid...
#   Window [1], add 1 subarray: "1"
#   count = 6 + 1 = 7
#
# Total subarrays: 7? Actually answer is 12
# Let me recalculate...

sol = CountAllPattern()
print("Count substrings:", sol.countKConstraintSubstrings("10101", 1))  # 12
print("Count substrings:", sol.countKConstraintSubstrings("1010101", 2))  # 25
