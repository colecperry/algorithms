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
Eliminate half the search space each iteration:

Step 1: Check middle (index 4): 9 < 13
        Eliminate left half [1,3,5,7,9]
        Search right half [11,13,15,17,19]

Step 2: Check middle (index 6): 13 = 13 ✓

Comparisons needed: 2
Worst case: log₂(n) comparisons

════════════════════════════════════════════════════
COMPLEXITY COMPARISON
════════════════════════════════════════════════════

Array Size | Linear Search | Binary Search | Improvement
-----------|---------------|---------------|-------------
    10     |      10       |       4       |   2.5x faster
   100     |     100       |       7       |  14x faster
  1,000    |   1,000       |      10       | 100x faster
 10,000    |  10,000       |      14       | 714x faster
100,000    | 100,000       |      17       | 5,882x faster
1,000,000  |1,000,000      |      20       | 50,000x faster

Real-world impact:
- Searching 1 million elements:
  * Linear: 1,000,000 comparisons
  * Binary: 20 comparisons
  * Binary search is 50,000x faster!

Growth comparison:
- Linear: Double array size → Double comparisons
- Binary: Double array size → Add just 1 comparison
- At n=1,000,000: Linear needs 1M checks, Binary needs 20

Why such a difference?
- Linear: Checks every element → n operations
- Binary: Halves space each time → log₂(n) operations
- log₂(1,000,000) = 20 (halving: 1M → 500k → 250k → ... → 1)

How binary search works:
1. Start with left and right pointers at array boundaries
2. Calculate middle index
3. Compare middle element with target
4. If equal: found target
5. If middle < target: target must be in right half
6. If middle > target: target must be in left half
7. Repeat until found or search space exhausted

Visual example:
    Array: [1, 3, 5, 7, 9, 11, 13, 15], target = 7
    
    Step 1: [1, 3, 5, 7, 9, 11, 13, 15]
             L        M              R
             7 > 5, search right half
    
    Step 2:           [7, 9, 11, 13, 15]
                       L  M          R
             7 < 9, search left half
    
    Step 3:           [7]
                       LMR
             Found!

When to use Binary Search:
- Array is sorted or has monotonic property
- Need O(log n) search time
- Can eliminate half of search space based on comparison
- Searching answer space (min/max value that satisfies condition)
- Finding boundaries or insertion points

When NOT to use Binary Search:
- Array is unsorted and can't be sorted
- No way to eliminate half the search space
- Need all occurrences of element (might need multiple searches)
- Linear scan is simpler and sufficient

Common binary search problem types:
- Standard search in sorted array
- Find insertion position
- Search rotated or modified sorted arrays
- Binary search on answer space
- 2D matrix search
- Find peak/valley elements
- Find boundaries (first/last occurrence)

BINARY SEARCH CORE TEMPLATES
=============================
"""

from typing import List, Optional

# ================================================================
#              STANDARD BINARY SEARCH TEMPLATE
# ================================================================
def binary_search_template(nums, target):
    """
    Standard binary search for finding target in sorted array
    
    TC: O(log n) - halve search space each iteration
    SC: O(1) for iterative, O(log n) for recursive
    
    WHEN TO USE:
    - Search for exact value in sorted array
    - Find if element exists
    - Return index of target
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
    SC: O(log n) - recursion call stack
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

# ================================================================
#                   2D MATRIX TEMPLATE
# ================================================================
def matrix_search_template(matrix, target):
    """
    Problem: Search in m x n matrix where:
    - Integers in each row are sorted left to right
    - First integer of each row > last integer of previous row
    
    Example:
        matrix = [
            [1,  3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ]
        target = 3
        Output: True
    
    TC: O(log(m*n)) - treating as 1D sorted array of m*n elements
    SC: O(1)
    
    WHEN TO USE:
    - Matrix rows sorted left to right
    - Each row's first element > previous row's last element
    - Essentially a flattened sorted array
    
    KEY TRICK:
    # Treat 2D matrix as flattened 1D array, then binary search
    # Example: [[1,3,5,7], [10,11,16,20]] becomes [1,3,5,7,10,11,16,20]
    # Use math to convert between 1D index and 2D coordinates
    """
    # Edge case: empty matrix
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    
    # Binary search on "virtual" 1D array of length rows*cols
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Convert 1D index to 2D coordinates
        # Example: mid=5, cols=4 -> row=5//4=1, col=5%4=1 -> matrix[1][1]
        row = mid // cols  # Which row?
        col = mid % cols   # Which column in that row?
        value = matrix[row][col]
        
        # Standard binary search comparisons
        if value == target:
            return True
        elif value < target:
            left = mid + 1   # Target is in right half
        else:
            right = mid - 1  # Target is in left half
    
    return False  # Target not found


