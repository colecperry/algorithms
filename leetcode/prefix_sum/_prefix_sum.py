"""
=================================================================
PREFIX SUM GUIDE
=================================================================

WHAT IS PREFIX SUM?
-------------------
Prefix sum is a preprocessing technique that builds an array where each element stores the cumulative sum of all elements up to that index. It enables O(1) range sum queries after O(n) preprocessing — trading space for repeated query speed.


HOLA HOLA HOLA


Key characteristics:
- Preprocessing: build prefix sum array in O(n) time
- Query: answer any range sum in O(1) time
- Space-time tradeoff: O(n) extra space for O(1) queries
- Formula: sum(left, right) = prefix[right+1] - prefix[left]

Basic concept:
    Original: [3,  1,  4,  1,  5 ]
    Prefix:   [0,  3,  4,  8,  9,  14]
               ↑   ↑   ↑   ↑   ↑   ↑
               0  [3] [3+1] ...  sum of all elements

Without prefix sum: O(n) per range query → O(n * q) total for q queries
With prefix sum:    O(n) build + O(1) per query → O(n + q) total

When to use Prefix Sum:
- Multiple range sum queries on a static array
- Finding subarrays with a specific sum property
- Rectangle sum queries on a 2D grid
- Batching multiple range update operations

Common Prefix Sum problem types:
- Range sum queries (1D and 2D)
- Subarray sum equals k
- Subarray sum divisible by k
- Contiguous array with equal 0s and 1s
- Range addition / batch updates

PREFIX SUM CORE PATTERNS
=========================
"""

from typing import List

"""
PREFIX SUM COMPLEXITY REFERENCE
================================

+---------------------------+------------------+------------------+
| Pattern                   | Time             | Space            |
+---------------------------+------------------+------------------+
| 1D Prefix Sum (build)     | O(n)             | O(n)             |
| 1D Prefix Sum (query)     | O(1)             | O(1)             |
| Prefix Sum + HashMap      | O(n)             | O(n)             |
| 2D Prefix Sum (build)     | O(m * n)         | O(m * n)         |
| 2D Prefix Sum (query)     | O(1)             | O(1)             |
| Difference Array          | O(n + k)         | O(n)             |
+---------------------------+------------------+------------------+

n = array length, m/n = matrix dimensions, k = number of updates

NOTES:
- 1D and 2D queries are O(1) only after the O(n) or O(m*n) build — preprocessing pays off with multiple queries
- HashMap: stores up to n distinct prefix sums; seed {0: 1} is required to handle subarrays starting at index 0
- Difference array: each of k updates costs O(1) instead of O(n); reconstruction is one final O(n) pass
"""

"""
====================
PREFIX SUM PATTERNS
====================
"""

"""
================================================================
PATTERN 1: 1D PREFIX SUM (RANGE SUM QUERIES)
PATTERN EXPLANATION: Precompute cumulative sums to answer range sum queries in O(1). Build a prefix array where prefix[i] = sum of nums[0..i-1], with prefix[0] = 0 as a sentinel. Any range sum from left to right equals prefix[right+1] - prefix[left]. The +1 offset means every valid index pair maps cleanly with no boundary edge cases.

Applications: Range sum queries, immutable array sum, any repeated range calculation on a static array.
================================================================
"""

class RangeSumQuery:
    """
    Problem: Given an int array, handle multiple sumRange(left, right) queries.

    Example:
        nums = [1, 2, 3, 4, 5]
        sumRange(0, 2) → 6    # [1,2,3]
        sumRange(1, 4) → 14   # [2,3,4,5]

    Steps:
    1. Build prefix where prefix[i] = sum(nums[0..i-1]), prefix[0] = 0
    2. sumRange(left, right) = prefix[right+1] - prefix[left]
         prefix[right+1] covers nums[0..right]
         prefix[left]    covers nums[0..left-1]
         Difference      = nums[left..right]
    """
    def __init__(self, nums: List[int]):  # LC 303 - Range Sum Query Immutable
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        """
        TC: O(1) per query (O(n) build in __init__)
        SC: O(1)
        """
        return self.prefix[right + 1] - self.prefix[left]

    # Trace: nums = [1, 2, 3, 4, 5]
    # prefix = [0, 1, 3, 6, 10, 15]
    # sumRange(1, 3): prefix[4] - prefix[1] = 10 - 1 = 9  ([2,3,4] = 9) ✓

