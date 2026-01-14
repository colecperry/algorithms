"""
=================================================================
HEAP/PRIORITY QUEUE COMPLETE GUIDE
=================================================================

WHAT IS A HEAP?
--------------
A heap is a complete binary tree data structure that maintains a specific ordering property:
- Min Heap: Parent node is always smaller than or equal to children
- Max Heap: Parent node is always greater than or equal to children
- Root contains the minimum (min heap) or maximum (max heap) element
- NOT fully sorted - only root is guaranteed to be min/max

Array representation (zero-indexed):
- Parent of node at index i: (i - 1) // 2
- Left child of node at index i: 2 * i + 1
- Right child of node at index i: 2 * i + 2

Example Min Heap:
      1
     / \
    3   2
   / \ / \
  7  5 4  6

Array: [1, 3, 2, 7, 5, 4, 6]

Heap Properties:
- Insert: O(log n) - add to end, bubble up
- Remove min/max: O(log n) - move last element to the root, sink down
- Peek min/max: O(1) - just check root
- Heapify: O(n) - convert unsorted array to heap -> start at first non leaf node and sink it down until heap property satisfied (node smaller than both children)

When to use Heap:
- Need repeated access to min/max element
- Priority queue operations
- Top k elements problems
- K-way merge problems

HEAP CORE TEMPLATES
===================
"""

from typing import List, Optional
import heapq
from collections import Counter

# ================================================================
# MIN HEAP TEMPLATE (Python heapq) -> python implements a MIN HEAP by default
# ================================================================
def min_heap_template():
    """
    Template for min heap operations using Python's heapq
    
    TC: Insert O(log n), Remove O(log n), Peek O(1), Heapify O(n)
    SC: O(n) for heap storage
    
    WHEN TO USE:
    - Need to repeatedly access smallest element
    - Priority queue with ascending priority
    - K smallest elements
    
    KEY OPERATIONS:
    - heappush(heap, item): Insert and bubble up
    - heappop(heap): Remove min and sink down
    - heap[0]: Peek at minimum (don't pop)
    - heapify(list): Convert list to heap in-place
    """
    heap = []
    
    # Insert elements
    heapq.heappush(heap, 5)
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 7)
    
    # Peek at minimum
    min_val = heap[0]  # 3
    
    # Remove minimum
    removed = heapq.heappop(heap)  # 3
    
    # Heapify an array
    arr = [9, 5, 6, 2, 3]
    heapq.heapify(arr)  # arr becomes valid min heap
    
    return heap

# ================================================================
# MAX HEAP TEMPLATE (Python 3.14+)
# ================================================================
def max_heap_template():
    """
    Template for max heap using Python 3.14+ native support
    
    TC: Insert O(log n), Remove O(log n), Peek O(1), Heapify O(n)
    SC: O(n) for heap storage
    
    WHEN TO USE:
    - Need to repeatedly access largest element
    - Priority queue with descending priority
    - K largest elements
    
    KEY OPERATIONS (Python 3.14+):
    - heappush_max(heap, item): Insert and bubble up
    - heappop_max(heap): Remove max and sink down
    - heap[0]: Peek at maximum (don't pop)
    - heapify_max(list): Convert list to max heap in-place
    
    NOTE: Requires Python 3.14 or later!
    For older versions, use negation approach (see below)
    """
    heap = []
    
    # Insert elements
    heapq.heappush_max(heap, 5)
    heapq.heappush_max(heap, 3)
    heapq.heappush_max(heap, 7)
    
    # Peek at maximum
    max_val = heap[0]  # 7 (no negation needed!)
    
    # Remove maximum
    removed = heapq.heappop_max(heap)  # 7
    
    # Heapify an array into max heap
    arr = [9, 5, 6, 2, 3]
    heapq.heapify_max(arr)  # arr becomes valid max heap
    
    return heap

# ================================================================
# MAX HEAP TEMPLATE (Legacy - Negation for Python < 3.14)
# ================================================================
def max_heap_legacy():
    """
    Legacy approach using negation for Python < 3.14
    
    USE THIS IF:
    - Python version < 3.14
    - LeetCode hasn't updated to 3.14 yet
    - Need backward compatibility
    """
    heap = []
    
    # Insert (negate when pushing)
    heapq.heappush(heap, -5)
    heapq.heappush(heap, -3)
    heapq.heappush(heap, -7)
    
    # Peek at maximum (negate to get original)
    max_val = -heap[0]  # 7
    
    # Remove maximum (negate result)
    removed = -heapq.heappop(heap)  # 7
    
    return heap