# Test cases
matrix = [
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
print(matrix_search_template(matrix, 3))   # True
print(matrix_search_template(matrix, 13))  # False
print(matrix_search_template(matrix, 60))  # True


"""
================================================================
PATTERN 1: STANDARD SEARCH IN SORTED ARRAY
PATTERN EXPLANATION: Find target value in sorted array by repeatedly comparing with middle element and eliminating half of search space. Classic divide and conquer approach where we divide array at midpoint and conquer by searching only the relevant half.

TYPICAL STEPS:
1. Initialize left=0, right=len(nums)-1
2. While left <= right:
    - Calculate mid = left + (right - left) // 2
    - If nums[mid] == target: found, return mid
    - If nums[mid] < target: search right half (left = mid + 1)
    - If nums[mid] > target: search left half (right = mid - 1)
3. Return -1 if not found

Applications: Search in sorted array, check if element exists, find exact match.
================================================================
"""

class StandardSearchPattern:
    """
    Problem: Given sorted array of integers nums and target value, return index of target.
    If target not found, return -1.
    
    How it works:
    1. Compare target with middle element
    2. If equal: found target
    3. If target larger: must be in right half (all left half elements smaller)
    4. If target smaller: must be in left half (all right half elements larger)
    5. Repeat until found or search space exhausted
    
    Why O(log n):
    - Each iteration eliminates half the elements
    - n → n/2 → n/4 → ... → 1
    - Number of halvings: log₂(n)
    """
    def search(self, nums: List[int], target: int) -> int: # LC 704
        """
        - TC: O(log n) - halve search space each iteration
        - SC: O(1) - only pointer variables
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
        
        return -1

# Example:
# nums = [-1,0,3,5,9,12], target = 9
#
# Step 1: left=0, right=5, mid=2
#   nums[2]=3 < 9
#   Eliminate left: [9,12]
#
# Step 2: left=3, right=5, mid=4
#   nums[4]=9 == 9 ✓
#   Found at index 4
#
# Comparisons: 2 (vs 5 for linear search)
# Output: 4

sol = StandardSearchPattern()
print("Binary search:", sol.search([-1,0,3,5,9,12], 9))  # 4
print("Binary search:", sol.search([-1,0,3,5,9,12], 2))  # -1

"""
================================================================
PATTERN 2: FIND INSERTION POSITION
PATTERN EXPLANATION: Find index where target should be inserted to maintain sorted order. When binary search completes without finding target, left pointer naturally points to correct insertion position. This works because left tracks the smallest index where nums[index] >= target.

TYPICAL STEPS:
1. Initialize left=0, right=len(nums)-1
2. Binary search as normal
3. If target found, return its index
4. If not found, return left (insertion position)

Applications: Insert into sorted array, find lower/upper bound, first/last occurrence.
================================================================
"""

class InsertionPositionPattern:
    """
    Problem: Given sorted array and target, return index where target would be inserted
    to maintain sorted order. If target exists, return its current index.
    
    How it works:
    1. Perform standard binary search
    2. If target found, return its index
    3. If not found, left pointer points to insertion position
    
    Why left is insertion position:
    - Left always points to smallest element >= target
    - When search ends, left > right
    - All elements at indices < left are < target
    - All elements at indices >= left are >= target
    - So target belongs at index left
    """
    def searchInsert(self, nums: List[int], target: int) -> int: # LC 35
        """
        - TC: O(log n)
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

# Example:
# nums = [1,3,5,6], target = 2
#
# Step 1: mid=2, nums[2]=5 > 2
#   Search left: [1,3]
#
# Step 2: mid=0, nums[0]=1 < 2
#   Search right: [3]
#   left=1, right=0 (left > right, done)
#
# left=1 points to where 2 should go: [1,2,3,5,6]
# Output: 1
#
# Example 2:
# nums = [1,3,5,6], target = 7
#
# Search eliminates all elements
# left=4 (after last element)
# Insert at end: [1,3,5,6,7]
# Output: 4

sol = InsertionPositionPattern()
print("Insert position:", sol.searchInsert([1,3,5,6], 5))  # 2
print("Insert position:", sol.searchInsert([1,3,5,6], 2))  # 1
print("Insert position:", sol.searchInsert([1,3,5,6], 7))  # 4

"""
================================================================
PATTERN 3: SEARCH IN ROTATED SORTED ARRAY
PATTERN EXPLANATION: Search in array that was sorted then rotated at unknown pivot.
Key insight: after rotation, one half is always still properly sorted. Identify which half is sorted by comparing endpoints with middle. Then check if target is in sorted half's range to decide which half to search.

TYPICAL STEPS:
1. Compare nums[left] with nums[mid] to identify sorted half
2. If left half sorted (nums[left] <= nums[mid]):
   - Check if target in range [nums[left], nums[mid]]
   - If yes: search left, if no: search right
3. If right half sorted (nums[mid] <= nums[right]):
   - Check if target in range [nums[mid], nums[right]]
   - If yes: search right, if no: search left
4. Repeat until found or exhausted

Applications: Search rotated sorted array, find minimum in rotated array.
================================================================
"""

class RotatedArrayPattern:
    """
    Problem: Search for target in sorted array rotated at unknown pivot. Original: [0,1,2,4,5,6,7] rotated to [4,5,6,7,0,1,2]
    
    How it works:
    1. One half is always properly sorted
    2. Check if left half sorted: nums[left] <= nums[mid]
    3. If sorted, check if target in that half's range
    4. Search the half that could contain target
    
    Why one half is always sorted:
    - Rotation creates one breakpoint
    - Breakpoint is in one half, other half unaffected
    - Sorted half has nums[left] <= nums[mid] or nums[mid] <= nums[right]
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
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                # Is target in sorted right half?
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
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
print("Rotated search:", sol.search([4,5,6,7,0,1,2], 0))  # 4
print("Rotated search:", sol.search([4,5,6,7,0,1,2], 3))  # -1

"""
================================================================
PATTERN 4: BINARY SEARCH ON ANSWER SPACE
PATTERN EXPLANATION: Instead of searching in given array, search a range of possible answers. Define minimum and maximum possible answers, then binary search to find optimal.
Use helper function to test if candidate answer satisfies constraints. Common in "minimize maximum" or "maximize minimum" problems.

TYPICAL STEPS:
1. Define answer range: [min_answer, max_answer]
2. Write is_valid(candidate) helper that checks if candidate works
3. Binary search on range:
   - If candidate valid: save it, try to optimize (smaller or larger)
   - If invalid: adjust search direction
4. Return best valid answer found

Applications: Capacity to ship packages, koko eating bananas, split array, minimize max.
================================================================
"""
import math

class AnswerSpacePattern:
    """
    Problem: Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
    
    Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
    
    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
    
    Return the minimum integer k such that she can eat all the bananas within h hours.

    Example 1:
    Input: piles = [3,6,7,11], h = 8
    Output: 4
    
    How it works:
    1. Answer range: [1, max(piles)]
        - Minimum speed: 1 banana/hour
        - Maximum speed: max(piles) (eat largest pile in 1 hour)
    2. For each candidate speed, calculate total hours needed
    3. Binary search to find minimum speed that works
    
    Why binary search on speed:
    - If speed K works, all speeds > K also work (monotonic)
    - Want minimum K, so when K works, try smaller
    - When K doesn't work, try larger
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int: # LC 875
        """
        - TC: O(n log(max_pile)) - n to check if speed works, log(max) for binary search
        - SC: O(1)
        """
        
        def can_finish(speed):
            """Check if Koko can finish all piles with this speed"""
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / speed)
            return total_hours <= h
        
        # Define answer space
        left, right = 1, max(piles)
        result = right
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if can_finish(mid):
                result = mid       # This speed works
                right = mid - 1    # Try slower (minimize)
            else:
                left = mid + 1     # Too slow, need faster
        
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
PATTERN 5: SEARCH IN 2D MATRIX (FLATTENED SEARCH)
PATTERN EXPLANATION: Treat 2D sorted matrix as flattened 1D array. Convert between 1D index and 2D coordinates to apply standard binary search. Works when matrix is sorted row by row and each row's first element is greater than previous row's last element.

