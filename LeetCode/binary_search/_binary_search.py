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

# -----------------------------------------------------------------------------
# Pattern 1: Find Insertion Position in Sorted Array
# -----------------------------------------------------------------------------

def search_insert(nums, target):  # LC 35
    """
    Problem: Given a sorted array, find the index where target should be inserted to maintain sorted order. If target exists, return its current index.
    
    Examples: [1,3,5,6], target = 5 → 2 (exists at index 2)
              [1,3,5,6], target = 2 → 1 (insert between 1 and 3)  
              [1,3,5,6], target = 7 → 4 (insert at end)

    # Key Insight - binary search ensures that the start ptr always ends up at the smallest index where the target could be inserted
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

# -----------------------------------------------------------------------------
# Pattern 2 - Search in rotated sorted array
# -----------------------------------------------------------------------------

def search_rotated(nums, target):
    """
    Problem: Search for target in a sorted array that has been rotated at some pivot. Array was originally [0,1,2,4,5,6,7] but rotated to become [4,5,6,7,0,1,2].
    
    Key insight: After rotation, one half is always properly sorted (side that includes the middle element [4,5,6,7]). Identify which half is sorted, then decide to search left or right since we can compare the target to the ends of each sorted half. The sorted half allows you to quickly eliminate half of the search space, guarenteeing you can find the target in O(log n).
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

# -----------------------------------------------------------------------------
# Pattern 3: Find Minimum Element in Rotated Sorted Array
# -----------------------------------------------------------------------------

def find_min_rotated(nums):  # LC 153
    """
    Problem: Find minimum element in rotated sorted array
    Example: [3,4,5,1,2] → return 1

    Key insight: The minimum element is always in the "unsorted" portion since it includes the rotation point. If left portion is sorted, minimum must be in right portion.
    
    Key Pattern:
    1. If current portion is sorted (nums[left] < nums[right]), minimum is at left
    2. Otherwise, check which half contains the minimum:
       - If nums[mid] > nums[right], minimum is in right half
       - If nums[mid] < nums[right], minimum is in left half

    Binary Search Guarentee: When we maintain the invariant that the minimum element is always within our [left, right] range and continuously shrink this range by eliminating portions that don't contain the minimum, binary search mathematically guarantees that left and right will converge exactly on the minimum element.
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        # If this portion is sorted, minimum is at left
        if nums[left] < nums[right]:
            return nums[left]
            
        mid = left + (right - left) // 2
        
        # If middle element > rightmost element, right side is unsorted
        # minimum must be in right half (after rotation point)
        if nums[mid] > nums[right]:
            left = mid + 1
        
        else: # If middle element < rightmost element,
            right = mid # minimum must be in left half (including mid)
            
    return nums[left]  # left and right converge on minimum

# Test cases
print(find_min_rotated([3,4,5,1,2]))     # 1
print(find_min_rotated([4,5,6,7,0,1,2])) # 0
print(find_min_rotated([11,13,15,17]))   # 11
print(find_min_rotated([4,5,1,2,3]))     # 1

# -----------------------------------------------------------------------------------------------
# Pattern 4: Mathematical Binary Search - Finding a single correct answer that satisfies a
# formula
# -----------------------------------------------------------------------------------------------

def my_sqrt(x):  # LC 69
    """
    Problem: Find the integer square root of x (largest integer whose square ≤ x).
    Examples: x=8 → 2 (since 2²=4 ≤ 8 < 3²=9)
              x=4 → 2 (since 2²=4 exactly)
    
    Key insight: Instead of searching a given array, we create our own search space in the range [0, x//2]. This applies binary search to mathematical problems on any sorted range where you can test if candidates are too big, too small, or just right.
    """
    if x <= 1: # Handles edge case where x = 0 or x = 1 (bin search ranges would be incorrect)
        return x 
    
    l, r = 0, x // 2 # Define search space -> any number greater than x//2 would have square > x

    while l <= r:
        mid = l + (r - l) // 2 # Calc midpoint
        square = mid * mid # Find square of mid
        if square == x:
            return mid
        elif square > x: # Our guess mid is too large (square exceeds target)
            r = mid - 1 # need a smaller number, search left half
        else: # Our guess mid is too small
            l = mid + 1 # need a bigger num, search right half
    return r  # r points to the last valid position

print(my_sqrt(4)) # Expected output: 2
print(my_sqrt(8)) # Expected output: 2

# -----------------------------------------------------------------------------
# Pattern 5: Binary Search on Answer Space - Optimizing a min/max value among many possible 
# valid answers
# -----------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------
# Pattern 6: 2D Matrix Binary Search
# -----------------------------------------------------------------------------

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