# ================================================================
# COMPARISON: MIN HEAP VS MAX HEAP
# ================================================================
"""
MIN HEAP (heapq default):
    heapq.heappush(heap, item)
    heapq.heappop(heap)
    heapq.heapify(heap)
    min_val = heap[0]

MAX HEAP (Python 3.14+):
    heapq.heappush_max(heap, item)
    heapq.heappop_max(heap)
    heapq.heapify_max(heap)
    max_val = heap[0]

MAX HEAP (Legacy - Python < 3.14):
    heapq.heappush(heap, -item)
    -heapq.heappop(heap)
    heapify with negated values
    max_val = -heap[0]
"""

# ================================================================
# FIXED SIZE HEAP TEMPLATE (Top K Pattern)
# ================================================================
def fixed_size_heap_template(nums, k):
    """
    Template for maintaining heap of size k
    
    TC: O(n log k) where n = total elements
    SC: O(k) for heap storage
    
    WHEN TO USE:
    - Find k largest/smallest elements
    - Top k frequent elements
    - K closest points
    
    KEY INSIGHT:
    - For k LARGEST: use MIN heap of size k
      Root is kth largest (smallest of the k largest)
    - For k SMALLEST: use MAX heap of size k
      Root is kth smallest (largest of the k smallest)
    """
    # For k LARGEST: use min heap
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap  # Contains k largest

    # For k SMALLEST: use max heap (Python 3.14+)
    heap = []
    for num in nums:
        heapq.heappush_max(heap, num)
        if len(heap) > k:
            heapq.heappop_max(heap)
    return heap  # Contains k smallest

# ================================================================
# TWO HEAPS TEMPLATE (Median Pattern)
# ================================================================
def two_heaps_template():
    """
    Template for balancing two heaps (Python 3.14+)
    
    TC: Insert O(log n), Get median O(1)
    SC: O(n) for both heaps
    
    WHEN TO USE:
    - Find median in stream
    - Balance left and right halves
    
    KEY INSIGHT:
    - Max heap stores smaller half (left side)
    - Min heap stores larger half (right side)
    - Keep heaps balanced: |size_diff| <= 1
    """
    max_heap = []  # Smaller half - now native max heap!
    min_heap = []  # Larger half
    
    def add_num(num):
        # Add to max heap first
        heapq.heappush_max(max_heap, num)
        
        # Balance: move largest from max to min
        heapq.heappush(min_heap, heapq.heappop_max(max_heap))
        
        # Keep max_heap size >= min_heap size
        if len(min_heap) > len(max_heap):
            heapq.heappush_max(max_heap, heapq.heappop(min_heap))
    
    def find_median():
        if len(max_heap) > len(min_heap):
            return max_heap[0]  # No negation needed!
        return (max_heap[0] + min_heap[0]) / 2
    
    return add_num, find_median
"""
HEAP PATTERNS
=============
"""

# ================================================================
# PATTERN 1: TOP K ELEMENTS (FIXED SIZE HEAP)
# PATTERN EXPLANATION: Maintain a heap of size k to efficiently track the k "best" elements.
# Key insight: 
    # - For k largest, use MIN heap of size k. Root is kth largest (smallest of the k largest). When heap exceeds k, remove the smallest
    # - For k smallest, use MAX heap - root is kth smallest (largest of the k smallest). This is more efficient than full sorting when k << n.
#
# TYPICAL STEPS:
# 1. Create empty heap
# 2. For each element:
#    - Add element to heap
#    - If heap size > k, remove root
# 3. Heap now contains k best elements
# 4. Extract elements from heap
#
# Applications: Top k frequent, k closest points, kth largest/smallest, top k scores.
# ================================================================

