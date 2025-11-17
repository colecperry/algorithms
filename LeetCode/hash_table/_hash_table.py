"""
=================================================================
HASH TABLE COMPLETE GUIDE
=================================================================

WHAT IS A HASH TABLE?
---------------------
A Hash Table (Hash Map, Dictionary) is a data structure that implements an associative array,
mapping keys to values. It uses a hash function to compute an index into an array of buckets
or slots, from which the desired value can be found. Provides average O(1) time for insert,
delete, and lookup operations.

Key characteristics:
- Key-Value pairs: Each key maps to exactly one value
- Hash function: Converts key to array index
- Collision handling: Multiple keys may hash to same index
- Average O(1) operations: Insert, delete, lookup
- No ordering: Elements not stored in any particular order
- Dynamic sizing: Resizes when load factor exceeds threshold

Basic operations:
```python
hash_map = {}
hash_map[key] = value      # Insert/Update: O(1) average
value = hash_map[key]      # Lookup: O(1) average
if key in hash_map: ...    # Check existence: O(1) average
del hash_map[key]          # Delete: O(1) average
hash_map.get(key, default) # Lookup with default
```

When to use Hash Table:
- Need fast lookup by key
- Counting frequencies/occurrences
- Detecting duplicates or uniqueness
- Caching/memoization
- Group elements by property
- Track visited/seen elements
- Two sum / complement problems

Common Hash Table problem types:
- Frequency counting (character/element counts)
- Two sum / K sum problems
- Anagram grouping
- Duplicate detection
- Sliding window with constraints
- Design problems (LRU cache, time-based key-value)
- Subarray sum problems
- Longest substring problems
- Pattern matching

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
    value = hash_map.get('key', 'default')
    
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
        freq_map[item] = freq_map.get(item, 0) + 1
    
    # Method 2: Using defaultdict
    freq_map = defaultdict(int)
    for item in arr:
        freq_map[item] += 1
    
    # Method 3: Using Counter
    from collections import Counter
    freq_map = Counter(arr)
    
    return freq_map

# ================================================================
# TWO SUM TEMPLATE (COMPLEMENT LOOKUP)
# ================================================================
def two_sum_template(nums, target):
    """
    Find two numbers that sum to target
    TC: O(n) - single pass
    SC: O(n) - hash table storage
    """
    seen = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return []

# ================================================================
# SLIDING WINDOW WITH HASH TABLE TEMPLATE
# ================================================================
def sliding_window_hash_template(s, k):
    """
    Sliding window with character/element tracking
    TC: O(n)
    SC: O(k) where k = unique elements in window
    """
    char_count = {}
    left = 0
    result = 0
    
    for right in range(len(s)):
        # Add right character
        char = s[right]
        char_count[char] = char_count.get(char, 0) + 1
        
        # Shrink window if invalid
        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1
        
        # Update result
        result = max(result, right - left + 1)
    
    return result

# ================================================================
# GROUPING TEMPLATE
# ================================================================
def grouping_template(strs):
    """
    Group elements by some property
    TC: O(n * m) where m = average string length
    SC: O(n)
    """
    groups = defaultdict(list)
    
    for s in strs:
        # Generate key based on property
        key = ''.join(sorted(s))  # Example: sort for anagrams
        groups[key].append(s)
    
    return list(groups.values())

"""
TIME & SPACE COMPLEXITY REFERENCE
==================================

HASH TABLE OPERATIONS COMPLEXITY:
----------------------------------
+---------------------------+------------------+------------------+
| Operation                 | Time (Average)   | Time (Worst)     |
+---------------------------+------------------+------------------+
| Insert                    | O(1)             | O(n)             |
| Delete                    | O(1)             | O(n)             |
| Lookup                    | O(1)             | O(n)             |
| Check existence           | O(1)             | O(n)             |
| Iterate all elements      | O(n)             | O(n)             |
+---------------------------+------------------+------------------+

SPACE COMPLEXITY:
-----------------
+---------------------------+------------------+
| Hash Table Type           | Space            |
+---------------------------+------------------+
| Basic hash table          | O(n)             |
| With collision handling   | O(n)             |
| defaultdict               | O(n)             |
| Counter                   | O(k)             |
+---------------------------+------------------+

WHERE:
- n = total number of elements
- k = number of unique elements

COMMON HASH TABLE PATTERNS COMPLEXITY:
---------------------------------------
+---------------------------+------------------+------------------+
| Pattern                   | Time Complexity  | Space Complexity |
+---------------------------+------------------+------------------+
| Frequency Counting        | O(n)             | O(k)             |
| Two Sum                   | O(n)             | O(n)             |
| Group Anagrams            | O(n * m log m)   | O(n * m)         |
| Longest Substring         | O(n)             | O(min(n,k))      |
| Subarray Sum Equals K     | O(n)             | O(n)             |
| First Unique Character    | O(n)             | O(k)             |
| Valid Anagram             | O(n)             | O(k)             |
| Four Sum                  | O(n²)            | O(n²)            |
+---------------------------+------------------+------------------+

