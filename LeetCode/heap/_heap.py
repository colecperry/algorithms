import heapq
from typing import List
from collections import Counter
from math import sqrt

# =============================================================================
# WHAT IS A HEAP?
# =============================================================================
"""
A heap is a binary tree data structure where:
- Parent node is always smaller (min-heap) or larger (max-heap) than children
- Tree is complete (filled left to right, level by level)
- Root contains the minimum (min-heap) or maximum (max-heap) element
- Heap is not fully sorted -> only root is guaranteed min/max
- Array Based Storage - We store heaps in arrays/lists, not with node ptrs
- Index relationships: For any node at index 'i':
    - Left child: 2 * i + 1
    - Right child: 2 * i + 2
    - Parent: (i - 1) // 2

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
- Python heapq default min heap simulates this with negatives: [-10, -8, -9, -4, -6, -5, -3]

## Example with Key Operations

### Max Heap Example:

Initial array: [95, 75, 80, 55, 60, 50, 65]

Visual representation:
        95
       /  \
      75   80
     / \   / \
    55 60 50 65

"""

# =============================================================================
# HEAP ADVANTAGES
# =============================================================================
"""
- Heaps provide O(1) access to min/max + O(log n) insert/delete.
- Perfect for: repeated access to extremes, priority queues, top k problems.
- Better than sorting when data changes frequently.

    Operation       | Heap     | Sorted Array | Unsorted Array
    ----------------|----------|--------------|----------------
    Find min/max    | O(1)     | O(1)         | O(n)
    Insert          | O(log n) | O(n)         | O(1)
    Remove min/max  | O(log n) | O(n)         | O(n)

"""

# =============================================================================
# KEY OPERATIONS
# =============================================================================
"""
1. **Insert(90)**: Add to end, then "bubble up" ele to correct level by comparing to parent
    - Add 90 to end: [95, 75, 80, 55, 60, 50, 65, 90]
    - Compare with parent (75): 90 > 75, swap
    - Compare with parent (95): 90 < 95, stop
    - Result: [95, 90, 80, 75, 60, 50, 65, 55]

2. **Remove()**: Remove root, move last ele to root, then "sink down" by comparing to children
    - Remove 95, move 65 to root: [65, 75, 80, 55, 60, 50]
    - Compare 65 with children (75, 80): 80 is largest, swap
    - Compare 65 with children (50): 65 > 50, stop
    - Result: [80, 75, 65, 55, 60, 50]

3. **Heapify**: Convert unsorted array into valid heap
    - Start from last non-leaf node, sink down each element
    - Works bottom-up to ensure heap property
"""

# =============================================================================
# TIME COMPLEXITY
# =============================================================================
"""
| Operation                  | Time Complexity | Explanation                           |
|----------------------------|-----------------|---------------------------------------|
| Insert                     | O(log n)        | Insert node at the bottom and bubble up at most the height of tree  |
| Remove (extract max/min)   | O(log n)        | Swap last node with root & sink down at most the height of tree  |
| Peek (get max/min)         | O(1)            | Just return first element             |
| Heapify                    | O(n)            | Converts unsorted array to valid heap by working bottom up from last parent to the root (leaf nodes cannot voilate heap property) |
| Search                     | O(n)            | Must check all elements   
"""

# =============================================================================
# WHEN TO USE HEAPS
# =============================================================================

# When heaps shine:
    # Dynamic data - Elements constantly being added/removed
    # Priority matters - Always need the "best" element
    # Don't need full sorting - Only care about extremes, not complete order

# Real-world use cases:
    # Task scheduling: Always grab highest priority task
    # Event simulation: Always process next event in time order
    # Top K problems: Maintain k best elements efficiently
    # Streaming data: Handle continuous input, always know current min/max

