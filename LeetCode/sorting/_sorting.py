"""
=================================================================
SORTING COMPLETE GUIDE
=================================================================

WHAT IS SORTING?
----------------
Sorting is the process of arranging elements in a specific order (ascending or descending).
It's one of the most fundamental operations in computer science, enabling efficient searching,
data organization, and optimization. Many complex problems become simpler after sorting the
input data first.

Key characteristics:
- In-place vs Extra space: Modify original array vs create new array
- Stable vs Unstable: Preserve relative order of equal elements vs not
- Comparison-based vs Non-comparison: Compare elements vs use other properties
- Adaptive: Faster on partially sorted data
- Time complexity: O(n²), O(n log n), or O(n) depending on algorithm

Common sorting algorithms:
```
Comparison-based (can't be faster than O(n log n) in general):
- Bubble Sort: O(n²) - Simple but inefficient
- Insertion Sort: O(n²) - Good for small/nearly sorted arrays
- Selection Sort: O(n²) - Simple but inefficient
- Merge Sort: O(n log n) - Stable, predictable, needs O(n) space
- Quick Sort: O(n log n) avg - Fast in-place, O(n²) worst case
- Heap Sort: O(n log n) - In-place, not stable

Non-comparison (can be O(n) with constraints):
- Counting Sort: O(n + k) - Integer range [0, k]
- Bucket Sort: O(n + k) - Distribute into buckets
- Radix Sort: O(d * n) - Sort by digit positions
```

When to use Sorting:
- Need data in specific order
- Optimize search (binary search requires sorted data)
- Find duplicates, closest pairs, intervals
- Greedy algorithms often require sorted input
- Simplify problem by establishing order

Common Sorting problem types:
- Sort by custom criteria (comparator)
- Find kth largest/smallest element
- Merge sorted arrays/lists
- Sort with constraints (colors, 0s-1s-2s)
- Interval problems (meeting rooms, merge intervals)
- Relative ordering problems
- Top K problems
- Sorting characters/strings

SORTING CORE TEMPLATES
=======================
"""

from typing import List
import heapq
from collections import Counter, defaultdict

# ================================================================
# BASIC SORTING (PYTHON BUILT-IN)
# ================================================================
def basic_sort_template(arr):
    """
    Python's built-in sorting (Timsort)
    TC: O(n log n)
    SC: O(n) for sorted(), O(1) for sort()
    """
    # In-place sorting (modifies original)
    arr.sort()  # Ascending
    arr.sort(reverse=True)  # Descending
    
    # Create new sorted array (original unchanged)
    sorted_arr = sorted(arr)
    sorted_desc = sorted(arr, reverse=True)
    
    # Sort with key function
    arr.sort(key=lambda x: x[1])  # Sort by second element
    
    return sorted_arr

# ================================================================
# MERGE SORT TEMPLATE
# ================================================================
def merge_sort_template(arr):
    """
    Divide and conquer sorting
    TC: O(n log n) - always
    SC: O(n) - temporary arrays
    """
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort_template(arr[:mid])
    right = merge_sort_template(arr[mid:])
    
    # Conquer (merge)
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
# QUICK SORT TEMPLATE
# ================================================================
def quick_sort_template(arr, left, right):
    """
    Partition-based sorting
    TC: O(n log n) average, O(n²) worst
    SC: O(log n) - recursion stack
    """
    if left < right:
        # Partition and get pivot position
        pivot_idx = partition(arr, left, right)
        
        # Sort left and right of pivot
        quick_sort_template(arr, left, pivot_idx - 1)
        quick_sort_template(arr, pivot_idx + 1, right)

def partition(arr, left, right):
    """Partition array around pivot"""
    pivot = arr[right]
    i = left - 1
    
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

# ================================================================
# COUNTING SORT TEMPLATE
# ================================================================
def counting_sort_template(arr, max_val):
    """
    Integer sorting for limited range
    TC: O(n + k) where k is range
    SC: O(k) for count array
    """
    count = [0] * (max_val + 1)
    
    # Count occurrences
    for num in arr:
        count[num] += 1
    
    # Build sorted array
    result = []
    for num in range(len(count)):
        result.extend([num] * count[num])
    
    return result

# ================================================================
# QUICK SELECT TEMPLATE (KTH ELEMENT)
# ================================================================
def quick_select_template(arr, k):
    """
    Find kth smallest element without full sort
    TC: O(n) average, O(n²) worst
    SC: O(1)
    """
    def select(left, right, k_smallest):
        if left == right:
            return arr[left]
        
        # Partition
        pivot_idx = partition(arr, left, right)
        
        # Check position
        if k_smallest == pivot_idx:
            return arr[k_smallest]
        elif k_smallest < pivot_idx:
            return select(left, pivot_idx - 1, k_smallest)
        else:
            return select(pivot_idx + 1, right, k_smallest)
    
    return select(0, len(arr) - 1, k)