WHERE:
- n = array/string length
- m = average string length
- k = alphabet size or unique elements

COMPLEXITY NOTES:
-----------------
1. Hash Table Average vs Worst Case:
   - Average O(1): Good hash function, low load factor
   - Worst O(n): All elements collide, linear search in bucket
   - Python dict uses open addressing, very rare worst case
   
   Load factor = n / capacity
   Python dict resizes when load factor > 2/3

2. Frequency Counting: O(n) time, O(k) space
   - Single pass through array: O(n)
   - Space: O(k) where k = unique elements
   - k ≤ n always, often k << n
   
   Best for: Character frequencies, element counts
   Pattern: freq[item] = freq.get(item, 0) + 1

3. Two Sum Pattern: O(n) time, O(n) space
   - Check complement in O(1): hash table lookup
   - Single pass vs O(n²) nested loops
   - Space: Store up to n elements
   
   Why O(n)? Each element checked once
   Key insight: target - num gives complement

4. Group Anagrams: O(n * m log m) time
   - Sort each string: O(m log m)
   - n strings: O(n * m log m)
   - Alternative: O(n * m) with character count as key
   
   Space: O(n * m) to store all strings
   Key: Sorted string or character count tuple

5. Sliding Window with Hash: O(n) time, O(k) space
   - Each element enters/exits window once: O(n)
   - Space: O(k) for unique elements in window
   - k limited by window size or alphabet
   
   Pattern: Expand right, shrink left when invalid
   Hash table tracks window state efficiently

6. Subarray Sum (Prefix Sum + Hash): O(n) time, O(n) space
   - Single pass with prefix sum: O(n)
   - Hash table stores prefix sums: O(n)
   - Check if (current_sum - target) exists: O(1)
   
   Converts O(n²) to O(n)
   Same pattern as Two Sum but for subarrays

7. Four Sum: O(n²) time, O(n²) space
   - Generate all pairs: O(n²)
   - Store pair sums in hash table: O(n²)
   - Check complement pairs: O(n²)
   
   Better than O(n³) three nested loops
   Space tradeoff: Store n² pairs

WHEN TO USE HASH TABLE:
-----------------------
Use Hash Table when:
- Need O(1) lookup by key
- Counting/frequency problems
- Detecting duplicates
- Finding complements (two sum)
- Grouping by property
- Caching results

Don't use Hash Table when:
- Need ordered traversal (use TreeMap/sorted)
- Need range queries (use TreeMap)
- Only sequential access (use array)
- Memory critical and n is huge

HASH TABLE VS OTHER STRUCTURES:
--------------------------------
Hash Table vs Array:
- Hash: O(1) lookup by key, no order
- Array: O(n) lookup by value, O(1) by index, ordered

Hash Table vs Set:
- Hash Table: key-value pairs
- Set: keys only, check membership

Hash Table vs TreeMap:
- Hash: O(1) average, no order
- TreeMap: O(log n), ordered keys

COLLISION HANDLING:
-------------------
Python dict uses open addressing:
- Hash collision: Try next slots
- Resize when load factor > 2/3
- Very efficient in practice

Alternative: Chaining
- Each bucket is linked list
- More predictable worst case
- Slightly more memory

SPACE-TIME TRADEOFFS:
---------------------
Hash table trades space for time:
- More space: O(n) for hash table
- Faster operations: O(1) vs O(n) linear search
- Worth it for repeated lookups

