from typing import Optional, List

# ========================================================
# DIVIDE AND CONQUER MASTER TEMPLATE
# ========================================================

# ------------------------------------------------------------------------------
# 🔥 TEMPLATE 1: CLASSIC DIVIDE AND CONQUER STRUCTURE
# ------------------------------------------------------------------------------
def divide_and_conquer_template(arr, left, right):
    """
    Universal Divide and Conquer Template
    
    Pattern:
    1. BASE CASE: Handle trivial subproblems
    2. DIVIDE: Split problem into smaller subproblems  
    3. CONQUER: Recursively solve subproblems
    4. COMBINE: Merge solutions from subproblems
    
    Time: Often O(n log n), Space: O(log n) recursion stack
    """
    # 1. BASE CASE
    if left >= right:
        return None  # or appropriate base value
    
    # 2. DIVIDE - split at midpoint
    mid = left + (right - left) // 2
    
    # 3. CONQUER - solve subproblems
    left_result = divide_and_conquer_template(arr, left, mid)
    right_result = divide_and_conquer_template(arr, mid + 1, right)
    
    # 4. COMBINE - merge solutions
    return combine_solutions(left_result, right_result)

def combine_solutions(left_result, right_result):
    """Merge step - varies by problem"""
    pass

# ------------------------------------------------------------------------------
# 🔥 TEMPLATE 2: MERGE SORT (Classic D&C Example)
# ------------------------------------------------------------------------------
def merge_sort(arr):
    """
    Merge Sort - Perfect D&C example
    
    Divide: Split array in half
    Conquer: Sort each half recursively  
    Combine: Merge sorted halves
    
    Time: O(n log n), Space: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Conquer
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Combine
    return merge(left_sorted, right_sorted)

def merge(left, right):
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
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test merge sort
test_array = [64, 34, 25, 12, 22, 11, 90]
print("Original:", test_array)
print("Sorted:", merge_sort(test_array))

# ------------------------------------------------------------------------------
# 🔥 TEMPLATE 3: QUICKSORT (D&C with Different Partitioning)
# ------------------------------------------------------------------------------
def quicksort(arr, low, high):
    """
    Quicksort - D&C with pivot partitioning
    
    Different from merge sort:
    - Divide: Partition around pivot (not midpoint)
    - Conquer: Sort partitions recursively
    - Combine: No merge needed (in-place)
    
    Time: O(n log n) average, O(n²) worst
    """
    if low < high:
        # Divide: partition and get pivot index
        pivot_index = partition(arr, low, high)
        
        # Conquer: sort partitions
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    """Partition array around pivot"""
    pivot = arr[high]  # Choose last element as pivot
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Test quicksort
test_array_2 = [64, 34, 25, 12, 22, 11, 90]
print("\nQuicksort test:")
print("Original:", test_array_2)
quicksort(test_array_2, 0, len(test_array_2) - 1)
print("Sorted:", test_array_2)

# ------------------------------------------------------------------------------
# 🔥 TEMPLATE 4: MAXIMUM SUBARRAY (Kadane's Algorithm Alternative)
# ------------------------------------------------------------------------------
def max_subarray_dc(arr, left, right):
    """
    Maximum subarray using divide and conquer
    Alternative to Kadane's algorithm
    
    Three cases:
    1. Max subarray entirely in left half
    2. Max subarray entirely in right half  
    3. Max subarray crosses the middle
    
    Time: O(n log n), Space: O(log n)
    """
    # Base case
    if left == right:
        return arr[left]
    
    # Divide
    mid = (left + right) // 2
    
    # Conquer
    left_sum = max_subarray_dc(arr, left, mid)
    right_sum = max_subarray_dc(arr, mid + 1, right)
    
    # Combine: find max crossing sum
    cross_sum = max_crossing_sum(arr, left, mid, right)
    
    return max(left_sum, right_sum, cross_sum)

def max_crossing_sum(arr, left, mid, right):
    """Find max sum of subarray that crosses midpoint"""
    # Max sum ending at mid (going left)
    left_sum = float('-inf')
    current_sum = 0
    for i in range(mid, left - 1, -1):
        current_sum += arr[i]
        left_sum = max(left_sum, current_sum)
    
    # Max sum starting at mid+1 (going right)
    right_sum = float('-inf')
    current_sum = 0
    for i in range(mid + 1, right + 1):
        current_sum += arr[i]
        right_sum = max(right_sum, current_sum)
    
    return left_sum + right_sum

# Test max subarray
test_array_3 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("\nMax subarray sum:", max_subarray_dc(test_array_3, 0, len(test_array_3) - 1))

# ------------------------------------------------------------------------------
# 🔥 TEMPLATE 5: BINARY SEARCH (D&C on Sorted Data)
# ------------------------------------------------------------------------------
def binary_search(arr, target, left, right):
    """
    Binary search using D&C approach
    
    Different strategy:
    - Divide: Choose middle element
    - Conquer: Search only relevant half
    - Combine: Return result directly
    
    Time: O(log n), Space: O(log n) recursive
    """
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

# Test binary search
sorted_array = [2, 3, 4, 10, 40]
target = 10
result = binary_search(sorted_array, target, 0, len(sorted_array) - 1)
print(f"\nBinary search for {target}: index {result}")

# ------------------------------------------------------------------------------
# 🔥 TEMPLATE 6: POWER CALCULATION (Mathematical D&C)
# ------------------------------------------------------------------------------
def power(base, exponent):
    """
    Calculate base^exponent using D&C
    Instead of O(n) multiplication, use O(log n)
    
    Key insight: x^n = (x^(n/2))^2 if n is even
                 x^n = x * (x^(n/2))^2 if n is odd
    
    Time: O(log n), Space: O(log n)
    """
    # Base cases
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    
    # Divide: calculate base^(exponent/2)
    half_power = power(base, exponent // 2)
    
    # Combine: square the result
    if exponent % 2 == 0:
        return half_power * half_power
    else:
        return base * half_power * half_power

# Test power calculation  
print(f"\n2^10 = {power(2, 10)}")
print(f"3^7 = {power(3, 7)}")

# ------------------------------------------------------------------------------
# 🔥 TEMPLATE 7: TREE CONSTRUCTION FROM SORTED ARRAY (LC 108)
# ------------------------------------------------------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sorted_array_to_bst(nums):
    """
    LC 108: Convert Sorted Array to Height-Balanced BST
    
    Perfect D&C example:
    - Divide: Split array at midpoint
    - Conquer: Build left and right subtrees  
    - Combine: Create root node connecting subtrees
    
    Time: O(n), Space: O(log n)
    """
    def build_tree(left, right):
        if left > right:
            return None
        
        # Divide: choose middle as root for balance
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        
        # Conquer: build subtrees
        root.left = build_tree(left, mid - 1)
        root.right = build_tree(mid + 1, right)
        
        return root
    
    return build_tree(0, len(nums) - 1)

def print_inorder(root):
    """Helper to verify BST property"""
    if root:
        print_inorder(root.left)
        print(root.val, end=' ')
        print_inorder(root.right)

# Test tree construction
nums = [1, 2, 3, 4, 5, 6, 7]
bst_root = sorted_array_to_bst(nums)
print(f"\nBuilding BST from {nums}")
print("Inorder traversal:", end=' ')
print_inorder(bst_root)
print()

# =========================================================
# DIVIDE AND CONQUER DECISION FRAMEWORK
# =========================================================
"""
🎯 WHEN TO USE DIVIDE AND CONQUER:
1. Problem can be broken into similar subproblems
2. Subproblems can be solved independently  
3. Solutions can be combined efficiently
4. Base case is simple to handle