"""
TIME & SPACE COMPLEXITY REFERENCE
==================================

SORTING ALGORITHMS COMPLEXITY:
-------------------------------
+---------------------------+------------------+------------------+------------------+
| Algorithm                 | Time (Best)      | Time (Average)   | Time (Worst)     |
+---------------------------+------------------+------------------+------------------+
| Bubble Sort               | O(n)             | O(n²)            | O(n²)            |
| Insertion Sort            | O(n)             | O(n²)            | O(n²)            |
| Selection Sort            | O(n²)            | O(n²)            | O(n²)            |
| Merge Sort                | O(n log n)       | O(n log n)       | O(n log n)       |
| Quick Sort                | O(n log n)       | O(n log n)       | O(n²)            |
| Heap Sort                 | O(n log n)       | O(n log n)       | O(n log n)       |
| Counting Sort             | O(n + k)         | O(n + k)         | O(n + k)         |
| Bucket Sort               | O(n + k)         | O(n + k)         | O(n²)            |
| Radix Sort                | O(d * n)         | O(d * n)         | O(d * n)         |
| Quick Select              | O(n)             | O(n)             | O(n²)            |
+---------------------------+------------------+------------------+------------------+

SPACE COMPLEXITY:
-----------------
+---------------------------+------------------+
| Algorithm                 | Space            |
+---------------------------+------------------+
| Bubble Sort               | O(1)             |
| Insertion Sort            | O(1)             |
| Selection Sort            | O(1)             |
| Merge Sort                | O(n)             |
| Quick Sort                | O(log n)         |
| Heap Sort                 | O(1)             |
| Counting Sort             | O(k)             |
| Bucket Sort               | O(n + k)         |
| Radix Sort                | O(n + k)         |
| Quick Select              | O(1)             |
+---------------------------+------------------+

WHERE:
- n = number of elements
- k = range of values (max - min)
- d = number of digits/characters

COMMON SORTING PATTERNS COMPLEXITY:
------------------------------------
+---------------------------+------------------+------------------+
| Pattern                   | Time Complexity  | Space Complexity |
+---------------------------+------------------+------------------+
| Custom Comparator         | O(n log n)       | O(n) or O(1)     |
| Quick Select (Kth)        | O(n) avg         | O(1)             |
| Counting Sort             | O(n + k)         | O(k)             |
| Bucket Sort               | O(n + k)         | O(n + k)         |
| Sort + Two Pointers       | O(n log n)       | O(1)             |
| Merge K Sorted Lists      | O(n log k)       | O(k)             |
| Sort Intervals            | O(n log n)       | O(1)             |
| Partial Sort (Heap)       | O(n log k)       | O(k)             |
+---------------------------+------------------+------------------+

COMPLEXITY NOTES:
-----------------
1. Comparison-based Sorting Lower Bound: O(n log n)
   - Any comparison-based sorting has Ω(n log n) worst case
   - This is a proven theoretical limit
   - Merge sort, heap sort achieve this
   
   Why? Decision tree has n! leaves (all permutations)
   Height ≥ log(n!) = Θ(n log n)

2. Python's sort() and sorted(): O(n log n), Stable
   - Uses Timsort (hybrid of merge sort and insertion sort)
   - Optimized for real-world data
   - Adaptive: faster on partially sorted data
   - sort() is in-place O(1) extra space
   - sorted() creates new list O(n) space

3. Quick Sort: O(n log n) average, O(n²) worst
   - In-place sorting: O(log n) recursion stack
   - Worst case when already sorted with bad pivot
   - Randomized pivot selection improves performance
   - Not stable
   
   Why fast? Good cache locality, in-place
   Average case: T(n) = T(n/2) + T(n/2) + O(n) = O(n log n)

4. Merge Sort: O(n log n) always, Stable
   - Predictable performance
   - Needs O(n) extra space for merging
   - Used in Timsort as base
   - Great for linked lists (no extra space needed)
   
   Recurrence: T(n) = 2T(n/2) + O(n) = O(n log n)

5. Counting Sort: O(n + k) where k = range
   - Not comparison-based, can beat O(n log n)
   - Only works for integers in limited range
   - Stable sorting
   - Space: O(k) for count array
   
   When to use: k is not too large (k = O(n))
   Example: Sort array where values in [0, 100]

6. Bucket Sort: O(n + k) average
   - Distribute elements into buckets
   - Sort each bucket individually
   - Good for uniformly distributed data
   - Worst case O(n²) if all in one bucket
   
   Use when: Input uniformly distributed

7. Quick Select: O(n) average for kth element
   - Find kth smallest without sorting entire array
   - Like quick sort but recurse on one side only
   - Average: T(n) = T(n/2) + O(n) = O(n)
   - Worst: T(n) = T(n-1) + O(n) = O(n²)
   
   Why O(n)? Only recurse on one partition
   n + n/2 + n/4 + ... = 2n = O(n)

8. Heap-based Kth Element: O(n log k)
   - Maintain min/max heap of size k
   - Better than O(n log n) full sort when k << n
   - Space: O(k) for heap
   
   Use for: Top K problems when k is small

WHEN TO USE EACH ALGORITHM:
----------------------------
Built-in sort (Timsort):
  - Default choice for most problems
  - Optimal for general-purpose sorting
  - Use with custom comparator for complex criteria

Quick Select:
  - Find kth largest/smallest
  - Don't need full sorted array
  - O(n) average vs O(n log n) sort

Counting Sort:
  - Integer array with limited range
  - When k (range) is not too large
  - Need stable sort

Bucket Sort:
  - Uniformly distributed floating-point data
  - Can achieve O(n) average case

Merge Sort:
  - Need stable sort
  - Linked list sorting (O(1) extra space)
  - External sorting (large datasets)

Quick Sort:
  - In-place sorting important
  - Average case performance critical
  - Don't need stable sort

Heap Sort:
  - In-place O(n log n) needed
  - Worst-case guarantees important
  - Don't need stable sort

CHOOSING SORTING APPROACH:
--------------------------
Problem requires:
- Full sorted array → Built-in sort O(n log n)
- Kth element only → Quick select O(n) or Heap O(n log k)
- Top K elements → Min/Max heap O(n log k)
- Limited range integers → Counting sort O(n + k)
- Stable sort → Merge sort or Timsort
- In-place with O(n log n) → Heap sort or Quick sort
- Custom criteria → Sort with key/comparator
"""

"""
SORTING PATTERNS
================
"""

# ================================================================
# PATTERN 1: CUSTOM COMPARATOR SORTING
# PATTERN EXPLANATION: Sort by custom criteria using key function or comparator. Python's
# sort() and sorted() accept key parameter for transformation function. Use lambda or
# custom function to define sorting logic. Can sort by multiple keys, computed values, or
# complex conditions. Most common pattern in real-world sorting problems.
#
# TYPICAL STEPS:
# 1. Identify sorting criteria (what determines order?)
# 2. Define key function that extracts/computes sort value
# 3. Use sorted(arr, key=...) or arr.sort(key=...)
# 4. For multiple criteria, return tuple of keys
# 5. Use reverse=True for descending order
#
# Applications: Sort by multiple keys, sort objects, relative ordering, priority sorting.
# ================================================================

