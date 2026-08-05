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
- Heappush: O(log n) - add element to end of heap, bubble up to correct pos
- Heappop: O(log n) - move last element to the root (swap with root), sink down root to correct pos
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
    
    KEY OPERATIONS:
    - heappush(heap, item): Insert and bubble up - O(log n)
    - heappop(heap): Remove min and sink down - O(log n)
    - heap[0]: Peek at minimum (don't pop) - O(1)
    - heapify(list): Convert list to heap in-place - O(n)
    """
    heap = []
    
    # Insert elements
    heapq.heappush(heap, 5)
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 7)
    
    # Peek at minimum
    min_val = heap[0]  # 3
    
    # Remove minimum (root)
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
    Template for max heap using Python 3.14+ native support for max heaps (heapq.heappush_max, heapq.heappop_max, heapq.heapify_max)
    
    TC: Insert O(log n), Remove O(log n), Peek O(1), Heapify O(n)
    SC: O(n) for heap storage
    
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

    # Remember heapq uses a min heap, so the smallest (most negative) value is the maximum of the original values -> [-7, -5, -3]
    
    # Peek at maximum (negate to get original)
    max_val = -heap[0]  # 7
    
    # Remove maximum (negate result)
    removed = -heapq.heappop(heap)  # 7
    
    return heap

"""
=================================================================
HEAP/PRIORITY QUEUE PATTERNS
=================================================================

CORE CONCEPTS:
- Min Heap: root is always the smallest element
- Max Heap: root is always the largest element
- Python's heapq is a MIN HEAP by default
- For max heap: negate values on push, negate again on pop
- heappush / heappop: O(log n) | peek via heap[0]: O(1) | heapify: O(n)

WHEN TO USE A HEAP:
- Need repeated access to min/max element
- Priority queue operations
- Top K elements
- Merging sorted sources
- Scheduling / interval problems
=================================================================
"""

from typing import List, Optional
import heapq
from collections import Counter

"""
HEAP COMPLEXITY REFERENCE
==========================

+--------------------------+------------+-------+
| Pattern                  | Time       | Space |
+--------------------------+------------+-------+
| Top K Elements           | O(n log k) | O(n)  |
| K-Way Merge              | O(n log k) | O(k)  |
| Greedy + Heap            | O(n log n) | O(n)  |
| Active Interval Tracking | O(n log n) | O(n)  |
+--------------------------+------------+-------+

n = total number of elements/nodes processed, k = heap size cap (Top K Elements) or
number of sources being merged (K-Way Merge)

WHAT EACH PATTERN IS:
- Top K Elements: keep a small heap of just the k best candidates seen so far, tossing
  out the weakest one whenever there are too many, so you never have to sort everything.
- K-Way Merge: repeatedly grab the smallest item across several already-sorted sources
  by keeping one candidate per source in a heap, pulling in that source's next item
  each time you take one out.
- Greedy + Heap: repeatedly pull out the best (biggest or smallest) item, do something
  with it, and put the result back in, so you're always acting on the most extreme
  item first.
- Active Interval Tracking: track how many intervals are open at the same time by
  keeping the end times of currently running intervals in a heap, dropping any that
  have already finished before adding a new one.

NOTES:
- Top K Elements: n elements each pushed/popped on a heap capped at size k -> O(log k)
  per op, O(n log k) total; frequency map is O(n), heap is O(k) (bounded by n overall)
- K-Way Merge: heap never holds more than one node per source (k sources) -> O(log k)
  per push/pop; n total nodes each enter/exit the heap once -> O(n log k); SC O(k)
- Greedy + Heap: heapify is O(n), then up to n pop+push operations each O(log n) ->
  O(n log n); heap stores up to n elements -> O(n) space
- Active Interval Tracking: sorting is O(n log n); each interval is pushed/popped from
  the heap at most once at O(log n) per op -> O(n log n) total; heap holds up to n
  end times -> O(n) space
"""

"""
================================================================
PATTERN 1: TOP K ELEMENTS
PATTERN EXPLANATION: Maintain a heap of size k to track the k "best" elements without
sorting the entire input.

To find k LARGEST: use a MIN heap of size k
  - Root = smallest of your k candidates (weakest survivor)
  - When heap exceeds k, pop root → evicts smallest, retains large values
  - k=3 largest from [1,2,3,4,5]:
    [1,2,3] → push 4, pop 1 → [2,3,4] → push 5, pop 2 → [3,4,5] ✓

To find k SMALLEST: use a MAX heap of size k (negate on push, negate on pop)
  - Root = largest of your k candidates (weakest survivor)
  - When heap exceeds k, pop root → evicts largest, retains small values
  - k=3 smallest from [5,4,3,2,1] (stored negated):
    [-5,-4,-3] → push -2, pop -5 → [-4,-3,-2] → push -1, pop -4 → [-3,-2,-1] → [3,2,1] ✓

Applications: Kth largest/smallest, k most frequent elements, k closest points to origin.
================================================================
"""

class TopKPattern:
    """
    Giveaway: "return the k most frequent elements" — needing just the top k by
    frequency (not a full ranking) out of a large unsorted collection is the
    classic signal for a size-capped heap that evicts its weakest member,
    instead of sorting all n frequencies.

    Problem: Given an integer array nums and integer k, return the k most frequent elements.

    Example:
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1, 2]

        Frequencies: {1:3, 2:2, 3:1}
        We want the 2 elements with highest frequency -> 1 and 2

    Steps:
    1. Create empty heap
    2. For each element:
       a. Push element onto heap
       b. If heap size exceeds k, pop root (evicts weakest candidate)
    3. Heap now contains the k best elements
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  # LC 347
        """
        - TC: O(n log k) — count frequencies O(n), push/pop on heap of size k O(log k) per element
        - SC: O(n) — frequency map O(n), heap O(k)
        """
        freq_map = Counter(nums) # Count frequencies

        heap = []
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num)) # Push (freq, num) onto min heap -> heapq uses first element of tuple for ordering
            if len(heap) > k:
                heapq.heappop(heap)  # Evict lowest frequency element if we have more than k candidates   

        return [num for freq, num in heap] # unpacks the tuple and returns only the numbers

