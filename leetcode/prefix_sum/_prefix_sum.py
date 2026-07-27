"""
=================================================================
PREFIX SUM GUIDE
=================================================================

WHAT IS PREFIX SUM?
-------------------
Prefix sum is a preprocessing technique that builds an array where each element stores the cumulative sum of all elements up to that index. It enables O(1) range sum queries after O(n) preprocessing — trading space for repeated query speed.

Key characteristics:
- Preprocessing: build prefix sum array in O(n) time
- Query: answer any range sum in O(1) time
- Space-time tradeoff: O(n) extra space for O(1) queries
- Formula: sum(left, right) = prefix[right+1] - prefix[left]
  (prefix[right+1] includes arr[right]; prefix[left] excludes arr[left] — subtracting them leaves exactly arr[left..right])

---------- 1D Array Example --------------

sum(arr[left..right]) = (total through right) - (total before left)
We subtract only the leftover chunk to the LEFT of our slice — everything at index `left` or later must stay, since that's what we want.

Example: arr = [3, 1, 4, 1, 5], want indices 1..3 -> 1+4+1 = 6
   prefix = [0, 3, 4, 8, 9, 14]   # prefix[i] = sum of arr[0..i-1]
   sum(1, 3) = prefix[4] - prefix[1] = 9 - 3 = 6

Without prefix sum: O(n) per range query → O(n * q) total for q queries
With prefix sum: O(n) build + O(1) per query → O(n + q) total

---------- 2D Array Example --------------

prefix[r][c] = sum of the whole rectangle from top-left to bottom-right (r-1, c-1).

Build each cell from 3 neighbors you've already filled:
    prefix[r][c] = matrix[r-1][c-1]   (this cell)
                 + prefix[r-1][c]     (rectangle above)
                 + prefix[r][c-1]     (rectangle to the left)
                 - prefix[r-1][c-1]   (overlap added twice, remove once)

Why subtract? "above" and "left" both include the top-left block,
so it's double-counted. Subtract it once to fix that.

matrix = [[1, 2, 3],
          [4, 5, 6]]

prefix = [[0, 0,  0,  0],
          [0, 1,  3,  6],
          [0, 5, 12, 21]]

Filling prefix[2][2] (rows 0-1, cols 0-1 -> should be 1+2+4+5 = 12):
    matrix[1][1] = 5     (this cell)
  + prefix[1][2] = 3     (the 1,2 above)
  + prefix[2][1] = 5     (the 1,4 to the left)
  - prefix[1][1] = 1     (the 1 counted in both)
  = 12  ✓

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
        self.prefix = [0] * (len(nums) + 1) # prefix array has an extra 0
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i] # curr prefix sum = prefix sum up to last num + curr num

    def sumRange(self, left: int, right: int) -> int:
        """
        Total TC: O(n) build + O(1) per query
        SC: O(1)
        """
        return self.prefix[right + 1] - self.prefix[left]

    # Trace: nums = [1, 2, 3, 4, 5]
    # prefix = [0, 1, 3, 6, 10, 15]
    # sumRange(1, 3): prefix[4] - prefix[1] = 10 - 1 = 9  ([2,3,4] = 9) ✓

rsq = RangeSumQuery([1, 2, 3, 4, 5]) # prefix = [0, 1, 3, 6, 10, 15]
print(rsq.sumRange(0, 2))  # sum of nums[0:3] = prefix[3] - prefix[0] = 6
print(rsq.sumRange(1, 4))  # sum of nums[1:5] = prefix[5] - prefix[1] = 14


"""
================================================================
PATTERN 2: PREFIX SUM + HASHMAP (SUBARRAY SUM PROBLEMS)

As you walk through the array left to right, keep a running total.
The running total at any point tells you the sum of everything from
the start up to there. If two points in the array have the SAME
running total, that means nothing changed in between — the chunk of
array between those two points must sum to zero.

That's the core trick: instead of re-adding every possible chunk to
check its sum (slow), you keep a record of every running total
you've seen so far. Then at each new step, you do a quick lookup
instead of a re-sum. This turns a slow check-every-pair approach
into a single pass.

