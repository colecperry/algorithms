"""
=================================================================
HASH TABLE COMPLETE GUIDE
=================================================================

WHAT IS A HASH TABLE?
---------------------
A Hash Table (Hash Map, Dictionary) is a data structure that implements an associative array, mapping keys to values. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found. Provides average O(1) time for insert, delete, and lookup operations.

Key characteristics:
- Key-Value pairs: Each key maps to exactly one value
- Hash function: Converts key to array index
- Collision handling: Multiple keys may hash to same index
- Average O(1) operations: Insert, delete, lookup
- No ordering: Elements not stored in any particular order
- Dynamic sizing: Resizes when load factor exceeds threshold

When to use Hash Table:
- Need fast lookup by key
- Counting frequencies/occurrences
- Detecting duplicates or uniqueness
- Caching/memoization
- Group elements by property
- Track visited/seen elements
- Two sum / complement problems

HASH TABLE CORE TEMPLATES
==========================
"""

from typing import List, Optional
from collections import defaultdict, Counter
import heapq

# ================================================================
# BASIC HASH TABLE TEMPLATE
# ================================================================
def basic_hash_table_template():
    """
    Basic hash table operations in Python
    TC: O(1) average for all operations
    SC: O(n) where n = number of elements
    """
    # Create hash table
    hash_map = {}
    
    # Insert/Update
    hash_map['key'] = 'value'
    hash_map[1] = 100
    
    # Lookup
    value = hash_map.get('key')
    
    # Check existence
    if 'key' in hash_map:
        pass
    
    # Delete
    if 'key' in hash_map:
        del hash_map['key']
    
    # Iterate
    for key, value in hash_map.items():
        print(key, value)
    
    # Get all keys/values
    keys = list(hash_map.keys())
    values = list(hash_map.values())
    
    return hash_map

# ================================================================
# HASH SET TEMPLATE
# ================================================================
def hash_set_template(arr):
    """
    Hash set for unique elements and O(1) lookups
    TC: O(n)
    SC: O(k) where k = unique elements
    """
    # Create set
    seen = set()
    
    # Add elements
    for item in arr:
        seen.add(item)
    
    # Check existence (most common use)
    if item in seen:
        pass
    
    # Remove
    seen.discard(item)  # No error if not found
    # OR
    seen.remove(item)   # Raises error if not found
    
    # Set operations
    set_a = {1, 2, 3}
    set_b = {2, 3, 4}
    intersection = set_a & set_b  # {2, 3}
    union = set_a | set_b          # {1, 2, 3, 4}
    difference = set_a - set_b     # {1}
    
    return seen

# ================================================================
# FREQUENCY COUNTER TEMPLATE
# ================================================================
def frequency_counter_template(arr):
    """
    Count frequency of elements
    TC: O(n)
    SC: O(k) where k = unique elements
    """
    # Method 1: Manual counting
    freq_map = {}
    for item in arr:
        freq_map[item] = freq_map.get(item, 0) + 1 # Get current count (or 0 if new), then increment
    
    # Method 2: Using defaultdict
    freq_map = defaultdict(int)
    for item in arr:
        freq_map[item] += 1
    
    # Method 3: Using Counter
    from collections import Counter
    freq_map = Counter(arr)
    
    return freq_map

"""
TIME & SPACE COMPLEXITY REFERENCE
==================================

HASH TABLE OPERATIONS COMPLEXITY:
----------------------------------
+---------------------------+------------------+
| Operation                 | Time Complexity  |
+---------------------------+------------------+
| Insert                    | O(1)             |
| Delete                    | O(1)             |
| Lookup                    | O(1)             |
| Check existence           | O(1)             |
| Iterate all elements      | O(n)             |
+---------------------------+------------------+

SPACE COMPLEXITY:
-----------------
+---------------------------+------------------+
| Hash Table Type           | Space            |
+---------------------------+------------------+
| Basic hash table          | O(n)             |
| defaultdict               | O(n)             |
| Counter                   | O(k)*            |
| Hash set                  | O(k)*            |
+---------------------------+------------------+
* k = number of unique elements

WHAT EACH PATTERN IS:
- Frequency Counting / Character Count: tally how many times each element shows up
  by using the element as the key and a running count as the value — the basis for
  anagrams, "most common element," and matching-frequency checks.
- Hash Table for Lookup (Two Sum Pattern): remember every element you've already
  seen so that, for any new element, you can instantly check whether its "missing
  partner" (e.g. target - current) has already shown up.
- Hash Table + Sliding Window: keep a hash table of what's currently inside a moving
  window of a string/array, growing the window by adding elements and shrinking it
  from the front when a rule gets violated.
- Hash Table for Grouping / Categorization: compute some shared "signature" for each
  element (like its sorted letters) and use that signature as a key so everything
  with the same signature lands in the same bucket.
- Hash Table for Caching / Memoization: save the answer to a computation the first
  time you work it out, keyed by the inputs, so if you're ever asked the same
  question again you can just look it up instead of redoing the work.

"""
"""
================================================================
PATTERN 1: FREQUENCY COUNTING / CHARACTER COUNT
PATTERN EXPLANATION: Count occurrences of elements using hash table. Store element as key, count as value. Essential for finding most/least frequent elements, checking if frequencies match, or validating anagrams. Single pass through data with O(1) increment per element.
#
Applications: Anagrams, most frequent elements, valid parentheses, character frequency.
================================================================
"""