class TopKPattern:
    """
    Problem: Given an integer array nums and an integer k, return the k most frequent elements.

    Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
    
    TC: O(n log k) - n elements, each heap operation O(log k)
        - Count frequencies: O(n)
        - Process m unique elements: O(m log k)
        - Extract result: O(k)
        - Total: O(n + m log k) which simplifies to O(n log k)
    SC: O(n) - frequency map O(m), heap O(k), result O(k)
    
    How it works:
    1. Count frequency of each element
    2. Use MIN heap of size k (key = frequency)
    3. For each unique element:
       - Add (frequency, element) to heap
       - If heap size > k, remove minimum frequency
    4. Result: k most frequent elements remain in heap
    
    Why min heap for k LARGEST frequencies:
    - Root has smallest frequency among k most frequent
    - When new element arrives, compare with root
    - If new freq > root, remove root and add new
    - Heap maintains k highest frequencies
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: # LC 347
        # Count frequencies
        freq_map = Counter(nums)
        
        # Min heap of size k: (frequency, number)
        heap = []
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num)) # Heap sorted by freq
            if len(heap) > k: # Make heap size k
                heapq.heappop(heap)  # Remove lowest frequency
        
        # Extract the k elements -> unpack a tuple into freq and num and only keeps num
        return [num for freq, num in heap]

# Example:
# nums = [1,1,1,2,2,3], k = 2
#
# Frequencies: {1:3, 2:2, 3:1}
#
# Process 1 (freq=3): heap = [(3,1)]
# Process 2 (freq=2): heap = [(2,2), (3,1)]
# Process 3 (freq=1): heap = [(2,2), (3,1), (1,3)]
#   Heap size > 2, pop (1,3): heap = [(2,2), (3,1)]
#
# Result: [2, 1] (order may vary)
# Output: [1,2]

sol = TopKPattern()
print("Top 2 frequent:", sol.topKFrequent([1,1,1,2,2,3], 2))  # [1,2]
print("Top 1 frequent:", sol.topKFrequent([1], 1))  # [1]


# ================================================================
# PATTERN 2: K-WAY MERGE
# PATTERN EXPLANATION: Efficiently merge k sorted data structures into one sorted output.
# Use min heap to track the smallest unprocessed element from each source. Always extract
# minimum (guaranteed smallest across all sources), add to result, then push next element
# from same source. Heap maintains "frontier" of k candidates.
#
# TYPICAL STEPS:
# 1. Initialize heap with first element from each source
#    Store: (value, source_id, position_in_source)
# 2. While heap not empty:
#    - Extract minimum element
#    - Add to result
#    - Push next element from same source (if exists)
# 3. Result is fully merged sorted output
#
# Applications: Merge k sorted lists/arrays, smallest range, kth smallest in matrix.
# ================================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class KWayMergePattern:
    """
    Problem: Merge k sorted linked lists and return it as one sorted list.
    
    TC: O(N log k) where N = total elements across all lists, k = number of lists
        - Initialize heap: O(k log k) - add first node from each list
        - Process N elements: O(N log k) - each pop and push is O(log k)
        - Total: O(k log k + N log k) = O(N log k)
    SC: O(k) - heap stores at most k nodes (one from each list)
    
    How it works:
    1. Add first node from each list to min heap
       Tuple: (node_value, list_index, node_reference)
    2. Extract minimum node (smallest across all lists)
    3. Add to result linked list
    4. Push next node from same list into heap
    5. Repeat until heap empty
    
    Why heap size stays k:
    - Always have at most one element from each list in heap
    - Extract one, add one from same list
    - Heap represents current "frontier" across all lists
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: # LC 23
        heap = []
        
        # Step 1: Add first node from each list
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        
        # Dummy node for result list
        dummy = ListNode(0)
        current = dummy
        
        # Step 2: Extract min, add to result, push next from same list
        while heap:
            val, list_idx, node = heapq.heappop(heap)
            
            # Add to result list
            current.next = node
            current = current.next
            
            # Push next node from same list
            if node.next:
                heapq.heappush(heap, (node.next.val, list_idx, node.next))
        
        return dummy.next

# Example:
# lists = [[1,4,5], [1,3,4], [2,6]]
#
# Initial heap: [(1,0,L0), (1,1,L1), (2,2,L2)]
#   L0=list0, L1=list1, L2=list2
#
# Extract (1,0,L0): result=[1]
#   Push (4,0,L0): heap=[(1,1,L1), (2,2,L2), (4,0,L0)]
#
# Extract (1,1,L1): result=[1,1]
#   Push (3,1,L1): heap=[(2,2,L2), (3,1,L1), (4,0,L0)]
#
# Extract (2,2,L2): result=[1,1,2]
#   Push (6,2,L2): heap=[(3,1,L1), (4,0,L0), (6,2,L2)]
#
# Continue until heap empty...
# Final result: [1,1,2,3,4,4,5,6]