TYPICAL STEPS:
1. Treat matrix as 1D array with rows*cols elements
2. Binary search on range [0, rows*cols - 1]
3. For each mid:
   - Convert to 2D: row = mid // cols, col = mid % cols
   - Access value: matrix[row][col]
   - Compare and update search bounds
4. Return true if found, false otherwise

Applications: 2D matrix search, grid search with sorted property.
================================================================
"""

class MatrixSearchPattern:
    """
    Problem: Search target in mxn matrix where:
    - Each row sorted in ascending order
    - First integer of each row > last integer of previous row
    
    How it works:
    1. Conceptually flatten matrix into 1D sorted array
    2. Apply binary search on flattened representation
    3. Convert 1D index back to 2D coordinates for access
    
    Key conversions:
    - Total elements: rows * cols
    - 1D index to 2D: row = index // cols, col = index % cols
    - Example: index 7 in 3x4 matrix → row=7//4=1, col=7%4=3 → matrix[1][3]
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: # LC 74
        """
        - TC: O(log(m*n)) - binary search on total elements
        - SC: O(1)
        """
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        
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
PATTERN 6: FIND PEAK ELEMENT (ELIMINATION LOGIC)
PATTERN EXPLANATION: Find peak in unsorted array using comparison with neighbor to eliminate half the search space. Even without global sorting, local comparisons reveal which direction guarantees a peak. If slope increases (mid < mid+1), peak must be to right. If slope decreases (mid > mid+1), peak is at mid or to left.