# ============================================================================
# CORE TEMPLATE 1: MIN HEAP IMPLEMENTATION WITHOUT HEAPQ LIBRARY
# ============================================================================

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def left_child(self, index):
        return 2 * index + 1
    
    def right_child(self, index):
        return 2 * index + 2
    
    def parent(self, index):
        return (index - 1) // 2
    
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    # Insert: Add element and bubble up
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        
        # Bubble up: swap with parent if current is SMALLER
        while current > 0 and self.heap[current] < self.heap[self.parent(current)]: # Max heap uses >
            self.swap(current, self.parent(current))
            current = self.parent(current)
    
    # Remove: Extract min element (root)
    def remove(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop() # Moving last ele to first index removes min
        self.sink_down(0) # Then sink it down to correct place
        return min_value
    
    # Sink down: Move element down to correct position
    def sink_down(self, index):
        min_index = index # Track smallest pos between curr and children
        
        while True:
            left_index = self.left_child(index) # Get children indexes
            right_index = self.right_child(index)
            
            # Check if left child exists and is SMALLER
            if left_index < len(self.heap) and self.heap[left_index] < self.heap[min_index]: # Max heap uses >
                min_index = left_index
            
            # Check if right child exists and is SMALLER
            if right_index < len(self.heap) and self.heap[right_index] < self.heap[min_index]: # Max heap >
                min_index = right_index
            
            # If min_index changed, swap and continue
            if min_index != index:
                self.swap(index, min_index)
                index = min_index # Update idx of node we're sinking down & continue
            else:
                return 
    
    # Peek: Get min without removing
    def peek(self):
        return self.heap[0] if self.heap else None
    
    # Heapify: Convert unsorted array to valid heap
    def heapify(self, arr):
        self.heap = arr
        # Work from bottom to top b/c sink down assumes children are valid heaps
        for i in range(len(self.heap) // 2 - 1, -1, -1): # (len // 2 - 1) gives us last parent node (last node that has children) and works backwards to the root
            self.sink_down(i)


# Create and build min heap
min_heap = MinHeap()
values = [50, 30, 40, 10, 20, 35, 25]

# Insert
for val in values:
    min_heap.insert(val)

# Peek at min
print(f"\nPeek (min value): {min_heap.peek()}")

# Remove operations
print(f"\nRemove min: {min_heap.remove()}")
print(f"\nRemove min: {min_heap.remove()}")

# Heapify an unsorted array
unsorted = [3, 9, 2, 1, 4, 5]
min_heap_heapify = MinHeap()

min_heap_heapify.heapify(unsorted.copy())

# ============================================================================
# CORE TEMPLATE 2: MIN HEAP IMPLEMENTATION USING PYTHON'S HEAPQ LIBRARY (LEETCODE STANDARD)
# ============================================================================
"""
Python's heapq library implements a MIN HEAP by default.
All operations work on regular Python lists.

Key functions:
- heapq.heappush(heap, item)      # Insert item, O(log n)
- heapq.heappop(heap)             # Remove and return smallest, O(log n) 
- heapq.heapify(list)             # Convert list to heap in-place, O(n)
- heap[0]                         # Peek at smallest (don't use heapq function), O(1)
- heapq.heappushpop(heap, item)   # Push then pop, O(log n)
- heapq.heapreplace(heap, item)   # Pop then push, O(log n)

PYTHON HEAPQ SPECIFICS:
- Only implements min-heap
- Use negative values for max-heap: heappush(-x), -heappop()
- heapify() is O(n), faster than n insertions
- Heap property: parent <= children, but siblings unordered
"""

# ============================================================================
# MIN HEAP EXAMPLES
# ============================================================================

# Create empty min heap (just a regular list)
min_heap = []

# Insert elements
values = [50, 30, 40, 10, 20, 35, 25]
for val in values:
    heapq.heappush(min_heap, val) # heappush inserts an item to end of the list & bubbles it up

# Peek at minimum (just access index 0)
min_val = min_heap[0]

# Remove minimum
removed = heapq.heappop(min_heap) # heappop removes root (min or max) by swapping with last node and sinking down last node to correct spot

# Insert new value and bubble it up to correct place
heapq.heappush(min_heap, 15)

# ============================================================================
# HEAPIFY EXAMPLE
# ============================================================================

# Convert unsorted list to heap in-place
unsorted = [3, 9, 2, 1, 4, 5]
heapq.heapify(unsorted) # Heapifies the whole list

# ============================================================================
# MAX HEAP WORKAROUND (Negate values)
# ============================================================================

"""
heapq only supports min heap, so for max heap:
1. Negate values when inserting: push(-value)
2. Negate values when removing: -pop()
"""

max_heap = []
values = [95, 75, 80, 55, 60, 50, 65]

for val in values:
    heapq.heappush(max_heap, -val)  # Negate to simulate max heap

# Peek at maximum (negate the first element so it's not negative)
max_val = -max_heap[0]

# Remove maximum (negate the popped value)
removed_max = -heapq.heappop(max_heap)

# =============================================================================
                        # COMMON HEAP PATTERNS
# =============================================================================

# ================================================================
# PATTERN 1: TOP K ELEMENTS (Heap of Size K)
# PATTERN EXPLANATION: Maintain a min heap of size k to track the k "best" elements.
# Key insight: 
#   - For k LARGEST: Use MIN heap of size k
#     → Root is kth largest (smallest of the k largest)
#     → Remove smallest when heap > k
#   - For k SMALLEST: Use MAX heap of size k (negate values)
#     → Root is kth smallest (largest of the k smallest)
#     → Remove largest when heap > k
# Applications: Top k frequent, k closest points, kth largest/smallest
# Time Complexity: O(n log k) - better than sorting O(n log n) when k << n
# ================================================================

# PROBLEM 1A: LC 347 - Top K Frequent Elements
# Key Insight: Use min heap of size k with frequency as priority to maintain k most frequent

class TopKFrequent:
    '''
    Given an integer array nums and an integer k, return the k most frequent elements. 
    You may return the answer in any order.

    Ex. 1
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

    TC: 
        - Counting: O(n)
        - Iterating through freq dict: O(m) where m = unique elements
        - heappush() and heappop(): O(log k) for sink down/bubble up
        - Extracting result: O(k)
        - Total TC: O(n + m log k) → O(n log k)
    SC: 
        - Storing freq dict: O(m) where m = unique elements
        - Storing the heap: O(k)
        - Output list: O(k)
        - Total SC: O(m + k) → O(n) worst case
    '''
    def topKFrequent(self, nums, k):
        # Step 1: Count frequencies & create dict
        count = Counter(nums)
        
        # Step 2: Use min heap of size k (key = frequency)
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))  # Python compares by first ele in tuple
            if len(heap) > k:
                heapq.heappop(heap)  # Remove element with smallest frequency (root)
        
        # Step 3: Extract all k elements from heap
        return [num for freq, num in heap]  # Loop through tuples, unpack, only take num

