"""
=================================================================
DIVIDE AND CONQUER COMPLETE GUIDE
=================================================================

WHAT IS DIVIDE AND CONQUER?
---------------------------
Divide and Conquer is an algorithm design paradigm that solves problems by breaking them
into smaller independent subproblems, solving each subproblem recursively, then combining
the solutions. Unlike dynamic programming, subproblems are independent (don't overlap).

Key characteristics:
- Divide: Break problem into smaller independent subproblems
- Conquer: Solve subproblems recursively (base case handles smallest)
- Combine: Merge subproblem solutions to get final answer
- Typically uses recursion
- Often results in O(n log n) time complexity

Three steps:
1. DIVIDE: Split problem into smaller subproblems
2. CONQUER: Recursively solve each subproblem
3. COMBINE: Merge solutions from subproblems

Visual example (Merge Sort):
    Array: [38, 27, 43, 3]
    
    DIVIDE:
    [38, 27, 43, 3]
         ↓
    [38, 27]  [43, 3]
         ↓         ↓
    [38] [27]  [43] [3]
    
    CONQUER (base case): Single elements already sorted
    
    COMBINE:
    [27, 38]  [3, 43]  ← Merge pairs
         ↓
    [3, 27, 38, 43]    ← Merge halves

Divide & Conquer vs Dynamic Programming:
- D&C: Independent subproblems, no overlap, typically O(n log n)
- DP: Overlapping subproblems, memoization needed, typically O(n²)

Divide & Conquer vs Greedy:
- D&C: Explores multiple branches, combines results
- Greedy: Makes one choice, never reconsiders

When to use Divide & Conquer:
- Problem can be broken into independent subproblems
- Subproblems are similar to original problem (just smaller)
- Solutions can be combined efficiently
- Natural recursive structure
- Often see "sorted", "search", "maximum", "closest"

When NOT to use Divide & Conquer:
- Subproblems overlap significantly (use DP)
- Can't efficiently combine solutions
- Greedy approach works
- Iterative solution is simpler

Common divide & conquer problem types:
- Sorting algorithms (merge sort, quick sort)
- Searching (binary search)
- Array problems (maximum subarray)
- Tree problems (traversal, diameter)
- Closest pair problems
- Master theorem problems

DIVIDE AND CONQUER CORE TEMPLATES
==================================
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ================================================================
# BINARY SEARCH TEMPLATE (CLASSIC D&C)
# ================================================================
def binary_search_template(arr, target):
    """
    Template for binary search (classic divide & conquer)
    
    TC: O(log n) - halve search space each iteration
    SC: O(1) for iterative, O(log n) for recursive
    
    WHEN TO USE:
    - Search in sorted array
    - Find insertion position
    - Find boundary (first/last occurrence)
    
    DIVIDE & CONQUER:
    - Divide: Split array at middle
    - Conquer: Search one half based on comparison
    - Combine: Return result (no merging needed)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    return -1  # Not found

# ================================================================
# MERGE SORT TEMPLATE
# ================================================================
def merge_sort_template(arr):
    """
    Template for merge sort
    
    TC: O(n log n) - log n levels, O(n) work per level
    SC: O(n) - temporary arrays for merging
    
    WHEN TO USE:
    - Need to sort array
    - Need stable sort
    - Guaranteed O(n log n) performance
    
    DIVIDE & CONQUER:
    - Divide: Split array in half
    - Conquer: Recursively sort both halves
    - Combine: Merge two sorted halves
    """
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort_template(arr[:mid])
    right = merge_sort_template(arr[mid:])
    
    # Combine (merge two sorted halves)
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ================================================================
# TREE DIVIDE & CONQUER TEMPLATE
# ================================================================
def tree_dc_template(root):
    """
    Template for tree divide & conquer
    
    TC: O(n) - visit each node once
    SC: O(h) - recursion stack depth
    
    WHEN TO USE:
    - Tree problems needing info from both subtrees
    - Maximum/minimum path problems
    - Tree diameter, height, paths
    
    DIVIDE & CONQUER:
    - Divide: Split at root into left and right subtrees
    - Conquer: Recursively solve for each subtree
    - Combine: Use results from both subtrees
    """
    if not root:
        return base_value
    
    # Divide & Conquer
    left_result = tree_dc_template(root.left)
    right_result = tree_dc_template(root.right)
    
    # Combine
    return combine(left_result, right_result, root.val)

