"""
=====================================================================
ARRAY DATA STRUCTURE COMPLETE GUIDE
=====================================================================

WHAT ARE ARRAYS?
----------------
Arrays are contiguous memory structures that store elements of the 
same type, accessible by index in O(1) time.

Key characteristics:
- Direct access by index: arr[i] in O(1)
- Fixed size (in most languages, dynamic in Python)
- Cache-friendly due to contiguous memory
- Efficient iteration: O(n) to visit all elements

Array fundamentals:
- Indexing: 0-based (first element at index 0)
- Length: len(arr) or arr.length
- Mutable: can modify elements in-place
- Common operations: access O(1), search O(n), insert/delete O(n)

ARRAY CORE OPERATIONS
======================
"""

from typing import List

# ================================================================
# BASIC ARRAY OPERATIONS
# ================================================================

def array_operations_template():
    """
    Essential array operations and their time complexities
    """
    arr = [1, 2, 3, 4, 5]
    
    # ============ ACCESS ============
    # TC: O(1) - direct index access
    first = arr[0]  # 1
    last = arr[-1]  # 5 (negative indexing from end)
    middle = arr[len(arr) // 2]  # 3
    
    # ============ MODIFICATION ============
    # TC: O(1) - modify single element
    arr[0] = 10  # [10, 2, 3, 4, 5]
    
    # ============ APPEND ============
    # TC: O(1) amortized - add to end
    arr.append(6)  # [10, 2, 3, 4, 5, 6]
    
    # ============ INSERT ============
    # insert(index, value)
    # TC: O(n) - shifts all elements after insertion point
    arr.insert(0, 0)  # [0, 10, 2, 3, 4, 5, 6]
    arr.insert(2, 99)  # [0, 10, 99, 2, 3, 4, 5, 6]
    
    # ============ DELETE ============
    # TC: O(n) - shifts elements to fill gap
    arr.pop()  # removes last: [0, 10, 99, 2, 3, 4, 5]
    arr.pop(0)  # removes first: [10, 99, 2, 3, 4, 5]
    del arr[1]  # removes at index: [10, 2, 3, 4, 5]
    
    # ============ SEARCH ============
    # Linear Search - TC: O(n)
    def linear_search(arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i  # Return index if found
        return -1  # Return -1 if not found

    # "in" -> must iterate through whole array
    # TC: O(n) - must check each element
    if 3 in arr:  # True
        index = arr.index(3)  # 2
    
    # ============ SLICING ============
    # TC: O(k) where k is slice size - creates new array
    sub = arr[1:4]  # [2, 3, 4]
    copy = arr[:]  # [10, 2, 3, 4, 5]
    
    # ============ REVERSAL ============
    # TC: O(n) - must visit every element
    arr.reverse()  # in-place: [5, 4, 3, 2, 10]
    reversed_copy = arr[::-1]  # new array: [10, 2, 3, 4, 5]
    
    # ============ SORTING ============
    # TC: O(n log n) - comparison-based sorting
    arr.sort()  # in-place sort -> returns nothing
    sorted_copy = sorted(arr)  # returns new sorted array
    arr.sort(reverse=True)  # descending order
    
    # ============ COMMON PATTERNS ============
    # Initialize array with default values
    zeros = [0] * 5  # [0, 0, 0, 0, 0]
    matrix = [[0] * 3 for _ in range(2)] # 2x3 matrix of zeros
    
    # List comprehension
    squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
    evens = [x for x in arr if x % 2 == 0]  # filter evens
    
    # Enumerate (index + value)
    for i, val in enumerate(arr):
        print(f"Index {i}: {val}")
    
    # Min/Max
    minimum = min(arr)
    maximum = max(arr)
    
    # Sum
    total = sum(arr)
    
    return arr

# Example usage
print("Array operations:")
result = array_operations_template()
print(result)

"""
# ==================================================================
# PATTERN 1: BOYER-MOORE VOTING ALGORITHM
# PATTERN EXPLANATION: Find majority element (appears >n/2 times) using
# cancellation/voting concept. Maintain a candidate and counter. When 
# count reaches 0, switch candidate. The majority element will survive 
# because it outnumbers all others combined. Works in O(n) time with 
# O(1) space.
#
# RECOGNITION TRIGGERS:
# - Find element appearing more than n/2 times (or n/3, n/k)
# - "Majority element" in problem title
# - Guaranteed majority exists
# - Need O(1) space solution
#
#
# Applications: Majority element, majority element II (>n/3), finding
# elements with specific frequency thresholds.
# ===================================================================
"""

def majorityElement(nums: List[int]) -> int: # LC 169
    """
    Problem: Given array of size n, find the majority element. 
    The majority element is the element that appears more than 
    ⌊n/2⌋ times. You may assume the majority element always exists.
    
    Example 1:
    Input: nums = [3,2,3]
    Output: 3
    
    TC: O(n) - single pass through array
    SC: O(1) - only two variables
    
    How it works:
    1. Think of it as a voting system where majority "cancels out" 
    minorities
    2. Candidate represents current potential majority
    3. Count tracks how many "votes ahead" candidate is
    4. When count=0, no element has advantage, switch candidate
    5. Majority element survives because it outnumbers all others 
    combined
    """
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            # No current majority, adopt this element as candidate
            candidate = num
            count = 1
        elif num == candidate:
            # Supporting vote for current candidate
            count += 1
        else:
            # Opposing vote, cancels out one candidate vote
            count -= 1
    
    return candidate

print("Majority Element:", majorityElement([2,2,1,1,1,2,2]))  # 2
print("Majority Element:", majorityElement([3,2,3]))  # 3

"""
# ==================================================================
# PATTERN 2: MERGE INTERVALS
# PATTERN EXPLANATION: Sort intervals by start time, then merge 
# overlapping ones in single pass. Two intervals [a,b] and [c,d] 
# overlap if b ≥ c (first's end reaches or exceeds second's start). 
# Merged interval is [a, max(b,d)]. Sorting ensures we only need to 
# compare consecutive intervals.
#
# RECOGNITION TRIGGERS:
# - Problem involves intervals/ranges: [start, end]
# - "Merge overlapping intervals"
# - "Insert interval into sorted intervals"
# - "Find meeting rooms needed"
# - "Non-overlapping intervals"
#
# Applications: Merge intervals, insert interval, meeting rooms, 
# non-overlapping intervals, interval list intersections.
# ==================================================================
"""
def merge(intervals: List[List[int]]) -> List[List[int]]: # LC 56
    """
    Problem: Given array of intervals [start, end], merge all 
    overlapping intervals and return array of non-overlapping intervals.

    Example 1:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them 
    into [1,6].
    
    TC: O(n log n) - dominated by sorting
    SC: O(n) - output array (or O(log n) for sorting if we don't count 
    output)
    
    How it works:
    1. Sort intervals by start time
    2. Compare each interval with last merged interval
    3. If current.start ≤ last.end, they overlap → merge
    4. If no overlap, add current as new interval
    5. Merging: extend last interval's end to max(last.end, current.end)
    """
    intervals.sort(key=lambda x: x[0]) # sort by start
    result = []
    start, end = intervals[0] # get initial start & end by destructuring

    for curr_start, curr_end in intervals[1:]: # iterate & unpack from i=1 
        if curr_start <= end: # check for overlap with prev interval
            end = max(end, curr_end) # update end pointer
        else: # no overlap
            result.append([start, end]) # add merged interval to res
            start, end = curr_start, curr_end # move pointers
    
    result.append([start, end]) # Append to res after no more overlaps
    return result

print("Merge Intervals:", merge([[1,3],[2,6],[8,10],[15,18]]))  
# [[1,6],[8,10],[15,18]]
"""
# ==================================================================
# PATTERN 3: ARRAY ROTATION TECHNIQUES
# PATTERN EXPLANATION: Rotate array by k positions efficiently using 
# the reversal method. Key insight: rotating [1,2,3,4,5] right by 2 
# gives [4,5,1,2,3]. This is equivalent to: reverse all, reverse first 
# k, reverse rest. Works in O(n) time with O(1) space through in-place reversals.
#
# RECOGNITION TRIGGERS:
# - "Rotate array left/right by k positions"
# - "Shift elements circularly"
# - O(1) space requirement
# - In-place modification required
#
# Applications: Rotate array, rotate string, circular array problems,
# shift operations.
# ===================================================================
"""
def rotate(nums: List[int], k: int) -> None: # LC 189
    """
    Problem: Given an integer array, rotate the array to the right by 
    k steps where k is non-negative. Modify the array in-place with 
    O(1) extra space.

    Example 1:
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]

    TC: O(n) - three reversals, each O(n)
    SC: O(1) - only swap operations
    
    How it works (Reversal Method):
    1. Normalize k to handle k > len(nums)
    2. Reverse entire array: [1,2,3,4,5] → [5,4,3,2,1]
    3. Reverse first k elements: [5,4,3,2,1] → [4,5,3,2,1] (k=2)
    4. Reverse remaining elements: [4,5,3,2,1] → [4,5,1,2,3]
    
    """
    n = len(nums)
    k = k % n  # Handle k > n (rotating by n is same as no rotation)
    
    def reverse(left: int, right: int) -> None:
        """Helper function to reverse array segment in-place"""
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    # Step 1: Reverse entire array
    reverse(0, n - 1)
    
    # Step 2: Reverse first k elements
    reverse(0, k - 1)
    
    # Step 3: Reverse remaining elements
    reverse(k, n - 1)

print(rotate([1,2,3,4,5,6,7], 3)) # [5,6,7,1,2,3,4]