class CustomComparator:
    """
    Problem 1: Sort array of strings by length, then lexicographically if same length.
    
    Example:
        Input: ["apple", "pie", "a", "banana", "cat"]
        Output: ["a", "cat", "pie", "apple", "banana"]
        
        Explanation:
        - Length 1: "a"
        - Length 3: "cat", "pie" (alphabetical)
        - Length 5: "apple"
        - Length 6: "banana"
    
    TC: O(n log n) - sorting dominates
    SC: O(n) - for sorted() output or O(1) for sort()
    
    How it works:
    1. Primary key: string length
    2. Secondary key: lexicographic order
    3. Return tuple (len, string) for multi-key sorting
    """
    def sortByLengthThenAlpha(self, words: List[str]) -> List[str]:
        # Sort by length first, then alphabetically
        return sorted(words, key=lambda x: (len(x), x))

# Example trace:
# words = ["apple", "pie", "a", "banana", "cat"]
# 
# Keys generated:
# "apple" → (5, "apple")
# "pie" → (3, "pie")
# "a" → (1, "a")
# "banana" → (6, "banana")
# "cat" → (3, "cat")
#
# Sorted by tuple comparison:
# (1, "a") < (3, "cat") < (3, "pie") < (5, "apple") < (6, "banana")
# Result: ["a", "cat", "pie", "apple", "banana"]

    def largestNumber(self, nums: List[int]) -> str:  # LC 179
        """
        Problem 2: Arrange numbers to form largest number.
        
        Example:
            Input: [3, 30, 34, 5, 9]
            Output: "9534330"
            
            Why? 9 > 5 > 34 > 3 > 30
            Compare: "934" vs "349", "330" vs "303"
        
        TC: O(n log n) - sorting
        SC: O(n) - string conversion
        
        How it works:
        1. Convert numbers to strings
        2. Custom comparator: compare concatenations
        3. For a, b: if a+b > b+a, then a should come first
        4. Use functools.cmp_to_key for custom comparator
        """
        from functools import cmp_to_key
        
        # Convert to strings
        nums_str = [str(num) for num in nums]
        
        # Custom comparator
        def compare(a, b):
            # Compare concatenations: a+b vs b+a
            if a + b > b + a:
                return -1  # a should come before b
            elif a + b < b + a:
                return 1   # b should come before a
            else:
                return 0
        
        # Sort with custom comparator
        nums_str.sort(key=cmp_to_key(compare))
        
        # Handle edge case: all zeros
        result = ''.join(nums_str)
        return '0' if result[0] == '0' else result

# Example trace:
# nums = [3, 30, 34, 5, 9]
# nums_str = ["3", "30", "34", "5", "9"]
#
# Comparisons:
# "9" vs "5": "95" > "59" → "9" first
# "5" vs "34": "534" > "345" → "5" first
# "34" vs "3": "343" > "334" → "34" first
# "3" vs "30": "330" > "303" → "3" first
#
# Sorted: ["9", "5", "34", "3", "30"]
# Result: "9534330"

    def sortColors(self, nums: List[int]) -> None:  # LC 75 - Dutch National Flag
        """
        Problem 3: Sort array with only 0s, 1s, and 2s in-place.
        
        Example:
            Input: [2,0,2,1,1,0]
            Output: [0,0,1,1,2,2]
        
        TC: O(n) - single pass
        SC: O(1) - in-place
        
        How it works (Three-way partitioning):
        1. Three pointers: left (0s boundary), right (2s boundary), current
        2. If 0: swap with left, move both forward
        3. If 2: swap with right, move right backward
        4. If 1: just move current forward
        """
        left, current, right = 0, 0, len(nums) - 1
        
        while current <= right:
            if nums[current] == 0:
                # Swap with left boundary
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1
            elif nums[current] == 2:
                # Swap with right boundary
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
                # Don't increment current (need to check swapped value)
            else:  # nums[current] == 1
                current += 1

# Example trace:
# nums = [2,0,2,1,1,0]
# left=0, current=0, right=5
#
# current=0, nums[0]=2: swap with right
#   [0,0,2,1,1,2], right=4
# current=0, nums[0]=0: swap with left
#   [0,0,2,1,1,2], left=1, current=1
# current=1, nums[1]=0: swap with left
#   [0,0,2,1,1,2], left=2, current=2
# current=2, nums[2]=2: swap with right
#   [0,0,1,1,2,2], right=3
# current=2, nums[2]=1: move forward
#   current=3
# current=3, nums[3]=1: move forward
#   current=4
# current > right, done
# Result: [0,0,1,1,2,2]

sol = CustomComparator()
print("Sort by Length:", sol.sortByLengthThenAlpha(["apple", "pie", "a", "banana", "cat"]))
print("Largest Number:", sol.largestNumber([3, 30, 34, 5, 9]))
nums = [2,0,2,1,1,0]
sol.sortColors(nums)
print("Sort Colors:", nums)


# ================================================================
# PATTERN 2: QUICK SELECT (PARTIAL SORTING)
# PATTERN EXPLANATION: Find kth smallest/largest element without fully sorting array.
# Uses partition logic from quick sort but only recurses on relevant side. Average O(n)
# time by eliminating half of array each iteration. Alternative: use heap for O(n log k).
# Essential for "top K" problems where full sort is unnecessary.
#
# TYPICAL STEPS:
# 1. Choose pivot and partition array
# 2. Check pivot position against k
# 3. If pivot at k: found answer
# 4. If pivot > k: recurse on left side
# 5. If pivot < k: recurse on right side
# 6. Average case eliminates half each time → O(n)
#
# Applications: Kth largest/smallest, median finding, top K elements, percentile.
# ================================================================