# ================================================================
# ARRAY DIVIDE & CONQUER TEMPLATE
# ================================================================
def array_dc_template(arr, left, right):
    """
    Template for array divide & conquer
    
    TC: O(n log n) typically
    SC: O(log n) for recursion stack
    
    WHEN TO USE:
    - Maximum subarray
    - Closest pair
    - Inversion count
    - Problems requiring splitting array
    
    DIVIDE & CONQUER:
    - Divide: Split array at midpoint
    - Conquer: Solve for left half and right half
    - Combine: Consider cross-boundary solution
    """
    if left >= right:
        return base_case
    
    mid = (left + right) // 2
    
    # Divide & Conquer
    left_result = array_dc_template(arr, left, mid)
    right_result = array_dc_template(arr, mid + 1, right)
    cross_result = compute_cross(arr, left, mid, right)
    
    # Combine (max of three possibilities)
    return max(left_result, right_result, cross_result)

"""
COMPLEXITY QUICK REFERENCE
==========================

Divide & Conquer Time Complexity:
- Binary Search: O(log n) - eliminate half each time
- Merge Sort: O(n log n) - log n levels, O(n) merge per level
- Quick Sort: O(n log n) average, O(n²) worst
- Maximum Subarray: O(n log n) - D&C approach
- Closest Pair: O(n log n)
- Tree problems: O(n) - visit each node once

Master Theorem (for recurrence relations):
T(n) = aT(n/b) + f(n)
- a = number of subproblems
- n/b = size of each subproblem
- f(n) = cost of divide and combine

Common cases:
- T(n) = 2T(n/2) + O(1): Binary search → O(log n)
- T(n) = 2T(n/2) + O(n): Merge sort → O(n log n)
- T(n) = T(n/2) + O(1): Binary search → O(log n)

Space Complexity:
- Recursion stack: O(log n) for balanced divide
- Merge operations: O(n) for temporary arrays
- In-place: O(log n) for recursion only

Why O(n log n):
- Divide into halves: log n levels
- Work at each level: O(n)
- Total: O(n) work × log n levels = O(n log n)

Pattern Complexities:
1. Binary Search: O(log n) time, O(1) space
2. Merge Sort: O(n log n) time, O(n) space
3. Maximum Subarray: O(n log n) time, O(log n) space
4. Tree D&C: O(n) time, O(h) space
5. Closest Pair: O(n log n) time, O(n) space

When to Use Each Pattern:
1. Binary Search: Sorted array, search/find problems
2. Merge/Sort: Need to sort, combine sorted subarrays
3. Maximum Subarray: Optimization across split point
4. Tree D&C: Combine info from left and right subtrees
5. Closest Pair: Geometric problems, finding optimal pairs
"""

"""
DIVIDE AND CONQUER PATTERNS
============================
"""

# ================================================================
# PATTERN 1: BINARY SEARCH (SEARCH IN SORTED SPACE)
# PATTERN EXPLANATION: Eliminate half of search space at each step by comparing with middle
# element. Works on sorted arrays or monotonic functions. Key insight: mid element determines
# which half contains target. Repeatedly halve search space until target found or space exhausted.
#
# TYPICAL STEPS:
# 1. Initialize left=0, right=len(arr)-1
# 2. While left <= right:
#    - Calculate mid = (left + right) // 2
#    - If arr[mid] == target: found, return mid
#    - If arr[mid] < target: search right half (left = mid + 1)
#    - If arr[mid] > target: search left half (right = mid - 1)
# 3. If not found, return -1 or insertion position
#
# Applications: Search sorted array, find insertion position, search rotated array, find peak.
# ================================================================

class BinarySearchPattern:
    """
    Problem: Given sorted array of distinct integers and target value, return index of
    target if found. If not found, return -1.
    
    TC: O(log n) - halve search space each iteration
    SC: O(1) for iterative, O(log n) for recursive (call stack)
    
    How it works (Divide & Conquer):
    1. DIVIDE: Compare target with middle element, choose which half to search
    2. CONQUER: Recursively search chosen half
    3. COMBINE: Return result (no merging needed - just return index)
    
    Why O(log n):
    - Each iteration eliminates half the remaining elements
    - Search space: n → n/2 → n/4 → ... → 1
    - Number of halving operations: log₂(n)
    """
    def search(self, nums: List[int], target: int) -> int: # LC 704
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1  # Target in right half
            else:
                right = mid - 1  # Target in left half
        
        return -1  # Not found
    
    # Recursive version
    def search_recursive(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left > right:
                return -1
            
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, right)
            else:
                return binary_search(left, mid - 1)
        
        return binary_search(0, len(nums) - 1)

