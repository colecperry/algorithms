"""
=================================================================
PREFIX SUM COMPLETE GUIDE
=================================================================

WHAT IS PREFIX SUM?
-------------------
Prefix Sum is a preprocessing technique that creates an array where each element stores
the cumulative sum of all elements up to that index. It enables O(1) range sum queries
after O(n) preprocessing, transforming expensive repeated calculations into efficient
lookups. The core idea: precompute cumulative values to answer range queries instantly.

Key characteristics:
- Preprocessing: Build prefix sum array in O(n) time
- Query: Answer range sum in O(1) time
- Space-time tradeoff: Use O(n) extra space for O(1) queries
- Formula: sum[i:j] = prefix[j] - prefix[i-1]
- Variants: Works for any associative operation (sum, XOR, product)

Basic concept:
```
Original array:  [3, 1, 4, 1, 5]
Prefix sum:      [3, 4, 8, 9, 14]
                  ↑  ↑  ↑  ↑   ↑
                  3  3+1 3+1+4 ... sum of all elements up to index
```

When to use Prefix Sum:
- Multiple range sum queries on static array
- Subarray sum problems (equals k, divisible by k)
- Counting subarrays with certain properties
- Converting O(n²) solutions to O(n)
- 2D matrix range sum queries
- Range update problems (difference array)

Common Prefix Sum problem types:
- Range sum queries (1D and 2D)
- Subarray sum equals k
- Continuous subarray sum
- Maximum subarray sum variations
- Count of subarrays with property
- Range update queries (difference array)
- Product/XOR prefix problems

PREFIX SUM CORE TEMPLATES
==========================
"""

from typing import List
from collections import defaultdict

# ================================================================
# 1D PREFIX SUM TEMPLATE
# ================================================================
def prefix_sum_1d_template(nums):
    """
    Build 1D prefix sum array for range queries
    TC: O(n) - build prefix array
    SC: O(n) - prefix array storage
    """
    n = len(nums)
    prefix = [0] * (n + 1)  # Extra space for index 0
    
    # Build prefix sum: prefix[i] = sum of nums[0] to nums[i-1]
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
    
    # Range sum query: sum of nums[left] to nums[right]
    def rangeSum(left, right):
        return prefix[right + 1] - prefix[left]
    
    return prefix, rangeSum

# ================================================================
# 2D PREFIX SUM TEMPLATE
# ================================================================
def prefix_sum_2d_template(matrix):
    """
    Build 2D prefix sum for matrix range queries
    TC: O(m * n) - build prefix matrix
    SC: O(m * n) - prefix matrix storage
    """
    if not matrix or not matrix[0]:
        return None
    
    rows, cols = len(matrix), len(matrix[0])
    # prefix[i][j] = sum of rectangle from (0,0) to (i-1,j-1)
    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
    
    # Build 2D prefix sum
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            prefix[r][c] = (matrix[r-1][c-1] + 
                           prefix[r-1][c] + 
                           prefix[r][c-1] - 
                           prefix[r-1][c-1])
    
    # Range sum query: sum of rectangle from (r1,c1) to (r2,c2)
    def rangeSumMatrix(r1, c1, r2, c2):
        return (prefix[r2+1][c2+1] - 
                prefix[r1][c2+1] - 
                prefix[r2+1][c1] + 
                prefix[r1][c1])
    
    return prefix, rangeSumMatrix

# ================================================================
# PREFIX SUM WITH HASHMAP TEMPLATE
# ================================================================
def prefix_sum_hashmap_template(nums, target):
    """
    Use prefix sum with hashmap for subarray problems
    TC: O(n) - single pass with hashmap
    SC: O(n) - hashmap storage
    """
    prefix_sum = 0
    count = 0
    # Map: prefix_sum -> frequency
    sum_freq = {0: 1}  # Base case: empty subarray
    
    for num in nums:
        prefix_sum += num
        
        # Check if (prefix_sum - target) exists
        if prefix_sum - target in sum_freq:
            count += sum_freq[prefix_sum - target]
        
        # Update frequency map
        sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1
    
    return count

# ================================================================
# DIFFERENCE ARRAY TEMPLATE
# ================================================================
def difference_array_template(n, updates):
    """
    Use difference array for range update queries
    TC: O(n + k) where k = number of updates
    SC: O(n) - difference array
    """
    diff = [0] * (n + 1)  # Extra space to avoid boundary check
    
    # Apply all updates to difference array
    for start, end, value in updates:
        diff[start] += value
        diff[end + 1] -= value
    
    # Convert difference array to actual array (prefix sum of diff)
    result = [0] * n
    result[0] = diff[0]
    for i in range(1, n):
        result[i] = result[i-1] + diff[i]
    
    return result

