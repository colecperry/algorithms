"""
=================================================================
QUEUE COMPLETE GUIDE
=================================================================

WHAT IS A QUEUE?
----------------
A Queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.
Elements are added at the rear (enqueue) and removed from the front (dequeue), like a
line of people waiting - the first person in line is the first to be served.

Key characteristics:
- FIFO ordering: First element added is first to be removed
- Two main operations: enqueue (add to rear) and dequeue (remove from front)
- Additional operations: peek (view front), isEmpty, size
- Can be implemented with arrays, linked lists, or deque

Python Queue implementations:
- collections.deque: Most efficient, O(1) for both ends
- list: O(1) append, O(n) pop from front (use deque instead)
- queue.Queue: Thread-safe but slower (use for multithreading only)

When to use Queue:
- Level-order traversal (BFS in trees)
- Shortest path in unweighted graphs
- Processing elements in order of arrival
- Scheduling, task management, buffering
- Sliding window problems (with deque)

Common Queue problem types:
- BFS traversal (trees, graphs, grids)
- Level-order processing
- Shortest path problems
- Sliding window maximum/minimum
- Design problems (implement queue, circular queue)
- Task scheduling and ordering

QUEUE CORE TEMPLATES
=====================
"""

from typing import List, Optional
from collections import deque

# ================================================================
# BASIC QUEUE TEMPLATE
# ================================================================
def basic_queue_template():
    """
    Basic queue operations using Python's deque
    TC: O(1) for all operations
    SC: O(n) where n = number of elements
    """
    # Initialize queue
    queue = deque()
    
    # Enqueue (add to rear)
    queue.append(1)
    queue.append(2)
    queue.append(3)
    
    # Dequeue (remove from front)
    first = queue.popleft()  # Returns 1
    
    # Peek (view front without removing)
    if queue:
        front = queue[0]  # Returns 2
    
    # Check if empty
    is_empty = len(queue) == 0
    
    # Get size
    size = len(queue)
    
    return queue

# ================================================================
# BFS TEMPLATE (TREE LEVEL-ORDER)
# ================================================================
def bfs_tree_template(root):
    """
    BFS level-order traversal of tree
    TC: O(n) - visit each node once
    SC: O(w) - queue size is max width of tree
    """
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        # Process all nodes at current level
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            # Add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

# ================================================================
# BFS TEMPLATE (GRAPH/GRID)
# ================================================================
def bfs_graph_template(graph, start):
    """
    BFS traversal of graph with visited tracking
    TC: O(V + E) - visit each vertex and edge once
    SC: O(V) - queue and visited set
    """
    visited = set([start])
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        # Process neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

# ================================================================
# MONOTONIC QUEUE TEMPLATE (SLIDING WINDOW)
# ================================================================
def monotonic_queue_template(nums, k):
    """
    Sliding window maximum using monotonic deque
    TC: O(n) - each element enters/exits deque once
    SC: O(k) - deque stores at most k elements
    """
    result = []
    deq = deque()  # Stores indices, maintains decreasing order
    
    for i in range(len(nums)):
        # Remove elements outside window
        if deq and deq[0] < i - k + 1:
            deq.popleft()
        
        # Remove smaller elements (maintain decreasing order)
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        
        deq.append(i)
        
        # Add to result when window is full
        if i >= k - 1:
            result.append(nums[deq[0]])
    
    return result