rsq = RangeSumQuery([1, 2, 3, 4, 5])
print(rsq.sumRange(0, 2))  # 6
print(rsq.sumRange(1, 4))  # 14


"""
================================================================
PATTERN 2: PREFIX SUM + HASHMAP (SUBARRAY SUM PROBLEMS)
PATTERN EXPLANATION: Combine prefix sum with a hashmap to find subarrays with a specific sum property in O(n). Key insight: if prefix[j] - prefix[i] = k, then nums[i+1..j] sums to k. For each j, check if (prefix[j] - k) already exists in the map. Seed the map with {0: 1} to handle subarrays starting at index 0. This converts an O(n²) brute force into a single O(n) pass.

Applications: Subarray sum equals k, subarray sum divisible by k,
contiguous array with equal 0s and 1s, longest subarray with sum k.
================================================================
"""

class SubarraySumHashMap:
    """
    Problem: Count subarrays whose sum equals k.

    Example:
        nums = [1, 2, 3], k = 3
        [1, 2] sums to 3, [3] sums to 3 → return 2

    Steps:
    1. Maintain a running prefix_sum and a freq map of {prefix_sum: count}
    2. For each num, check if (prefix_sum - k) is in freq
       Each match is a valid subarray ending at the current index
    3. Seed map with {0: 1} to count subarrays starting from index 0
    """
    def subarraySum(self, nums: List[int], k: int) -> int:  # LC 560 - Subarray Sum Equals K
        """
        TC: O(n) - single pass
        SC: O(n) - hashmap stores up to n distinct prefix sums
        """
        count = 0
        prefix_sum = 0
        freq = {0: 1}

        for num in nums:
            prefix_sum += num
            count += freq.get(prefix_sum - k, 0)
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count

    # Trace: nums = [1, 2, 3], k = 3
    # freq = {0:1}, prefix_sum = 0, count = 0
    #
    # num=1: prefix_sum=1, check (1-3=-2)? No.   freq={0:1, 1:1}
    # num=2: prefix_sum=3, check (3-3=0)?  YES +1 ([1,2])  freq={0:1,1:1,3:1}
    # num=3: prefix_sum=6, check (6-3=3)?  YES +1 ([3])    freq={...,6:1}
    # Output: 2 ✓

sol = SubarraySumHashMap()
print(sol.subarraySum([1, 2, 3], 3))  # 2
print(sol.subarraySum([1, 1, 1], 2))  # 2


"""
================================================================
PATTERN 3: 2D PREFIX SUM (MATRIX RANGE QUERIES)
PATTERN EXPLANATION: Extend prefix sum to 2D for rectangle sum queries. Build a prefix matrix where prefix[r][c] = sum of all cells in the rectangle from (0,0) to (r-1,c-1). Use inclusion-exclusion to query any rectangle: add the bottom-right corner, subtract the top strip and left strip, then add back the top-left corner (subtracted twice). The extra zero-filled border row and column eliminate boundary edge cases.

Applications: Rectangle sum queries, submatrix sum problems, image area calculations.
================================================================
"""