# Example trace:
# nums = [1,1,1,2,2,3], k = 2
#
# freq_map = {1:3, 2:2, 3:1}
#
# Process (3, 1): heap = [(3,1)]
# Process (2, 2): heap = [(2,2), (3,1)]
# Process (1, 3): heap = [(1,3), (3,1), (2,2)]  size > k, pop (1,3)
#                 heap = [(2,2), (3,1)]
#
# Result: [2, 1]

sol = TopKPattern()
print("Top K Frequent:", sol.topKFrequent([1,1,1,2,2,3], 2))  # [1, 2]
print("Top K Frequent:", sol.topKFrequent([1], 1))             # [1]

"""
================================================================
PATTERN 2: K-WAY MERGE
PATTERN EXPLANATION: Efficiently merge k sorted data sources into one sorted output. Use a min heap to track the smallest unprocessed element across all sources. Always extract the global minimum (guaranteed by heap), add to result, then push the next element from that same source. Heap maintains the "frontier" — one candidate per source.

Applications: Merge k sorted lists/arrays, kth smallest in sorted matrix.
================================================================
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class KWayMergePattern: # LC 23
    """
    Giveaway: "merge k sorted linked lists... return as one sorted list" — you
    already have k independently-sorted streams and need the global minimum
    across all of them repeatedly, which is the tell for keeping one candidate
    per list in a min heap rather than concatenating and re-sorting everything.

    Problem: Merge k sorted linked lists and return as one sorted list.

    Example:
        Input: lists = [[1,4,5], [1,3,4], [2,6]]
        Output: [1,1,2,3,4,4,5,6]

        Merge three sorted lists into one sorted list.

    Steps:
    1. Initialize heap with first element from each source
       Store: (value, source_id, node) — source_id breaks ties since ListNode isn't comparable
    2. While heap not empty:
       a. Extract minimum node, append to result
       b. Push that node's next into the heap (if exists)
    3. Result is fully merged and sorted
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:  # LC 23
        """
        - TC: O(n log k)
            - O(n) - while loop runs N times total - once per node across all lists
            - O(log k) per heappush/heappop operation - after each push or pop the heap has to reorder itself to maintain the heap property which is log(heap size), the heap size is at most k since we only ever have one node from each list in the heap at a time
            - Total: O(n log k) where n is total number of nodes across all lists
        - SC: O(k) — heap holds at most one node per list - heap starts with k nodes and shrinks as lists are exhausted, but never exceeds k
        """
        heap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))  # (head.val, i, head) -> value for ordering, i to break ties, head for reference so we can access next node)

        dummy = ListNode(0) # Dummy head for result list
        current = dummy # Pointer to build result list

        while heap:
            val, list_idx, node = heapq.heappop(heap) # Get smallest node
            current.next = node # Append node to result list
            current = current.next # Move pointer forward
            if node.next: # Push next node from same list into heap
                heapq.heappush(heap, (node.next.val, list_idx, node.next))

        return dummy.next