class QuickSelect:
    """
    Problem 1: Find kth largest element in unsorted array.
    
    Example:
        Input: nums = [3,2,1,5,6,4], k = 2
        Output: 5
        
        Explanation: Sorted = [1,2,3,4,5,6]
        2nd largest = 5
    
    TC: O(n) average, O(n²) worst
    SC: O(1) - in-place
    
    How it works:
    1. Partition array around pivot
    2. If pivot at (n-k)th position, it's kth largest
    3. Otherwise recurse on relevant partition
    4. Each iteration reduces search space by ~half
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:  # LC 215
        def partition(left, right):
            """Partition array and return pivot index"""
            pivot = nums[right]
            i = left
            
            for j in range(left, right):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            
            nums[i], nums[right] = nums[right], nums[i]
            return i
        
        def select(left, right, k_smallest):
            """Find kth smallest element"""
            if left == right:
                return nums[left]
            
            pivot_idx = partition(left, right)
            
            if k_smallest == pivot_idx:
                return nums[pivot_idx]
            elif k_smallest < pivot_idx:
                return select(left, pivot_idx - 1, k_smallest)
            else:
                return select(pivot_idx + 1, right, k_smallest)
        
        # Kth largest = (n-k)th smallest
        return select(0, len(nums) - 1, len(nums) - k)

# Example trace:
# nums = [3,2,1,5,6,4], k = 2 (find 2nd largest)
# n - k = 6 - 2 = 4 (find 4th smallest, 0-indexed)
#
# select(0, 5, 4):
#   partition(0, 5) with pivot=4:
#     [3,2,1,4,6,5], pivot at index 3
#   4 == 4? No, 4 > 3, recurse right
#   select(4, 5, 4):
#     partition(4, 5) with pivot=5:
#       [3,2,1,4,5,6], pivot at index 4
#     4 == 4? Yes!
#     return nums[4] = 5

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  # LC 347
        """
        Problem 2: Find k most frequent elements.
        
        Example:
            Input: nums = [1,1,1,2,2,3], k = 2
            Output: [1, 2]
        
        TC: O(n) average with quick select
        SC: O(n) - frequency map
        
        Alternative: Min heap O(n log k)
        
        How it works:
        1. Count frequencies
        2. Use quick select on unique elements by frequency
        3. Partition by comparing frequencies
        """
        # Count frequencies
        freq_map = Counter(nums)
        unique = list(freq_map.keys())
        
        def partition(left, right):
            pivot_freq = freq_map[unique[right]]
            i = left
            
            for j in range(left, right):
                if freq_map[unique[j]] <= pivot_freq:
                    unique[i], unique[j] = unique[j], unique[i]
                    i += 1
            
            unique[i], unique[right] = unique[right], unique[i]
            return i
        
        def select(left, right, k_smallest):
            if left == right:
                return
            
            pivot_idx = partition(left, right)
            
            if k_smallest == pivot_idx:
                return
            elif k_smallest < pivot_idx:
                select(left, pivot_idx - 1, k_smallest)
            else:
                select(pivot_idx + 1, right, k_smallest)
        
        # Find top k = find (n-k)th smallest by frequency
        n = len(unique)
        select(0, n - 1, n - k)
        
        # Return top k (last k elements after partition)
        return unique[n - k:]

    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        """
        Alternative using min heap: O(n log k)
        Better when k is small compared to n
        """
        freq_map = Counter(nums)
        
        # Min heap of size k
        heap = []
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)  # Remove least frequent
        
        return [num for freq, num in heap]

sol = QuickSelect()
print("Kth Largest:", sol.findKthLargest([3,2,1,5,6,4], 2))  # 5
print("Top K Frequent:", sol.topKFrequent([1,1,1,2,2,3], 2))  # [1, 2]
print("Top K Frequent (Heap):", sol.topKFrequent_heap([1,1,1,2,2,3], 2))  # [1, 2]


# ================================================================
# PATTERN 3: COUNTING SORT / BUCKET SORT (LINEAR TIME)
# PATTERN EXPLANATION: Achieve O(n) sorting when values are integers in limited range or
# can be bucketed. Counting sort counts occurrences of each value. Bucket sort distributes
# into buckets then sorts each. Non-comparison based, can beat O(n log n) lower bound for
# comparison sorts. Use when range k is not too large (k = O(n)).
#
# TYPICAL STEPS:
# Counting Sort:
# 1. Find range of values [min, max]
# 2. Create count array of size (max - min + 1)
# 3. Count occurrences of each value
# 4. Reconstruct sorted array from counts
#
# Bucket Sort:
# 1. Create k buckets for value ranges
# 2. Distribute elements into buckets
# 3. Sort each bucket individually
# 4. Concatenate all buckets
#
# Applications: Sort limited range integers, sort by digit, color sorting, age sorting.
# ================================================================

class LinearTimeSorting:
    """
    Problem 1: Sort array where elements are in range [0, k].
    
    Example:
        Input: nums = [4, 2, 2, 8, 3, 3, 1], k = 10
        Output: [1, 2, 2, 3, 3, 4, 8]
    
    TC: O(n + k) - count occurrences + rebuild
    SC: O(k) - count array
    
    How it works (Counting Sort):
    1. Count frequency of each number
    2. Iterate through counts rebuilding sorted array
    3. Each value appears count[value] times
    """
    def countingSort(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        
        # Find range
        min_val, max_val = min(nums), max(nums)
        range_size = max_val - min_val + 1
        
        # Count occurrences
        count = [0] * range_size
        for num in nums:
            count[num - min_val] += 1
        
        # Rebuild sorted array
        result = []
        for i in range(range_size):
            result.extend([i + min_val] * count[i])
        
        return result

# Example trace:
# nums = [4, 2, 2, 8, 3, 3, 1]
# min_val = 1, max_val = 8, range = 8
#
# Count array (index 0 = value 1):
# count = [1, 2, 2, 1, 0, 0, 0, 1]
#          ^  ^  ^  ^  ^  ^  ^  ^
#          1  2  3  4  5  6  7  8
#
# Rebuild:
# i=0: 1 appears 1 time → [1]
# i=1: 2 appears 2 times → [1, 2, 2]
# i=2: 3 appears 2 times → [1, 2, 2, 3, 3]
# i=3: 4 appears 1 time → [1, 2, 2, 3, 3, 4]
# i=7: 8 appears 1 time → [1, 2, 2, 3, 3, 4, 8]

    def sortArrayByParity(self, nums: List[int]) -> List[int]:  # LC 905
        """
        Problem 2: Sort so all even numbers come before odd numbers.
        
        Example:
            Input: [3,1,2,4]
            Output: [2,4,3,1] (any order where evens before odds)
        
        TC: O(n) - single pass
        SC: O(1) - in-place with two pointers
        
        How it works:
        1. Two pointers: left (even position), right (odd position)
        2. When left is odd and right is even, swap
        3. Move appropriate pointer
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            # Find odd number from left
            while left < right and nums[left] % 2 == 0:
                left += 1
            
            # Find even number from right
            while left < right and nums[right] % 2 == 1:
                right -= 1
            
            # Swap odd-left with even-right
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        return nums

    def maximumGap(self, nums: List[int]) -> int:  # LC 164
        """
        Problem 3: Find maximum gap between sorted elements in O(n) time.
        
        Example:
            Input: [3,6,9,1]
            Sorted: [1,3,6,9]
            Gaps: 2, 3, 3
            Output: 3
        
        TC: O(n) - bucket sort approach
        SC: O(n) - buckets
        
        How it works (Bucket Sort):
        1. Divide range into n-1 buckets
        2. By pigeonhole principle, max gap >= bucket size
        3. Max gap must be between buckets (not within)
        4. Track min/max in each bucket
        5. Find max gap between bucket max and next bucket min
        """
        if len(nums) < 2:
            return 0
        
        min_val, max_val = min(nums), max(nums)
        
        if min_val == max_val:
            return 0
        
        n = len(nums)
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        # Track min and max in each bucket
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]
        
        # Place numbers in buckets
        for num in nums:
            idx = (num - min_val) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)
        
        # Find max gap between buckets
        max_gap = 0
        prev_max = min_val
        
        for bucket_min, bucket_max in buckets:
            if bucket_min == float('inf'):  # Empty bucket
                continue
            
            max_gap = max(max_gap, bucket_min - prev_max)
            prev_max = bucket_max
        
        return max_gap