"""
TIME & SPACE COMPLEXITY REFERENCE
==================================

QUEUE OPERATIONS COMPLEXITY:
----------------------------
+---------------------------+------------------+------------------+
| Operation                 | Time Complexity  | Space Complexity |
+---------------------------+------------------+------------------+
| Enqueue (append)          | O(1)             | O(1)             |
| Dequeue (popleft)         | O(1)             | O(1)             |
| Peek (front element)      | O(1)             | O(1)             |
| isEmpty                   | O(1)             | O(1)             |
| Size                      | O(1)             | O(1)             |
+---------------------------+------------------+------------------+

COMMON QUEUE PATTERNS COMPLEXITY:
---------------------------------
+---------------------------+------------------+------------------+
| Pattern                   | Time Complexity  | Space Complexity |
+---------------------------+------------------+------------------+
| Basic Queue Ops           | O(1) per op      | O(n)             |
| BFS Tree                  | O(n)             | O(w)             |
| BFS Graph                 | O(V + E)         | O(V)             |
| BFS Grid                  | O(m * n)         | O(m * n)         |
| Multi-source BFS          | O(m * n)         | O(m * n)         |
| Monotonic Queue           | O(n)             | O(k)             |
| Sliding Window Max        | O(n)             | O(k)             |
| Queue with Stacks         | O(1) amortized   | O(n)             |
| Circular Queue            | O(1) per op      | O(k)             |
+---------------------------+------------------+------------------+

WHERE:
- n = number of elements/nodes
- m, n = grid dimensions
- V = vertices, E = edges in graph
- w = maximum width of tree
- k = window size or queue capacity

COMPLEXITY NOTES:
----------------
1. Basic Queue Operations: O(1) time, O(n) space
   - Enqueue/dequeue are constant time with deque
   - Space grows linearly with number of elements
   - Use collections.deque for optimal performance
   
   Common pattern: queue.append(x), queue.popleft()

2. BFS Tree Traversal: O(n) time, O(w) space
   - Visit each node exactly once: O(n)
   - Queue size equals maximum tree width: O(w)
   - Worst case width: O(n) for skewed tree, O(n/2) for complete tree
   
   Level-order processing: process one level at a time
   Common pattern: level_size = len(queue), then process that many nodes

3. BFS Graph: O(V + E) time, O(V) space
   - Visit each vertex once: O(V)
   - Check each edge once: O(E)
   - Queue and visited set store vertices: O(V)
   
   Must track visited to avoid cycles
   Common pattern: visited.add(node), queue.append(neighbor)

4. BFS Grid: O(m * n) time, O(m * n) space
   - Visit each cell at most once: O(m * n)
   - Queue can hold all cells in worst case: O(m * n)
   - 4-directional: each cell has up to 4 neighbors
   
   Grid coordinates in queue: queue.append((r, c))
   Common pattern: check bounds, mark visited, explore 4 directions

5. Multi-source BFS: O(m * n) time, O(m * n) space
   - Same as regular BFS but start from multiple sources
   - Add all sources to queue initially
   - All sources process simultaneously
   
   Useful for: infection spread, distance from multiple points
   Common pattern: queue = deque(all_sources), then standard BFS

6. Monotonic Queue: O(n) time, O(k) space
   - Each element enters and exits deque at most once: O(n)
   - Deque stores at most k elements (window size): O(k)
   - Maintains increasing or decreasing order
   
   Key: remove elements that can't be answer
   Common pattern: while deq and condition: deq.pop()

7. Sliding Window Maximum: O(n) time, O(k) space
   - Process each element once: O(n)
   - Deque stores indices in decreasing order: O(k)
   - Remove elements outside window and smaller elements
   
   Specialized monotonic queue application
   Common pattern: deq stores indices, maintains max at front

8. Queue Implementation: O(1) amortized time, O(n) space
   - Using two stacks: push O(1), pop O(1) amortized
   - Amortized: each element moves between stacks at most twice
   - Using array: enqueue O(1), dequeue O(1) with circular buffer
   
   Two stacks pattern: one for input, one for output
   Circular queue: use modulo for wrap-around

GENERAL QUEUE OPTIMIZATION:
---------------------------
Space optimization:
- Use deque over list: O(1) operations on both ends
- In-place marking: modify grid instead of visited set
- Circular buffer: reuse array space in circular queue

Time optimization:
- Monotonic deque: maintain order for window problems
- Level-order: process entire level at once
- Early termination: stop when target found in BFS

WHEN TO USE EACH PATTERN:
--------------------------
Basic Queue:
  - Simple FIFO processing
  - Task scheduling, buffering
  - When order of arrival matters

BFS Tree:
  - Level-order traversal
  - Find depth/height
  - Process tree level by level

BFS Graph/Grid:
  - Shortest path (unweighted)
  - Connected components
  - Reachability problems
  - Flood fill, infection spread

Monotonic Queue:
  - Sliding window max/min
  - Next greater/smaller element
  - Maintain ordered subset

Queue Design:
  - Implement custom data structures
  - Circular buffer applications
  - Moving average, rate limiting
"""