sol = TopKFrequent()
print(sol.topKFrequent([1,1,1,2,2,3], 2))  # [1,2]
print(sol.topKFrequent([1], 1))  # [1]
print(sol.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))  # [1,2]


# PROBLEM 1B: LC 973 - K Closest Points to Origin
# Key Insight: Use max heap of size k with distance as priority to maintain k closest

class KClosest:
    '''
    Find the k closest points to the origin (0, 0) on a 2D plane.
    Distance from origin: sqrt(x² + y²)
    Return the k closest points in any order.

    Example:
    Input: points = [[1,3],[-2,2]], k = 1
    Output: [[-2,2]]
    Explanation: Distance (1,3) = sqrt(10) ≈ 3.16, distance (-2,2) = sqrt(8) ≈ 2.82
                    Since k=1, return the closest point

    TC:
        - heappush() → O(log k): Insert distance and coords, bubble up, heap size ≤ k
        - heappop() → O(log k): Remove root, sink down, heap size ≤ k
        - Loop n times → O(n log k)
        - Total: O(n log k)
    SC:
        - O(k) → heap stores at most k points
    '''
    def kClosest(self, points, k):
        max_heap = []  # Max heap of size k guarantees root is kth smallest distance
        
        for x, y in points:
            distance = sqrt((x ** 2) + (y ** 2))
            heapq.heappush(max_heap, (-distance, [x, y]))  # Negate for max heap
            if len(max_heap) > k:
                heapq.heappop(max_heap)  # Remove point with largest distance
        
        # Extract points (ignore distances)
        return [point for dist, point in max_heap]

sol = KClosest()
print(sol.kClosest([[1,3],[-2,2]], 1))  # [[-2,2]]
print(sol.kClosest([[3,3],[5,-1],[-2,4]], 2))  # [[3,3],[-2,4]]

