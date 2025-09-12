"""
Heap Complete Guide for LeetCode Problems
Based on problems: 215, 506, 703, 1046, 2231, 2558
"""

import heapq
from typing import List

# =============================================================================
# WHAT IS A HEAP?
# =============================================================================
"""
A heap is a binary tree data structure where:
- Parent node is always smaller (min-heap) or larger (max-heap) than children
- Tree is complete (filled left to right, level by level)
- Root contains the minimum (min-heap) or maximum (max-heap) element

Heap Visual Examples - 3 Levels Each

MIN-HEAP (parent <= children):
      1
     / \
    3   2
   / \ / \
  7  5 4  6

Array representation: [1, 3, 2, 7, 5, 4, 6]
- Root (1) is smallest element
- Parent at index i, children at 2i+1 and 2i+2
- 3 <= 7,5 and 2 <= 4,6 (heap property satisfied)
- Python's heapq implements min-heap by default

MAX-HEAP (parent >= children):
      10
     /  \
    8    9
   / \  / \
  4  6 5   3

Array representation: [10, 8, 9, 4, 6, 5, 3]
- Root (10) is largest element  
- 8 >= 4,6 and 9 >= 5,3 (heap property satisfied)
- Python heapq simulates this with negatives: [-10, -8, -9, -4, -6, -5, -3]

Key properties:
- O(log n) insertion and extraction
- O(1) access to min/max element
- Implemented as array for efficiency
"""

# =============================================================================
# BASIC HEAP OPERATIONS
# =============================================================================

def heap_operations_demo():
    """Basic heap operations using heapq"""
    
    # Create min-heap
    min_heap = []
    heapq.heappush(min_heap, 5)    # Add element
    heapq.heappush(min_heap, 2)
    heapq.heappush(min_heap, 8)
    print(f"Min-heap: {min_heap}")  # [2, 5, 8]
    
    # Extract minimum
    min_val = heapq.heappop(min_heap)
    print(f"Popped: {min_val}, Remaining: {min_heap}")
    
    # Convert list to heap
    nums = [4, 1, 7, 3]
    heapq.heapify(nums)  # O(n) operation
    print(f"Heapified: {nums}")
    
    # Simulate max-heap with negatives
    max_heap = []
    for val in [5, 2, 8]:
        heapq.heappush(max_heap, -val)  # Store negatives
    max_val = -heapq.heappop(max_heap)  # Negate when extracting
    print(f"Max value: {max_val}")

# =============================================================================
# COMMON HEAP PATTERNS
# =============================================================================

# Pattern 1: Find Kth Largest Element
def find_kth_largest(nums, k):  # LC 215
    """
    Problem: Find the kth largest element in unsorted array
    Approach: Use min-heap of size k to track k largest elements
    """

    heapq.heapify(nums) # convert array to min heap
    while len(nums) > k: 
        heapq.heappop(nums)  # Remove len(nums) - k ele's
    
    return nums[0]  # Root is kth largest

print(find_kth_largest([3,2,1,5,6,4], 2))
print(find_kth_largest([3,2,3,1,2,4,5,5,6], 4))

# Pattern 2: Streaming Kth Largest (Data Stream)
class KthLargest:  # LC 703
    """
    Problem: Maintain kth largest element as new values are added
    Approach: Keep min-heap of size k, root is always kth largest
    """
    
    def __init__(self, k, nums):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)  # Convert to heap
        
        # Keep only k largest elements
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
        
    def add(self, val):
        heapq.heappush(self.min_heap, val)  # Add new value
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)  # Remove smallest if size exceeds k
        return self.min_heap[0]  # Return kth largest

obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))

# Pattern 3: Simulation with Max-Heap
def last_stone_weight(stones):  # LC 1046
    """
    Problem: Simulate stone crushing - heaviest stones collide until one remains
    Approach: Use max-heap to always get two heaviest stones
    """
    # Convert to max-heap using negative values
    stones = [-s for s in stones]
    heapq.heapify(stones)
    
    while len(stones) > 1:
        first = heapq.heappop(stones)   # Heaviest stone (most negative)
        second = heapq.heappop(stones)  # Second heaviest
        
        # If stones have different weights, add difference back
        if second > first:  # Remember: we're using negatives
            heapq.heappush(stones, first - second)
    
    return abs(stones[0]) if stones else 0