# Test the templates
print("Basic Queue:", basic_queue_template())
print("Monotonic Queue (sliding max):", monotonic_queue_template([1,3,-1,-3,5,3,6,7], 3))

"""
QUEUE PATTERNS
==============
"""

# ================================================================
# PATTERN 1: BASIC QUEUE OPERATIONS
# PATTERN EXPLANATION: Use a queue (FIFO) to process elements in the order they arrive.
# Elements are added to the rear and removed from the front. Common for sequential processing,
# scheduling tasks, and maintaining order. Queue operations (enqueue, dequeue, peek) are O(1)
# with proper implementation (deque in Python).
#
# TYPICAL STEPS:
# 1. Initialize queue (use collections.deque)
# 2. Add elements to rear with append()
# 3. Remove elements from front with popleft()
# 4. Check front with [0] without removing
# 5. Process until queue is empty
#
# Applications: Task scheduling, print queue, buffering, order processing.
# ================================================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BasicQueue:
    """
    Problem: Implement a basic queue supporting enqueue, dequeue, peek, and isEmpty.
    
    Operations:
    - enqueue(x): Add element x to rear of queue
    - dequeue(): Remove and return front element
    - peek(): Return front element without removing
    - isEmpty(): Check if queue is empty
    
    TC: O(1) for all operations
    SC: O(n) where n = number of elements
    
    How it works:
    1. Use Python's deque (double-ended queue) for O(1) operations
    2. append() adds to rear (enqueue)
    3. popleft() removes from front (dequeue)
    4. Index [0] views front (peek)
    """
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, x: int) -> None:
        """Add element to rear of queue"""
        self.queue.append(x)
    
    def dequeue(self) -> int:
        """Remove and return front element"""
        if self.isEmpty():
            return -1
        return self.queue.popleft()
    
    def peek(self) -> int:
        """Return front element without removing"""
        if self.isEmpty():
            return -1
        return self.queue[0]
    
    def isEmpty(self) -> bool:
        """Check if queue is empty"""
        return len(self.queue) == 0
    
    def size(self) -> int:
        """Return number of elements"""
        return len(self.queue)

# Example usage:
# q = BasicQueue()
# q.enqueue(1)    # Queue: [1]
# q.enqueue(2)    # Queue: [1, 2]
# q.enqueue(3)    # Queue: [1, 2, 3]
# q.peek()        # Returns: 1 (front element)
# q.dequeue()     # Returns: 1, Queue: [2, 3]
# q.dequeue()     # Returns: 2, Queue: [3]
# q.size()        # Returns: 1

q = BasicQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Peek:", q.peek())        # 1
print("Dequeue:", q.dequeue())  # 1
print("Size:", q.size())        # 2


# ================================================================
# PATTERN 2: BFS - TREE LEVEL-ORDER TRAVERSAL
# PATTERN EXPLANATION: Use a queue to visit tree nodes level by level, from left to right.
# Process all nodes at current level before moving to next level. Queue maintains nodes to
# visit in order. Track level size to process complete levels at once.
#
# TYPICAL STEPS:
# 1. Initialize queue with root node
# 2. While queue not empty:
#    a. Record current level size
#    b. Process that many nodes (entire level)
#    c. Add children of processed nodes to queue
# 3. Children become next level
#
# Applications: Level-order traversal, tree width, zigzag traversal, level averages.
# ================================================================