class FrequencyCounting:
    """
    Problem 1: Check if two strings are anagrams.

    Example:
        Input: s = "anagram", t = "nagaram"
        Output: True

        Both have: a(3), n(1), g(1), r(1), m(1)

    Giveaway: checking whether two strings are anagrams of each other — needing
    to compare the exact count of every character between two strings (not just
    membership) is the signal for building frequency maps and comparing them,
    rather than sorting or a single hash set.

    Steps:
    1. Create two hash tables (one per string)
    2. Iterate through each string and increment count: freq[char] = freq.get(char, 0) + 1
    3. Compare the two frequency maps for equality
    """
    def isAnagram(self, s: str, t: str) -> bool:  # LC 242
        """
        - TC: O(n) where n = string length (iterate through both strings + compare dicts)
        - SC: O(k) where k = unique characters (at most 26 for lowercase English)
        """
        # Quick check: different lengths can't be anagrams
        if len(s) != len(t):
            return False
        
        # Count frequencies
        count_s = {}
        count_t = {}
        
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        
        # Compare frequencies
        return count_s == count_t

sol = FrequencyCounting()
print("Is Anagram:", sol.isAnagram("anagram", "nagaram"))  # True

"""
================================================================
PATTERN 2: HASH TABLE FOR LOOKUP (TWO SUM PATTERN)
PATTERN EXPLANATION: Use hash table for O(1) complement lookup. Store elements as you iterate, check if required complement exists. Converts O(n²) nested loop to O(n) single pass. Core pattern for sum problems, finding pairs, and matching problems.
#
Applications: Two sum, three sum, four sum, pair with target, subarray sum.
================================================================
"""