# Pattern 4: Separate Heaps by Property
def largest_integer(num):  # LC 2231
    """
    Problem: Rearrange digits to get largest number, keeping odd/even positions
    Approach: Use separate heaps for odd and even digits
    """
    arr = [int(i) for i in str(num)]  # Convert to digit array
    odd_heap, even_heap = [], []      # Separate heaps for parity
    
    # Distribute digits into appropriate heaps
    for digit in arr:
        if digit % 2:  # Odd digit
            heapq.heappush(odd_heap, -digit)   # Max-heap for largest odd
        else:  # Even digit  
            heapq.heappush(even_heap, -digit)  # Max-heap for largest even
    
    # Reconstruct using largest available digit of same parity
    result = []
    for original_digit in arr:
        if original_digit % 2:  # Was odd
            result.append(-heapq.heappop(odd_heap))
        else:  # Was even
            result.append(-heapq.heappop(even_heap))
    
    return int("".join(map(str, result)))


# =============================================================================
# HEAP IMPLEMENTATION NUANCES
# =============================================================================
"""
PYTHON HEAPQ SPECIFICS:
- Only implements min-heap
- Use negative values for max-heap: heappush(-x), -heappop()
- heapify() is O(n), faster than n insertions
- Heap property: parent <= children, but siblings unordered

MAX-HEAP SIMULATION:
- Store negatives: [1,3,2] becomes [-1,-3,-2] 
- Extract with negation: -heappop() gives maximum
- Comparison logic reverses with negatives

COMMON MISTAKES:
- Forgetting to negate when extracting from max-heap
- Assuming heap is fully sorted (only root is guaranteed min/max)
- Not handling empty heap cases
"""

# =============================================================================
# WHEN TO USE HEAPS
# =============================================================================
"""
Use heaps when you need:
- Repeated access to min/max element
- Kth largest/smallest element
- Priority-based processing
- Streaming data with order requirements

Don't use heaps when:
- Need full sorting (just use sort())
- Random access to middle elements
- All elements need to be processed in order
"""

# =============================================================================
# TIME & SPACE COMPLEXITY
# =============================================================================
"""
TIME COMPLEXITY:
- heappush(): O(log n) - bubble up operation
- heappop(): O(log n) - bubble down operation  
- heapify(): O(n) - build heap from array
- peek (access root): O(1)

SPACE COMPLEXITY:
- O(n) for storing n elements
- O(1) additional space for operations

COMPARISON WITH ALTERNATIVES:
- Sorted array: O(n log n) to sort, O(1) to access min/max
- Heap: O(n) to build, O(log n) per operation
- Use heap when you don't need full sorting, just min/max access
"""

# =============================================================================
# PROBLEM-SPECIFIC INSIGHTS  
# =============================================================================
"""
FIND KTH LARGEST (LC 215):
- Min-heap of size k: root is kth largest
- Alternative: max-heap, pop k-1 times to get kth largest

RANKING PROBLEMS (LC 506):
- Store (score, original_index) to maintain position mapping
- Max-heap gives natural ordering for ranking

STREAMING KTH LARGEST (LC 703):
- Maintain invariant: heap size ≤ k
- Root always contains kth largest seen so far

SIMULATION PROBLEMS (LC 1046, 2558):
- Max-heap for "take largest" operations
- Process until termination condition

DIGIT REARRANGEMENT (LC 2231):  
- Separate heaps maintain largest available digit of each type
- Reconstruct following original pattern
"""

# =============================================================================
# KEY TAKEAWAYS FOR INTERVIEWS
# =============================================================================
"""
1. Know when problem needs repeated min/max access
2. Master max-heap simulation with negatives  
3. Use heapify() for O(n) heap construction
4. Consider maintaining heap invariants (like size k)
5. Handle edge cases: empty heap, single element
6. Remember: heap gives min/max, not full sorting
7. For kth largest: min-heap of size k is often optimal
"""