Optimization:
- Use Counter for frequency
- Use defaultdict to avoid key checks
- Use get() with default instead of checking existence
- Clear hash table when done to free memory
"""

"""
HASH TABLE PATTERNS
===================
"""

# ================================================================
# PATTERN 1: FREQUENCY COUNTING / CHARACTER COUNT
# PATTERN EXPLANATION: Count occurrences of elements using hash table. Store element as key,
# count as value. Essential for finding most/least frequent elements, checking if frequencies
# match, or validating anagrams. Single pass through data with O(1) increment per element.
#
# TYPICAL STEPS:
# 1. Create hash table (dict, defaultdict, or Counter)
# 2. Iterate through elements
# 3. Increment count: freq[element] = freq.get(element, 0) + 1
# 4. Use counts to solve problem (find max, check equality, etc.)
#
# Applications: Anagrams, most frequent elements, valid parentheses, character frequency.
# ================================================================

class FrequencyCounting:
    """
    Problem 1: Check if two strings are anagrams.
    
    Example:
        Input: s = "anagram", t = "nagaram"
        Output: True
        
        Both have: a(3), n(1), g(1), r(1), m(1)
    
    TC: O(n) where n = string length
    SC: O(k) where k = unique characters (at most 26 for lowercase)
    
    How it works:
    1. Count character frequencies in both strings
    2. Compare frequency maps
    3. If identical, they're anagrams
    """
    def isAnagram(self, s: str, t: str) -> bool:  # LC 242
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
    
    # Alternative: Using Counter
    def isAnagram_counter(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)
    
    # Alternative: Using single hash table
    def isAnagram_single(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        
        # Add counts from s
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Subtract counts from t
        for char in t:
            count[char] = count.get(char, 0) - 1
            if count[char] < 0:
                return False
        
        return True

# Example trace:
# s = "anagram", t = "nagaram"
#
# count_s after processing:
# {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
#
# count_t after processing:
# {'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}
#
# count_s == count_t? True ✓

    def firstUniqChar(self, s: str) -> int:  # LC 387
        """
        Problem 2: Find first non-repeating character.
        
        Example:
            Input: s = "leetcode"
            Output: 0
            
            'l' appears once, first at index 0
        
        TC: O(n) - two passes
        SC: O(k) - character frequencies
        
        How it works:
        1. Count all character frequencies
        2. Iterate again to find first with count 1
        """
        # Count frequencies
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        # Find first unique
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i
        
        return -1

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  # LC 347
        """
        Problem 3: Find k most frequent elements.
        
        Example:
            Input: nums = [1,1,1,2,2,3], k = 2
            Output: [1,2]
            
            1 appears 3 times, 2 appears 2 times
        
        TC: O(n log k) with heap, O(n) with bucket sort
        SC: O(n) for frequency map
        
        Method 1: Heap (good for small k)
        """
        # Count frequencies
        freq = Counter(nums)
        
        # Use min heap of size k
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for count, num in heap]
    
    def topKFrequent_bucket(self, nums: List[int], k: int) -> List[int]:
        """
        Method 2: Bucket sort (O(n) time)
        """
        freq = Counter(nums)
        
        # Create buckets: index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)
        
        # Collect top k from highest frequency
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            result.extend(buckets[i])
            if len(result) >= k:
                return result[:k]
        
        return result

# Example trace for topKFrequent:
# nums = [1,1,1,2,2,3], k = 2
#
# freq = {1: 3, 2: 2, 3: 1}
#
# Using heap:
# Process 1 (count=3): heap = [(3,1)]
# Process 2 (count=2): heap = [(2,2), (3,1)]
# Process 3 (count=1): heap = [(2,2), (3,1)] (don't add, size=k)
# Result: [2, 1] or [1, 2]
#
# Using bucket sort:
# buckets[3] = [1]
# buckets[2] = [2]
# buckets[1] = [3]
#
# Collect from highest: [1] + [2] = [1, 2]

sol = FrequencyCounting()
print("Is Anagram:", sol.isAnagram("anagram", "nagaram"))  # True
print("First Unique Char:", sol.firstUniqChar("leetcode"))  # 0
print("Top K Frequent:", sol.topKFrequent([1,1,1,2,2,3], 2))  # [1,2]


# ================================================================
# PATTERN 2: HASH TABLE FOR LOOKUP (TWO SUM PATTERN)
# PATTERN EXPLANATION: Use hash table for O(1) complement lookup. Store elements as you
# iterate, check if required complement exists. Converts O(n²) nested loop to O(n) single
# pass. Core pattern for sum problems, finding pairs, and matching problems.
#
# TYPICAL STEPS:
# 1. Create hash table to store seen elements
# 2. For each element:
#    a. Calculate complement (target - element)
#    b. Check if complement exists in hash table
#    c. If yes: found answer
#    d. If no: add current element to hash table
# 3. Continue until found or end of array
#
# Applications: Two sum, three sum, four sum, pair with target, subarray sum.
# ================================================================

class LookupPattern:
    """
    Problem 1: Find two numbers that add up to target.
    
    Example:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        
        nums[0] + nums[1] = 2 + 7 = 9
    
    TC: O(n) - single pass
    SC: O(n) - hash table storage
    
    How it works:
    1. For each number, calculate complement = target - number
    2. Check if complement already seen
    3. If yes: found pair
    4. If no: store current number with index
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:  # LC 1
        seen = {}  # value -> index
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement exists
            if complement in seen:
                return [seen[complement], i]
            
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

    def twoSumSorted(self, numbers: List[int], target: int) -> List[int]:  # LC 167
        """
        Problem 2: Two sum in sorted array (1-indexed).
        
        Alternative: Two pointers (no hash table needed)
        
        TC: O(n)
        SC: O(1) with two pointers, O(n) with hash table
        """
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # 1-indexed
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:  # LC 454
        """
        Problem 3: Count tuples (i,j,k,l) where nums1[i] + nums2[j] + nums3[k] + nums4[l] = 0
        
        Example:
            nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
            Output: 2
            
            (0,0,0,1): 1 + (-2) + (-1) + 2 = 0
            (1,1,0,0): 2 + (-1) + (-1) + 0 = 0
        
        TC: O(n²) - better than O(n⁴) brute force
        SC: O(n²) - store all pair sums
        
        How it works:
        1. Calculate all sums from nums1 and nums2: O(n²)
        2. For each pair from nums3 and nums4:
           - Check if -(nums3[k] + nums4[l]) exists in first sums
           - Count occurrences
        """
        # Count all sums from first two arrays
        sum_count = {}
        for a in nums:
            for b in nums:
                sum_ab = a + b
                sum_count[sum_ab] = sum_count.get(sum_ab, 0) + 1
        
        # Check complements from last two arrays
        count = 0
        for c in nums:
            for d in nums:
                complement = target - (c + d)
                if complement in sum_count:
                    count += sum_count[complement]
        
        return count

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:  # LC 523
        """
        Problem 4: Check if array has subarray of size >= 2 with sum multiple of k.
        
        Example:
            Input: nums = [23,2,4,6,7], k = 6
            Output: True
            
            [2,4] sums to 6, which is multiple of 6
        
        TC: O(n)
        SC: O(min(n,k)) - at most k different remainders
        
        How it works:
        1. Use prefix sum with modulo k
        2. If same remainder seen before: subarray sum is multiple of k
        3. Store remainder -> index in hash table
        """
        # remainder -> first index seen
        remainder_map = {0: -1}  # Base case: subarray from start
        prefix_sum = 0
        
        for i, num in enumerate(nums):
            prefix_sum += num
            
            if k != 0:
                remainder = prefix_sum % k
            else:
                remainder = prefix_sum
            
            if remainder in remainder_map:
                # Check if subarray length >= 2
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                remainder_map[remainder] = i
        
        return False