# ================================================================
# PATTERN 2: SIMULATION with Repeated Max/Min Operations (Extract → Process → Re-insert)
# PATTERN EXPLANATION: Repeatedly extract the largest/smallest elements and process them.
# Key insight: Use heap to efficiently get extremes, simulate game/process, push results back.
# Applications: Stone games, gift reduction, task scheduling, rope connection cost.
# ================================================================

# PROBLEM 2: LC 2558 - Take Gifts From the Richest Pile
# Extract max, transform (sqrt), re-insert - continues for k iterations

class Simulation:
    '''
    # You are given an integer array gifts denoting the number of gifts in various piles and an integer k. Every second, you choose the pile with the maximum number of gifts and take the floor of the square root of the gifts in that pile, leaving the rest behind. Return the number of gifts remaining after k seconds.

    # Example:
    # Input: gifts = [25,64,9,4,100], k = 4
    # Output: 29
    # Explanation: 
    # Second 1: Choose pile with 100 gifts, take sqrt(100) = 10, leave 10 gifts
    # Second 2: Choose pile with 64 gifts, take sqrt(64) = 8, leave 8 gifts  
    # Second 3: Choose pile with 25 gifts, take sqrt(25) = 5, leave 5 gifts
    # Second 4: Choose pile with 10 gifts, take sqrt(10) = 3, leave 3 gifts
    # Remaining gifts: 3 + 8 + 5 + 4 + 9 = 29

    # TC:
    #     - Initial heapify -> O(n)
    #     - heappop() -> O(log n): Remove root (largest value), sink down
    #     - heappush() -> O(log n): Insert negative value (max heap simulation), bubble up
    #     - Loop k times -> O(k log n)
    #     - Total -> O(n + k log n)
    # SC:
    #     - O(n) -> heap stores all n piles
    '''
    def pickGifts(self, gifts, k):
        gifts = [-g for g in gifts]  # Max heap using negatives
        heapq.heapify(gifts) # Heapify the arr
        
        for _ in range(k):
            if gifts[0] == -1:  # If the pile gets to 1, we do nothing 
                break
            val = heapq.heappop(gifts) # Pop off the root
            val = (int(abs(val) ** 0.5)) * -1  # Take the square root (keep it negative)
            heapq.heappush(gifts, val) # Push the val back onto the heap
        
        return abs(sum(gifts)) # Return the absolute value of sum of the gifts arr

sol = Simulation()
print(sol.pickGifts([25,64,9,4,100], 4))
print(sol.pickGifts([1,1,1,1], 1))

# ================================================================
# PATTERN 3: MERGE K SORTED LISTS/ARRAYS (K-Way Merge)
# PATTERN EXPLANATION: Efficiently merge k sorted data sources into one sorted output.
# Key insight: 
#   1. Initialize heap with first element from each source
#   2. Always extract minimum element (guaranteed smallest across all sources)
#   3. Add extracted element to result
#   4. Push next element from same source into heap
#   5. Repeat until all sources exhausted
# Why it works: Heap maintains "frontier" of smallest unprocessed element from each source.
# Applications: Merge k sorted lists/arrays, smallest range covering k lists, kth element in matrix.
# Time Complexity: O(N log k) where N = total elements, k = number of sources
# ================================================================