class BFSTree:
    """
    Problem: Given the root of a binary tree, return the level order traversal of its
    nodes' values (i.e., from left to right, level by level).
    
    Example:
        Tree:       3
                   / \
                  9  20
                    /  \
                   15   7
        
        Output: [[3], [9,20], [15,7]]
    
    TC: O(n) - visit each node exactly once
    SC: O(w) - queue size equals maximum tree width (w)
           - Worst case: O(n) for skewed tree
           - Best case: O(n/2) for complete tree
    
    How it works:
    1. Start with root in queue
    2. For each level, record how many nodes are in queue
    3. Process exactly that many nodes (complete level)
    4. Add their children to queue (next level)
    5. Children are processed in next iteration
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:  # LC 102
        if not root:
            return []
        
        result = []
        queue = deque([root])  # Start with root
        
        while queue:
            level_size = len(queue)  # Number of nodes at current level
            level = []  # Store current level's values
            
            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                
                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        return result

# Example:
#       3
#      / \
#     9  20
#       /  \
#      15   7
#
# BFS trace:
# Initial: queue = [3], result = []
# 
# Level 0: level_size = 1
#   Process 3: level = [3], add 9 and 20 to queue
#   queue = [9, 20], result = [[3]]
#
# Level 1: level_size = 2
#   Process 9: level = [9], queue = [20]
#   Process 20: level = [9, 20], add 15 and 7 to queue
#   queue = [15, 7], result = [[3], [9, 20]]
#
# Level 2: level_size = 2
#   Process 15: level = [15]
#   Process 7: level = [15, 7]
#   queue = [], result = [[3], [9, 20], [15, 7]]
#
# Output: [[3], [9, 20], [15, 7]]

sol = BFSTree()
tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print("Level Order:", sol.levelOrder(tree))  # [[3], [9, 20], [15, 7]]


# ================================================================
# PATTERN 3: BFS - GRAPH/GRID (SHORTEST PATH & MULTI-SOURCE)
# PATTERN EXPLANATION: Use BFS to explore grid or graph layer by layer, tracking visited
# cells/nodes. BFS guarantees shortest path in unweighted graphs. Multi-source BFS starts
# from multiple points simultaneously. Perfect for distance calculations, infection spread,
# and reachability problems.
#
# TYPICAL STEPS:
# 1. Initialize queue with starting cell(s) and visited set
# 2. For multi-source: add all sources to queue initially
# 3. While queue not empty:
#    a. Dequeue cell/node
#    b. Check if target reached (optional early exit)
#    c. Explore neighbors (4 or 8 directions for grid)
#    d. Mark visited and add to queue if valid
# 4. Track distance/steps if needed
#
# Applications: Shortest path, rotting oranges, walls and gates, island problems.
# ================================================================

class BFSGrid:
    """
    Problem: You are given an m x n grid where each cell can have one of three values:
    - 0 representing an empty cell
    - 1 representing a fresh orange
    - 2 representing a rotten orange
    
    Every minute, any fresh orange adjacent (4-directionally) to a rotten orange becomes rotten.
    Return the minimum number of minutes until no cell has a fresh orange. If impossible, return -1.
    
    Example:
        Input: [[2,1,1],
                [1,1,0],
                [0,1,1]]
        
        Minute 0: (0,0) is rotten
        Minute 1: (0,1) and (1,0) become rotten
        Minute 2: (0,2) and (1,1) become rotten
        Minute 3: (1,2) becomes rotten
        Minute 4: (2,2) becomes rotten
        
        Output: 4
    
    TC: O(m * n) - visit each cell at most once
    SC: O(m * n) - queue can hold all cells in worst case
    
    How it works:
    1. Multi-source BFS: start from ALL rotten oranges simultaneously
    2. Add all initial rotten oranges to queue
    3. Process level by level (each level = 1 minute)
    4. Rotten oranges spread to adjacent fresh oranges
    5. Count minutes and check if all fresh oranges rotted
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:  # LC 994
        if not grid or not grid[0]:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Find all initially rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))  # Add rotten orange to queue
                elif grid[r][c] == 1:
                    fresh_count += 1  # Count fresh oranges
        
        # If no fresh oranges, already done
        if fresh_count == 0:
            return 0
        
        # BFS: spread rot level by level
        minutes = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]  # Right, Down, Left, Up
        
        while queue:
            level_size = len(queue)  # All rotten oranges at current minute
            
            # Process all oranges that are rotten at this minute
            for _ in range(level_size):
                r, c = queue.popleft()
                
                # Try to rot adjacent fresh oranges
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Check bounds and if cell has fresh orange
                    if (0 <= nr < rows and 0 <= nc < cols and 
                        grid[nr][nc] == 1):
                        # Rot this orange
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))  # Will spread next minute
            
            # One minute passed (if any oranges rotted this minute)
            if queue:
                minutes += 1
        
        # Check if all fresh oranges rotted
        return minutes if fresh_count == 0 else -1