# Example trace for maximumGap:
# nums = [3,6,9,1]
# min=1, max=9, range=8, n=4
# bucket_size = 8/3 = 2 (rounded)
# buckets: 3 buckets covering [1-3), [3-5), [5-7), [7-9]
# 
# Place numbers:
# 1 → bucket 0: [1, 1]
# 3 → bucket 1: [3, 3]
# 6 → bucket 2: [6, 6]
# 9 → bucket 3: [9, 9]
#
# Calculate gaps:
# Gap from prev_max=1 to bucket[1].min=3: 3-1=2
# Gap from prev_max=3 to bucket[2].min=6: 6-3=3
# Gap from prev_max=6 to bucket[3].min=9: 9-6=3
# Max gap = 3

sol = LinearTimeSorting()
print("Counting Sort:", sol.countingSort([4,2,2,8,3,3,1]))  # [1,2,2,3,3,4,8]
print("Sort by Parity:", sol.sortArrayByParity([3,1,2,4]))  # [2,4,3,1] or similar
print("Maximum Gap:", sol.maximumGap([3,6,9,1]))  # 3


# ================================================================
# PATTERN 4: SORT + GREEDY
# PATTERN EXPLANATION: Many greedy algorithms require sorted input to make optimal local
# choices. Sort first to establish order, then apply greedy logic. Common pattern: sort by
# one attribute, then greedily process in order. Sorting enables the greedy choice property
# where local optimal leads to global optimal.
#
# TYPICAL STEPS:
# 1. Sort input by key attribute (start time, end time, value, etc.)
# 2. Initialize greedy variables (count, last selected, etc.)
# 3. Iterate through sorted elements
# 4. Make greedy choice at each step
# 5. Update state and accumulate result
#
# Applications: Interval scheduling, job sequencing, fractional knapsack, meeting rooms.
# ================================================================

class SortAndGreedy:
    """
    Problem 1: Minimum number of meeting rooms needed.
    
    Example:
        Input: intervals = [[0,30],[5,10],[15,20]]
        Output: 2
        
        Explanation:
        [0,30] and [5,10] overlap → need 2 rooms
        [15,20] can reuse a room
    
    TC: O(n log n) - sorting dominates
    SC: O(n) - for heap
    
    How it works:
    1. Sort intervals by start time
    2. Use min heap to track room end times
    3. For each interval:
       - If earliest ending room finishes before current starts: reuse
       - Otherwise: allocate new room
    4. Heap size = number of rooms needed
    """
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:  # LC 253
        if not intervals:
            return 0
        
        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        # Min heap to track room end times
        heap = []
        
        for start, end in intervals:
            # If earliest ending room is free, reuse it
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            
            # Allocate room (or reuse) with this end time
            heapq.heappush(heap, end)
        
        return len(heap)

