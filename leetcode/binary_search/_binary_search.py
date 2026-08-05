"""
----------------------
WHAT IS BINARY SEARCH?
----------------------
Binary search is an efficient algorithm for finding a target value in a sorted array or
search space by repeatedly dividing the search interval in half. Instead of checking every
element linearly, it eliminates half of the remaining elements with each comparison.

Key characteristics:
- Requires sorted array or monotonic property
- Divides search space in half each iteration
- Compares target with middle element to decide direction
- O(log n) time complexity
- Works on sorted arrays, answer spaces, or any monotonic function

# =============================================================================
# BINARY SEARCH ADVANTAGE: O(n) LINEAR SEARCH vs O(log n) BINARY SEARCH
# =============================================================================
════════════════════════════════════════════════════
PROBLEM: Find target value 13 in sorted array
════════════════════════════════════════════════════

Array: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

────────────────────────────────────────────────────
LINEAR SEARCH (Brute Force) - O(n)
────────────────────────────────────────────────────
Check every element from left to right until found:

Step 1: Check index 0: 1 ≠ 13 ❌
Step 2: Check index 1: 3 ≠ 13 ❌
Step 3: Check index 2: 5 ≠ 13 ❌
Step 4: Check index 3: 7 ≠ 13 ❌
Step 5: Check index 4: 9 ≠ 13 ❌
Step 6: Check index 5: 11 ≠ 13 ❌
Step 7: Check index 6: 13 = 13 ✓

Comparisons needed: 7
Worst case: n comparisons (if target at end or not present)

────────────────────────────────────────────────────
BINARY SEARCH - O(log n)
────────────────────────────────────────────────────
Eliminate half the search space each iteration.

Why log₂(n)? The base matches the divisor.
- Divide the search space by 2 each step → log base 2
- Divide the seatch space by 3 each step → log base 3

Example: n = 1,000,000
1M → 500K → 250K → 125K → ... → 1
Only 20 halvings to reach 1 element. That's log₂(1M) ≈ 20.

────────────────────────────────────────────────────
COMPLEXITY COMPARISON
────────────────────────────────────────────────────
Array Size | Linear | Binary | Improvement
-----------|--------|--------|------------
    1,000  |  1,000 |     10 |    100x
  100,000  |100,000 |     17 |  5,882x
1,000,000  |  1M    |     20 | 50,000x

Key insight:
- Linear: Double array → double comparisons
- Binary: Double array → add 1 comparison

────────────────────────────────────────────────────
WHEN TO USE
────────────────────────────────────────────────────
✓ Array is sorted (or has monotonic property)
✓ Can eliminate half based on comparison
✓ Searching for min/max value that satisfies condition

✗ Array unsorted and can't be sorted
✗ No way to eliminate half the search space

BINARY SEARCH CORE TEMPLATES
=============================
"""

from typing import List, Optional

"""
BINARY SEARCH COMPLEXITY REFERENCE
===================================

+-------------------------------+-------------------+-------+
| Pattern                       | Time              | Space |
+-------------------------------+-------------------+-------+
| Find Insertion Position       | O(log n)          | O(1)  |
| Search Rotated Sorted Array   | O(log n)          | O(1)  |
| Binary Search on Answer Space | O(n log(max_val)) | O(1)  |
| Search in 2D Matrix           | O(log(m * n))     | O(1)  |
| Find Peak Element             | O(log n)          | O(1)  |
+-------------------------------+-------------------+-------+

n = array length, m/n = matrix row/column dimensions,
max_val = size of the answer search space (e.g. largest pile)

WHAT EACH PATTERN IS:
- Find Insertion Position: run a normal binary search; when the target isn't found,
  the search naturally stops at the exact spot where it would need to be inserted to
  keep the array sorted.
- Search Rotated Sorted Array: search a sorted array that got rotated at some unknown
  point, by figuring out which half of the current range is still in proper order and
  checking whether the target could be hiding in it.
- Binary Search on Answer Space: instead of searching for a value inside an array,
  search over the range of possible answers themselves, using a check function to test
  whether a candidate answer would work, then narrow toward the best one.
- Search in 2D Matrix: treat a row-sorted grid as if it were one long sorted line,
  converting back and forth between a single index and its row/column position.
- Find Peak Element: find a value that's bigger than both of its neighbors by always
  stepping toward the side that's still going uphill, without needing the whole array
  to be sorted.

NOTES:
- Find Insertion Position: standard binary search halves the range each step -> O(log n);
  no extra structures used -> O(1)
- Search Rotated Sorted Array: exactly one half of the array is always properly
  ordered, so comparing against it still eliminates half the range each iteration -> O(log n)
- Binary Search on Answer Space: the outer binary search over the answer range costs
  O(log(max_val)), and each candidate is validated with an O(n) feasibility check -> O(n log(max_val)) total
- Search in 2D Matrix: index arithmetic (row = mid // cols, col = mid % cols) lets one
  binary search run over all m*n cells -> O(log(m * n))
- Find Peak Element: comparing a node to just one neighbor still discards half the
  remaining search space each step, even without global sorting -> O(log n)
"""