# Example:
# grid = [[2,1,1],
#         [1,1,0],
#         [0,1,1]]
#
# Initial: queue = [(0,0)], fresh_count = 6
#
# Minute 1: Process (0,0)
#   - Rot (0,1): grid[0][1] = 2, queue = [(0,1), (1,0)]
#   - Rot (1,0): grid[1][0] = 2
#   fresh_count = 4
#
# Minute 2: Process (0,1) and (1,0)
#   From (0,1): Rot (0,2), queue = [(0,2), (1,1)]
#   From (1,0): Rot (1,1)
#   fresh_count = 2
#
# Minute 3: Process (0,2) and (1,1)
#   From (1,1): Rot (1,2), queue = [(1,2), (2,1)]
#   From (0,2): nothing
#   fresh_count = 1
#
# Minute 4: Process (1,2) and (2,1)
#   From (1,2): Rot (2,2), queue = [(2,2)]
#   fresh_count = 0
#
# Output: 4 minutes

sol = BFSGrid()
print("Rotting Oranges:", sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))  # 4
print("Rotting Oranges:", sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))  # -1


# ================================================================
# PATTERN 4: MONOTONIC QUEUE/DEQUE (SLIDING WINDOW)
# PATTERN EXPLANATION: Maintain elements in a deque in monotonically increasing or decreasing
# order. Remove elements that can never be the answer (smaller than current in max problem,
# larger in min problem). Used for sliding window maximum/minimum where we need to efficiently
# track the best element in a moving window.
#
# TYPICAL STEPS:
# 1. Initialize deque to store indices (not values)
# 2. For each element:
#    a. Remove indices outside current window (left side)
#    b. Remove elements that can't be answer (right side)
#    c. Add current index to deque
#    d. Front of deque is the answer for current window
# 3. Maintain monotonic property (increasing/decreasing)
#
# Applications: Sliding window max/min, next greater element, monotonic stack problems.
# ================================================================