# Example trace:
# intervals = [[0,30],[5,10],[15,20]]
# Sorted: [[0,30],[5,10],[15,20]]
#
# Process [0,30]:
#   heap = [], no room to reuse
#   Push end=30, heap = [30]
#
# Process [5,10]:
#   heap[0] = 30 > 5, can't reuse
#   Push end=10, heap = [10, 30]
#
# Process [15,20]:
#   heap[0] = 10 <= 15, can reuse!
#   Pop 10, heap = [30]
#   Push end=20, heap = [20, 30]
#
# Result: len(heap) = 2 rooms

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:  # LC 435
        """
        Problem 2: Minimum number of intervals to remove to make non-overlapping.
        
        Example:
            Input: [[1,2],[2,3],[3,4],[1,3]]
            Output: 1
            
            Remove [1,3] to make [[1,2],[2,3],[3,4]] non-overlapping
        
        TC: O(n log n) - sorting
        SC: O(1) - in-place
        
        How it works (Greedy by end time):
        1. Sort by end time
        2. Keep track of last selected interval's end
        3. If current starts before last end: overlaps, must remove
        4. Otherwise: select current interval
        5. Always keep interval that ends earliest
        """
        if not intervals:
            return 0
        
        # Sort by end time (greedy: prefer intervals that end early)
        intervals.sort(key=lambda x: x[1])
        
        removed = 0
        last_end = float('-inf')
        
        for start, end in intervals:
            if start >= last_end:
                # No overlap, keep this interval
                last_end = end
            else:
                # Overlap, must remove one
                removed += 1
                # Keep the one with earlier end (already in last_end)
        
        return removed

# Example trace:
# intervals = [[1,2],[2,3],[3,4],[1,3]]
# Sort by end: [[1,2],[2,3],[1,3],[3,4]]
#
# last_end = -inf, removed = 0
#
# [1,2]: 1 >= -inf, keep. last_end=2
# [2,3]: 2 >= 2, keep. last_end=3
# [1,3]: 1 < 3, overlap! removed=1, keep last_end=3
# [3,4]: 3 >= 3, keep. last_end=4
#
# Result: removed = 1

    def mergeSortedArray(self, nums1: List[int], m: int, 
                          nums2: List[int], n: int) -> None:  # LC 88
        """
        Problem 3: Merge nums2 into nums1 (both sorted).
        nums1 has space for both.
        
        Example:
            Input: nums1 = [1,2,3,0,0,0], m = 3
                   nums2 = [2,5,6], n = 3
            Output: [1,2,2,3,5,6]
        
        TC: O(m + n) - single pass
        SC: O(1) - in-place
        
        How it works (Merge from back):
        1. Three pointers: p1 (end of nums1), p2 (end of nums2), p (end of result)
        2. Compare nums1[p1] and nums2[p2]
        3. Place larger at nums1[p]
        4. Work backwards to avoid overwriting
        """
        p1 = m - 1  # Last element in nums1
        p2 = n - 1  # Last element in nums2
        p = m + n - 1  # Last position in merged array
        
        # Merge from back to front
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # Copy remaining from nums2 (if any)
        # No need to copy from nums1 (already in place)
        nums1[:p2+1] = nums2[:p2+1]

# Example trace:
# nums1 = [1,2,3,0,0,0], m=3
# nums2 = [2,5,6], n=3
# p1=2, p2=2, p=5
#
# Compare nums1[2]=3 vs nums2[2]=6: 6 larger
#   nums1[5]=6, p2=1, p=4
#   nums1 = [1,2,3,0,0,6]
#
# Compare nums1[2]=3 vs nums2[1]=5: 5 larger
#   nums1[4]=5, p2=0, p=3
#   nums1 = [1,2,3,0,5,6]
#
# Compare nums1[2]=3 vs nums2[0]=2: 3 larger
#   nums1[3]=3, p1=1, p=2
#   nums1 = [1,2,3,3,5,6]
#
# Compare nums1[1]=2 vs nums2[0]=2: equal, take nums2
#   nums1[2]=2, p2=-1, p=1
#   nums1 = [1,2,2,3,5,6]
#
# p2 < 0, done
# Result: [1,2,2,3,5,6]

sol = SortAndGreedy()
print("Min Meeting Rooms:", sol.minMeetingRooms([[0,30],[5,10],[15,20]]))  # 2
print("Erase Overlap Intervals:", sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))  # 1
nums1 = [1,2,3,0,0,0]
sol.mergeSortedArray(nums1, 3, [2,5,6], 3)
print("Merge Sorted Array:", nums1)  # [1,2,2,3,5,6]