# Example trace for checkSubarraySum:
# nums = [23,2,4,6,7], k = 6
#
# remainder_map = {0: -1}
#
# i=0, num=23:
#   prefix_sum = 23
#   remainder = 23 % 6 = 5
#   5 not in map, remainder_map = {0:-1, 5:0}
#
# i=1, num=2:
#   prefix_sum = 25
#   remainder = 25 % 6 = 1
#   1 not in map, remainder_map = {0:-1, 5:0, 1:1}
#
# i=2, num=4:
#   prefix_sum = 29
#   remainder = 29 % 6 = 5
#   5 in map at index 0!
#   i - remainder_map[5] = 2 - 0 = 2 >= 2 ✓
#   return True
#
# Subarray [2,4] from index 1 to 2 sums to 6

sol = LookupPattern()
print("Two Sum:", sol.twoSum([2,7,11,15], 9))  # [0,1]
print("Two Sum Sorted:", sol.twoSumSorted([2,7,11,15], 9))  # [1,2]
print("Check Subarray Sum:", sol.checkSubarraySum([23,2,4,6,7], 6))  # True


# ================================================================
# PATTERN 3: HASH TABLE + SLIDING WINDOW
# PATTERN EXPLANATION: Combine hash table with sliding window for substring/subarray problems
# with character constraints. Hash table tracks elements in current window. Expand window by
# adding elements, shrink when constraint violated. Efficient for longest/shortest substring
# with unique characters or specific conditions.
#
# TYPICAL STEPS:
# 1. Initialize hash table for window elements
# 2. Use two pointers: left and right
# 3. Expand window: add right element to hash table
# 4. While window invalid:
#    a. Remove left element from hash table
#    b. Move left pointer right
# 5. Update result (max length, count, etc.)
#
# Applications: Longest substring, minimum window, character replacement.
# ================================================================

class SlidingWindowHash:
    """
    Problem 1: Longest substring without repeating characters.
    
    Example:
        Input: s = "abcabcbb"
        Output: 3
        
        "abc" has length 3 with no repeats
    
    TC: O(n) - each character visited at most twice
    SC: O(min(n,k)) where k = alphabet size
    
    How it works:
    1. Expand window by adding character at right
    2. If character repeats, shrink from left until no repeat
    3. Track maximum window size
    """
    def lengthOfLongestSubstring(self, s: str) -> int:  # LC 3
        char_index = {}  # character -> last seen index
        left = 0
        max_length = 0
        
        for right, char in enumerate(s):
            # If character seen and within current window
            if char in char_index and char_index[char] >= left:
                # Move left past the previous occurrence
                left = char_index[char] + 1
            
            # Update last seen index
            char_index[char] = right
            
            # Update max length
            max_length = max(max_length, right - left + 1)
        
        return max_length