class MonotonicQueue:
    """
    Problem: You are given an array of integers nums and an integer k. There is a sliding
    window of size k which is moving from the very left to the very right. You can only
    see the k numbers in the window. Return the max sliding window.
    
    Example:
        nums = [1,3,-1,-3,5,3,6,7], k = 3
        
        Windows:
        [1  3  -1] -3  5  3  6  7  -> max = 3
         1 [3  -1  -3] 5  3  6  7  -> max = 3
         1  3 [-1  -3  5] 3  6  7  -> max = 5
         1  3  -1 [-3  5  3] 6  7  -> max = 5
         1  3  -1  -3 [5  3  6] 7  -> max = 6
         1  3  -1  -3  5 [3  6  7] -> max = 7
        
        Output: [3,3,5,5,6,7]
    
    TC: O(n) - each element enters and exits deque exactly once
    SC: O(k) - deque stores at most k indices
    
    How it works:
    1. Deque stores indices in decreasing order of values
    2. Front of deque always has index of maximum in current window
    3. Remove indices outside window from front
    4. Remove smaller values from back (they can't be max)
    5. Add current index to back
    
    Key insight: If nums[i] >= nums[j] and i > j, then nums[j] can never be
    the maximum (nums[i] is larger and stays in window longer)
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:  # LC 239
        result = []
        deq = deque()  # Stores indices, maintains decreasing order of values
        
        for i in range(len(nums)):
            # Remove indices outside current window (left side)
            # Window is [i-k+1, i], so remove if index < i-k+1
            if deq and deq[0] < i - k + 1:
                deq.popleft()
            
            # Remove smaller elements from back (can't be maximum)
            # Maintain decreasing order: front has largest
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            
            # Add current index
            deq.append(i)
            
            # Add maximum of current window to result
            # (once we have k elements, i.e., i >= k-1)
            if i >= k - 1:
                result.append(nums[deq[0]])  # Front has max index
        
        return result

# Example:
# nums = [1,3,-1,-3,5,3,6,7], k = 3
#
# Deque stores indices, maintaining decreasing order of VALUES
#
# i=0 (val=1): deq = [0], not enough for window yet
# i=1 (val=3): 3 > 1, remove 0, deq = [1]
# i=2 (val=-1): -1 < 3, add to back, deq = [1,2], window full!
#   result = [nums[1]] = [3]
#
# i=3 (val=-3): -3 < -1, add to back, deq = [1,2,3]
#   result = [3, nums[1]] = [3, 3]
#
# i=4 (val=5): 5 > -3, remove 3, 5 > -1, remove 2, 5 > 3, remove 1
#   deq = [4]
#   result = [3, 3, nums[4]] = [3, 3, 5]
#
# i=5 (val=3): 3 < 5, add to back, deq = [4,5]
#   result = [3, 3, 5, nums[4]] = [3, 3, 5, 5]
#
# i=6 (val=6): 6 > 3, remove 5, 6 > 5, remove 4, deq = [6]
#   result = [3, 3, 5, 5, nums[6]] = [3, 3, 5, 5, 6]
#
# i=7 (val=7): 7 > 6, remove 6, deq = [7]
#   result = [3, 3, 5, 5, 6, nums[7]] = [3, 3, 5, 5, 6, 7]
#
# Output: [3, 3, 5, 5, 6, 7]

sol = MonotonicQueue()
print("Sliding Window Max:", sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
print("Sliding Window Max:", sol.maxSlidingWindow([1], 1))  # [1]


# ================================================================
# PATTERN 5: QUEUE DESIGN & IMPLEMENTATION
# PATTERN EXPLANATION: Implement queue using other data structures (like stacks) or design
# special queue variants (circular queue, moving average). Focus on maintaining FIFO property
# and achieving O(1) operations. Common in design problems that test understanding of queue
# operations and optimizations.
#
# TYPICAL STEPS:
# For Queue with Stacks:
# 1. Use two stacks: input stack and output stack
# 2. Push: add to input stack
# 3. Pop: if output empty, move all from input to output, then pop
# 4. Amortized O(1): each element moves between stacks at most once
#
# For Circular Queue:
# 1. Use fixed-size array and head/tail pointers
# 2. Use modulo to wrap around
# 3. Track size or use (tail+1)%capacity == head for full check
#
# Applications: Queue implementation, circular buffer, moving average, rate limiting.
# ================================================================

class QueueDesign:
    """
    Problem 1: Implement a queue using two stacks. The queue should support push (add to rear),
    pop (remove from front), peek (get front), and empty operations.
    
    TC: O(1) amortized for all operations
    SC: O(n) where n = number of elements
    
    How it works:
    1. Two stacks: input_stack (for push), output_stack (for pop/peek)
    2. Push: add to input_stack - O(1)
    3. Pop/Peek: if output_stack empty, transfer all from input_stack - O(n) worst case
       - Each element transferred at most once, so amortized O(1)
    4. Elements reversed twice (once per stack) = correct FIFO order
    """
    def __init__(self):  # LC 232 - Implement Queue using Stacks
        self.input_stack = []   # For enqueue
        self.output_stack = []  # For dequeue
    
    def push(self, x: int) -> None:
        """Add element to rear of queue"""
        self.input_stack.append(x)
    
    def pop(self) -> int:
        """Remove and return front element"""
        self._transfer()
        return self.output_stack.pop()
    
    def peek(self) -> int:
        """Get front element without removing"""
        self._transfer()
        return self.output_stack[-1]
    
    def empty(self) -> bool:
        """Check if queue is empty"""
        return not self.input_stack and not self.output_stack
    
    def _transfer(self):
        """Transfer elements from input to output if output is empty"""
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

# Example:
# Operations: push(1), push(2), peek(), pop(), empty()
#
# push(1):
#   input_stack = [1], output_stack = []
#
# push(2):
#   input_stack = [1, 2], output_stack = []
#
# peek():
#   Transfer: input_stack = [], output_stack = [2, 1]
#   Return: 1 (top of output_stack)
#
# pop():
#   output_stack = [2, 1]
#   Return: 1, output_stack = [2]
#
# empty():
#   input_stack = [], output_stack = [2]
#   Return: False


class CircularQueue:
    """
    Problem 2: Design a circular queue with fixed capacity. Support enqueue, dequeue,
    front, rear, isEmpty, and isFull operations.
    
    TC: O(1) for all operations
    SC: O(k) where k = queue capacity
    
    How it works:
    1. Fixed-size array with head and tail pointers
    2. Head points to front element, tail points to next empty slot
    3. Use modulo (%) to wrap around when reaching end of array
    4. Track size to distinguish empty vs full
    """
    def __init__(self, k: int):  # LC 622 - Design Circular Queue
        self.queue = [0] * k
        self.capacity = k
        self.head = 0   # Points to front element
        self.size = 0   # Current number of elements
    
    def enQueue(self, value: int) -> bool:
        """Add element to rear of queue"""
        if self.isFull():
            return False
        
        # Calculate tail position: (head + size) wrapped around
        tail = (self.head + self.size) % self.capacity
        self.queue[tail] = value
        self.size += 1
        return True
    
    def deQueue(self) -> bool:
        """Remove element from front of queue"""
        if self.isEmpty():
            return False
        
        # Move head forward (wrap around with modulo)
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True
    
    def Front(self) -> int:
        """Get front element"""
        if self.isEmpty():
            return -1
        return self.queue[self.head]
    
    def Rear(self) -> int:
        """Get rear element"""
        if self.isEmpty():
            return -1
        # Tail is one position before where next element would go
        tail = (self.head + self.size - 1) % self.capacity
        return self.queue[tail]
    
    def isEmpty(self) -> bool:
        """Check if queue is empty"""
        return self.size == 0
    
    def isFull(self) -> bool:
        """Check if queue is full"""
        return self.size == self.capacity

# Example: CircularQueue with capacity 3
# queue = [_, _, _], head = 0, size = 0
#
# enQueue(1):
#   tail = (0+0) % 3 = 0
#   queue = [1, _, _], head = 0, size = 1
#
# enQueue(2):
#   tail = (0+1) % 3 = 1
#   queue = [1, 2, _], head = 0, size = 2
#
# enQueue(3):
#   tail = (0+2) % 3 = 2
#   queue = [1, 2, 3], head = 0, size = 3 (FULL)
#
# deQueue():
#   head = (0+1) % 3 = 1
#   queue = [1, 2, 3], head = 1, size = 2
#
# enQueue(4):
#   tail = (1+2) % 3 = 0 (wrapped around!)
#   queue = [4, 2, 3], head = 1, size = 3
#   Logical order: [2, 3, 4]

q1 = QueueDesign()
q1.push(1)
q1.push(2)
print("Queue with Stacks - Peek:", q1.peek())  # 1
print("Queue with Stacks - Pop:", q1.pop())    # 1

q2 = CircularQueue(3)
print("Circular Queue - Enqueue 1:", q2.enQueue(1))  # True
print("Circular Queue - Enqueue 2:", q2.enQueue(2))  # True
print("Circular Queue - Enqueue 3:", q2.enQueue(3))  # True
print("Circular Queue - Enqueue 4:", q2.enQueue(4))  # False (full)
print("Circular Queue - Front:", q2.Front())         # 1
print("Circular Queue - Rear:", q2.Rear())           # 3


# ================================================================
# PATTERN 6: DEQUE (DOUBLE-ENDED QUEUE) FOR SPECIAL CASES
# PATTERN EXPLANATION: Use deque when you need efficient operations on both ends of the queue.
# Unlike regular queue (add rear, remove front), deque allows O(1) add/remove on both ends.
# Useful for palindrome checks, reversible operations, and when direction might change.
#
# TYPICAL STEPS:
# 1. Initialize deque
# 2. Use append()/pop() for right end (rear)
# 3. Use appendleft()/popleft() for left end (front)
# 4. Access with [0] (front) or [-1] (rear)
# 5. Choose operations based on problem requirements
#
# Applications: Palindrome, reversible queue, task prioritization from both ends.
# ================================================================

class DequePattern:
    """
    Problem: Design a data structure that supports adding and removing elements from both
    front and rear efficiently. Also demonstrate palindrome checking using deque.
    
    TC: O(1) for all operations
    SC: O(n) where n = number of elements
    
    How it works:
    1. Deque allows O(1) operations on both ends
    2. appendleft/popleft for front operations
    3. append/pop for rear operations
    4. Can be used for sliding window, palindrome, reversible queue
    """
    def __init__(self):
        self.deq = deque()
    
    def addFront(self, x: int) -> None:
        """Add element to front"""
        self.deq.appendleft(x)
    
    def addRear(self, x: int) -> None:
        """Add element to rear"""
        self.deq.append(x)
    
    def removeFront(self) -> int:
        """Remove element from front"""
        if not self.deq:
            return -1
        return self.deq.popleft()
    
    def removeRear(self) -> int:
        """Remove element from rear"""
        if not self.deq:
            return -1
        return self.deq.pop()
    
    def isPalindrome(self, s: str) -> bool:
        """Check if string is palindrome using deque"""
        # Remove non-alphanumeric and convert to lowercase
        s = ''.join(c.lower() for c in s if c.isalnum())
        
        dq = deque(s)
        
        # Compare from both ends
        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
        
        return True

# Example 1: Deque operations
# dq = DequePattern()
# addFront(1):  deq = [1]
# addFront(2):  deq = [2, 1]
# addRear(3):   deq = [2, 1, 3]
# removeFront: returns 2, deq = [1, 3]
# removeRear:  returns 3, deq = [1]

# Example 2: Palindrome check
# "A man, a plan, a canal: Panama"
# Clean: "amanaplanacanalpanama"
# 
# deq = ['a','m','a','n','a','p','l','a','n','a','c','a','n','a','l','p','a','n','a','m','a']
# Compare: 'a' == 'a' ✓, remove both ends
# Compare: 'm' == 'm' ✓, remove both ends
# ... continues until empty or mismatch
# Result: True (is palindrome)

sol = DequePattern()
sol.addFront(1)
sol.addFront(2)
sol.addRear(3)
print("Deque - Remove Front:", sol.removeFront())  # 2
print("Deque - Remove Rear:", sol.removeRear())    # 3
print("Palindrome Check:", sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
print("Palindrome Check:", sol.isPalindrome("race a car"))  # False


# ================================================================
# SUMMARY OF QUEUE PATTERNS
# ================================================================
"""
Pattern 1 - Basic Queue Operations:
  - Simple FIFO processing with enqueue/dequeue
  - O(1) operations with proper implementation
  - Use for: Task scheduling, order processing, buffering
  - Example: Basic queue implementation with deque