# ================================================================
# PATTERN 5: MERGE SORTED ARRAYS/LISTS
# PATTERN EXPLANATION: Merge multiple sorted sequences efficiently. Use merge operation
# (two pointers for 2 arrays) or min heap (for k arrays). Each sorted array/list has
# internal order that must be preserved. Common in divide-and-conquer sorting and external
# sorting. Key: compare current elements from each sequence and pick smallest.
#
# TYPICAL STEPS:
# For 2 arrays:
# 1. Two pointers, one for each array
# 2. Compare current elements
# 3. Add smaller to result, advance pointer
# 4. Copy remaining elements
#
# For K arrays:
# 1. Min heap with (value, array_idx, element_idx)
# 2. Pop minimum, add to result
# 3. Push next element from same array
# 4. Repeat until heap empty
#
# Applications: Merge sort, merge k sorted lists/arrays, external sorting.
# ================================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeSorted:
    """
    Problem 1: Merge k sorted linked lists.
    
    Example:
        Input: lists = [[1,4,5],[1,3,4],[2,6]]
        Output: [1,1,2,3,4,4,5,6]
    
    TC: O(n log k) where n = total nodes, k = number of lists
    SC: O(k) - heap size
    
    How it works:
    1. Use min heap with (value, list_index, node)
    2. Initially add head of each list
    3. Pop minimum, add to result
    4. Push next node from same list
    5. Repeat until heap empty
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:  # LC 23
        if not lists:
            return None
        
        # Min heap: (value, index, node)
        heap = []
        
        # Add head of each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            
            # Add to result
            current.next = node
            current = current.next
            
            # Add next from same list
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next

# Example trace:
# lists = [[1,4,5],[1,3,4],[2,6]]
# 
# Initial heap: [(1,0,node1), (1,1,node1'), (2,2,node2)]
#
# Pop (1,0,node1): result=[1], push (4,0,node4)
# heap = [(1,1,node1'), (2,2,node2), (4,0,node4)]
#
# Pop (1,1,node1'): result=[1,1], push (3,1,node3)
# heap = [(2,2,node2), (3,1,node3), (4,0,node4)]
#
# Pop (2,2,node2): result=[1,1,2], push (6,2,node6)
# heap = [(3,1,node3), (4,0,node4), (6,2,node6)]
#
# ... continues until heap empty
# Result: [1,1,2,3,4,4,5,6]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:  # LC 56
        """
        Problem 2: Merge overlapping intervals.
        
        Example:
            Input: [[1,3],[2,6],[8,10],[15,18]]
            Output: [[1,6],[8,10],[15,18]]
            
            [1,3] and [2,6] overlap → merge to [1,6]
        
        TC: O(n log n) - sorting
        SC: O(n) - output
        
        How it works:
        1. Sort intervals by start time
        2. For each interval:
           - If overlaps with last merged: extend last
           - Otherwise: add as new interval
        3. Overlap check: current.start <= last.end
        """
        if not intervals:
            return []
        
        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for start, end in intervals[1:]:
            last_start, last_end = merged[-1]
            
            if start <= last_end:
                # Overlap: merge by extending last interval
                merged[-1][1] = max(last_end, end)
            else:
                # No overlap: add as new interval
                merged.append([start, end])
        
        return merged

# Example trace:
# intervals = [[1,3],[2,6],[8,10],[15,18]]
# Sorted (already sorted)
#
# merged = [[1,3]]
#
# [2,6]: 2 <= 3? Yes, overlap
#   Extend: merged[-1][1] = max(3,6) = 6
#   merged = [[1,6]]
#
# [8,10]: 8 <= 6? No
#   Add new: merged = [[1,6],[8,10]]
#
# [15,18]: 15 <= 10? No
#   Add new: merged = [[1,6],[8,10],[15,18]]
#
# Result: [[1,6],[8,10],[15,18]]

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:  # LC 378
        """
        Problem 3: Find kth smallest in sorted matrix (each row and column sorted).
        
        Example:
            matrix = [[1, 5, 9],
                      [10,11,13],
                      [12,13,15]]
            k = 8
            Output: 13
            
            Sorted: [1,5,9,10,11,12,13,13,15]
            8th element = 13
        
        TC: O(k log n) where n = number of rows
        SC: O(n) - heap size
        
        How it works (Merge k sorted arrays):
        1. Treat each row as sorted array
        2. Min heap with (value, row, col)
        3. Initially add first element of each row
        4. Pop k times, each time adding next in same row
        """
        n = len(matrix)
        heap = []
        
        # Add first element of each row
        for r in range(min(n, k)):  # Only need k rows
            heapq.heappush(heap, (matrix[r][0], r, 0))
        
        # Pop k-1 times
        result = 0
        for _ in range(k):
            result, r, c = heapq.heappop(heap)
            
            # Add next element from same row
            if c + 1 < n:
                heapq.heappush(heap, (matrix[r][c+1], r, c+1))
        
        return result

# Example trace:
# matrix = [[1,5,9],[10,11,13],[12,13,15]], k=8
#
# Initial heap: [(1,0,0), (10,1,0), (12,2,0)]
#
# Pop 1: (1,0,0), push (5,0,1)
# heap = [(5,0,1), (10,1,0), (12,2,0)]
#
# Pop 2: (5,0,1), push (9,0,2)
# heap = [(9,0,2), (10,1,0), (12,2,0)]
#
# Pop 3: (9,0,2), row 0 done
# heap = [(10,1,0), (12,2,0)]
#
# Pop 4: (10,1,0), push (11,1,1)
# heap = [(11,1,1), (12,2,0)]
#
# Pop 5: (11,1,1), push (13,1,2)
# heap = [(12,2,0), (13,1,2)]
#
# Pop 6: (12,2,0), push (13,2,1)
# heap = [(13,1,2), (13,2,1)]
#
# Pop 7: (13,1,2), row 1 done
# heap = [(13,2,1)]
#
# Pop 8: (13,2,1) ← This is the answer!
# Result: 13

sol = MergeSorted()
print("Merge Intervals:", sol.merge([[1,3],[2,6],[8,10],[15,18]]))
print("Kth Smallest in Matrix:", sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))


# ================================================================
# PATTERN 6: SORT + TWO POINTERS
# PATTERN EXPLANATION: Combine sorting with two-pointer technique for efficient solutions.
# Sort first to enable two-pointer approach from ends or same direction. Common for problems
# finding pairs, triplets, or subarrays with specific sum/property. Sorting creates order
# that allows strategic pointer movement.
#
# TYPICAL STEPS:
# 1. Sort array
# 2. Initialize two pointers (both ends or same start)
# 3. While pointers valid:
#    a. Check current pair/window
#    b. If condition met: record result
#    c. Move pointer(s) based on comparison with target
# 4. Return accumulated results
#
# Applications: Two sum, three sum, closest sum, container with most water.
# ================================================================

class SortTwoPointers:
    """
    Problem 1: Find all unique triplets that sum to zero.
    
    Example:
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
    
    TC: O(n²) - O(n log n) sort + O(n²) two pointers
    SC: O(1) excluding output
    
    How it works:
    1. Sort array
    2. Fix first element, use two pointers for remaining
    3. If sum = 0: found triplet
    4. If sum < 0: move left pointer right
    5. If sum > 0: move right pointer left
    6. Skip duplicates to avoid duplicate triplets
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:  # LC 15
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Two pointers for remaining elements
            left, right = i + 1, len(nums) - 1
            target = -nums[i]
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result