class RangeSumQuery2D:
    """
    Problem: Given a 2D matrix, handle multiple sumRegion(r1, c1, r2, c2) queries.

    Example:
        matrix = [[3,0,1,4,2],
                  [5,6,3,2,1],
                  [1,2,0,1,5],
                  [4,1,0,1,7],
                  [1,0,3,0,5]]
        sumRegion(2, 1, 4, 3) → 8

    Steps:
    1. Build 2D prefix where prefix[r][c] = sum of rectangle (0,0) to (r-1,c-1)
         prefix[r][c] = matrix[r-1][c-1] + prefix[r-1][c] + prefix[r][c-1] - prefix[r-1][c-1]
    2. Query (r1,c1) to (r2,c2) using inclusion-exclusion:
         = bottom-right - top-strip - left-strip + top-left-corner (subtracted twice)
    """
    def __init__(self, matrix: List[List[int]]):  # LC 304 - Range Sum Query 2D Immutable
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                self.prefix[r][c] = (
                    matrix[r-1][c-1]
                    + self.prefix[r-1][c]
                    + self.prefix[r][c-1]
                    - self.prefix[r-1][c-1]
                )

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        """
        TC: O(1) per query (O(m*n) build in __init__)
        SC: O(1)
        """
        return (
            self.prefix[r2+1][c2+1]
            - self.prefix[r1][c2+1]
            - self.prefix[r2+1][c1]
            + self.prefix[r1][c1]
        )

    # Trace: matrix = [[1,2],[3,4]]
    # prefix = [[0, 0, 0],
    #           [0, 1, 3],
    #           [0, 4, 10]]
    #
    # sumRegion(0,0,1,1): prefix[2][2] - prefix[0][2] - prefix[2][0] + prefix[0][0]
    #                   = 10 - 0 - 0 + 0 = 10  (1+2+3+4) ✓
    # sumRegion(0,1,1,1): prefix[2][2] - prefix[0][2] - prefix[2][1] + prefix[0][1]
    #                   = 10 - 0 - 4 + 0 = 6   (2+4) ✓

nm = RangeSumQuery2D([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
print(nm.sumRegion(2, 1, 4, 3))  # 8
print(nm.sumRegion(1, 1, 2, 2))  # 11


"""
================================================================
PATTERN 4: DIFFERENCE ARRAY (RANGE UPDATE QUERIES)
PATTERN EXPLANATION: Batch multiple range updates efficiently using a difference array. For each update (l, r, val), mark only the boundaries: diff[l] += val, diff[r+1] -= val. After all updates, take the prefix sum of diff to reconstruct the final array. This turns k range updates from O(k*n) to O(n+k) — each update is O(1), reconstruction is one O(n) pass.

Applications: Range addition, car pooling, corporate flight bookings, employee free time.
================================================================
"""

class DifferenceArray:
    """
    Problem: Each trip = [passengers, from, to]. Return True if car never exceeds capacity.

    Example:
        trips = [[2,1,5],[3,3,7]], capacity = 4
        At location 3: 2+3=5 passengers → exceeds capacity → False

    Steps:
    1. Build diff array: diff[from] += passengers, diff[to] -= passengers
       (passengers board at 'from', exit at 'to' — 'to' is not included in the ride)
    2. Prefix sum of diff gives current passengers at each location
    3. If current passengers ever exceed capacity, return False
    """
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:  # LC 1094 - Car Pooling
        """
        TC: O(n + max_location) - n trips + one pass over all locations
        SC: O(max_location) - difference array
        """
        max_loc = max(trip[2] for trip in trips)
        diff = [0] * (max_loc + 2)

        for passengers, start, end in trips:
            diff[start] += passengers
            diff[end] -= passengers

        current = 0
        for delta in diff:
            current += delta
            if current > capacity:
                return False

        return True

    # Trace: trips = [[2,1,5],[3,3,7]], capacity = 4
    # diff = [0, 2, 0, 3, 0, -2, 0, -3]
    #
    # Running prefix sum:
    # loc 0: 0
    # loc 1: 2   (2 board)
    # loc 2: 2
    # loc 3: 5   (3 more board) → 5 > 4, exceeds capacity → False ✓

sol = DifferenceArray()
print(sol.carPooling([[2,1,5],[3,3,7]], 4))  # False
print(sol.carPooling([[2,1,5],[3,3,7]], 5))  # True