# ================================================================
#              STANDARD BINARY SEARCH TEMPLATE
# ================================================================
def binary_search_template(nums, target):
    """
    Standard binary search for finding target in sorted array
    - TC: O(log n) - halve the search space each iteration
    - SC: O(1) for iterative, O(log n) for recursive
    """
    left, right = 0, len(nums) - 1 # Left and Right pointers start on the edges
    
    while left <= right:
        mid = left + (right - left) // 2 # Calc middle
        
        if nums[mid] == target: # Check if we found target
            return mid
        elif nums[mid] < target: # Ele at midpoint less than target
            left = mid + 1  # Search right half
        else: # Ele at midpoint greater than target
            right = mid - 1  # Search left half
    
    return -1  # Not found

# ================================================================
#            RECURSIVE BINARY SEARCH TEMPLATE
# ================================================================
def binary_search_recursive(nums, target, left, right):
    """
    Recursive binary search
    
    TC: O(log n)
    SC: O(log n) - each recursive call halves the search space -> stack depth
    """
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if nums[mid] == target:
        return mid
    elif nums[mid] < target: # Ele at midpoint less than target
        return binary_search_recursive(nums, target, mid + 1, right) # Search right recursively (l = mid + 1)
    else: # Ele at midpoint greater than target
        return binary_search_recursive(nums, target, left, mid - 1) # Search left recursively (r = mid - 1)

"""
================================================================
PATTERN 1: FIND INSERTION POSITION

PATTERN EXPLANATION: Find index where target should be inserted to maintain sorted order. When binary search completes without finding target, left pointer naturally points to correct insertion position. This works because left tracks the smallest index where nums[index] >= target.

Why left is insertion position:
- Think of left as: "first position I haven't ruled out yet"
- [1, 3, 5, 7], target = 4
- Is 3 valid? No, too small. Rule it out: left = 2
- Is 5 valid? Yes, could insert before it. Keep left = 2

- Answer: 2

- left only moves forward when we find something too small.
- It never moves backward. So it stops at the first valid spot.

Applications: Insert into sorted array, find lower/upper bound, first/last occurrence.
================================================================
"""

class InsertionPositionPattern:
    """
    Giveaway: "return the index where target would be inserted" to keep an already
    sorted array sorted is the signal for binary search — you don't need to find
    the target, just the boundary it belongs at, which is exactly where a normal
    binary search's left pointer lands when the loop ends without a match.

    Problem: Given sorted array and target, return index where target would be inserted
    to maintain sorted order. If target exists, return its current index.

    Example 1:
        Input: nums = [1,3,5,6], target = 5
        Output: 2

    Steps:
    1. Initialize left=0, right=len(nums)-1
    2. Binary search as normal
    3. If target found, return its index
    4. If not found, return left (insertion position)
    """
    def searchInsert(self, nums: List[int], target: int) -> int: # LC 35
        """
        - TC: O(log n) - we half the search space each iteration
        - SC: O(1)
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left  # Insertion position

sol = InsertionPositionPattern()
print("Insert position:", sol.searchInsert([1,3,5,6], 2))  # 1
print("Insert position:", sol.searchInsert([1,3,5,6], 7))  # 4

"""
================================================================
PATTERN 2: SEARCH IN ROTATED SORTED ARRAY

