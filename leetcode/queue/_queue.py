"""
=================================================================
QUEUE COMPLETE GUIDE
=================================================================

WHAT IS A QUEUE?
----------------
A Queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.
Elements are added at the rear (enqueue) and removed from the front (dequeue), like a
line of people waiting — the first person in line is the first to be served.

Key characteristics:
- FIFO ordering: First element added is first to be removed
- O(1) enqueue (append) and dequeue (popleft) with collections.deque
- Foundation of BFS: queue processes nodes level by level
- Monotonic variant (deque) enables O(n) sliding window extremes

Python implementation:
    from collections import deque
    queue = deque()
    queue.append(x)      # enqueue — O(1)
    queue.popleft()      # dequeue — O(1)
    queue[0]             # peek front — O(1)

When to use Queue:
- Level-order traversal (BFS on trees)
- Shortest path in unweighted graphs or grids
- Multi-source BFS (multiple starting points simultaneously)
- Sliding window maximum/minimum (monotonic deque)
- Design problems (implement queue using other structures)

Common Queue problem types:
- BFS tree level-order traversal
- BFS grid: shortest path, infection spread
- Multi-source BFS: distance from multiple origins
- Sliding window max/min with monotonic deque
- Queue implementation and design

QUEUE CORE PATTERNS
===================
"""

from typing import List, Optional
from collections import deque

"""
QUEUE COMPLEXITY REFERENCE
===========================

+---------------------------+------------------+------------------+
| Pattern                   | Time             | Space            |
+---------------------------+------------------+------------------+
| BFS Tree Level-Order      | O(n)             | O(w)             |
| BFS Grid / Multi-source   | O(m * n)         | O(m * n)         |
| Monotonic Deque           | O(n)             | O(k)             |
| Queue with Two Stacks     | O(1) amortized   | O(n)             |
+---------------------------+------------------+------------------+

n = number of nodes/elements, w = max tree width,
m/n = grid dimensions, k = window size

NOTES:
- BFS tree: queue holds at most one full level (max width w) at a time
- BFS grid: each cell visited once; queue can hold up to m*n cells
- Monotonic deque: each element enters and exits at most once -> O(n) total
- Queue with stacks: each element crosses between stacks at most once -> amortized O(1) pop
"""

"""
==============
QUEUE PATTERNS
==============
"""

"""
================================================================
PATTERN 1: BFS TREE LEVEL-ORDER TRAVERSAL
PATTERN EXPLANATION: Use a queue to visit tree nodes level by level. Record the queue's
current size before each level to know exactly how many nodes to process at that level —
children enqueued during processing belong to the NEXT level. The level_size snapshot
is the key mechanism that separates levels cleanly.

Applications: Level-order traversal, right side view, zigzag traversal, level averages.
================================================================
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BFSTree:
    """
    Problem: Given the root of a binary tree, return the level order traversal
    of its nodes' values (left to right, level by level).

    Example:
        Tree:    3
                / \\
               9  20
                 /  \\
                15   7

        Output: [[3], [9, 20], [15, 7]]

    Steps:
    1. Initialize queue with root
    2. While queue not empty:
       a. Snapshot level_size = len(queue) — all nodes at current level
       b. Process exactly level_size nodes, collecting their values
       c. Enqueue their children (they form the next level)
    3. Append each level's values to result
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:  # LC 102
        """
        TC: O(n) - visit each node exactly once
        SC: O(w) - queue holds at most one level at a time (w = max width)
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result

    # Trace: tree = [3, 9, 20, null, null, 15, 7]
    # queue=[3], level_size=1 -> level=[3], enqueue 9,20
    # queue=[9,20], level_size=2 -> level=[9,20], enqueue 15,7
    # queue=[15,7], level_size=2 -> level=[15,7]
    # Output: [[3],[9,20],[15,7]] ✓

sol = BFSTree()
tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print("Level Order:", sol.levelOrder(tree))  # [[3], [9, 20], [15, 7]]


"""
================================================================
PATTERN 2: BFS GRID / MULTI-SOURCE BFS
PATTERN EXPLANATION: BFS on a 2D grid explores cells layer by layer, guaranteeing
shortest path in unweighted graphs. Multi-source BFS initializes the queue with ALL
starting cells at once — they all process simultaneously, spreading outward in sync.
Mark cells as visited (or modify grid in-place) before enqueuing to prevent reprocessing.