TYPICAL STEPS:
1. Initialize left=0, right=len(nums)-1
2. While left < right: (not <=, converging to answer)
   - Compare nums[mid] with nums[mid+1]
   - If nums[mid] < nums[mid+1]: peak on right (left = mid + 1)
   - Else: peak at mid or left (right = mid)
3. Return left (or right, they're equal)

Applications: Find peak, find local maximum, bitonic array search.
================================================================
"""

class PeakElementPattern:
    """
    Problem: Find peak element where nums[i] > nums[i-1] and nums[i] > nums[i+1] and return it's index.

    Neighbors of out-of-bound indices are -infinity.
    
    How it works:
    1. Compare mid with mid+1 to determine slope
    2. If increasing slope (mid < mid+1): peak guaranteed to right
       - Why: Either slope continues up and hits boundary (peak)
       - Or slope goes down (peak found)
    3. If decreasing slope (mid > mid+1): peak at mid or to left
       - Why: Either slope continues down from left and mid is peak
       - Or slope goes up to left (peak found)
    
    Why this works without sorting:
    - Not searching for specific value
    - Using local property (slope) to eliminate half
    - Guarantee: eliminated half cannot contain peak
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
                # Downward slope, peak at mid or to the left
                right = mid
        
        return left  # left == right at peak

# Example:
# nums = [1,2,3,1]
#
# Step 1: left=0, right=3, mid=1
#   nums[1]=2 < nums[2]=3 (upward slope)
#   Peak to right: [3,1]
#
# Step 2: left=2, right=3, mid=2
#   nums[2]=3 > nums[3]=1 (downward slope)
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