class LookupPattern:
    """
    Problem 1: Find two numbers that add up to target.

    Example:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]

        nums[0] + nums[1] = 2 + 7 = 9

    TC: O(n) - single pass
    SC: O(n) - hash table storage

    Giveaway: "find two numbers that add up to target" — needing a complementary
    value (target - current) for each element in one pass is what signals storing
    seen elements in a hash map for O(1) complement lookup instead of nested
    loops.

    Steps:
    1. Create a hash table to store seen elements (value -> index)
    2. For each number:
       a. Calculate complement = target - number
       b. Check if complement exists in hash table
       c. If yes: return indices of complement and current number
       d. If no: add current number with its index to hash table
    3. Continue until pair is found or end of array
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:  # LC 1
        """
        - TC: O(n) where n = len(nums) (single pass through array)
        - SC: O(n) (hash table stores at most n elements)
        """
        seen = {}  # value -> index
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement exists
            if complement in seen:
                return [seen[complement], i] # return index of both nums
            
            # Store current number
            seen[num] = i
        
        return []

# Example trace:
# nums = [2,7,11,15], target = 9
#
# i=0, num=2:
#   complement = 9 - 2 = 7
#   7 in seen? No
#   seen = {2: 0}
#
# i=1, num=7:
#   complement = 9 - 7 = 2
#   2 in seen? Yes! seen[2] = 0
#   return [0, 1]

sol = LookupPattern()
print("Two Sum:", sol.twoSum([2,7,11,15], 9))  # [0,1]

"""
================================================================
PATTERN 3: HASH TABLE + SLIDING WINDOW
PATTERN EXPLANATION: Combine hash table with sliding window for substring/subarray problems with character constraints. Hash table tracks elements in current window. Expand window by adding elements, shrink when constraint violated. Efficient for longest/shortest substring with unique characters or specific conditions.
#
Applications: Longest substring, minimum window, character replacement.
================================================================
"""

class SlidingWindowHash:
    """
    Problem 1: Longest substring without repeating characters.

    Example:
        Input: s = "abcabcbb"
        Output: 3

        "abc" has length 3 with no repeats

    Giveaway: "longest substring without repeating characters" — needing the
    longest contiguous run under a no-duplicates constraint means tracking what's
    currently in a window and shrinking it from the left the moment a repeat
    appears, which is the hash-set-plus-two-pointers tell.

    Steps:
    1. Initialize a hash set to track characters in the current window and two pointers (left, right)
    2. Expand the window: move right pointer and add s[right] to the hash set
    3. While window is invalid (s[right] already in set):
       a. Remove s[left] from the hash set
       b. Move left pointer right
    4. Update max length (right - left + 1)
    """
    def lengthOfLongestSubstring(self, s: str) -> int: # LC 3
        """
        - TC: O(n) where n = len(s) (each char visited at most twice - once by right, once removed by left)
        - SC: O(min(n, k)) where k = charset size (at most 26 for lowercase, 128 for ASCII)
        """
        left = 0
        seen = set()  # Tracks characters in current window [left, right]
        max_len = 0
        
        for right in range(len(s)):
            # Shrink window from left until s[right] is no longer a duplicate
            while s[right] in seen:
                seen.remove(s[left])   # Remove leftmost char
                left += 1              # Move window right
            
            # Now s[right] is unique in window, add it
            seen.add(s[right])
            
            # Update max length (window size = right - left + 1)
            max_len = max(max_len, right - left + 1)
        
        return max_len

# Example trace:
# s = "abcabcbb"
#
# right=0, s[right]='a':
#   'a' not in seen
#   seen = {'a'}, window = "a", max_len = 1
#
# right=1, s[right]='b':
#   'b' not in seen
#   seen = {'a','b'}, window = "ab", max_len = 2
#
# right=2, s[right]='c':
#   'c' not in seen
#   seen = {'a','b','c'}, window = "abc", max_len = 3
#
# right=3, s[right]='a':
#   'a' IS in seen (duplicate!)
#   while loop: remove s[0]='a', left=1, seen = {'b','c'}
#   'a' not in seen anymore
#   seen = {'b','c','a'}, window = "bca", max_len = 3
#
# right=4, s[right]='b':
#   'b' IS in seen (duplicate!)
#   while loop: remove s[1]='b', left=2, seen = {'c','a'}
#   'b' not in seen anymore
#   seen = {'c','a','b'}, window = "cab", max_len = 3
#
# ... continues
# Final: max_len = 3

sol = SlidingWindowHash()
print("Longest Substring:", sol.lengthOfLongestSubstring("abcabcbb"))  # 3

"""
================================================================
PATTERN 4: HASH TABLE FOR GROUPING / CATEGORIZATION
PATTERN EXPLANATION: Group elements by some computed property using hash table. Generate key based on element characteristics, use as hash table key. All elements with same key go in same group. Efficient for categorizing data by pattern, structure, or attribute.
#
Applications: Group anagrams, group by pattern, categorize strings/numbers.
================================================================
"""

class GroupingPattern:
    """
    Problem 1: Group anagrams together.

    Example:
        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

        "eat", "tea", "ate" are anagrams (same characters)

    Giveaway: "group anagrams together" — needing to bucket many strings by a
    shared property (same letters, different order) is what signals computing a
    canonical key per element and using a hash map of key -> list to route each
    element into its group.

    Steps:
    1. Initialize a defaultdict(list) to hold groups
    2. For each string:
       a. Compute the key by sorting its characters (canonical form)
       b. Append the string to the group at that key
    3. Return all groups as a list of lists
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  # LC 49
        """
        - TC: O(n * m log m) where n = strings, m = max length, we iterate over n strings, and sort each string with an average length of m -> (m log m). Key difference is that nums in an array is O(1) space but strings are O(m) space
        - SC: O(n * m) - we store n strings in the dict with average length m as values, and n strings with an average length of m as sorted keys
        """
        # Method 1: Using sorted string as key
        groups = defaultdict(list)
        
        for s in strs:
            # Sort characters to get canonical form
            key = ''.join(sorted(s))
            groups[key].append(s)
        
        return list(groups.values())

# Example trace:
# strs = ["eat","tea","tan","ate","nat","bat"]
#
# Process "eat":
#   sorted = "aet"
#   groups = {"aet": ["eat"]}
#
# Process "tea":
#   sorted = "aet"
#   groups = {"aet": ["eat","tea"]}
#
# Process "tan":
#   sorted = "ant"
#   groups = {"aet": ["eat","tea"], "ant": ["tan"]}
#
# Process "ate":
#   sorted = "aet"
#   groups = {"aet": ["eat","tea","ate"], "ant": ["tan"]}
#
# Process "nat":
#   sorted = "ant"
#   groups = {"aet": ["eat","tea","ate"], "ant": ["tan","nat"]}
#
# Process "bat":
#   sorted = "abt"
#   groups = {"aet": ["eat","tea","ate"], "ant": ["tan","nat"], "abt": ["bat"]}
#
# Result: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