# Example:
# nums = [-1,0,3,5,9,12], target = 9
#
# Step 1: left=0, right=5, mid=2
#   nums[2]=3 < 9, search right half
#
# Step 2: left=3, right=5, mid=4
#   nums[4]=9 == 9, found!
#
# Output: 4
#
# Search space reduction:
# [_1,0,3,5,9,12] → 6 elements
# [5,9,12]        → 3 elements
# [9]             → 1 element (found!)

sol = BinarySearchPattern()
print("Binary search:", sol.search([-1,0,3,5,9,12], 9))  # 4
print("Binary search:", sol.search([-1,0,3,5,9,12], 2))  # -1


# ================================================================
# PATTERN 2: MERGE SORT (SORT BY MERGING)
# PATTERN EXPLANATION: Recursively divide array in half until single elements (base case),
# then merge sorted halves back together. Each merge combines two sorted subarrays into one
# sorted array. Guaranteed O(n log n) performance regardless of input. Stable sort.
#
# TYPICAL STEPS:
# 1. Base case: if array length <= 1, already sorted
# 2. DIVIDE: Split array at midpoint into left and right halves
# 3. CONQUER: Recursively sort both halves
# 4. COMBINE: Merge two sorted halves using two pointers
#    - Compare front elements, take smaller
#    - Continue until both halves merged
# 5. Return merged sorted array
#
# Applications: Sort array, count inversions, merge intervals, sort linked list.
# ================================================================

class MergeSortPattern:
    """
    Problem: Given array nums, sort it in ascending order using merge sort.
    
    TC: O(n log n) - log n levels of recursion, O(n) merge at each level
    SC: O(n) - temporary arrays for merging
    
    How it works (Divide & Conquer):
    1. DIVIDE: Split array into two halves at midpoint
    2. CONQUER: Recursively sort left half and right half
    3. COMBINE: Merge two sorted halves into one sorted array
    
    Why O(n log n):
    - Tree has log n levels (halving each time)
    - Each level does O(n) total work (merging)
    - Total: O(n) × log n = O(n log n)
    
    Merge operation:
    - Two pointers for sorted halves
    - Compare and take smaller element
    - Copy remaining elements
    """
    def sortArray(self, nums: List[int]) -> List[int]: # LC 912
        # Base case: single element or empty
        if len(nums) <= 1:
            return nums
        
        # DIVIDE: Split at midpoint
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]
        
        # CONQUER: Recursively sort both halves
        left_sorted = self.sortArray(left_half)
        right_sorted = self.sortArray(right_half)
        
        # COMBINE: Merge sorted halves
        return self.merge(left_sorted, right_sorted)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        """Merge two sorted arrays"""
        result = []
        i = j = 0
        
        # Compare and merge
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # Copy remaining elements
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result

# Example:
# nums = [5,2,3,1]
#
# Level 0: [5,2,3,1]
#           ↓ DIVIDE
# Level 1: [5,2]    [3,1]
#           ↓ DIVIDE  ↓ DIVIDE
# Level 2: [5] [2]  [3] [1]
#           ↓ MERGE   ↓ MERGE
# Level 1: [2,5]    [1,3]
#           ↓ MERGE
# Level 0: [1,2,3,5]
#
# Work at each level:
# Level 2: 4 single elements (base case)
# Level 1: Merge [5,2]→[2,5] and [3,1]→[1,3] (4 comparisons)
# Level 0: Merge [2,5] and [1,3]→[1,2,3,5] (4 comparisons)
#
# Output: [1,2,3,5]

sol = MergeSortPattern()
print("Merge sort:", sol.sortArray([5,2,3,1]))  # [1,2,3,5]
print("Merge sort:", sol.sortArray([5,1,1,2,0,0]))  # [0,0,1,1,2,5]