"""
TIME & SPACE COMPLEXITY REFERENCE
==================================

PREFIX SUM OPERATIONS COMPLEXITY:
----------------------------------
+---------------------------+------------------+------------------+
| Operation                 | Time Complexity  | Space Complexity |
+---------------------------+------------------+------------------+
| Build 1D prefix sum       | O(n)             | O(n)             |
| Range sum query (1D)      | O(1)             | O(1)             |
| Build 2D prefix sum       | O(m * n)         | O(m * n)         |
| Range sum query (2D)      | O(1)             | O(1)             |
| Difference array build    | O(n + k)         | O(n)             |
| Prefix sum with hashmap   | O(n)             | O(n)             |
+---------------------------+------------------+------------------+

COMMON PREFIX SUM PATTERNS COMPLEXITY:
--------------------------------------
+---------------------------+------------------+------------------+
| Pattern                   | Time Complexity  | Space Complexity |
+---------------------------+------------------+------------------+
| Range Sum Query           | O(n) + O(1)*q    | O(n)             |
| 2D Range Sum Query        | O(m*n) + O(1)*q  | O(m * n)         |
| Subarray Sum Equals K     | O(n)             | O(n)             |
| Continuous Subarray Sum   | O(n)             | O(n)             |
| Maximum Subarray Sum      | O(n)             | O(1)             |
| Range Update Queries      | O(n + k)         | O(n)             |
| Product Except Self       | O(n)             | O(1) optimized   |
| Count Subarray Sum        | O(n)             | O(n)             |
+---------------------------+------------------+------------------+

WHERE:
- n = array length
- m, n = matrix dimensions
- q = number of queries
- k = number of updates

COMPLEXITY NOTES:
-----------------
1. 1D Prefix Sum (Range Query): O(n) build + O(1) per query
   - Build prefix array: O(n) preprocessing
   - Each range sum query: O(1) with formula prefix[r+1] - prefix[l]
   - Total for q queries: O(n + q)
   
   Without prefix sum: O(q * n) - each query scans range
   With prefix sum: O(n + q) - much better for multiple queries
   
   Use when: Multiple queries on static array
   Common pattern: prefix[i] = prefix[i-1] + nums[i]

2. 2D Prefix Sum (Matrix Range Query): O(m*n) build + O(1) per query
   - Build 2D prefix matrix: O(m * n) preprocessing
   - Each rectangle sum query: O(1) with inclusion-exclusion formula
   - Total for q queries: O(m*n + q)
   
   Formula: sum = bottom-right - top-right - bottom-left + top-left
   Use when: Multiple rectangle sum queries on static matrix
   Common pattern: Include top, left, exclude diagonal overlap

3. Prefix Sum with HashMap: O(n) time, O(n) space
   - Single pass through array: O(n)
   - HashMap stores prefix sum frequencies: O(n)
   - Check if (current_sum - target) exists: O(1) per element
   
   Key insight: If prefix[j] - prefix[i] = k, then subarray i+1 to j sums to k
   Use when: Finding subarrays with specific sum property
   Common pattern: sum_map[prefix_sum - target] gives count
   
   Similar to two-sum pattern but for subarrays

4. Difference Array (Range Updates): O(n + k) time, O(n) space
   - Build difference array: O(k) for k updates
   - Convert to result: O(n) prefix sum of differences
   - Total: O(n + k)
   
   Without difference array: O(k * n) - each update scans range
   With difference array: O(n + k) - batch all updates
   
   Key insight: Range update [l, r] becomes point updates: diff[l]++, diff[r+1]--
   Use when: Multiple range updates, then query result
   Common pattern: Increment start, decrement end+1

5. Maximum Subarray Sum (Kadane's): O(n) time, O(1) space
   - Single pass: O(n)
   - Only track current sum and max: O(1) space
   - Not traditional prefix sum but related concept
   
   Pattern: Keep running sum, reset if negative
   Use when: Finding optimal contiguous subarray
   Variant of prefix sum optimization

6. Product Except Self: O(n) time, O(1) space
   - Left pass and right pass: O(n)
   - Can be done in-place in output array: O(1) extra space
   - Uses prefix product concept
   
   Pattern: product[i] = left_product * right_product
   Use when: Need contribution from both sides excluding current
   Related to prefix/suffix products

GENERAL PREFIX SUM OPTIMIZATION:
---------------------------------
Space optimization:
- Use in-place modification when possible
- For 2D, optimize to O(min(m,n)) if queries are limited
- Difference array reuses space

Time optimization:
- Preprocessing pays off with multiple queries
- HashMap for O(n) instead of O(n²) subarray checks
- Batch updates with difference array

WHEN TO USE EACH PATTERN:
--------------------------
Basic Prefix Sum:
  - Multiple range sum queries
  - Static array (no updates between queries)
  - Want O(1) query time

Prefix Sum + HashMap:
  - Subarray sum problems (equals k, divisible by k)
  - Count subarrays with property
  - Find longest/shortest subarray

Difference Array:
  - Multiple range updates
  - Want to batch all updates before querying
  - Range increment/decrement operations

2D Prefix Sum:
  - Matrix range sum queries
  - Rectangle sum in grid
  - 2D cumulative calculations

Running Sum Variants:
  - Product except self
  - XOR prefix for range XOR
  - Maximum subarray (Kadane's)
  - Cumulative calculations
"""

"""
PREFIX SUM PATTERNS
===================
"""

