"""
Binary Search Essentials Guide
Based on problems: 33, 35, 69, 153, 167, 374, 441, 704, 1539
"""

from typing import List

# =============================================================================
# WHAT IS BINARY SEARCH?
# =============================================================================
"""
Binary search finds a target in sorted data by repeatedly halving the search space.
- O(log n) time complexity
- Requires sorted or monotonic property
- Uses two pointers and eliminates half each iteration
"""

# =============================================================================
# CORE TEMPLATE
# =============================================================================

# ITERATIVE
def binary_search_iterative(nums, target):
    """Standard template - memorize this"""
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Prevents overflow in some coding languages
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7  # Should return index 3
print(binary_search_iterative(nums, target))

# RECURSIVE
def binary_search_recursive(array, target, left, right):
    # Base case: If the range is invalid, the target is not in the list
    if left > right:
        return -1

    # Find the middle index
    mid = (left + right) // 2
    mid_value = array[mid]

    # Check if the target is at the middle
    if mid_value == target:
        return mid

    # If the target is smaller than the middle value, search the left half
    if target < mid_value: # pass in mid - 1 for right
        return binary_search_recursive(array, target, left, mid - 1)

    # If target > middle value, search right half (pass in mid + 1 for left)
    return binary_search_recursive(array, target, mid + 1, right)

# nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], target = 7
print(binary_search_recursive(nums, target, 0, len(nums) - 1))

# =============================================================================
# KEY PATTERNS
# =============================================================================

# ================================================================
# PATTERN 1: FINDING INSERTION POSITIONS
# PATTERN EXPLANATION: Use binary search to find where a target value should be inserted in a sorted array to keep the array in order.
# KEY INSIGHT: When binary search finishes without finding the target, the left pointer shows exactly where the target should be inserted. This works whether the target exists in the array or not.
# Applications: Finding insertion points, locating where values belong in sorted data, finding boundaries in sorted arrays, first/last occurrence problems.
# ================================================================

def search_insert(nums, target):  # LC 35
    """
    Problem: Given a sorted array, find the index where target should be inserted to maintain sorted order. If target exists, return its current index.
    
    Examples: [1,3,5,6], target = 5 → 2 (exists at index 2)
              [1,3,5,6], target = 2 → 1 (insert between 1 and 3)  
              [1,3,5,6], target = 7 → 4 (insert at end)

    # Key Insight - binary search ensures that the start ptr always ends up at the smallest index where the target could be inserted

    # TC: O(log n): Binary search eliminates half the search space in each iteration. Each comparison reduces the problem size by half
    # SC: O(1): no extra data structures needed
    """
    start, end = 0, len(nums) - 1
    while start <= end:
        middle = start + (end - start) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target: # num we are on is less than the target (need bigger num)
            start = middle + 1 # search the right half
        else: # num we are on is greater than the target (need smaller num)
            end = middle - 1 # search the left half
    return start  # Key insight: start points to insertion position

print(search_insert([1,3,5,6], 5)) # 2
print(search_insert([1,3,5,6], 2)) # 1
print(search_insert([1,3,5,6], 7)) # 4

# ================================================================
# PATTERN 2: BINARY SEARCH IN ROTATED ARRAYS
# PATTERN EXPLANATION: Search in arrays that have been rotated by finding which half is still properly sorted, then deciding which half to search next.
# KEY INSIGHT: In rotated sorted arrays, one half is always still in proper order. Find the sorted half, check if your target could be there, then search the correct half to eliminate impossible options.
# Applications: Rotated arrays, finding elements in shifted data, searching arrays where sorting has been disrupted but partial order remains.
# ================================================================