# PROBLEM: LC 23 - Merge k Sorted Lists
# Key Insight: Use min heap to track the smallest current element from each list.
#              Pop smallest, add to result, push next node from same list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeK:
    def mergeKLists(self, lists):
        '''
        You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

        Ex. 1
            Input: lists = [[1,4,5],[1,3,4],[2,6]]
            Output: [1,1,2,3,4,4,5,6]
            Explanation: The linked-lists are:
            [
            1->4->5,
            1->3->4,
            2->6
            ]
            merging them into one sorted linked list:
            1->1->2->3->4->4->5->6
        
        TC:
            - O(k log k) - initial heap setup pushes k nodes into heap using heappush (log k)
            - O(n) for iterating through the heap (one iteration for each node)
            - Each iteration: O(log k) to pop + O(log k) to push
            - Total: O(k log k) + O(N log k) = O(N log k)
        SC: 
            - O(k) - the heap only stores at nost k nodes at once (one from each list)
        '''
        heap = []
        
        # Step 1: Add first node from each list to heap
        # Tuple: (node_value, list_index, node (head is a reference to list1, list2, etc))
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head)) # head is a pointer to the first node
        
        dummy = ListNode(0) # Start LL after dummy node
        current = dummy
        
        # Step 2: Extract min, add to result, push next from same list
        while heap: # Continue building merged LL until no more nodes
            val, list_idx, node = heapq.heappop(heap) # pop min val & destructure tuple
            
            # Add node to merged LL
            current.next = node
            current = current.next # Move pointer forward
            
            # Push next node from same list
            if node.next:
                heapq.heappush(heap, (node.next.val, list_idx, node.next)) 
        
        return dummy.next # Return first node in merged LL

# Example 1: lists = [[1,4,5],[1,3,4],[2,6]]
list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = ListNode(2)
list3.next = ListNode(6)

sol = MergeK()
print(sol.mergeKLists([list1, list2, list3]))
# Expected output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

# ================================================================
# PATTERN 4: INTERVAL SCHEDULING (Min Heap for Event Processing)
# PATTERN EXPLANATION: Process time-based events efficiently using a min heap.
# Key insight: 
#   1. Sort events by start time (process in chronological order)
#   2. Use min heap to track ongoing events by their end times
#   3. When processing new event: remove expired events (heap top ≤ current time)
#   4. Heap size = number of overlapping/active events at current time
# Applications: Meeting rooms, resource allocation, task scheduling, capacity planning.
# Time Complexity: O(n log n) - sorting + heap operations
# ================================================================

# PROBLEM: LC 253 - Meeting Rooms II
# Key Insight: Sort meetings by start time, use min heap to track end times of ongoing meetings.
# Heap size at any point = minimum rooms needed.

class MeetingRooms:
    '''
    Given an array of meeting time intervals where intervals[i] = [start_i, end_i],
    return the minimum number of conference rooms required.
    
    Example:
    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: 2
    Explanation:
    - Meeting 1: 0-30 (needs room 1)
    - Meeting 2: 5-10 (starts while meeting 1 ongoing, needs room 2)
    - Meeting 3: 15-20 (meeting 2 ended at 10, can reuse room 2)
    Maximum rooms needed simultaneously: 2
    
    Strategy:
    1. Sort intervals by start time
    2. Use min heap to track end times of active meetings
    3. For each meeting:
        - Remove ended meetings (pop if heap top <= current start)
        - Add current meeting's end time
        - Heap size = rooms needed at this moment
    4. Return maximum heap size seen
    
        Visual Timeline:
        Time:  0    5    10   15   20   30
            |----Meeting 1------------| Room 1
                    |--M2--| Room 2
                        |-M3-| Room 2 (reused)
    
    Heap states:
    After M1: [30]           → 1 room
    After M2: [10, 30]       → 2 rooms (max!)
    After M3: [20, 30]       → 2 rooms
    
    TC: O(n log n) - sorting intervals + n heap operations (each O(log n))
    SC: O(n) - heap can store up to n meeting end times in worst case
    '''
    
    def minMeetingRooms(self, intervals):
        if not intervals: # Edge case for empty interval
            return 0
        
        # Sort meetings by start time to process them in order chronologically
        intervals.sort(key=lambda x: x[0])
        
        # Use min heap to track end times of ongoing meetings
        heap = []
        
        for start, end in intervals:
            # Check if earliest meeting's end time is less than new start time
            if heap and heap[0] <= start: 
                heapq.heappop(heap)
            
            # Add current meeting's end time
            heapq.heappush(heap, end)
            max_rooms = max(max_rooms, len(heap)) # Max # of rooms seen
        
        return max_rooms

sol = MeetingRooms()
print(sol.minMeetingRooms([[0,30],[5,10],[15,20]]))  # 2
print(sol.minMeetingRooms([[7,10],[2,4]]))  # 1
print(sol.minMeetingRooms([[1,5],[8,9],[8,9]]))  # 2