sol = GroupingPattern()
print("Group Anagrams:", sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

"""
================================================================
PATTERN 5: HASH TABLE FOR CACHING / MEMOIZATION
PATTERN EXPLANATION: Store computed results to avoid redundant calculations. Use problem
state as key, result as value. Check cache before computing. Essential for optimizing
recursive algorithms and avoiding repeated work. Related to dynamic programming.
#
Applications: Fibonacci, climbing stairs, LRU cache, memoization.
================================================================
"""

class CachingPattern:
    """
    Check if string can be segmented into words from dictionary.

        Example 1:
            Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
            Output: False

        Example 2:
            Input: s = "leetcode", wordDict = ["leet","code"]
            Output: true
            Explanation: Return true because "leetcode" can be segmented as "leet code".

        Giveaway: the recursion revisits the same starting index through multiple
        different word-splitting paths (repeatedly asking "can the rest of the
        string be segmented from here?") — those repeated overlapping subproblems,
        not just any recursion, are what signal memoizing results in a hash map
        instead of recomputing every branch.

        Steps:
        1. Convert wordDict to a set for O(1) lookups and create a memo cache
        2. Define recursive helper canSegmentFrom(start):
           a. Base case: if start == len(s), return True (full string segmented)
           b. If start is in memo, return cached result
           c. Try every end index from start+1 to len(s):
              - If s[start:end] is in word_set and canSegmentFrom(end) is True, cache True and return True
           d. Cache False and return False
        3. Call canSegmentFrom(0) to start from the beginning of the string
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:  # LC 139
        """
        - TC: O(n² * m) where n = len(s), m = average word length
              (n possible starting positions * n possible endings * m to check word in set)
        - SC: O(n) - memoization stores result for each starting index
        """
        word_set = set(wordDict)  # O(1) lookup for words
        memo = {}  # start_index -> can_break_from_here
        
        def canSegmentFrom(start):
            """
            Check if s[start:] can be segmented into dictionary words
            """
            # Base case: successfully processed entire string
            if start == len(s):
                return True
            
            # Check cache: have we already computed this subproblem?
            if start in memo:
                return memo[start]
            
            # Try all possible words starting from current position
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]  # Extract substring from start to end
                
                # First check: is this a valid dictionary word?
                if word in word_set:
                    # Second check: can we segment the rest of the string?
                    if canSegmentFrom(end):
                        memo[start] = True # starting from start, rest of the string can be segmented into dict words
                        return True # bubble up through callstack
                        
            # No valid segmentation found from this position
            memo[start] = False
            return False
        
        return canSegmentFrom(0)  # Start from beginning of string

# Example trace showing cache usage:
# s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# word_set = {"cats", "dog", "sand", "and", "cat"}
#
# canSegmentFrom(0):  # Can we segment "catsandog"?
#   Try "c": not in set
#   Try "ca": not in set
#   Try "cat": IN SET! ✓ Check canSegmentFrom(3)
#     
#     canSegmentFrom(3):  # Can we segment "sandog"?
#       Try "s": not in set
#       Try "sa": not in set
#       Try "san": not in set
#       Try "sand": IN SET! ✓ Check canSegmentFrom(7)
#         
#         canSegmentFrom(7):  # Can we segment "og"? (FIRST TIME HERE)
#           Try "o": not in set
#           Try "og": not in set
#           No valid segmentation found
#           memo[7] = False  ← CACHE THE FAILURE
#           return False
#         
#       "sand" found BUT canSegmentFrom(7) = False ✗
#       Try "sanda": not in set
#       Try "sando": not in set
#       Try "sandog": not in set
#       No valid segmentation found
#       memo[3] = False
#       return False
#     
#   "cat" found BUT canSegmentFrom(3) = False ✗
#   Try "cats": IN SET! ✓ Check canSegmentFrom(4)
#     
#     canSegmentFrom(4):  # Can we segment "andog"?
#       Try "a": not in set
#       Try "an": not in set
#       Try "and": IN SET! ✓ Check canSegmentFrom(7)
#         
#         canSegmentFrom(7):  # Can we segment "og"? (SECOND TIME HERE)
#           if 7 in memo:  ← CACHE HIT! ✓
#             return False  ← Instant lookup, no recomputation needed!
#         
#       "and" found BUT canSegmentFrom(7) = False ✗
#       Try remaining substrings... all fail
#       memo[4] = False
#       return False
#     
#   "cats" found BUT canSegmentFrom(4) = False ✗
#   Try remaining substrings... all fail
#   memo[0] = False
#   return False
#
# Result: False (cannot segment "catsandog")
#
# Cache benefit demonstrated:
# Position 7 ("og") was reached TWICE:
#   1st time (via "cat" + "sand"): Computed and cached False
#   2nd time (via "cats" + "and"): Cache hit! Instant False
# Without memo: would recompute canSegmentFrom(7) every time
# With memo: computed once, reused for all subsequent paths

sol = CachingPattern()
print("Word Break:", sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))  # False
print("Word Break:", sol.wordBreak("leetcode", ["leet", "code"]))  # True