PATTERN EXPLANATION: Search in array that was sorted then rotated at unknown pivot.

Key insight: after rotation, one half is always still properly sorted. Identify which half is sorted by comparing endpoints with middle. Then check if target is in sorted half's range to decide which half to search.

The rotation creates ONE break point. Mid splits the array into two halves.
The break point can only be in one half — the other half is guarenteed to be sorted.

    [4, 5, 6, 7, 0, 1, 2]
              ↑
           break point (7 → 0), mid = 7
    
    Left half:  [4, 5, 6, 7]  ← no break, sorted ✓
    Right half: [7, 0, 1, 2]  ← break is here, not sorted ✗

Applications: Search rotated sorted array, find minimum in rotated array.
================================================================
"""

class RotatedArrayPattern:
    """
    Giveaway: "sorted array rotated at an unknown pivot" is the tell — the array
    isn't fully sorted anymore, but splitting at mid still guarantees one side is
    properly ordered, so you can still eliminate half the search space each step by
    checking which half is sorted and whether the target falls in its range.

    Problem: Search for target in sorted array rotated at unknown pivot. Original: [0,1,2,4,5,6,7] rotated to [4,5,6,7,0,1,2]

    Example 1:
    - Input: nums = [4,5,6,7,0,1,2], target = 0
    - Output: 4

    Steps:
    1. Compare nums[left] with nums[mid] to identify sorted half
    2. If left half sorted (nums[left] <= nums[mid]):
       a. Check if target in range [nums[left], nums[mid]]
       b. If yes: search left, if no: search right
    3. If right half sorted (nums[mid] <= nums[right]):
       a. Check if target in range [nums[mid], nums[right]]
       b. If yes: search right, if no: search left
    4. Repeat until found or exhausted
    """
    def search(self, nums: List[int], target: int) -> int: # LC 33
        """
        TC: O(log n) - still halve search space each time
        SC: O(1)
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                # Is target in sorted left half?
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else: # target in right hallf
                    left = mid + 1
            
            else: # Right half is sorted
                # Is target in sorted right half?
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else: # target in left half
                    right = mid - 1
        
        return -1

# Example:
# nums = [4,5,6,7,0,1,2], target = 0
#
# Step 1: mid=3 (value 7)
#   Left half [4,5,6,7] is sorted (4 <= 7)
#   Is 0 in [4,7]? No
#   Search right: [0,1,2]
#
# Step 2: mid=5 (value 1)
#   Right half [1,2] is sorted (1 <= 2)
#   Is 0 in [1,2]? No
#   Search left: [0]
#
# Step 3: mid=4 (value 0)
#   Found!
#
# Output: 4

sol = RotatedArrayPattern()
print("Rotated search:", sol.search([4,5,6,7,0,1,2], 0))  # left half sorted -> 4
print("Rotated search:", sol.search([4,5,6,0,1,2,3], 5))  # right half sorted -> 1

"""
================================================================
PATTERN 3: BINARY SEARCH ON ANSWER SPACE

PATTERN EXPLANATION: Instead of searching in a given array, search a range of 
possible answers. Define min and max possible answers, then binary search to 
find the smallest or largest value that satisfies a condition. Use helper function to test if candidate answer satisfies constraints. Common in "minimize maximum" or "maximize minimum" problems.

Applications: Capacity to ship packages, koko eating bananas, split array, minimize max.
================================================================
"""
import math