# Example trace:
# lists = [[1,4,5], [1,3,4], [2,6]]
#
# Initial heap: [(1,0,L0→4→5), (1,1,L1→3→4), (2,2,L2→6)]
#
# Pop (1,0): result=[1], push (4,0): heap=[(1,1), (2,2), (4,0)]
# Pop (1,1): result=[1,1], push (3,1): heap=[(2,2), (3,1), (4,0)]
# Pop (2,2): result=[1,1,2], push (6,2): heap=[(3,1), (4,0), (6,2)]
# Pop (3,1): result=[1,1,2,3], push (4,1): heap=[(4,0), (4,1), (6,2)]
# Pop (4,0): result=[1,1,2,3,4], push (5,0): heap=[(4,1), (5,0), (6,2)]
# Pop (4,1): result=[1,1,2,3,4,4], no next: heap=[(5,0), (6,2)]
# Pop (5,0): result=[1,1,2,3,4,4,5], no next: heap=[(6,2)]
# Pop (6,2): result=[1,1,2,3,4,4,5,6], no next: heap=[]
#
# Output: 1->1->2->3->4->4->5->6

l1 = ListNode(1, ListNode(4, ListNode(5)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
l3 = ListNode(2, ListNode(6))
sol = KWayMergePattern()
print("Merged K Lists:", sol.mergeKLists([l1, l2, l3]))  # 1->1->2->3->4->4->5->6

"""
================================================================
PATTERN 3: GREEDY + HEAP
PATTERN EXPLANATION: Combine a heap with a greedy strategy to make locally optimal choices based on a dynamic priority. The heap keeps candidates sorted so we always act on the best available option. Often involves: extract max/min, apply a transformation, reinsert the result, and repeat. The greedy choice is valid because acting on extremes first either minimizes/maximizes the outcome or satisfies a constraint optimally.

Applications: Last stone weight, task scheduler, pick gifts, IPO, reorganize string.
================================================================
"""

class GreedyHeapPattern:
    """
    Giveaway: "each turn smash the two heaviest stones together" — the problem
    itself defines the operation as repeatedly acting on the current two
    largest values and feeding a new value back in, which is exactly what a max
    heap (extract-extract-reinsert) is built for, as opposed to sorting once
    up front.

    Problem: Given array 'stones', each turn smash the two heaviest stones together.
    If weights x <= y: both destroyed if equal, else stone of weight y-x remains.
    Return weight of last remaining stone, or 0 if none remain.

    Example:
        Input: stones = [2,7,4,1,8,1]
        Output: 1

        Smash 8,7 -> 1 remains. Smash 4,2 -> 2 remains.
        Smash 2,1 -> 1 remains. Smash 1,1 -> both destroyed.
        Last stone: 1

    Steps:
    1. Build max heap from all stones
    2. While heap has more than 1 stone:
       a. Pop two heaviest stones
       b. If unequal, push the difference back
    3. Return last stone or 0 if none remain
    """
    def lastStoneWeight(self, stones: List[int]) -> int:  # LC 1046
        """
        - TC: O(n log n) — heapify O(n), up to n smash operations each O(log n)
        - SC: O(n) — heap stores all stones
        """
        heap = [-s for s in stones] # Negate to use min heap as max heap
        heapq.heapify(heap) # O(n) to build heap

        while len(heap) > 1: 
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if first != second:
                heapq.heappush(heap, -(first - second)) # Push difference back if not zero

        return -heap[0] if heap else 0 # Return last stone weight or 0 if none remain

# Example trace:
# stones = [2,7,4,1,8,1]
# heap (negated) = [-8,-7,-4,-2,-1,-1]
#
# Pop 8, 7: diff=1, push -1 -> heap=[-4,-2,-1,-1,-1]
# Pop 4, 2: diff=2, push -2 -> heap=[-2,-1,-1,-1]
# Pop 2, 1: diff=1, push -1 -> heap=[-1,-1,-1]
# Pop 1, 1: equal, nothing pushed -> heap=[-1]
#
# Output: 1

sol = GreedyHeapPattern()
print("Last Stone Weight:", sol.lastStoneWeight([2,7,4,1,8,1]))  # 1
print("Last Stone Weight:", sol.lastStoneWeight([1]))             # 1

"""
================================================================
PATTERN 4: ACTIVE INTERVAL TRACKING
PATTERN EXPLANATION: Used when you need to know how many intervals are overlapping at once. Sort by start time, then use a min heap to store end times of active intervals. For each new interval, evict any that have already ended (heap[0] <= current start), then add the new end time. Heap size = number of currently overlapping intervals.

Applications: Meeting rooms, car pooling, minimum platforms, CPU scheduling.
================================================================
"""

class IntervalPattern:
    """
    Giveaway: "return minimum conference rooms required" for a list of meeting
    intervals — needing the maximum number of intervals overlapping AT THE SAME
    TIME (not just whether any overlap) is the tell for tracking active end
    times in a heap so you can cheaply evict any meeting that's already
    finished before adding a new one.

    Problem: Given meeting intervals [start, end], return minimum conference rooms required.

    Example:
        Input: intervals = [[0,30],[5,10],[15,20]]
        Output: 2

        [0,30] overlaps with [5,10] -> need 2 rooms.
        [15,20] starts after [5,10] ends -> reuses that room.
        Max concurrent = 2.

    Steps:
    1. Sort intervals by start time
    2. For each interval:
       a. Pop all expired end times (heap[0] <= current start)
       b. Push current end time
    3. Track max heap size — that's the minimum rooms needed
    """
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:  # LC 253
        """
        - TC: O(n log n) — sorting O(n log n), n heap operations O(log n) each
        - SC: O(n) — heap can hold all n end times in worst case
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])

        heap = [] # min heap tracks end times of curr meetings
        max_rooms = 0 # max concurrent meetings at any time

        for start, end in intervals:
            while heap and heap[0] <= start: # if curr meeting starts after earliest ending meeting
                heapq.heappop(heap) # Free that room
            heapq.heappush(heap, end)
            max_rooms = max(max_rooms, len(heap))

        return max_rooms

# Example trace:
# intervals = [[0,30],[5,10],[15,20]]  (already sorted by start)
#
# Process [0,30]:  heap=[], push 30  -> heap=[30], max_rooms=1
# Process [5,10]:  heap[0]=30 > 5, push 10 -> heap=[10,30], max_rooms=2
# Process [15,20]: heap[0]=10 <= 15, pop 10 -> heap=[30]
#                  push 20 -> heap=[20,30], max_rooms=2 (unchanged)
#
# Output: 2

sol = IntervalPattern()
print("Min Meeting Rooms:", sol.minMeetingRooms([[0,30],[5,10],[15,20]]))  # 2
print("Min Meeting Rooms:", sol.minMeetingRooms([[7,10],[2,4]]))           # 1