# ================================================================
# PATTERN 3: MAXIMUM SUBARRAY (KADANE'S ALTERNATIVE)
# PATTERN EXPLANATION: Find maximum sum subarray by considering three cases: max subarray
# entirely in left half, entirely in right half, or crossing the midpoint. Recursively find
# max in left and right halves, compute max crossing sum, return maximum of three. Less
# efficient than Kadane's O(n) but demonstrates divide & conquer.
#
# TYPICAL STEPS:
# 1. Base case: single element array
# 2. DIVIDE: Split array at midpoint
# 3. CONQUER: Find max subarray in left half and right half recursively
# 4. COMBINE: Compute max crossing subarray (spans midpoint)
#    - Find max sum extending left from mid
#    - Find max sum extending right from mid+1
#    - Crossing sum = left_sum + right_sum
# 5. Return max(left_max, right_max, crossing_max)
#
# Applications: Maximum subarray, maximum sum problems across partitions.
# ================================================================

class MaximumSubarrayPattern:
    """
    Problem: Given integer array nums, find contiguous subarray with largest sum.
    Return the sum.
    
    TC: O(n log n) - log n levels, O(n) work per level
        - Note: Kadane's algorithm solves this in O(n), but D&C demonstrates the paradigm
    SC: O(log n) - recursion stack
    
    How it works (Divide & Conquer):
    1. DIVIDE: Split array into left and right halves
    2. CONQUER: Find max subarray in left half, right half recursively
    3. COMBINE: Find max subarray crossing midpoint
       - Maximum can be entirely in left, entirely in right, or cross middle
       - Must check all three cases
    4. Return maximum of three cases
    
    Why three cases:
    - Subarray could be fully in left half
    - Subarray could be fully in right half
    - Subarray could span across midpoint (crosses boundary)
    - Must check all possibilities to find global maximum
    """
    def maxSubArray(self, nums: List[int]) -> int: # LC 53
        def divide_conquer(left, right):
            # Base case: single element
            if left == right:
                return nums[left]
            
            # DIVIDE: Find midpoint
            mid = (left + right) // 2
            
            # CONQUER: Max in left half and right half
            left_max = divide_conquer(left, mid)
            right_max = divide_conquer(mid + 1, right)
            
            # COMBINE: Max crossing midpoint
            # Find max sum extending left from mid
            left_sum = float('-inf')
            current_sum = 0
            for i in range(mid, left - 1, -1):
                current_sum += nums[i]
                left_sum = max(left_sum, current_sum)
            
            # Find max sum extending right from mid+1
            right_sum = float('-inf')
            current_sum = 0
            for i in range(mid + 1, right + 1):
                current_sum += nums[i]
                right_sum = max(right_sum, current_sum)
            
            # Crossing sum = left extension + right extension
            crossing_sum = left_sum + right_sum
            
            # Return max of three cases
            return max(left_max, right_max, crossing_sum)
        
        return divide_conquer(0, len(nums) - 1)

# Example:
# nums = [-2,1,-3,4,-1,2,1,-5,4]
#
# DIVIDE into halves:
# [-2,1,-3,4] | [-1,2,1,-5,4]
#
# Recursively divide left half:
# [-2,1] | [-3,4]
# Eventually: [-2], [1], [-3], [4]
#
# COMBINE (example at one level):
# Left half max: 4
# Right half max: 3 (subarray [2,1])
# Crossing max: 4 + (-1+2+1) = 6 (subarray [4,-1,2,1])
#
# Return max(4, 3, 6) = 6
#
# Final answer: 6 (subarray [4,-1,2,1])
# Output: 6