# Example trace:
# s = "abcabcbb"
#
# right=0, char='a':
#   'a' not in window, char_index={'a':0}
#   length = 0-0+1 = 1, max=1
#
# right=1, char='b':
#   'b' not in window, char_index={'a':0, 'b':1}
#   length = 1-0+1 = 2, max=2
#
# right=2, char='c':
#   'c' not in window, char_index={'a':0,'b':1,'c':2}
#   length = 2-0+1 = 3, max=3
#
# right=3, char='a':
#   'a' in window at index 0 >= left(0)
#   left = 0 + 1 = 1
#   char_index={'a':3,'b':1,'c':2}
#   length = 3-1+1 = 3, max=3
#
# ... continues
# Final: max=3 ("abc")

    def characterReplacement(self, s: str, k: int) -> int:  # LC 424
        """
        Problem 2: Longest substring with at most k character replacements.
        
        Example:
            Input: s = "AABABBA", k = 1
            Output: 4
            
            "AABA" -> replace one B -> "AAAA" (length 4)
        
        TC: O(n)
        SC: O(1) - at most 26 characters
        
        How it works:
        1. Track character frequencies in window
        2. If (window_size - max_frequency) > k: too many replacements needed
        3. Shrink window from left
        4. Track maximum valid window size
        """
        char_count = {}
        left = 0
        max_length = 0
        max_freq = 0
        
        for right, char in enumerate(s):
            # Add character to window
            char_count[char] = char_count.get(char, 0) + 1
            max_freq = max(max_freq, char_count[char])
            
            # Check if window is valid
            window_size = right - left + 1
            replacements_needed = window_size - max_freq
            
            if replacements_needed > k:
                # Shrink window
                left_char = s[left]
                char_count[left_char] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length

    def minWindow(self, s: str, t: str) -> str:  # LC 76
        """
        Problem 3: Minimum window substring containing all characters of t.
        
        Example:
            Input: s = "ADOBECODEBANC", t = "ABC"
            Output: "BANC"
        
        TC: O(n + m) where n = len(s), m = len(t)
        SC: O(m) - character frequencies of t
        
        How it works:
        1. Count required characters from t
        2. Expand window until all characters satisfied
        3. Shrink window while still valid
        4. Track minimum window
        """
        if not s or not t:
            return ""
        
        # Count required characters
        required = Counter(t)
        needed = len(required)
        formed = 0
        
        # Window character counts
        window_counts = {}
        
        left = 0
        min_len = float('inf')
        min_left = 0
        
        for right, char in enumerate(s):
            # Add character to window
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # Check if this character requirement is met
            if char in required and window_counts[char] == required[char]:
                formed += 1
            
            # Try to shrink window
            while formed == needed and left <= right:
                # Update minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left
                
                # Remove left character
                left_char = s[left]
                window_counts[left_char] -= 1
                
                # Check if requirement broken
                if left_char in required and window_counts[left_char] < required[left_char]:
                    formed -= 1
                
                left += 1
        
        return "" if min_len == float('inf') else s[min_left:min_left + min_len]

# Example trace for minWindow:
# s = "ADOBECODEBANC", t = "ABC"
# required = {'A':1, 'B':1, 'C':1}, needed = 3
#
# Expand until formed = 3:
# right=0-5: "ADOBEC", window has A(1), B(1), C(1), formed=3
#
# Shrink while valid:
# left=0: Remove 'A', formed=2 (invalid), stop
# Move right to find 'A' again...
#
# Eventually find "BANC" as minimum

sol = SlidingWindowHash()
print("Longest Substring:", sol.lengthOfLongestSubstring("abcabcbb"))  # 3
print("Character Replacement:", sol.characterReplacement("AABABBA", 1))  # 4
print("Min Window:", sol.minWindow("ADOBECODEBANC", "ABC"))  # "BANC"


# ================================================================
# PATTERN 4: HASH TABLE FOR GROUPING / CATEGORIZATION
# PATTERN EXPLANATION: Group elements by some computed property using hash table. Generate
# key based on element characteristics, use as hash table key. All elements with same key
# go in same group. Efficient for categorizing data by pattern, structure, or attribute.
#
# TYPICAL STEPS:
# 1. Initialize hash table (usually defaultdict(list))
# 2. For each element:
#    a. Compute key based on property (sorted chars, pattern, etc.)
#    b. Add element to group with that key
# 3. Extract groups from hash table values
#
# Applications: Group anagrams, group by pattern, categorize strings/numbers.
# ================================================================