Applications: Rotting oranges, walls and gates, shortest path in maze, flood fill.
================================================================
"""

class BFSGrid:
    """
    Problem: Given an m x n grid where 0 = empty, 1 = fresh orange, 2 = rotten orange.
    Every minute, rotten oranges spread to adjacent fresh oranges (4 directions).
    Return the minimum minutes until no fresh oranges remain, or -1 if impossible.

    Example:
        grid = [[2, 1, 1],
                [1, 1, 0],
                [0, 1, 1]]
        Output: 4

    Steps:
    1. Find all rotten oranges (sources) and count fresh oranges
    2. Multi-source BFS: enqueue all rotten oranges at time=0
    3. Each BFS level = 1 minute; spread rot to adjacent fresh oranges
    4. Return minutes elapsed if fresh_count == 0, else -1
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:  # LC 994
        """
        TC: O(m * n) - each cell visited at most once
        SC: O(m * n) - queue can hold all cells in worst case
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_time = 0

        while queue:
            r, c, time = queue.popleft()
            max_time = max(max_time, time)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, time + 1))

        return max_time if fresh == 0 else -1

    # Trace: grid=[[2,1,1],[1,1,0],[0,1,1]], fresh=6
    # queue=[(0,0,0)]
    # t=0: pop (0,0) -> rot (0,1),(1,0) -> queue=[(0,1,1),(1,0,1)], fresh=4
    # t=1: pop (0,1) -> rot (0,2),(1,1) -> fresh=2
    #      pop (1,0) -> (1,1) already rotten
    # t=2: pop (0,2)->nothing; pop (1,1)->rot (2,1) -> fresh=1
    # t=3: pop (2,1)->rot (2,2) -> fresh=0
    # t=4: pop (2,2)->nothing; fresh=0 -> return 4 ✓

sol = BFSGrid()
print("Rotting Oranges:", sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))  # 4
print("Rotting Oranges:", sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))  # -1


"""
================================================================
PATTERN 3: MONOTONIC DEQUE (SLIDING WINDOW EXTREMES)
PATTERN EXPLANATION: Maintain a deque of indices whose values are in monotonically
decreasing order. When the window slides, remove indices that fell outside the window
from the front. Remove values from the back that can never be the window's maximum —
any value smaller than the current element, added earlier, will always exit first.
The front of the deque is always the index of the current window's maximum.

Applications: Sliding window maximum/minimum, jump game, constrained subsequences.
================================================================
"""

class MonotonicDeque:
    """
    Problem: Given an integer array nums and integer k, return the maximum value
    in each sliding window of size k as the window moves left to right.

    Example:
        nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
        Windows: [1,3,-1]=3, [3,-1,-3]=3, [-1,-3,5]=5, [-3,5,3]=5, [5,3,6]=6, [3,6,7]=7
        Output: [3, 3, 5, 5, 6, 7]

    Steps:
    1. Maintain a deque of indices in decreasing order of their values
    2. For each index i:
       a. Remove front if it is outside the current window (i - deq[0] >= k)
       b. Remove all indices from back whose values < nums[i] (they can never be max)
       c. Append i to deque
       d. Once window is full (i >= k-1), record nums[deq[0]] as the window max
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:  # LC 239
        """
        TC: O(n) - each index pushed and popped at most once
        SC: O(k) - deque stores at most k indices
        """
        result = []
        deq = deque()  # Stores indices, values in decreasing order

        for i in range(len(nums)):
            if deq and deq[0] < i - k + 1:
                deq.popleft()

            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

            deq.append(i)

            if i >= k - 1:
                result.append(nums[deq[0]])

        return result

    # Trace: nums=[1,3,-1,-3,5,3,6,7], k=3
    # i=0 (1):  deq=[0]
    # i=1 (3):  3>1 pop 0 -> deq=[1]
    # i=2 (-1): deq=[1,2], window full -> result=[3]
    # i=3 (-3): deq=[1,2,3], result=[3,3]
    # i=4 (5):  5>-3 pop 3, 5>-1 pop 2, 5>3 pop 1 -> deq=[4], result=[3,3,5]
    # i=5 (3):  deq=[4,5], result=[3,3,5,5]
    # i=6 (6):  6>3 pop 5, 6>5 pop 4 -> deq=[6], result=[3,3,5,5,6]
    # i=7 (7):  7>6 pop 6 -> deq=[7], result=[3,3,5,5,6,7] ✓

sol = MonotonicDeque()
print("Sliding Window Max:", sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
print("Sliding Window Max:", sol.maxSlidingWindow([1], 1))  # [1]


"""
================================================================
PATTERN 4: QUEUE DESIGN (USING TWO STACKS)
PATTERN EXPLANATION: Simulate FIFO queue behavior using two LIFO stacks. The input
stack receives all pushes. On pop/peek, if the output stack is empty, transfer all
elements from input to output (reversing their order once). Because each element is
transferred at most once total, pop is O(1) amortized even though a single transfer
can cost O(n).

Applications: LC 232 (Queue with Stacks), design problems requiring FIFO from LIFO.
================================================================
"""

class QueueWithStacks:
    """
    Problem: Implement a FIFO queue using only two stacks. Support push, pop, peek,
    and empty in O(1) amortized time.

    Example:
        push(1), push(2)
        peek()  -> 1
        pop()   -> 1
        empty() -> False

    Steps:
    1. Two stacks: input_stack (accepts all pushes), output_stack (serves pops/peeks)
    2. push: append to input_stack — O(1)
    3. pop/peek: if output_stack empty, transfer everything from input_stack
       Each element crosses input -> output at most once -> amortized O(1)
    """
    def __init__(self):  # LC 232 - Implement Queue using Stacks
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        """TC: O(1)"""
        self.input_stack.append(x)

    def pop(self) -> int:
        """TC: O(1) amortized"""
        self._transfer()
        return self.output_stack.pop()

    def peek(self) -> int:
        """TC: O(1) amortized"""
        self._transfer()
        return self.output_stack[-1]

    def empty(self) -> bool:
        """TC: O(1)"""
        return not self.input_stack and not self.output_stack

    def _transfer(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

    # Trace: push(1), push(2), peek(), pop()
    # After pushes: input=[1,2], output=[]
    # peek(): output empty -> transfer: input=[], output=[2,1]
    #         output[-1] = 1 (front of queue) ✓
    # pop():  output=[2,1] -> pop -> return 1, output=[2]

q = QueueWithStacks()
q.push(1)
q.push(2)
print("Peek:", q.peek())    # 1
print("Pop:", q.pop())      # 1
print("Empty:", q.empty())  # False