Different problems tweak two things:
  - WHAT you store per running total (a count of how many times it's
    shown up, or the earliest index it occurred at)
  - WHAT you check for at each step (an exact repeat, the total
    minus your target, or the total's remainder when divided by k)

But the shape is always the same: scan once, keep a hashmap of
running totals, and use a lookup to instantly tell you something
about a subarray ending at the current position.

Result: O(n) instead of O(n²).

Applications: subarray sum = k, subarray sum divisible by k,
              equal 0s and 1s, longest subarray with sum k.
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
    2. For each num, check if (prefix_sum - k) is in freq map
       Each match is a valid subarray ending at the current index
    3. Seed map with {0: 1} to count subarrays starting from index 0
    """
    def subarraySum(self, nums: List[int], k: int) -> int: # LC 560
        """
        - TC: O(n) - single pass through array
        - SC: O(n) - store at most n prefix sums
        """
        res = 0  # Count of subarrays that sum to k
        curSum = 0  # Running prefix sum
        prefixSums = {0: 1} # Prefix Sum: Count
                            # Base case: handles subarrays starting from index 0
                            # (when curSum == k, diff will be 0)
        
        for num in nums:
            curSum += num  # Update running sum
            
            # Check if (curSum - k) exists in map
            # If yes: there's a previous prefix where removing it gives us sum k
            # Ex: curSum=5, k=3 → diff=2 → if sum=2 seen before -> add to res
            diff = curSum - k
            
            # Add count of how many times diff appeared (found that many subarrays), add 0 if that key is not present
            res += prefixSums.get(diff, 0)
            
            # ASSIGN current prefix sum frequency, add one if already there, if not, add zero
            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1
        
        return res

# Example trace:
# nums = [1,1,1], k = 2
#
# prefixSums = {0: 1}
#
# i=0, num=1:
#   curSum = 1
#   diff = 1 - 2 = -1
#   -1 not in prefixSums, res = 0
#   prefixSums = {0: 1, 1: 1}
#
# i=1, num=1:
#   curSum = 2
#   diff = 2 - 2 = 0
#   0 in prefixSums! (appears 1 time), res = 0 + 1 = 1
#   (Found subarray [1,1] from index 0-1)
#   prefixSums = {0: 1, 1: 1, 2: 1}
#
# i=2, num=1:
#   curSum = 3
#   diff = 3 - 2 = 1
#   1 in prefixSums! (appears 1 time), res = 1 + 1 = 2
#   (Found subarray [1,1] from index 1-2)
#   prefixSums = {0: 1, 1: 1, 2: 1, 3: 1}
#
# Return res = 2

sol = SubarraySumHashMap()
print(sol.subarraySum([1,1,1], 2))  # 2
print(sol.subarraySum([1,2,3], 3))  # 2

"""
================================================================
PATTERN 3: 2D PREFIX SUM (MATRIX RANGE QUERIES)

Same idea as 1D prefix sum, just extended to a grid. Instead of a
running total along a line, you build a running total across a
whole rectangle from the top-left corner.

To get the sum of any rectangle in the middle of the grid, do four
lookups in the prefix matrix and combine them like this:
  1. Start with the big rectangle running from the top-left corner down to
     your rectangle's bottom-right corner (current prefix sum cell)
  2. Subtract the prefix sum value directly above your current cell  
     (everything down to just above its top edge) 
  3. Subtract the prefix sum directly to the left of your current cell (everything
     across to just left of its left edge).
  4. Add back the small corner region up in the top-left (prefix[r-1][c-1])
     - it got subtracted twice in steps 2 and 3, so this puts it back once.

An extra empty row and column added around the edges just avoids
special-casing rectangles that touch the border.

Applications: Rectangle sum queries, submatrix sum problems,
image area calculations.
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
        # number of 0's in first array is the number of columns
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                self.prefix[r][c] = ( # prefix sum up to this point equals
                    matrix[r-1][c-1] # this cells value
                    + self.prefix[r-1][c] # + everything above
                    + self.prefix[r][c-1] # + everything to the left
                    - self.prefix[r-1][c-1] # - corner (counted twice above)
                )

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        """
        TC: O(1) per query (O(m*n) build in __init__)
        SC: O(1)
        NOTE: This fn uses the same inclusion exclusion trick as building the prefix sum 2d matrix
        """
        return (
            self.prefix[r2+1][c2+1]   # A: big rectangle from origin down to the region's bottom-right
            - self.prefix[r1][c2+1]   # B: subtract the strip ABOVE the region
            - self.prefix[r2+1][c1]   # C: subtract the strip LEFT of the region
            + self.prefix[r1][c1]     # D: add back the top-left corner (removed twice)
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

The mirror image of prefix sum: instead of asking "what's the sum
over this range," you're asking "add this value to every element in
this range," and you need to do that many times fast.

Applying an update to every element in [l, r] directly costs O(n)
per update. But if you only care about the FINAL array after all
updates are applied, you don't need to touch every element each
time — you just need to record where a change starts and where it
stops.

That's the diff array: diff[l] += val marks "starting here, add val,"
and diff[r+1] -= val marks "starting here, undo that val." Every
update becomes two O(1) writes at the boundaries. Once all updates
are recorded, take one prefix sum pass over diff — the running total
at each index naturally re-applies every val that started before it
and cancels every one that already ended, reconstructing the fully
updated array in a single O(n) sweep.

Result: k updates in O(n + k) instead of O(k*n).

Applications: Range addition, car pooling, corporate flight bookings,
              employee free time.
================================================================
"""

class DifferenceArray:
    """
    Problem: Array of length n initialized with all 0's and k update operations [startIndex, endIndex, inc].
    Each operation increments every element of A[startIndex..endIndex] (inclusive) by inc.
    Return the modified array after all k operations were executed.

    Example:
        length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
        Output: [-2,0,3,5,3]

    NOTE: diff[endIndex+1] -= inc needs a sentinel slot, so the diff array is length n+1 (endIndex can be n-1).
    """
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:  # LC 370 - Range Addition
        """
        - TC: O(n + k) - k updates (O(1) each) + one O(n) pass to reconstruct
        - SC: O(n) - diff array
        """
        diff = [0] * (length + 1)  # Extra slot so endIndex+1 never goes out of bounds

        for startIndex, endIndex, inc in updates:
            diff[startIndex] += inc      # Start applying inc from here on
            diff[endIndex + 1] -= inc    # Stop applying inc right after endIndex

        result = [] # result array
        curSum = 0  # Running total = value re-applied by every update that's "active" at this index

        for i in range(length):
            curSum += diff[i]
            result.append(curSum)

        return result

# Example trace:
# length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
#
# diff starts as [0,0,0,0,0,0] (length 6)
#
# NOTE:
# diff[start] += val — marks "starting from index start, add val from here onward"
# diff[end+1] -= val — marks "cancel that val addition from here onward"
#
# update [1,3,2]:  diff[1] += 2 -> diff[4] -= 2
#   diff = [0, 2, 0, 0, -2, 0]
#
# update [2,4,3]:  diff[2] += 3 -> diff[5] -= 3
#   diff = [0, 2, 3, 0, -2, -3]
#
# update [0,2,-2]: diff[0] += -2 -> diff[3] -= -2 (i.e. += 2)
#   diff = [-2, 2, 3, 2, -2, -3]
#
# Running sum over indices 0..4:
#   i=0: curSum = -2         -> result = [-2]
#   i=1: curSum = -2+2 = 0   -> result = [-2, 0]
#   i=2: curSum = 0+3 = 3    -> result = [-2, 0, 3]
#   i=3: curSum = 3+2 = 5    -> result = [-2, 0, 3, 5]
#   i=4: curSum = 5-2 = 3    -> result = [-2, 0, 3, 5, 3]
#
# Return result = [-2, 0, 3, 5, 3]

sol = DifferenceArray()
print(sol.getModifiedArray(5, [[1,3,2],[2,4,3],[0,2,-2]]))  # [-2, 0, 3, 5, 3]
print(sol.getModifiedArray(3, [[0,1,1],[1,2,-1]]))          # [1, 0, -1]