sol = MaximumSubarrayPattern()
print("Max subarray sum:", sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
print("Max subarray sum:", sol.maxSubArray([1]))  # 1


# ================================================================
# PATTERN 4: TREE DIVIDE & CONQUER (COMBINE SUBTREE INFO)
# PATTERN EXPLANATION: Solve tree problems by recursively solving for left and right subtrees,
# then combining their results at current node. Each node makes decision based on information
# from both children. Post-order traversal pattern where children processed before parent.
#
# TYPICAL STEPS:
# 1. Base case: null node returns default value
# 2. DIVIDE: Implicitly divide at root into left and right subtrees
# 3. CONQUER: Recursively solve for root.left and root.right
# 4. COMBINE: Use results from both subtrees to compute answer for current node
# 5. Return combined result
#
# Applications: Tree diameter, max path sum, height, validate BST, lowest common ancestor.
# ================================================================

class TreeDivideConquerPattern:
    """
    Problem: Given root of binary tree, return length of diameter. Diameter is length
    of longest path between any two nodes (may or may not pass through root).
    
    TC: O(n) - visit each node exactly once
    SC: O(h) - recursion stack depth where h = height
    
    How it works (Divide & Conquer):
    1. DIVIDE: At each node, split into left and right subtrees
    2. CONQUER: Get height of left subtree and right subtree
    3. COMBINE: Diameter through current node = left_height + right_height
       - Also track maximum diameter seen globally
       - Return height to parent: 1 + max(left_height, right_height)
    
    Why combine is important:
    - Each node could be "peak" of longest path
    - Path through node = left path + right path
    - Must check all nodes to find global maximum
    - But return height (not diameter) to parent for its calculation
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: # LC 543
        self.max_diameter = 0
        
        def height(node):
            if not node:
                return 0
            
            # DIVIDE & CONQUER: Get heights of subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # COMBINE: Calculate diameter through this node
            current_diameter = left_height + right_height
            self.max_diameter = max(self.max_diameter, current_diameter)
            
            # Return height for parent's calculation
            return 1 + max(left_height, right_height)
        
        height(root)
        return self.max_diameter

# Example:
#           1
#          / \
#         2   3
#        / \
#       4   5
#
# DIVIDE & CONQUER from bottom up:
#
# Node 4: left_h=0, right_h=0
#   diameter=0, return height=1
#
# Node 5: left_h=0, right_h=0
#   diameter=0, return height=1
#
# Node 2: left_h=1, right_h=1
#   diameter=1+1=2, return height=1+max(1,1)=2
#
# Node 3: left_h=0, right_h=0
#   diameter=0, return height=1
#
# Node 1: left_h=2, right_h=1
#   diameter=2+1=3 ← Maximum!
#   return height=1+max(2,1)=3
#
# Path of diameter: 4 → 2 → 1 → 3 (length 3)
# Output: 3

sol = TreeDivideConquerPattern()
test_tree = TreeNode(1,
    TreeNode(2, TreeNode(4), TreeNode(5)),
    TreeNode(3))
print("Tree diameter:", sol.diameterOfBinaryTree(test_tree))  # 3


# ================================================================
# PATTERN 5: QUICK SELECT (KTH ELEMENT)
# PATTERN EXPLANATION: Find kth smallest/largest element without fully sorting. Use
# partitioning (from quicksort): choose pivot, partition array so elements < pivot are left,
# elements > pivot are right. Pivot is now in final sorted position. Recursively search
# only the partition containing kth element.
#
# TYPICAL STEPS:
# 1. Choose pivot (often last element or random)
# 2. Partition array around pivot:
#    - Elements < pivot go left
#    - Elements > pivot go right
#    - Pivot ends at its final sorted position
# 3. If pivot index == k, found kth element
# 4. If k < pivot index, search left partition
# 5. If k > pivot index, search right partition
# 6. Return kth element
#
# Applications: Kth largest/smallest, median finding, top k elements.
# ================================================================

class QuickSelectPattern:
    """
    Problem: Given integer array nums and integer k, return kth largest element in array.
    Note: kth largest is kth largest in sorted order, not kth distinct element.
    
    TC: O(n) average, O(n²) worst case
        - Average: partition eliminates half each time → n + n/2 + n/4 + ... = 2n = O(n)
        - Worst: bad pivots lead to O(n²) (rare with good pivot selection)
    SC: O(1) for iterative, O(log n) average for recursive
    
    How it works (Divide & Conquer):
    1. DIVIDE: Partition array around pivot
       - Elements < pivot go left
       - Elements > pivot go right
       - Pivot in final sorted position
    2. CONQUER: Recursively search partition containing kth element
    3. COMBINE: No merging needed - just return kth element when found
    
    Why faster than sorting:
    - Full sort: O(n log n) - must sort everything
    - Quick select: O(n) average - only search one partition each time
    - Eliminates half the array without sorting it
    """
    def findKthLargest(self, nums: List[int], k: int) -> int: # LC 215
        # Convert kth largest to index (0-indexed from left)
        k = len(nums) - k
        
        def partition(left, right):
            """Partition array around pivot, return pivot's final position"""
            pivot = nums[right]
            i = left  # Boundary for elements < pivot
            
            for j in range(left, right):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            
            # Place pivot at boundary
            nums[i], nums[right] = nums[right], nums[i]
            return i
        
        def quick_select(left, right):
            if left == right:
                return nums[left]
            
            # DIVIDE: Partition and get pivot position
            pivot_idx = partition(left, right)
            
            # CONQUER: Search appropriate partition
            if k == pivot_idx:
                return nums[k]  # Found kth element
            elif k < pivot_idx:
                return quick_select(left, pivot_idx - 1)  # Search left
            else:
                return quick_select(pivot_idx + 1, right)  # Search right
        
        return quick_select(0, len(nums) - 1)

# Example:
# nums = [3,2,1,5,6,4], k = 2 (2nd largest)
# Convert: k = 6 - 2 = 4 (index of 2nd largest in sorted array)
#
# Partition around pivot=4:
# [3,2,1,4,6,5] → pivot at index 3
#
# k=4 > pivot_idx=3, search right: [6,5]
#
# Partition around pivot=5:
# [5,6] → pivot at index 4
#
# k=4 == pivot_idx=4, found!
#
# nums[4] = 5 (2nd largest)
# Output: 5

sol = QuickSelectPattern()
print("Kth largest:", sol.findKthLargest([3,2,1,5,6,4], 2))  # 5
print("Kth largest:", sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))  # 4