🎯 COMMON PATTERNS:
- Sorting: Split data, sort parts, merge
- Searching: Split search space, search relevant part
- Tree operations: Process subtrees, combine results
- Mathematical: Break down computation, combine results

🎯 TIME COMPLEXITY ANALYSIS:
- T(n) = aT(n/b) + f(n) (Master Theorem)
- Most D&C algorithms: O(n log n)
- Binary search type: O(log n)
- Tree construction: O(n)

🎯 DECISION FLOWCHART:
1. Can problem be split into smaller similar problems? → Yes: D&C candidate
2. Are subproblems independent? → Yes: Good for D&C
3. Is combining solutions efficient? → Yes: D&C works well
4. Is base case simple? → Yes: Perfect for D&C

🎯 COMMON LEETCODE PROBLEMS:
- LC 108: Convert Sorted Array to BST
- LC 23: Merge k Sorted Lists  
- LC 53: Maximum Subarray
- LC 169: Majority Element
- LC 215: Kth Largest Element

# ===================================================================
# LC 108 - Convert Sorted Array to BST 
# ===================================================================
# Pattern: BST Insert (create node + attach children) + BST with Bounds using Divide & Conquer
# Key Insight: Use middle element as root to maintain balance

def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    """
    Convert sorted array to a height balanced BST
    Time: O(n) - visit each element once
    Space: O(log n) - recursion depth for balanced tree
    """
    def recursive(left, right):
        if left > right:  # Base case: no more elements to process
            return None  # root.left or root.right becomes None
        
        mid = (left + right) // 2  # Get left middle element
        root = TreeNode(nums[mid])  # Create new node (root of subtree)
        
        # Recursively call for left and right subtrees
        root.left = recursive(left, mid - 1)
        root.right = recursive(mid + 1, right)
        
        return root  # Returns node and assigns to root.left/root.right
    
    return recursive(0, len(nums) - 1)  # Pass in left and right indexes