class AnswerSpacePattern:
    """
    Giveaway: asking for the MINIMUM (or maximum) value of some parameter — here
    Koko's eating speed k — that still satisfies a checkable condition ("finish
    within h hours") is the signal to binary search over the range of POSSIBLE
    ANSWERS themselves, testing each candidate speed with a feasibility function,
    rather than searching for a value inside an array.

    Problem: Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
    
    Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
    
    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
    
    Return the minimum integer k such that she can eat all the bananas within h hours.

    Example 1:
    Input: piles = [3,6,7,11], h = 8
    Output: 4
    
    Steps:
    1. Define answer range: [1, max(piles)]
       a. Minimum speed: 1 banana/hour
       b. Maximum speed: max(piles) (eat largest pile in 1 hour)
    2. Write can_finish(speed) helper that calculates total hours needed and checks if <= h
    3. Binary search on speed range:
       a. If can_finish(mid): save mid as result, try smaller (right = mid - 1)
       b. If not can_finish(mid): speed too slow, search larger (left = mid + 1)
    4. Return best valid speed found
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int: # LC 875
        """
        - TC: O(n log(max_pile)) - n to check if speed works, log(max_pile) for binary search space
        - SC: O(1)
        """
        
        def can_finish(speed):
            """Check if Koko can finish all piles with this speed"""
            total_hours = 0
            for pile in piles: # eat each pile
                total_hours += math.ceil(pile / speed) # hours to eat curr pile at curr speed
            return total_hours <= h
        
        # Define answer space
        left, right = 1, max(piles)
        result = right
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if can_finish(mid):
                result = mid       # This speed (mid) works
                right = mid - 1    # Try slower (minimize)
            else:
                left = mid + 1     # Speed too slow, need faster
        
        return result

# Example:
# piles = [3,6,7,11], h = 8
#
# Answer space: [1, 11]
#
# Test mid=6:
#   Hours: ceil(3/6) + ceil(6/6) + ceil(7/6) + ceil(11/6)
#        = 1 + 1 + 2 + 2 = 6 <= 8 ✓
#   Works! Try smaller: search [1,5]
#
# Test mid=3:
#   Hours: ceil(3/3) + ceil(6/3) + ceil(7/3) + ceil(11/3)
#        = 1 + 2 + 3 + 4 = 10 > 8 ✗
#   Too slow! Search [4,5]
#
# Test mid=4:
#   Hours: 1 + 2 + 2 + 3 = 8 <= 8 ✓
#   Works! Try smaller: search [4,3] (empty)
#
# Minimum speed: 4
# Output: 4

sol = AnswerSpacePattern()
print("Min eating speed:", sol.minEatingSpeed([3,6,7,11], 8))  # 4
print("Min eating speed:", sol.minEatingSpeed([30,11,23,4,20], 5))  # 30

"""
================================================================
PATTERN 4: SEARCH IN 2D MATRIX (FLATTENED SEARCH)
PATTERN EXPLANATION: Treat 2D sorted matrix as flattened 1D array. Convert between 1D index and 2D coordinates to apply standard binary search. Works when matrix is sorted row by row and each row's first element is greater than previous row's last element.

Applications: 2D matrix search, grid search with sorted property.
================================================================
"""

class MatrixSearchPattern:
    """
    Giveaway: a matrix described as row-sorted where "the first integer of each row
    is greater than the last integer of the previous row" is really one long sorted
    list in disguise — that specific guarantee is what lets a single binary search
    run over the whole grid via index-to-row/col conversion, instead of doing a
    separate search per row.

    Problem: Search target in m*n matrix where:
    - Each row sorted in ascending order
    - First integer of each row > last integer of previous row
    
    Steps:
    1. Treat matrix as 1D array with rows*cols elements
    2. Binary search on range [0, rows*cols - 1]
    3. For each mid:
       a. Convert to 2D: row = mid // cols, col = mid % cols
       b. Access value: matrix[row][col]
       c. Compare and update search bounds
    4. Return true if found, false otherwise

    Key conversions:
    - Total elements: rows * cols
    - 1D index to 2D: row = index // cols, col = index % cols
    - Example: index 7 in 3x4 matrix → row=7//4=1, col=7%4=3 → matrix[1][3]
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: # LC 74
        """
        - TC: O(log(m*n)) - binary search halves the total elements
        - SC: O(1)
        """
        if not matrix or not matrix[0]: # edge case -> empty matrix or first row
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1 # matrix search space = m*n
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Convert 1D index to 2D coordinates
            row = mid // cols
            col = mid % cols
            value = matrix[row][col]
            
            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