def search_rotated(nums, target): # LC 33
    """
    Problem: Search for target in a sorted array that has been rotated at some pivot. Array was originally [0,1,2,4,5,6,7] but rotated to become [4,5,6,7,0,1,2].
    
    Key insight: After rotation, one half is always properly sorted (side that includes the middle element [4,5,6,7]). Identify which half is sorted, then decide to search left or right since we can compare the target to the ends of each sorted half. The sorted half allows you to quickly eliminate half of the search space, guarenteeing you can find the target in O(log n).

    # TC: O(log n): Binary search eliminates half the search space in each iteration. Each comparison reduces the problem size by half
    # SC: O(1): no extra data structures needed
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Found target
        if nums[mid] == target:
            return mid
            
        # Left half is sorted
        if nums[left] <= nums[mid]:
            # Is target in the sorted left half?
            if nums[left] <= target <= nums[mid]:
                right = mid - 1  # search left half
            else:
                left = mid + 1   # search right half
                
        # Right half is sorted
        else:
            # Is target in the sorted right half?
            if nums[mid] <= target <= nums[right]:
                left = mid + 1   # search right half
            else:
                right = mid - 1  # search left half
                
    return -1

# Test cases
print(search_rotated([4,5,6,7,0,1,2], 0))  # 4
print(search_rotated([4,5,6,7,0,1,2], 3))  # -1
print(search_rotated([1], 0))              # -1

# ================================================================
# PATTERN 3: BINARY SEARCH ON MATHEMATICAL RANGES
# PATTERN EXPLANATION: Use binary search to find answers within a range of numbers by testing calculated values instead of searching through a given array.
# KEY INSIGHT: When you can calculate and test values in a number range, binary search can find the correct answer by treating the range like a sorted array where math calculations replace looking up array elements.
# Applications: Finding square roots, calculating powers, solving equations, any problem where you test numbers in a range to find the right answer.
# ================================================================

def min_eating_speed(piles, h):  # LC 875
    """
    Problem: Koko loves bananas and wants to eat all piles before guards return.
    She can choose her eating speed K (bananas per hour) and eats from one pile 
    at a time. If a pile has fewer bananas than K, she still takes the full hour.
    Find the minimum speed K such that she can eat all bananas within h hours.

    Key insight: Instead of searching in a given array, search the range of 
    possible answers and use a helper function to test if each candidate works.
    Find the minimum value that satisfies the constraint.

    Pattern:
    1. Define answer range [min_possible, max_possible]
    2. Write helper function to test if candidate answer works
    3. Binary search: if works, try smaller; if doesn't work, try larger

    TC: O(n * log(max_pile)) -> Binary search iterations: O(log(max_pile)) where max_pile is the largest pile, helper function per iteration: O(n) to check all piles
    SC: O(1) -> uses no additional data structures
    """
    import math

    def can_finish(speed):
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile / speed)
        return total_hours <= h

    left, right = 1, max(piles)  # Starting answer space: 
    result = right

    while left <= right:
        mid = left + (right - left) // 2
        if can_finish(mid):  # This speed works
            result = mid     # Save this answer
            right = mid - 1  # Try to find smaller speed
        else:                # This speed too slow
            left = mid + 1   # Need faster speed
            
    return result

# Test cases
print(min_eating_speed([3,6,7,11], 8))  # 4
print(min_eating_speed([30,11,23,4,20], 5))  # 30

# ================================================================
# PATTERN 4: BINARY SEARCH ON 2D MATRICES
# PATTERN EXPLANATION: Search sorted 2D matrices by treating them as flattened 1D arrays.
# KEY INSIGHT: Convert between 1D index positions and 2D row/column coordinates to apply standard binary search on matrix data that maintains sorted order.
# Applications: 2D matrix search, searching flattened representations of grids,
# any rectangular data that can be treated as a single sorted sequence.
# ================================================================

def search_matrix(matrix, target):  # LC 74
    """
    Problem: Search for target in m x n matrix where:
    - Each row is sorted in non-decreasing order
    - First integer of each row > last integer of previous row
    
    Examples: 
    Matrix = [[1, 3,  5,  7],
             [10, 11, 16, 20],
             [23, 30, 34, 60]]
    target = 3 → True (exists at matrix[0][1])
    target = 13 → False (doesn't exist)
    
    Key insight: Treat the 2D matrix as a flattened 1D sorted array.
    Convert between 1D index and 2D coordinates:
    - row = mid // cols
    - col = mid % cols

    TC: O(log(m * n)) where m = number of rows, n = number of columns, total elements: m * n, Binary search iterations: log₂(m * n)
    SC: O(1) -> uses no additional data structures
    """
    if not matrix or not matrix[0]: # Empty matrix or empty 1st row (breaks MxN matrix condition)
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Convert 1D index to 2D coordinates
        row = mid // cols # tells us how many complete rows we've passed through
        col = mid % cols # tells us how fr into current row we are
        value = matrix[row][col]
        
        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return False

# Test cases
print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))   # True
print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))  # False

# =============================================================================
# CRITICAL NUANCES
# =============================================================================
"""
ROTATED ARRAYS:
- One half is always sorted
- Check nums[left] <= nums[mid] to identify sorted half
- Be careful with duplicate elements

BOUNDARY CONDITIONS:
- Use left <= right (not left < right) for standard search
- Update with mid + 1 or mid - 1 (never just mid)
- Know what to return when target not found
- For first/last occurrence: continue searching when target found (LC 34)

MATHEMATICAL APPLICATIONS:
- Search answer space instead of array indices
- Common for problems involving formulas or calculations

2D MATRIX SEARCH:
- Verify matrix properties: rows sorted AND first element of each row > last of previous
- Handle empty matrix/row edge cases: check both matrix and matrix[0]
- 1D to 2D conversion: row = mid // cols, col = mid % cols
- Total elements = rows × cols, so right = rows * cols - 1
- This only works for "flattened sorted" matrices, not general 2D sorted matrices

COMMON MISTAKES:
- Integer overflow: use left + (right - left) // 2
- Infinite loops: ensure pointers always converge
- Off-by-one errors in boundary updates
- 2D conversion errors: mixing up row/col formulas or using wrong dimensions
"""

# =============================================================================
# TIME & SPACE COMPLEXITY
# =============================================================================
"""
TIME: O(log n) for searching in arrays of size n
- O(log(search_space)) for answer space problems - depends on value range, not array size
SPACE: O(1) iterative, O(log n) recursive (call stack)

When NOT to use binary search:
- Array is unsorted and can't be sorted
- Need all occurrences of target
- No monotonic property exists - data has no consistent increasing or decreasing trend that allows you to eliminate half of the search space
"""

# Other Problems to consider: 34, 1011, 875, 162, 852, 240