sol = KWayMergePattern()
# Create test lists
l1 = ListNode(1, ListNode(4, ListNode(5)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
l3 = ListNode(2, ListNode(6))
result = sol.mergeKLists([l1, l2, l3])
print("Merged k lists:", result)  # 1->1->2->3->4->4->5->6


# ================================================================
# PATTERN 3: TWO HEAPS (MEDIAN MAINTENANCE)
# PATTERN EXPLANATION: Balance two heaps to efficiently track median in a stream. Use max
# heap for smaller half (left) and min heap for larger half (right). Keep heaps balanced
# with size difference at most 1. Median is the root of larger heap (odd total) or average
# of both roots (even total). This allows O(1) median access with O(log n) insertions.
#
# TYPICAL STEPS:
# 1. Max heap (left) stores smaller half - negate values for heapq
# 2. Min heap (right) stores larger half
# 3. To add number:
#    - Add to max heap first
#    - Move largest from max to min (balance)
#    - If min larger, move smallest from min to max
# 4. To get median:
#    - If odd count: return root of larger heap
#    - If even count: return average of both roots
#
# Applications: Find median in stream, balance two halves, sliding window median.
# ================================================================

class TwoHeapsPattern:
    """
    Problem: Design a data structure that supports:
    - addNum(num): Add integer from stream to data structure
    - findMedian(): Return median of all elements so far
    
    TC: addNum O(log n), findMedian O(1)
    SC: O(n) for storing all elements in two heaps
    
    How it works:
    1. Max heap (left) has smaller half of numbers
    2. Min heap (right) has larger half of numbers
    3. Keep heaps balanced: |left_size - right_size| <= 1
    4. Median comes from root(s) of heaps
    
    Why it works:
    - Max heap root = largest of smaller half
    - Min heap root = smallest of larger half
    - These are the middle elements!
    - Balanced heaps ensure middle stays in O(1) reach
    
    Example with [1,2,3,4,5]:
    Left (max): [2,1]  Right (min): [3,4,5]
    Median = root of larger heap = 3
    """
    def __init__(self): # LC 295
        self.small = []  # Max heap (negate values)
        self.large = []  # Min heap
    
    def addNum(self, num: int) -> None:
        # Add to max heap (small half)
        heapq.heappush(self.small, -num)
        
        # Balance: move largest from small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # Keep small heap size >= large heap size
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
    
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0

# Example:
# Stream: [1, 2, 3]
#
# Add 1:
#   small = [-1], large = []
#   Move to large: small = [], large = [1]
#   Rebalance: small = [-1], large = []
#   Median = -small[0] = 1
#
# Add 2:
#   small = [-2, -1], large = []
#   Move to large: small = [-1], large = [2]
#   Sizes equal
#   Median = (-(-1) + 2) / 2 = 1.5
#
# Add 3:
#   small = [-2, -1], large = [2]
#   Move to large: small = [-1], large = [2, 3]
#   Rebalance: small = [-2, -1], large = [3]
#   Median = -small[0] = 2

sol = TwoHeapsPattern()
sol.addNum(1)
print("Median after [1]:", sol.findMedian())  # 1.0
sol.addNum(2)
print("Median after [1,2]:", sol.findMedian())  # 1.5
sol.addNum(3)
print("Median after [1,2,3]:", sol.findMedian())  # 2.0


# ================================================================
# PATTERN 4: INTERVAL/EVENT PROCESSING
# PATTERN EXPLANATION: Process time-based events efficiently using min heap to track active
# events. Sort events by start time, use heap to store end times of ongoing events. When
# processing new event, remove expired events (end time <= new start time) from heap. Heap
# size represents number of concurrent/overlapping events at any point.
#
# TYPICAL STEPS:
# 1. Sort events by start time (process chronologically)
# 2. Create min heap to track end times of active events
# 3. For each event:
#    - Remove expired events (heap top <= current start)
#    - Add current event's end time to heap
#    - Heap size = active events at this moment
# 4. Track maximum heap size seen
#
# Applications: Meeting rooms, resource allocation, CPU scheduling, capacity planning.
# ================================================================

class IntervalProcessingPattern:
    """
    Problem: Given array of meeting time intervals where intervals[i] = [start_i, end_i],
    return the minimum number of conference rooms required.
    
    TC: O(n log n) - sorting intervals + n heap operations (each O(log n))
    SC: O(n) - heap can store all n meeting end times in worst case
    
    How it works:
    1. Sort meetings by start time
    2. Use min heap to track end times of active meetings
    3. For each meeting:
       - Pop expired meetings (end <= current start)
       - Add current end time
       - Heap size = rooms needed now
    4. Max heap size = minimum rooms needed
    
    Why it works:
    - Heap always contains end times of currently active meetings
    - Heap size = number of overlapping meetings
    - Must have room for each overlapping meeting
    - Max concurrent meetings = minimum rooms needed
    """
    def minMeetingRooms(self, intervals: List[List[int]]) -> int: # LC 253
        if not intervals:
            return 0
        
        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        # Min heap tracks end times of active meetings
        heap = []
        max_rooms = 0
        
        for start, end in intervals:
            # Remove meetings that have ended
            while heap and heap[0] <= start:
                heapq.heappop(heap)
            
            # Add current meeting's end time
            heapq.heappush(heap, end)
            
            # Track maximum concurrent meetings
            max_rooms = max(max_rooms, len(heap))
        
        return max_rooms

# Example:
# intervals = [[0,30],[5,10],[15,20]]
#
# Sort by start: [[0,30],[5,10],[15,20]]
#
# Process [0,30]:
#   Heap empty, add 30: heap=[30]
#   max_rooms = 1
#
# Process [5,10]:
#   5 < 30, meeting ongoing
#   Add 10: heap=[10,30]
#   max_rooms = 2
#
# Process [15,20]:
#   15 > 10, remove 10: heap=[30]
#   Add 20: heap=[20,30]
#   max_rooms = 2 (stays 2)
#
# Timeline:
# 0    5    10   15   20   30
# |----M1------------------| Room 1
#      |--M2--|              Room 2
#                |-M3-|      Room 2 (reused)
#
# Maximum concurrent = 2
# Output: 2

sol = IntervalProcessingPattern()
print("Min rooms:", sol.minMeetingRooms([[0,30],[5,10],[15,20]]))  # 2
print("Min rooms:", sol.minMeetingRooms([[7,10],[2,4]]))  # 1


# ================================================================
# PATTERN 5: SIMULATION (EXTRACT-PROCESS-REINSERT)
# PATTERN EXPLANATION: Repeatedly extract max/min element, apply transformation, and reinsert
# the result. Use heap to efficiently get extremes for processing. Common in game simulations,
# resource reduction, or iterative transformations. Continue for k iterations or until condition met.
#
# TYPICAL STEPS:
# 1. Create heap from initial elements
# 2. For k iterations (or while condition holds):
#    - Extract max/min element
#    - Transform element (sqrt, divide, reduce, etc.)
#    - Reinsert transformed value (if non-zero)
# 3. Return final sum, count, or state
#
# Applications: Stone games, gift pile reduction, rope costs, last stone weight.
# ================================================================

class SimulationPattern:
    """
    Problem: Given array of integers 'gifts' and integer k. Every second, choose the pile
    with maximum gifts and take floor(sqrt(gifts)) from it, leaving the rest. Return total
    gifts remaining after k seconds.
    
    TC: O(n + k log n)
        - Initial heapify: O(n)
        - k iterations: O(k log n) - each pop/push is O(log n)
        - Final sum: O(n)
        - Total: O(n + k log n)
    SC: O(n) - heap stores all n piles
    
    How it works:
    1. Create max heap from gifts (negate for heapq)
    2. For k seconds:
       - Extract maximum pile
       - Take sqrt, leave remainder
       - Reinsert remainder into heap
    3. Sum remaining gifts
    
    Why heap:
    - Need to repeatedly find maximum pile
    - After transformation, need to reinsert efficiently
    - Heap gives O(log n) for both operations
    - Better than repeated sorting: O(k log n) vs O(k n log n)
    """
    def pickGifts(self, gifts: List[int], k: int) -> int: # LC 2558
        # Create max heap (negate values)
        heap = [-g for g in gifts]
        heapq.heapify(heap)
        
        for _ in range(k):
            if heap[0] == -1:  # If max is 1, no more reduction possible
                break
            
            # Extract max, take sqrt, reinsert
            max_pile = -heapq.heappop(heap)
            remaining = int(max_pile ** 0.5)
            heapq.heappush(heap, -remaining)
        
        # Return sum of remaining gifts (negate back to positive)
        return -sum(heap)

# Example:
# gifts = [25,64,9,4,100], k = 4
#
# Heap (negated): [-100,-64,-25,-9,-4]
#
# Second 1: Extract 100
#   sqrt(100) = 10, reinsert 10
#   Heap: [-64,-25,-10,-9,-4]
#
# Second 2: Extract 64
#   sqrt(64) = 8, reinsert 8
#   Heap: [-25,-10,-9,-8,-4]
#
# Second 3: Extract 25
#   sqrt(25) = 5, reinsert 5
#   Heap: [-10,-9,-8,-5,-4]
#
# Second 4: Extract 10
#   sqrt(10) = 3, reinsert 3
#   Heap: [-9,-8,-5,-4,-3]
#
# Final sum: 9+8+5+4+3 = 29
# Output: 29

sol = SimulationPattern()
print("Gifts remaining:", sol.pickGifts([25,64,9,4,100], 4))  # 29
print("Gifts remaining:", sol.pickGifts([1,1,1,1], 4))  # 4


# ================================================================
# PATTERN 6: HEAP + GREEDY
# PATTERN EXPLANATION: Combine heap with greedy strategy to make locally optimal choices
# based on priority. Heap maintains candidates sorted by priority, greedy algorithm always
# picks best available option. Common in scheduling, resource allocation, and optimization
# problems where order of selection matters.
#
# TYPICAL STEPS:
# 1. Sort items by one criterion (e.g., deadline, start time)
# 2. Use heap to track priorities dynamically
# 3. Greedily select from heap based on priority
# 4. Update heap as you process elements
# 5. Continue until goal met or heap empty
#
# Applications: Task scheduling with deadlines, maximize value within constraints.
# ================================================================

class HeapGreedyPattern:
    """
    Problem: Given array of integers 'stones', in each turn we choose the two heaviest stones
    and smash them together. If stones have weights x and y with x <= y:
    - If x == y, both stones destroyed
    - If x != y, stone of weight x destroyed, stone of weight y-x remains
    Return weight of last remaining stone, or 0 if none remain.
    
    TC: O(n log n) - heapify O(n), each operation O(log n), up to n operations
    SC: O(n) - heap stores stones
    
    How it works:
    1. Create max heap of all stones
    2. Greedily pick two heaviest stones
    3. Smash them: keep difference
    4. Reinsert difference into heap
    5. Continue until 0 or 1 stone remains
    
    Why greedy works:
    - Smashing heaviest stones reduces total weight most
    - Difference is smaller, gives more options later
    - Heap ensures we always get two heaviest efficiently
    """
    def lastStoneWeight(self, stones: List[int]) -> int: # LC 1046
        # Create max heap (negate for heapq)
        heap = [-s for s in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            # Extract two heaviest stones
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            
            # If different weights, keep difference
            if first != second:
                heapq.heappush(heap, -(first - second))
        
        # Return last stone weight or 0
        return -heap[0] if heap else 0

# Example:
# stones = [2,7,4,1,8,1]
#
# Heap (negated): [-8,-7,-4,-2,-1,-1]
#
# Smash 8 and 7: difference = 1
#   Heap: [-4,-2,-1,-1,-1]
#
# Smash 4 and 2: difference = 2
#   Heap: [-2,-1,-1,-1]
#
# Smash 2 and 1: difference = 1
#   Heap: [-1,-1,-1]
#
# Smash 1 and 1: both destroyed
#   Heap: [-1]
#
# Last stone: 1
# Output: 1

sol = HeapGreedyPattern()
print("Last stone weight:", sol.lastStoneWeight([2,7,4,1,8,1]))  # 1
print("Last stone weight:", sol.lastStoneWeight([1]))  # 1