class GroupingPattern:
    """
    Problem 1: Group anagrams together.
    
    Example:
        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        
        "eat", "tea", "ate" are anagrams (same characters)
    
    TC: O(n * m log m) where n = strings, m = max length
        O(n * m) with character count as key
    SC: O(n * m) - store all strings
    
    How it works:
    1. For each string, generate key (sorted string or char count)
    2. Group strings with same key
    3. Return all groups
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  # LC 49
        # Method 1: Using sorted string as key
        groups = defaultdict(list)
        
        for s in strs:
            # Sort characters to get canonical form
            key = ''.join(sorted(s))
            groups[key].append(s)
        
        return list(groups.values())
    
    def groupAnagrams_count(self, strs: List[str]) -> List[List[str]]:
        """
        Method 2: Using character count as key (O(n*m))
        """
        groups = defaultdict(list)
        
        for s in strs:
            # Count characters (26 letters)
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Use tuple of counts as key
            key = tuple(count)
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

    def findDuplicates(self, nums: List[int]) -> List[int]:  # LC 442
        """
        Problem 2: Find all duplicates in array where 1 ≤ nums[i] ≤ n.
        
        Example:
            Input: nums = [4,3,2,7,8,2,3,1]
            Output: [2,3]
        
        TC: O(n)
        SC: O(n) with hash table, O(1) with index marking
        
        Method 1: Hash table
        """
        seen = set()
        duplicates = []
        
        for num in nums:
            if num in seen:
                duplicates.append(num)
            else:
                seen.add(num)
        
        return duplicates
    
    def findDuplicates_inplace(self, nums: List[int]) -> List[int]:
        """
        Method 2: Index marking (O(1) space)
        Use sign to mark seen numbers
        """
        duplicates = []
        
        for num in nums:
            index = abs(num) - 1
            
            # If already negative, seen before
            if nums[index] < 0:
                duplicates.append(abs(num))
            else:
                # Mark as seen
                nums[index] *= -1
        
        return duplicates

    def isIsomorphic(self, s: str, t: str) -> bool:  # LC 205
        """
        Problem 3: Check if two strings are isomorphic.
        
        Example:
            Input: s = "egg", t = "add"
            Output: True
            
            'e' maps to 'a', 'g' maps to 'd'
        
        TC: O(n)
        SC: O(k) where k = unique characters
        
        How it works:
        1. Create two mappings: s->t and t->s
        2. For each character pair:
           - Check if mapping exists and matches
           - If not, create new mapping
        3. Must be one-to-one (bijection)
        """
        if len(s) != len(t):
            return False
        
        s_to_t = {}
        t_to_s = {}
        
        for char_s, char_t in zip(s, t):
            # Check s -> t mapping
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t
            
            # Check t -> s mapping (must be one-to-one)
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s
        
        return True

# Example trace for isIsomorphic:
# s = "egg", t = "add"
#
# i=0: 'e'->'a'
#   s_to_t = {'e':'a'}
#   t_to_s = {'a':'e'}
#
# i=1: 'g'->'d'
#   s_to_t = {'e':'a', 'g':'d'}
#   t_to_s = {'a':'e', 'd':'g'}
#
# i=2: 'g'->'d'
#   'g' maps to 'd'? Yes (s_to_t['g']=='d')
#   'd' maps to 'g'? Yes (t_to_s['d']=='g')
#   Valid!
#
# Return True

sol = GroupingPattern()
print("Group Anagrams:", sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print("Find Duplicates:", sol.findDuplicates([4,3,2,7,8,2,3,1]))  # [2,3]
print("Is Isomorphic:", sol.isIsomorphic("egg", "add"))  # True


# ================================================================
# PATTERN 5: HASH TABLE WITH COMPLEX KEYS
# PATTERN EXPLANATION: Use tuples, strings, or custom objects as hash table keys when
# simple values insufficient. Combine multiple attributes into single key. Enables
# tracking complex states, coordinate pairs, or multi-dimensional data. Powerful for
# problems requiring composite keys.
#
# TYPICAL STEPS:
# 1. Identify what attributes define uniqueness
# 2. Combine attributes into hashable key (tuple, frozenset, string)
# 3. Use as hash table key
# 4. Common patterns: (x, y) for coordinates, tuple for state
#
# Applications: Matrix coordinates, state tracking, multi-attribute indexing.
# ================================================================

class ComplexKeysPattern:
    """
    Problem 1: Check if there exists a path from start to end in grid.
    Track visited coordinates using (row, col) tuples.
    
    TC: O(m * n) - visit each cell once
    SC: O(m * n) - visited set
    """
    def validPath(self, grid: List[List[int]], start: List[int], end: List[int]) -> bool:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = [tuple(start)]
        visited.add(tuple(start))
        
        while queue:
            r, c = queue.pop(0)
            
            if [r, c] == end:
                return True
            
            # Try 4 directions
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = r + dr, c + dc
                
                if (0 <= nr < rows and 0 <= nc < cols and 
                    (nr, nc) not in visited and grid[nr][nc] == 0):
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        
        return False

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:  # LC 447
        """
        Problem 2: Count boomerang triplets (i,j,k) where distance(i,j) = distance(i,k).
        
        Example:
            Input: points = [[0,0],[1,0],[2,0]]
            Output: 2
            
            [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
        
        TC: O(n²)
        SC: O(n) - distance counts per point
        
        How it works:
        1. For each point i as center
        2. Count distances to all other points
        3. For distance d appearing k times: k*(k-1) ordered pairs
        """
        count = 0
        
        for i in range(len(points)):
            # Count distances from point i
            distance_count = {}
            
            for j in range(len(points)):
                if i == j:
                    continue
                
                # Calculate squared distance (avoid sqrt)
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                dist = dx * dx + dy * dy
                
                distance_count[dist] = distance_count.get(dist, 0) + 1
            
            # Count boomerangs for this center
            for d, cnt in distance_count.items():
                # Choose 2 from cnt points: cnt * (cnt-1)
                count += cnt * (cnt - 1)
        
        return count

# Example trace for numberOfBoomerangs:
# points = [[0,0],[1,0],[2,0]]
#
# Center at [0,0]:
#   Distance to [1,0]: 1² + 0² = 1
#   Distance to [2,0]: 2² + 0² = 4
#   distance_count = {1: 1, 4: 1}
#   No boomerangs (need count >= 2)
#
# Center at [1,0]:
#   Distance to [0,0]: 1² + 0² = 1
#   Distance to [2,0]: 1² + 0² = 1
#   distance_count = {1: 2}
#   Boomerangs: 2 * (2-1) = 2
#
# Center at [2,0]:
#   Distance to [0,0]: 2² + 0² = 4
#   Distance to [1,0]: 1² + 0² = 1
#   distance_count = {4: 1, 1: 1}
#   No boomerangs
#
# Total: 2

    def subarraySum(self, nums: List[int], k: int) -> int:  # LC 560
        """
        Problem 3: Count subarrays with sum equal to k.
        
        Example:
            Input: nums = [1,1,1], k = 2
            Output: 2
            
            [1,1] at indices 0-1 and 1-2
        
        TC: O(n)
        SC: O(n) - prefix sum counts
        
        How it works:
        1. Use prefix sum with hash table
        2. If (current_sum - k) exists in map: found subarray
        3. Count frequency of each prefix sum
        """
        prefix_sum = 0
        sum_count = {0: 1}  # Base case: empty prefix
        count = 0
        
        for num in nums:
            prefix_sum += num
            
            # Check if (prefix_sum - k) exists
            if prefix_sum - k in sum_count:
                count += sum_count[prefix_sum - k]
            
            # Update prefix sum count
            sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
        
        return count

sol = ComplexKeysPattern()
print("Number of Boomerangs:", sol.numberOfBoomerangs([[0,0],[1,0],[2,0]]))  # 2
print("Subarray Sum:", sol.subarraySum([1,1,1], 2))  # 2


# ================================================================
# PATTERN 6: HASH TABLE FOR CACHING / MEMOIZATION
# PATTERN EXPLANATION: Store computed results to avoid redundant calculations. Use problem
# state as key, result as value. Check cache before computing. Essential for optimizing
# recursive algorithms and avoiding repeated work. Related to dynamic programming.
#
# TYPICAL STEPS:
# 1. Define what represents state (parameters, current position, etc.)
# 2. Create hash table for cache
# 3. Before computing:
#    a. Check if state in cache
#    b. If yes: return cached result
# 4. Compute result
# 5. Store in cache
# 6. Return result
#
# Applications: Fibonacci, climbing stairs, LRU cache, memoization.
# ================================================================

class CachingPattern:
    """
    Problem 1: Fibonacci with memoization.
    
    TC: O(n) with memoization vs O(2^n) without
    SC: O(n) - cache storage
    
    How it works:
    1. Cache computed Fibonacci numbers
    2. Check cache before recursive call
    3. Store result in cache
    """
    def fib(self, n: int) -> int:  # LC 509
        cache = {}
        
        def helper(n):
            # Base cases
            if n <= 1:
                return n
            
            # Check cache
            if n in cache:
                return cache[n]
            
            # Compute and cache
            result = helper(n-1) + helper(n-2)
            cache[n] = result
            
            return result
        
        return helper(n)

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:  # LC 139
        """
        Problem 2: Check if string can be segmented into words from dictionary.
        
        Example:
            Input: s = "leetcode", wordDict = ["leet","code"]
            Output: True
            
            "leetcode" = "leet" + "code"
        
        TC: O(n² * m) where n = len(s), m = average word length
        SC: O(n) - memoization
        
        How it works:
        1. Try breaking string at each position
        2. Check if prefix in dictionary
        3. Recursively check suffix
        4. Memoize results for each starting position
        """
        word_set = set(wordDict)
        memo = {}
        
        def canBreak(start):
            # Base case: reached end
            if start == len(s):
                return True
            
            # Check cache
            if start in memo:
                return memo[start]
            
            # Try all possible words from this position
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                
                if word in word_set and canBreak(end):
                    memo[start] = True
                    return True
            
            memo[start] = False
            return False
        
        return canBreak(0)

# Example trace for wordBreak:
# s = "leetcode", wordDict = ["leet","code"]
# word_set = {"leet","code"}
#
# canBreak(0):
#   Try "l": not in set
#   Try "le": not in set
#   Try "lee": not in set
#   Try "leet": in set! Try canBreak(4)
#     canBreak(4):
#       Try "c": not in set
#       Try "co": not in set
#       Try "cod": not in set
#       Try "code": in set! Try canBreak(8)
#         canBreak(8):
#           start == len(s), return True
#         return True
#       memo[4] = True
#       return True
#     return True
#   memo[0] = True
#   return True

    def climbStairs(self, n: int) -> int:  # LC 70
        """
        Problem 3: Count ways to climb n stairs (1 or 2 steps at a time).
        
        TC: O(n) with memoization
        SC: O(n)
        """
        memo = {}
        
        def helper(n):
            if n <= 2:
                return n
            
            if n in memo:
                return memo[n]
            
            result = helper(n-1) + helper(n-2)
            memo[n] = result
            
            return result
        
        return helper(n)

sol = CachingPattern()
print("Fibonacci(10):", sol.fib(10))  # 55
print("Word Break:", sol.wordBreak("leetcode", ["leet","code"]))  # True
print("Climb Stairs(5):", sol.climbStairs(5))  # 8


# ================================================================
# SUMMARY OF HASH TABLE PATTERNS
# ================================================================
"""
Pattern 1 - Frequency Counting:
  - Count element occurrences
  - O(n) time, O(k) space
  - Use for: Anagrams, most frequent, character count
  - Example: LC 242 (Valid Anagram), LC 347 (Top K Frequent)

Pattern 2 - Hash Table for Lookup (Two Sum):
  - O(1) complement lookup
  - Convert O(n²) to O(n)
  - Use for: Sum problems, finding pairs, matching
  - Example: LC 1 (Two Sum), LC 523 (Subarray Sum)

Pattern 3 - Hash Table + Sliding Window:
  - Track elements in window
  - Expand/shrink with O(1) checks
  - Use for: Longest/shortest substring with constraints
  - Example: LC 3 (Longest Substring), LC 76 (Min Window)

Pattern 4 - Hash Table for Grouping:
  - Group by computed property
  - Generate key from characteristics
  - Use for: Group anagrams, categorization, pattern matching
  - Example: LC 49 (Group Anagrams), LC 205 (Isomorphic Strings)

Pattern 5 - Hash Table with Complex Keys:
  - Use tuples/custom keys
  - Track coordinates, states, multi-dimensional data
  - Use for: Grid problems, state tracking, composite keys
  - Example: LC 447 (Boomerangs), LC 560 (Subarray Sum)

Pattern 6 - Hash Table for Caching:
  - Memoize computed results
  - Avoid redundant calculations
  - Use for: DP problems, recursive optimization
  - Example: LC 139 (Word Break), LC 70 (Climb Stairs)

Master these 6 patterns and you'll handle 80-90% of hash table problems on LeetCode!

KEY TAKEAWAYS:
--------------
1. Hash table provides O(1) average lookup, insert, delete
2. Use Counter for frequency counting
3. Use defaultdict to avoid key existence checks
4. Two sum pattern: check if complement exists
5. Sliding window + hash for substring problems
6. Group by generating key from properties
7. Tuples work as hash table keys for coordinates/states
8. Memoization with hash table optimizes recursion
9. Space-time tradeoff: O(n) space for O(1) operations
10. Python dict is highly optimized, use it liberally

WHEN TO USE HASH TABLE:
-----------------------
✓ Use Hash Table when:
  - Need fast lookup by key
  - Counting frequencies
  - Detecting duplicates
  - Finding complements/pairs
  - Grouping by property
  - Caching results

✗ Don't use Hash Table when:
  - Need sorted order (use TreeMap)
  - Need range queries (use TreeMap/Array)
  - Only sequential access (use Array/List)
  - Memory critical and can use other structures

COMMON MISTAKES:
----------------
1. Forgetting to check if key exists before accessing
2. Using mutable objects as keys (lists, sets)
3. Not considering hash collisions in complexity
4. Iterating when lookup would be faster
5. Not using Counter/defaultdict when appropriate

OPTIMIZATION TIPS:
------------------
1. Use get() with default instead of checking existence
2. Use Counter for frequency counting
3. Use defaultdict to avoid initializing values
4. Clear large hash tables when done
5. Consider space-time tradeoff
6. Use sets when only need keys (no values)
"""