Pattern 2 - BFS Tree Level-Order:
  - Process tree nodes level by level
  - Track level size to process complete levels
  - Use for: Level-order traversal, tree depth, level averages
  - Example: LC 102 (Binary Tree Level Order Traversal)

Pattern 3 - BFS Graph/Grid:
  - Explore graph/grid layer by layer with visited tracking
  - Multi-source BFS for simultaneous starting points
  - Use for: Shortest path, infection spread, distance calculations
  - Example: LC 994 (Rotting Oranges)

Pattern 4 - Monotonic Queue:
  - Maintain elements in sorted order using deque
  - Remove elements that can't be answer
  - Use for: Sliding window max/min, next greater element
  - Example: LC 239 (Sliding Window Maximum)

Pattern 5 - Queue Design:
  - Implement queue with other structures (stacks, arrays)
  - Circular queue for fixed capacity
  - Use for: Custom queue implementations, moving average
  - Example: LC 232 (Queue using Stacks), LC 622 (Circular Queue)

Pattern 6 - Deque (Double-ended Queue):
  - O(1) operations on both ends
  - Flexible add/remove from front or rear
  - Use for: Palindrome, reversible operations, bidirectional processing
  - Example: Palindrome check, task prioritization

Master these 6 patterns and you'll handle 80-90% of queue problems on LeetCode!

KEY TAKEAWAYS:
--------------
1. Use collections.deque for O(1) operations on both ends
2. BFS guarantees shortest path in unweighted graphs
3. Track visited to avoid revisiting nodes/cells
4. Process levels one at a time for level-order problems
5. Monotonic queue maintains order for window problems
6. Multi-source BFS starts from all sources simultaneously
7. Queue with stacks achieves amortized O(1) with two stacks
8. Circular queue uses modulo for wrap-around
"""