# ================================================================
# PATTERN 1: BASIC 1D PREFIX SUM (RANGE SUM QUERIES)
# PATTERN EXPLANATION: Precompute cumulative sums to answer range sum queries in O(1) time.
# Build prefix array where prefix[i] = sum of elements from 0 to i-1. Range sum from index
# left to right equals prefix[right+1] - prefix[left]. Use extra space at index 0 to avoid
# edge cases. Essential for problems with multiple queries on static array.
#
# TYPICAL STEPS:
# 1. Create prefix array with size n+1 (index 0 = 0 for convenience)
# 2. Build prefix: prefix[i] = prefix[i-1] + nums[i-1]
# 3. Query range [left, right]: return prefix[right+1] - prefix[left]
# 4. Handle multiple queries in O(1) each after O(n) preprocessing
#
# Applications: Range sum queries, immutable array range sum, sparse matrix queries.
# ================================================================

class RangeSumQuery:
    """
    Problem: Given an integer array nums, handle multiple queries of the following type:
    Calculate the sum of elements between indices left and right (inclusive).
    
    Example:
        nums = [1, 2, 3, 4, 5]
        
        Query(0, 2): sum of [1,2,3] = 6
        Query(1, 4): sum of [2,3,4,5] = 14
        Query(2, 2): sum of [3] = 3
    
    TC: O(n) preprocessing, O(1) per query
    SC: O(n) for prefix array
    
    How it works:
    1. Build prefix sum: prefix[i] = sum of first i elements
    2. Range sum formula: prefix[right+1] - prefix[left]
    3. Example: sum(1 to 4) = prefix[5] - prefix[1] = 14 - 1 = 13
    
    Why it works:
    prefix[right+1] = sum(0 to right)
    prefix[left] = sum(0 to left-1)
    Difference = sum(left to right)
    """
    def __init__(self, nums: List[int]):  # LC 303 - Range Sum Query Immutable
        # Build prefix sum array
        # prefix[i] = sum of nums[0] to nums[i-1]
        self.prefix = [0] * (len(nums) + 1)
        
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]
    
    def sumRange(self, left: int, right: int) -> int:
        """Return sum of elements from left to right (inclusive)"""
        return self.prefix[right + 1] - self.prefix[left]

# Example trace:
# nums = [1, 2, 3, 4, 5]
#
# Build prefix:
# prefix[0] = 0
# prefix[1] = 0 + 1 = 1     (sum of nums[0:1])
# prefix[2] = 1 + 2 = 3     (sum of nums[0:2])
# prefix[3] = 3 + 3 = 6     (sum of nums[0:3])
# prefix[4] = 6 + 4 = 10    (sum of nums[0:4])
# prefix[5] = 10 + 5 = 15   (sum of nums[0:5])
# prefix = [0, 1, 3, 6, 10, 15]
#
# Query(1, 3): sum of nums[1:4] = [2,3,4]
#   prefix[4] - prefix[1] = 10 - 1 = 9 ✓
#
# Query(0, 2): sum of nums[0:3] = [1,2,3]
#   prefix[3] - prefix[0] = 6 - 0 = 6 ✓

# Test
rsq = RangeSumQuery([1, 2, 3, 4, 5])
print("Range Sum Query (0,2):", rsq.sumRange(0, 2))  # 6
print("Range Sum Query (1,4):", rsq.sumRange(1, 4))  # 14


# ================================================================
# PATTERN 2: 2D PREFIX SUM (MATRIX RANGE SUM)
# PATTERN EXPLANATION: Extend prefix sum to 2D for rectangle sum queries. Build matrix where
# each cell stores sum of rectangle from (0,0) to (i-1,j-1). Use inclusion-exclusion principle
# for queries: add bottom-right, subtract top strip and left strip, add back top-left corner
# (which was subtracted twice). Essential for multiple rectangle sum queries.
#
# TYPICAL STEPS:
# 1. Create prefix matrix with size (m+1) x (n+1)
# 2. Build: prefix[i][j] = matrix[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
# 3. Query rectangle (r1,c1) to (r2,c2):
#    sum = prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]
# 4. Each query is O(1) after O(m*n) preprocessing
#
# Applications: 2D range sum, image processing, submatrix sum problems.
# ================================================================

class RangeSumQuery2D:
    """
    Problem: Given a 2D matrix, handle multiple queries of sum of elements inside
    rectangle defined by (row1, col1) as top-left and (row2, col2) as bottom-right.
    
    Example:
        matrix = [[3, 0, 1, 4, 2],
                  [5, 6, 3, 2, 1],
                  [1, 2, 0, 1, 5],
                  [4, 1, 0, 1, 7],
                  [1, 0, 3, 0, 5]]
        
        Query(2,1,4,3): Sum of rectangle from (2,1) to (4,3)
        = 2+0+1 + 1+0+1 + 0+3+0 = 8
    
    TC: O(m * n) preprocessing, O(1) per query
    SC: O(m * n) for prefix matrix
    
    How it works:
    1. prefix[i][j] = sum of rectangle from (0,0) to (i-1,j-1)
    2. To build: add current cell + sum from top + sum from left - diagonal (counted twice)
    3. To query: use inclusion-exclusion to get exact rectangle
    
    Inclusion-Exclusion formula:
    Sum = Bottom-right - Top strip - Left strip + Top-left corner
    (Top-left added back because it was subtracted in both strips)
    """
    def __init__(self, matrix: List[List[int]]):  # LC 304 - Range Sum Query 2D
        if not matrix or not matrix[0]:
            self.prefix = None
            return
        
        rows, cols = len(matrix), len(matrix[0])
        # prefix[i][j] = sum of rectangle (0,0) to (i-1,j-1)
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        # Build 2D prefix sum
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                self.prefix[r][c] = (
                    matrix[r-1][c-1] +           # Current cell
                    self.prefix[r-1][c] +        # Sum from top
                    self.prefix[r][c-1] -        # Sum from left
                    self.prefix[r-1][c-1]        # Remove diagonal (counted twice)
                )
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """Return sum of rectangle from (row1,col1) to (row2,col2)"""
        if not self.prefix:
            return 0
        
        # Inclusion-exclusion formula
        return (
            self.prefix[row2+1][col2+1] -      # Bottom-right (includes everything)
            self.prefix[row1][col2+1] -        # Subtract top strip
            self.prefix[row2+1][col1] +        # Subtract left strip
            self.prefix[row1][col1]            # Add back top-left (subtracted twice)
        )