# Example:
# matrix = [[1, 3, 5, 7],
#           [10,11,16,20],
#           [23,30,34,60]]
# target = 3
#
# Flattened: [1,3,5,7,10,11,16,20,23,30,34,60]
# rows=3, cols=4, total=12 elements
#
# Step 1: mid=5 (1D)
#   row=5//4=1, col=5%4=1 → matrix[1][1]=11
#   11 > 3, search left
#
# Step 2: mid=2 (1D)
#   row=2//4=0, col=2%4=2 → matrix[0][2]=5
#   5 > 3, search left
#
# Step 3: mid=0 (1D)
#   row=0//4=0, col=0%4=0 → matrix[0][0]=1
#   1 < 3, search right
#
# Step 4: mid=1 (1D)
#   row=1//4=0, col=1%4=1 → matrix[0][1]=3
#   Found!
#
# Output: True

sol = MatrixSearchPattern()
print("Matrix search:", sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))  # True
print("Matrix search:", sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))  # False

"""
================================================================
PATTERN 5: FIND PEAK ELEMENT (ELIMINATION LOGIC)
PATTERN EXPLANATION: Find peak in unsorted array using comparison with neighbor to eliminate half the search space. Even without global sorting, local comparisons reveal which direction guarantees a peak. If slope increases (mid < mid+1), peak must be to right. If slope decreases (mid > mid+1), peak is at mid or to left.

    Why this works:
    - A peak exists somewhere (boundaries are -∞)
    - Follow the upward slope — it must eventually turn down or hit a boundary
    - We always move toward higher ground and keep potential peaks in the search space

Applications: Find peak, find local maximum, bitonic array search.
================================================================
"""

class PeakElementPattern:
    """
    Giveaway: "find a peak element" (greater than both neighbors) in an array that
    is NOT stated to be sorted is the tell for this binary search variant —
    comparing mid to just its next neighbor still reveals which direction is
    "uphill," letting you discard half the array each step with no global ordering.

    Problem: Find peak element where nums[i] > nums[i-1] and nums[i] > nums[i+1] and return it's index.

    Neighbors of out-of-bound indices are -infinity.

    Example 1:
    - Input: nums = [1,2,3,1]
    - Output: 2
    - Explanation: 3 is a peak element and your function should return the index number 2.

    Steps:
    1. Compare nums[mid] with nums[mid+1] to determine slope direction
    2. If nums[mid] < nums[mid+1] (going up): peak must be to the right, set left = mid + 1
    3. If nums[mid] > nums[mid+1] (going down): peak is at mid or to the left, set right = mid
    4. When left == right, return left as the peak index
    """
    def findPeakElement(self, nums: List[int]) -> int: # LC 162
        """
        - TC: O(log n) - eliminate half each iteration
        - SC: O(1)
        """
        left, right = 0, len(nums) - 1
        
        while left < right:  # Note: < not <=
            mid = left + (right - left) // 2
            
            if nums[mid] < nums[mid + 1]:
                # Upward slope, peak must be to the right
                left = mid + 1
            else:
                # Downward slope, peak could be at mid or to the left
                right = mid
        
        return left  # left == right at peak

# Example:
# nums = [1,2,3,1]
#
# Step 1: left=0, right=3, mid=1
#   2 < 3 (upward slope)
#   Peak to right: [3,1]
#   left = 2
#
# Step 2: left=2, right=3, mid=2
#   3 > 1 (downward slope)
#   Peak at mid or left: [3]
#   right=2
#
# left==right==2, found peak at index 2
# Output: 2
#
# Example 2:
# nums = [1,2,1,3,5,6,4]
#
# Multiple peaks possible: indices 1 (value 2) or 5 (value 6)
# Binary search finds one of them
# Output: 1 or 5 (either valid)

sol = PeakElementPattern()
print("Peak element:", sol.findPeakElement([1,2,3,1]))  # 2
print("Peak element:", sol.findPeakElement([1,2,1,3,5,6,4]))  # 1 or 5