# Example trace:
# nums = [-1,0,1,2,-1,-4]
# Sorted: [-4,-1,-1,0,1,2]
#
# i=0, nums[0]=-4, target=4:
#   left=1, right=5: -1+2=1 < 4, left++
#   left=2, right=5: -1+2=1 < 4, left++
#   left=3, right=5: 0+2=2 < 4, left++
#   left=4, right=5: 1+2=3 < 4, left++
#   left >= right, done
#
# i=1, nums[1]=-1, target=1:
#   left=2, right=5: -1+2=1 == 1, found [-1,-1,2]!
#   Skip duplicates, left=3, right=4
#   left=3, right=4: 0+1=1 == 1, found [-1,0,1]!
#   left >= right, done
#
# i=2, nums[2]=-1, skip (duplicate)
#
# Result: [[-1,-1,2],[-1,0,1]]

    def threeSumClosest(self, nums: List[int], target: int) -> int:  # LC 16
        """
        Problem 2: Find triplet with sum closest to target.
        
        Example:
            Input: nums = [-1,2,1,-4], target = 1
            Output: 2
            
            Explanation: Sum closest to 1 is 2 (-1+2+1)
        
        TC: O(n²)
        SC: O(1)
        
        How it works:
        1. Similar to three sum
        2. Track closest sum seen so far
        3. Update closest when current sum is closer to target
        """
        nums.sort()
        closest = float('inf')
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest if current is closer
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum
                
                # Move pointers
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target  # Exact match
        
        return closest

    def maxArea(self, height: List[int]) -> int:  # LC 11
        """
        Problem 3: Find two lines that form container with most water.
        
        Example:
            Input: height = [1,8,6,2,5,4,8,3,7]
            Output: 49
            
            Lines at index 1 (height 8) and 8 (height 7)
            Distance = 7, min_height = 7, area = 49
        
        TC: O(n) - single pass with two pointers
        SC: O(1)
        
        How it works:
        1. Two pointers at both ends
        2. Calculate area with current pair
        3. Move pointer with shorter height inward
        4. Why? Moving taller doesn't help (limited by shorter)
        """
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate area
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height
            max_area = max(max_area, area)
            
            # Move pointer with shorter height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# Example trace:
# height = [1,8,6,2,5,4,8,3,7]
# left=0, right=8
#
# Area = (8-0) * min(1,7) = 8*1 = 8
# height[0]=1 < height[8]=7, left++
#
# left=1, right=8
# Area = (8-1) * min(8,7) = 7*7 = 49
# height[1]=8 > height[8]=7, right--
#
# left=1, right=7
# Area = (7-1) * min(8,3) = 6*3 = 18
# height[1]=8 > height[7]=3, right--
#
# ... continues
# Max area = 49

sol = SortTwoPointers()
print("Three Sum:", sol.threeSum([-1,0,1,2,-1,-4]))  # [[-1,-1,2],[-1,0,1]]
print("Three Sum Closest:", sol.threeSumClosest([-1,2,1,-4], 1))  # 2
print("Max Area:", sol.maxArea([1,8,6,2,5,4,8,3,7]))  # 49


# ================================================================
# SUMMARY OF SORTING PATTERNS
# ================================================================
"""
Pattern 1 - Custom Comparator Sorting:
  - Sort by custom criteria using key function
  - Multi-key sorting with tuples
  - Use for: Complex sorting rules, object sorting
  - Example: LC 179 (Largest Number), LC 75 (Sort Colors)

Pattern 2 - Quick Select (Partial Sorting):
  - Find kth element without full sort
  - O(n) average vs O(n log n) full sort
  - Use for: Top K, kth largest/smallest
  - Example: LC 215 (Kth Largest), LC 347 (Top K Frequent)

Pattern 3 - Counting/Bucket Sort (Linear Time):
  - O(n) sorting for limited range integers
  - Non-comparison based
  - Use for: Integer range sorting, color sorting
  - Example: LC 164 (Maximum Gap), LC 905 (Sort by Parity)

Pattern 4 - Sort + Greedy:
  - Sort first, then apply greedy logic
  - Common in interval/scheduling problems
  - Use for: Meeting rooms, interval merging, job scheduling
  - Example: LC 253 (Meeting Rooms II), LC 435 (Erase Overlap)

Pattern 5 - Merge Sorted Arrays/Lists:
  - Merge k sorted sequences efficiently
  - Use min heap for k-way merge
  - Use for: Merge sort, k sorted lists, sorted matrix
  - Example: LC 23 (Merge K Lists), LC 56 (Merge Intervals)

Pattern 6 - Sort + Two Pointers:
  - Combine sorting with two-pointer technique
  - Efficient for sum problems, pairs, triplets
  - Use for: Two/three sum, closest sum, container problems
  - Example: LC 15 (Three Sum), LC 11 (Container With Most Water)

Master these 6 patterns and you'll handle 80-90% of sorting problems on LeetCode!

KEY TAKEAWAYS:
--------------
1. Python's sort() is in-place O(1) space, sorted() creates new list O(n)
2. Timsort is O(n log n) stable sort, great for real-world data
3. Custom comparator: use key=lambda for simple, functools.cmp_to_key for complex
4. Quick select finds kth element in O(n) average without full sort
5. Counting sort is O(n) but only for limited integer range
6. Sort intervals by start/end time for greedy algorithms
7. Use min heap for k-way merge: O(n log k)
8. Sort + two pointers pattern very common for sum problems
9. Always check if full sort is needed or partial/linear sort works
10. Stable sort preserves relative order of equal elements

COMPLEXITY QUICK REFERENCE:
---------------------------
- Comparison sort lower bound: Ω(n log n)
- Python built-in: O(n log n)
- Quick select: O(n) average, O(n²) worst
- Counting sort: O(n + k) where k = range
- Bucket sort: O(n + k) average
- K-way merge: O(n log k)
- Sort + two pointers: O(n log n) + O(n) = O(n log n)
"""