# Example trace:
# matrix = [[1,2],
#           [3,4]]
#
# Build prefix:
# prefix[0][0] = 0, prefix[0][1] = 0, prefix[0][2] = 0
# prefix[1][0] = 0, prefix[1][1] = 1, prefix[1][2] = 1+2 = 3
# prefix[2][0] = 0, prefix[2][1] = 1+3 = 4, prefix[2][2] = 1+2+3+4 = 10
#
# prefix = [[0, 0, 0],
#           [0, 1, 3],
#           [0, 4, 10]]
#
# Query(0,0,1,1): Sum of entire matrix
#   prefix[2][2] - prefix[0][2] - prefix[2][0] + prefix[0][0]
#   = 10 - 0 - 0 + 0 = 10 ✓
#
# Query(0,1,1,1): Sum of right column [2,4]
#   prefix[2][2] - prefix[0][2] - prefix[2][1] + prefix[0][1]
#   = 10 - 0 - 4 + 0 = 6 ✓

# Test
rsq2d = RangeSumQuery2D([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
print("2D Range Sum Query (2,1,4,3):", rsq2d.sumRegion(2, 1, 4, 3))  # 8
print("2D Range Sum Query (1,1,2,2):", rsq2d.sumRegion(1, 1, 2, 2))  # 11


# ================================================================
# PATTERN 3: PREFIX SUM WITH HASHMAP (SUBARRAY SUM PROBLEMS)
# PATTERN EXPLANATION: Combine prefix sum with hashmap to find subarrays with specific sum
# properties in O(n) time. Key insight: if prefix[j] - prefix[i] = k, then subarray from
# i+1 to j has sum k. Store prefix sums in hashmap to check if (current_sum - target) exists.
# This converts O(n²) brute force to O(n) with hashmap lookups.
#
# TYPICAL STEPS:
# 1. Initialize hashmap with {0: 1} for empty subarray case
# 2. Iterate through array, maintaining running prefix sum
# 3. Check if (prefix_sum - target) exists in hashmap
# 4. If yes, found subarrays ending at current index
# 5. Update hashmap with current prefix_sum
#
# Applications: Subarray sum equals k, continuous subarray sum, subarray sum divisible by k.
# ================================================================

class SubarraySumProblems:
    """
    Problem: Given an array of integers and target k, return the total number of
    continuous subarrays whose sum equals k.
    
    Example:
        nums = [1, 2, 3, 4, 5], k = 5
        
        Subarrays with sum 5:
        - [5] at index 4
        - [2, 3] at indices 1-2
        
        Output: 2
    
    TC: O(n) - single pass through array
    SC: O(n) - hashmap stores prefix sums
    
    How it works:
    1. Track cumulative sum (prefix sum) as we go
    2. If (current_sum - k) exists in map, found subarrays
    3. Why? If prefix[j] - prefix[i] = k, then sum(i+1 to j) = k
    4. Example: prefix_sum = 8, k = 5
       - Need prefix_sum = 3 to exist before current position
       - If prefix[i] = 3 and prefix[j] = 8, then sum(i+1 to j) = 5
    """
    def subarraySum(self, nums: List[int], k: int) -> int:  # LC 560
        count = 0
        prefix_sum = 0
        # Map: prefix_sum -> frequency
        # Initialize with 0:1 for subarrays starting from index 0
        sum_freq = {0: 1}
        
        for num in nums:
            # Update running sum
            prefix_sum += num
            
            # Check if there's a previous prefix sum such that
            # current_prefix_sum - previous_prefix_sum = k
            # i.e., previous_prefix_sum = current_prefix_sum - k
            if prefix_sum - k in sum_freq:
                count += sum_freq[prefix_sum - k]
            
            # Update frequency of current prefix sum
            sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1
        
        return count

# Example trace:
# nums = [1, 2, 3, 4, 5], k = 9
#
# sum_freq = {0: 1}, count = 0
#
# i=0, num=1:
#   prefix_sum = 1
#   Check 1-9=-8 in map? No
#   sum_freq = {0:1, 1:1}, count = 0
#
# i=1, num=2:
#   prefix_sum = 3
#   Check 3-9=-6 in map? No
#   sum_freq = {0:1, 1:1, 3:1}, count = 0
#
# i=2, num=3:
#   prefix_sum = 6
#   Check 6-9=-3 in map? No
#   sum_freq = {0:1, 1:1, 3:1, 6:1}, count = 0
#
# i=3, num=4:
#   prefix_sum = 10
#   Check 10-9=1 in map? YES! count += 1
#   (Subarray from index 1 to 3: [2,3,4] = 9)
#   sum_freq = {0:1, 1:1, 3:1, 6:1, 10:1}, count = 1
#
# i=4, num=5:
#   prefix_sum = 15
#   Check 15-9=6 in map? YES! count += 1
#   (Subarray from index 3 to 4: [4,5] = 9)
#   sum_freq = {..., 15:1}, count = 2
#
# Output: 2

    def subarraysDivByK(self, nums: List[int], k: int) -> int:  # LC 974
        """
        Problem: Count subarrays with sum divisible by k.
        
        Key insight: If (prefix[j] - prefix[i]) % k = 0, then subarray sum is divisible by k
        This means: prefix[j] % k = prefix[i] % k
        
        TC: O(n), SC: O(k) - at most k different remainders
        """
        count = 0
        prefix_sum = 0
        # Map: remainder -> frequency
        remainder_freq = {0: 1}  # Empty subarray has remainder 0
        
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            
            # Handle negative remainders (Python modulo can be negative)
            if remainder < 0:
                remainder += k
            
            # If this remainder seen before, those positions form valid subarrays
            if remainder in remainder_freq:
                count += remainder_freq[remainder]
            
            remainder_freq[remainder] = remainder_freq.get(remainder, 0) + 1
        
        return count

# Example:
# nums = [4,5,0,-2,-3,1], k = 5
#
# Remainders when divided by 5:
# prefix_sum: 4, 9, 9, 7, 4, 5
# remainder:  4, 4, 4, 2, 4, 0
#
# When remainder=4 appears 4 times:
# - First and second: subarray [5] divisible by 5? No, but [5,0,-2,-3,1] is
# Actually let me recalculate...
# prefix: 4(r=4), 9(r=4), 9(r=4), 7(r=2), 4(r=4), 5(r=0)
# Count subarrays where prefix[j]%k = prefix[i]%k
# r=4 appears at indices 0,1,2,4: can form 6 pairs
# ... this gives us subarrays [5,0,-2,-3,1], [0], [-2,-3], [5,0], etc.

sol = SubarraySumProblems()
print("Subarray Sum Equals K:", sol.subarraySum([1,1,1], 2))  # 2
print("Subarrays Divisible by K:", sol.subarraysDivByK([4,5,0,-2,-3,1], 5))  # 7


# ================================================================
# PATTERN 4: DIFFERENCE ARRAY (RANGE UPDATE QUERIES)
# PATTERN EXPLANATION: Optimize multiple range updates using difference array. Instead of
# updating every element in range [l, r], mark only boundaries: increment start, decrement
# end+1. After all updates, compute prefix sum of difference array to get final values.
# Converts O(k*n) for k updates to O(n+k). Essential for batch range modifications.
#
# TYPICAL STEPS:
# 1. Create difference array initialized to 0
# 2. For each update [left, right, val]:
#    - diff[left] += val
#    - diff[right+1] -= val
# 3. Compute prefix sum of difference array to get final result
# 4. result[i] = result[i-1] + diff[i]
#
# Applications: Range addition, car pooling, corporate flight bookings, meeting rooms.
# ================================================================

class RangeUpdateQueries:
    """
    Problem: You are given an empty array of length n. Perform multiple operations to
    add value val to all elements in range [left, right]. Return final array.
    
    Example:
        n = 5, updates = [[1,3,2], [2,4,3], [0,2,-2]]
        
        Initial: [0, 0, 0, 0, 0]
        After [1,3,2]: [0, 2, 2, 2, 0]
        After [2,4,3]: [0, 2, 5, 5, 3]
        After [0,2,-2]: [-2, 0, 3, 5, 3]
        
        Output: [-2, 0, 3, 5, 3]
    
    TC: O(n + k) where k = number of updates
    SC: O(n) for difference array
    
    How it works:
    1. Use difference array: diff[i] = result[i] - result[i-1]
    2. Range update [l, r, val] becomes:
       - diff[l] += val (start of range)
       - diff[r+1] -= val (end of range)
    3. Final array = prefix sum of difference array
    
    Why it works:
    - Incrementing diff[l] propagates +val to all elements from l onward
    - Decrementing diff[r+1] stops the propagation after r
    - Prefix sum converts differences back to actual values
    """
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:  # LC 370
        # Difference array
        diff = [0] * (length + 1)  # Extra space to avoid boundary check
        
        # Apply all updates to difference array
        for left, right, val in updates:
            diff[left] += val        # Start range
            diff[right + 1] -= val   # End range (stop propagation)
        
        # Convert difference array to result using prefix sum
        result = [0] * length
        result[0] = diff[0]
        for i in range(1, length):
            result[i] = result[i-1] + diff[i]
        
        return result

# Example trace:
# length = 5, updates = [[1,3,2], [2,4,3], [0,2,-2]]
#
# Initial diff: [0, 0, 0, 0, 0, 0]
#
# Update [1,3,2]:
#   diff[1] += 2, diff[4] -= 2
#   diff = [0, 2, 0, 0, -2, 0]
#
# Update [2,4,3]:
#   diff[2] += 3, diff[5] -= 3
#   diff = [0, 2, 3, 0, -2, -3]
#
# Update [0,2,-2]:
#   diff[0] += -2, diff[3] -= -2
#   diff = [-2, 2, 3, 2, -2, -3]
#
# Compute prefix sum:
# result[0] = -2
# result[1] = -2 + 2 = 0
# result[2] = 0 + 3 = 3
# result[3] = 3 + 2 = 5
# result[4] = 5 + (-2) = 3
#
# Output: [-2, 0, 3, 5, 3]

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:  # LC 1094
        """
        Problem: Car with capacity can pick up/drop off passengers. Each trip is
        [numPassengers, from, to]. Return if possible to complete all trips.
        
        This is range update problem:
        - Each trip adds passengers at 'from' and removes at 'to'
        - Check if capacity ever exceeded
        
        TC: O(n + max_location), SC: O(max_location)
        """
        # Find max location to determine array size
        max_loc = max(trip[2] for trip in trips)
        diff = [0] * (max_loc + 1)
        
        # Apply all trips to difference array
        for passengers, start, end in trips:
            diff[start] += passengers      # Pick up passengers
            diff[end] -= passengers        # Drop off passengers
        
        # Check if capacity exceeded at any point
        current_passengers = 0
        for i in range(max_loc + 1):
            current_passengers += diff[i]
            if current_passengers > capacity:
                return False
        
        return True

# Example:
# trips = [[2,1,5],[3,3,7]], capacity = 4
#
# diff = [0, 0, 0, 0, 0, 0, 0, 0]
#
# Trip [2,1,5]:
#   diff[1] += 2, diff[5] -= 2
#   diff = [0, 2, 0, 0, 0, -2, 0, 0]
#
# Trip [3,3,7]:
#   diff[3] += 3, diff[7] -= 3
#   diff = [0, 2, 0, 3, 0, -2, 0, -3]
#
# Check capacity:
# Location 0: 0 passengers
# Location 1: 2 passengers (OK)
# Location 2: 2 passengers (OK)
# Location 3: 5 passengers (EXCEEDS capacity 4!)
# 
# Output: False

sol = RangeUpdateQueries()
print("Range Addition:", sol.getModifiedArray(5, [[1,3,2],[2,4,3],[0,2,-2]]))  # [-2,0,3,5,3]
print("Car Pooling:", sol.carPooling([[2,1,5],[3,3,7]], 4))  # False


# ================================================================
# PATTERN 5: PREFIX SUM OPTIMIZATION (CONVERT O(N²) TO O(N))
# PATTERN EXPLANATION: Use prefix sum to optimize problems from O(n²) to O(n) by avoiding
# repeated sum calculations. Common in problems where you need to check all subarrays or
# compute something for each position based on previous positions. Prefix sum eliminates
# the inner loop by providing instant access to range sums.
#
# TYPICAL STEPS:
# 1. Identify O(n²) brute force that recalculates sums
# 2. Build prefix sum array in O(n)
# 3. Replace inner sum loop with O(1) prefix lookup
# 4. Overall complexity reduces from O(n²) to O(n)
#
# Applications: Contiguous array, max subarray average, ways to split array, running sums.
# ================================================================

class PrefixSumOptimization:
    """
    Problem 1: Given array with equal numbers of 0s and 1s, find maximum length of
    contiguous subarray with equal number of 0s and 1s.
    
    Example:
        nums = [0,1,0,1,1,0]
        
        Subarray [0,1,0,1] has equal 0s and 1s, length = 4
        Subarray [1,0,1,0] has equal 0s and 1s, length = 4
        
        Output: 4
    
    TC: O(n) - single pass with hashmap
    SC: O(n) - hashmap for prefix sums
    
    How it works:
    1. Convert 0s to -1s: equal 0s and 1s ⟺ sum = 0
    2. Use prefix sum with hashmap
    3. If prefix_sum seen before, subarray between has sum 0
    4. Track earliest occurrence of each prefix_sum for max length
    
    Key insight: If prefix[i] = prefix[j], then sum(i+1 to j) = 0
    """
    def findMaxLength(self, nums: List[int]) -> int:  # LC 525
        max_length = 0
        prefix_sum = 0
        # Map: prefix_sum -> earliest index
        sum_index = {0: -1}  # Base case: sum 0 before start
        
        for i, num in enumerate(nums):
            # Convert 0 to -1 for sum calculation
            prefix_sum += 1 if num == 1 else -1
            
            if prefix_sum in sum_index:
                # Found subarray with sum 0 (equal 0s and 1s)
                length = i - sum_index[prefix_sum]
                max_length = max(max_length, length)
            else:
                # Store earliest occurrence
                sum_index[prefix_sum] = i
        
        return max_length

# Example trace:
# nums = [0,1,0,1,1,0]
# Convert 0→-1: [-1,1,-1,1,1,-1]
#
# sum_index = {0: -1}, max_length = 0
#
# i=0, num=-1:
#   prefix_sum = -1
#   Not in map, sum_index = {0:-1, -1:0}
#
# i=1, num=1:
#   prefix_sum = 0
#   In map! length = 1 - (-1) = 2
#   max_length = 2
#   (Subarray [0,1] has equal 0s and 1s)
#
# i=2, num=-1:
#   prefix_sum = -1
#   In map! length = 2 - 0 = 2
#   max_length = 2
#
# i=3, num=1:
#   prefix_sum = 0
#   In map! length = 3 - (-1) = 4
#   max_length = 4
#   (Subarray [0,1,0,1] has equal 0s and 1s)
#
# i=4, num=1:
#   prefix_sum = 1
#   Not in map, sum_index = {..., 1:4}
#
# i=5, num=-1:
#   prefix_sum = 0
#   In map! length = 5 - (-1) = 6
#   max_length = 6
#   (Entire array has equal 0s and 1s)
#
# Output: 6

    def pivotIndex(self, nums: List[int]) -> int:  # LC 724
        """
        Problem 2: Find pivot index where sum of left elements equals sum of right.
        
        Brute force: O(n²) - for each index, sum left and right
        Optimized: O(n) - use total sum and running sum
        
        TC: O(n), SC: O(1)
        """
        total_sum = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            # Right sum = total - left - current
            right_sum = total_sum - left_sum - num
            
            if left_sum == right_sum:
                return i
            
            left_sum += num
        
        return -1

    def productExceptSelf(self, nums: List[int]) -> List[int]:  # LC 238
        """
        Problem 3: Return array where answer[i] = product of all elements except nums[i].
        Cannot use division and must be O(n).
        
        Solution: Use prefix and suffix products
        - answer[i] = left_product[i-1] * right_product[i+1]
        
        TC: O(n), SC: O(1) excluding output array
        """
        n = len(nums)
        answer = [1] * n
        
        # Build left products in answer array
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
        
        # Build right products and multiply with left
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer

# Example for product except self:
# nums = [1, 2, 3, 4]
#
# Left products:
# i=0: answer[0] = 1, left_product = 1
# i=1: answer[1] = 1, left_product = 2
# i=2: answer[2] = 2, left_product = 6
# i=3: answer[3] = 6, left_product = 24
# answer = [1, 1, 2, 6]
#
# Right products:
# i=3: answer[3] = 6 * 1 = 6, right_product = 4
# i=2: answer[2] = 2 * 4 = 8, right_product = 12
# i=1: answer[1] = 1 * 12 = 12, right_product = 24
# i=0: answer[0] = 1 * 24 = 24, right_product = 24
# answer = [24, 12, 8, 6]
#
# Output: [24, 12, 8, 6]

sol = PrefixSumOptimization()
print("Max Length Equal 0s 1s:", sol.findMaxLength([0,1,0,1,1,0]))  # 6
print("Pivot Index:", sol.pivotIndex([1,7,3,6,5,6]))  # 3
print("Product Except Self:", sol.productExceptSelf([1,2,3,4]))  # [24,12,8,6]


# ================================================================
# PATTERN 6: RUNNING SUM VARIATIONS (CUMULATIVE CALCULATIONS)
# PATTERN EXPLANATION: Extend prefix sum concept to other operations like products, XOR,
# maximum, minimum, or custom cumulative functions. The key is any operation that can be
# computed incrementally. Often combined with additional data structures or conditions.
# Use when you need cumulative information while traversing array.
#
# TYPICAL STEPS:
# 1. Initialize accumulator (sum, product, xor, max, etc.)
# 2. Iterate through array updating accumulator
# 3. Use accumulator for current decision or calculation
# 4. May combine with hashmap, sliding window, or other techniques
#
# Applications: Running sum, maximum subarray (Kadane's), XOR queries, cumulative max/min.
# ================================================================

class RunningSumVariations:
    """
    Problem 1: Given array, return running sum where runningSum[i] = sum(nums[0]...nums[i]).
    
    Example:
        nums = [1, 2, 3, 4]
        Output: [1, 3, 6, 10]
    
    TC: O(n), SC: O(1) excluding output
    """
    def runningSum(self, nums: List[int]) -> List[int]:  # LC 1480
        """Basic running sum (in-place prefix sum)"""
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

    def maxSubArray(self, nums: List[int]) -> int:  # LC 53 - Kadane's Algorithm
        """
        Problem 2: Find contiguous subarray with largest sum.
        
        Example:
            nums = [-2,1,-3,4,-1,2,1,-5,4]
            Subarray [4,-1,2,1] has largest sum = 6
        
        TC: O(n), SC: O(1)
        
        How it works (Kadane's Algorithm):
        1. Track current sum and max sum
        2. At each position, decide: extend current or start new
        3. If current_sum < 0, starting fresh is better
        4. Update max_sum with current_sum
        
        This is running sum with reset condition.
        """
        max_sum = nums[0]
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            # Either extend current subarray or start new from current element
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        
        return max_sum

# Example trace for Kadane's:
# nums = [-2,1,-3,4,-1,2,1,-5,4]
#
# max_sum = -2, current_sum = -2
#
# i=1, num=1:
#   current_sum = max(1, -2+1=-1) = 1 (start new)
#   max_sum = max(-2, 1) = 1
#
# i=2, num=-3:
#   current_sum = max(-3, 1-3=-2) = -2
#   max_sum = 1
#
# i=3, num=4:
#   current_sum = max(4, -2+4=2) = 4 (start new)
#   max_sum = max(1, 4) = 4
#
# i=4, num=-1:
#   current_sum = max(-1, 4-1=3) = 3 (extend)
#   max_sum = 4
#
# i=5, num=2:
#   current_sum = max(2, 3+2=5) = 5 (extend)
#   max_sum = max(4, 5) = 5
#
# i=6, num=1:
#   current_sum = max(1, 5+1=6) = 6 (extend)
#   max_sum = max(5, 6) = 6
#
# i=7, num=-5:
#   current_sum = max(-5, 6-5=1) = 1 (extend)
#   max_sum = 6
#
# i=8, num=4:
#   current_sum = max(4, 1+4=5) = 5 (extend)
#   max_sum = 6
#
# Output: 6

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:  # LC 1310
        """
        Problem 3: Answer queries where each query asks for XOR of arr[left:right+1].
        
        XOR has property: a ^ a = 0, so prefix_xor[right] ^ prefix_xor[left-1] gives range XOR
        
        TC: O(n + q) where q = number of queries
        SC: O(n) for prefix XOR array
        """
        n = len(arr)
        # Build prefix XOR
        prefix_xor = [0] * (n + 1)
        for i in range(n):
            prefix_xor[i+1] = prefix_xor[i] ^ arr[i]
        
        # Answer queries
        result = []
        for left, right in queries:
            # XOR of range [left, right] = prefix_xor[right+1] ^ prefix_xor[left]
            result.append(prefix_xor[right+1] ^ prefix_xor[left])
        
        return result

# Example for XOR:
# arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
#
# Build prefix XOR:
# prefix_xor[0] = 0
# prefix_xor[1] = 0 ^ 1 = 1
# prefix_xor[2] = 1 ^ 3 = 2
# prefix_xor[3] = 2 ^ 4 = 6
# prefix_xor[4] = 6 ^ 8 = 14
# prefix_xor = [0, 1, 2, 6, 14]
#
# Query [0,1]: prefix_xor[2] ^ prefix_xor[0] = 2 ^ 0 = 2 (1^3=2) ✓
# Query [1,2]: prefix_xor[3] ^ prefix_xor[1] = 6 ^ 1 = 7 (3^4=7) ✓
# Query [0,3]: prefix_xor[4] ^ prefix_xor[0] = 14 ^ 0 = 14 (1^3^4^8=14) ✓
# Query [3,3]: prefix_xor[4] ^ prefix_xor[3] = 14 ^ 6 = 8 (just 8) ✓
#
# Output: [2, 7, 14, 8]

sol = RunningSumVariations()
print("Running Sum:", sol.runningSum([1,2,3,4]))  # [1,3,6,10]
print("Max Subarray Sum:", sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
print("XOR Queries:", sol.xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]))  # [2,7,14,8]


# ================================================================
# SUMMARY OF PREFIX SUM PATTERNS
# ================================================================
"""
Pattern 1 - Basic 1D Prefix Sum:
  - Precompute cumulative sums for O(1) range queries
  - Build prefix array in O(n), query in O(1)
  - Use for: Range sum queries, immutable array problems
  - Example: LC 303 (Range Sum Query - Immutable)

Pattern 2 - 2D Prefix Sum:
  - Extend to matrices for rectangle sum queries
  - Use inclusion-exclusion principle
  - Use for: Matrix range sum, image processing
  - Example: LC 304 (Range Sum Query 2D - Immutable)

Pattern 3 - Prefix Sum with HashMap:
  - Find subarrays with specific sum properties
  - Convert O(n²) to O(n) with hashmap lookups
  - Use for: Subarray sum equals k, continuous subarray sum
  - Example: LC 560 (Subarray Sum Equals K), LC 974 (Subarray Sums Divisible by K)

Pattern 4 - Difference Array:
  - Batch multiple range updates efficiently
  - Convert O(k*n) to O(n+k) for k updates
  - Use for: Range addition, car pooling, flight bookings
  - Example: LC 370 (Range Addition), LC 1094 (Car Pooling)

Pattern 5 - Prefix Sum Optimization:
  - Optimize O(n²) brute force to O(n)
  - Eliminate repeated sum calculations
  - Use for: Contiguous array, product except self
  - Example: LC 525 (Contiguous Array), LC 238 (Product Except Self)

Pattern 6 - Running Sum Variations:
  - Extend to other cumulative operations (XOR, product, max)
  - Combine with other techniques (Kadane's algorithm)
  - Use for: Maximum subarray, XOR queries, running calculations
  - Example: LC 53 (Maximum Subarray), LC 1310 (XOR Queries)

Master these 6 patterns and you'll handle 80-90% of prefix sum problems on LeetCode!

KEY TAKEAWAYS:
--------------
1. Prefix sum trades space for time: O(n) space for O(1) queries
2. Range sum formula: prefix[right+1] - prefix[left]
3. 2D uses inclusion-exclusion: sum = BR - TR - BL + TL
4. HashMap trick: if prefix[j] - prefix[i] = k, found subarray
5. Difference array: mark boundaries, then compute prefix sum
6. Initialize hashmap with {0: 1} or {0: -1} for empty subarray case
7. XOR prefix: prefix[j] ^ prefix[i] gives range XOR
8. Kadane's algorithm is running sum with reset condition
9. Product except self: left_product * right_product
10. Always handle edge cases: empty array, single element, negative numbers
"""