# ================================================================
# PATTERN 6: DIVIDE & CONQUER WITH PREPROCESSING
# PATTERN EXPLANATION: Preprocess input (like sorting) then apply divide & conquer. Sorting
# enables efficient division and combination. Common in geometric problems or when dividing
# on sorted property improves efficiency. Combines sorting (O(n log n)) with D&C recursion.
#
# TYPICAL STEPS:
# 1. Preprocess: Sort input by key property
# 2. DIVIDE: Split sorted input at midpoint
# 3. CONQUER: Recursively solve for both halves
# 4. COMBINE: Merge results considering boundary cases
# 5. Return combined result
#
# Applications: Closest pair of points, maximum distance, skyline problem.
# ================================================================

class PreprocessingPattern:
    """
    Problem: Given array of points where points[i] = [xi, yi], return k closest points
    to origin (0, 0). Distance is Euclidean: sqrt(x² + y²).
    
    TC: O(n log n) - sorting by distance
        - Note: Can be solved in O(n) average with quick select
        - D&C approach here for demonstration
    SC: O(n) - sorting space
    
    How it works (with preprocessing):
    1. PREPROCESS: Calculate distance for each point, sort by distance
    2. DIVIDE: Not needed here (but could split for parallel processing)
    3. CONQUER: Take first k points after sorting
    4. COMBINE: Return k closest points
    
    This is simplified D&C (sorting does the heavy lifting):
    - Sorting is itself divide & conquer
    - Then we just take k elements
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]: # LC 973
        # Preprocess: Sort by distance to origin
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        
        # Return first k points (closest)
        return points[:k]
    
    # Alternative: Using divide & conquer more explicitly
    def kClosest_dc(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        More explicit D&C using partitioning (like quick select)
        TC: O(n) average
        """
        def distance(point):
            return point[0]**2 + point[1]**2
        
        def partition(left, right):
            pivot_dist = distance(points[right])
            i = left
            
            for j in range(left, right):
                if distance(points[j]) <= pivot_dist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            
            points[i], points[right] = points[right], points[i]
            return i
        
        def quick_select(left, right):
            if left >= right:
                return
            
            pivot_idx = partition(left, right)
            
            if k == pivot_idx + 1:
                return  # Found k closest
            elif k < pivot_idx + 1:
                quick_select(left, pivot_idx - 1)  # Search left
            else:
                quick_select(pivot_idx + 1, right)  # Search right
        
        quick_select(0, len(points) - 1)
        return points[:k]

# Example:
# points = [[1,3],[-2,2],[2,2]], k = 2
#
# Calculate distances:
# [1,3]: sqrt(1+9) = sqrt(10) ≈ 3.16
# [-2,2]: sqrt(4+4) = sqrt(8) ≈ 2.83
# [2,2]: sqrt(4+4) = sqrt(8) ≈ 2.83
#
# Sort by distance:
# [[-2,2],[2,2],[1,3]]
#
# Take first k=2:
# [[-2,2],[2,2]]
#
# Output: [[-2,2],[2,2]]

sol = PreprocessingPattern()
print("K closest points:", sol.kClosest([[1,3],[-2,2],[2,2]], 2))
# [[-2,2],[2,2]] or [[2,2],[-2,2]]
