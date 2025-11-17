"""
=================================================================
GREEDY ALGORITHMS COMPLETE GUIDE
=================================================================

WHAT ARE GREEDY ALGORITHMS?
---------------------------
Greedy algorithms make locally optimal choices at each step with the hope of finding a
global optimum. Unlike dynamic programming which considers all possibilities, greedy makes
one choice and never reconsiders it.

Key characteristics:
- Make the best choice at current step (local optimum)
- Never backtrack or reconsider previous choices
- Assumes local optimum leads to global optimum
- Generally faster than DP but doesn't always work
- Requires proof that greedy choice property holds

Greedy Choice Property:
- A global optimum can be reached by making locally optimal choices
- Not all problems have this property
- When it exists, greedy is optimal and efficient

When to use Greedy:
- Problem asks for maximum/minimum value
- Can prove local optimal choice leads to global optimum
- Choices are irrevocable (can't undo)
- Problem exhibits optimal substructure
- Sorting often reveals greedy strategy

When NOT to use Greedy:
- Need to explore all possibilities (use backtracking/DP)
- Local optimum doesn't guarantee global optimum
- Counterexamples show greedy fails

Common greedy problem types:
- Interval scheduling/merging
- Jump games and array traversal
- Two pointer optimization
- Resource allocation/distribution
- Activity selection
- Huffman coding

GREEDY ALGORITHM CORE TEMPLATES
================================
"""

from typing import List
import heapq
from collections import Counter

# ================================================================
# INTERVAL SCHEDULING TEMPLATE
# ================================================================
def interval_scheduling_template(intervals):
    """
    Template for interval scheduling and merging problems
    
    TC: O(n log n) - sorting dominates
    SC: O(1) for counting, O(n) for returning merged intervals
    
    SOLVES: Problems involving time intervals, meetings, or ranges
    
    WHEN TO USE:
    - Problem gives you intervals/ranges with start and end times
    - Need to select maximum non-overlapping intervals
    - Need to merge overlapping intervals
    - Need to find minimum resources needed (meeting rooms)
    
    KEY INDICATORS:
    - "intervals", "meetings", "appointments"
    - "overlapping", "non-overlapping", "merge"
    - Given array of [start, end] pairs
    
    GREEDY STRATEGY:
    - Sort by end time (or start time depending on variant)
    - For max non-overlapping: pick interval that ends earliest
    - For merging: sort by start, merge if overlapping
    """
    if not intervals:
        return []
    
    # Sort by end time (greedy choice: finish earliest activities first)
    intervals.sort(key=lambda x: x[1])
    
    result = []
    last_end = float('-inf')
    
    for start, end in intervals:
        # If current interval doesn't overlap with last selected
        if start >= last_end:
            result.append([start, end])
            last_end = end
    
    return result

print("Interval Scheduling:", interval_scheduling_template([[1,3],[2,4],[3,5]]))

# ================================================================
# JUMP GAME TEMPLATE
# ================================================================
def jump_game_template(nums):
    """
    Template for jump/reach problems in arrays
    
    TC: O(n) - single pass through array
    SC: O(1) - only track max reach
    
    SOLVES: Problems about reaching end of array with jump constraints
    
    WHEN TO USE:
    - Array represents positions you can move through
    - Each element tells you maximum jump distance from that position
    - Need to determine if end is reachable OR minimum jumps needed
    
    KEY INDICATORS:
    - "jump", "reach", "destination"
    - nums[i] = max jump length from position i
    - "can you reach the last index"
    
    GREEDY STRATEGY:
    - Track maximum reachable position at each step
    - Always try to reach as far as possible
    - If current position > max_reach, impossible
    """
    max_reach = 0
    
    for i in range(len(nums)):
        # If current position is unreachable, can't proceed
        if i > max_reach:
            return False
        
        # Update maximum reachable position from here
        max_reach = max(max_reach, i + nums[i])
        
        # Early termination if can reach end
        if max_reach >= len(nums) - 1:
            return True
    
    return True

print("Jump Game:", jump_game_template([2,3,1,1,4]))

# ================================================================
# TWO POINTER GREEDY TEMPLATE
# ================================================================
def two_pointer_greedy_template(nums):
    """
    Template for two pointer greedy optimization
    
    TC: O(n) - single pass with two pointers
    SC: O(1) - only pointer variables
    
    SOLVES: Problems needing to optimize by choosing between two ends
    
    WHEN TO USE:
    - Have two choices at each step (from left end or right end)
    - Need to maximize/minimize some value
    - Moving one pointer is clearly better than the other
    
    KEY INDICATORS:
    - "maximize", "largest", "most water"
    - Can only choose from two ends
    - No need to consider middle elements first
    
    GREEDY STRATEGY:
    - Start with pointers at both ends
    - Calculate result with current pointers
    - Move pointer that limits the result (the bottleneck)
    """
    left, right = 0, len(nums) - 1
    result = 0
    
    while left < right:
        # Calculate current result
        current = min(nums[left], nums[right]) * (right - left)
        result = max(result, current)
        
        # Greedy choice: move pointer with smaller value (the bottleneck)
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
    
    return result

print("Two Pointer:", two_pointer_greedy_template([1,8,6,2,5,4,8,3,7]))

# ================================================================
# HEAP-BASED GREEDY TEMPLATE
# ================================================================
def heap_greedy_template(tasks):
    """
    Template for greedy with priority queue
    
    TC: O(n log k) - n operations, each O(log k) where k is heap size
    SC: O(k) - heap storage
    
    SOLVES: Problems needing to repeatedly process highest/lowest priority element
    
    WHEN TO USE:
    - Need to repeatedly get max/min element
    - Priority of elements changes over time
    - Order of processing matters
    - Scheduling tasks with frequencies or priorities
    
    KEY INDICATORS:
    - "schedule", "process", "frequency"
    - "most frequent", "highest priority"
    - Priorities change dynamically
    
    GREEDY STRATEGY:
    - Use heap to always get max/min element efficiently
    - Process highest priority element first
    - Update priorities and reinsert into heap
    """
    # Build max heap (negate values for min heap in Python)
    heap = [-count for count in tasks.values()]
    heapq.heapify(heap)
    
    result = 0
    
    while heap:
        # Process highest priority element
        count = -heapq.heappop(heap)
        result += 1
        
        # If more work remains, add back to heap with updated priority
        if count > 1:
            heapq.heappush(heap, -(count - 1))
    
    return result

# ================================================================
# DISTRIBUTION TEMPLATE
# ================================================================
def distribution_template(items, targets):
    """
    Template for greedy distribution/assignment problems
    
    TC: O(n log n + m log m) - sorting both arrays
    SC: O(1) - no extra space (excluding sort space)
    
    SOLVES: Problems about matching or assigning items to targets optimally
    
    WHEN TO USE:
    - Have two arrays: items to assign and targets to assign to
    - Want to maximize number of successful assignments
    - Each item can be assigned to at most one target
    
    KEY INDICATORS:
    - "assign", "distribute", "allocate"
    - "satisfy", "content", "happy"
    - Two arrays with matching criteria
    
    GREEDY STRATEGY:
    - Sort both arrays (usually ascending)
    - Match smallest item to smallest target that it satisfies
    - Use two pointers to traverse both arrays
    """
    items.sort()
    targets.sort()
    
    i, j = 0, 0
    count = 0
    
    # Greedily assign smallest item to smallest satisfiable target
    while i < len(items) and j < len(targets):
        if items[i] <= targets[j]:
            # Item i satisfies target j, make assignment
            count += 1
            i += 1
            j += 1
        else:
            # Item i too big for target j, try next target
            j += 1
    
    return count

# ================================================================
# CIRCULAR ARRAY TEMPLATE
# ================================================================
def circular_array_template(values):
    """
    Template for circular array problems with cumulative tracking
    
    TC: O(n) - single pass
    SC: O(1) - only track totals
    
    SOLVES: Problems where you traverse circular path and track surplus/deficit
    
    WHEN TO USE:
    - Problem involves circular route (end connects to start)
    - Need to find valid starting position
    - Track cumulative gain/loss as you traverse
    
    KEY INDICATORS:
    - "circular", "around", "loop"
    - "gas station", "fuel", "journey"
    - Each position has cost and benefit
    
    GREEDY STRATEGY:
    - Track total (overall balance) and current (from current start)
    - If current goes negative, can't start from any position up to here
    - Try next position as new start
    """
    total_surplus = 0
    current_surplus = 0
    start = 0
    
    for i in range(len(values)):
        total_surplus += values[i]
        current_surplus += values[i]
        
        # If deficit at current position, can't start from here or earlier
        if current_surplus < 0:
            start = i + 1
            current_surplus = 0
    
    # Valid start exists only if total surplus is non-negative
    return start if total_surplus >= 0 else -1


"""
GREEDY PATTERNS
===============
"""

from typing import List
import heapq
from collections import Counter

# ================================================================
# PATTERN 1: INTERVAL SCHEDULING (GREEDY CHOICE)
# PATTERN EXPLANATION: Select optimal intervals from a collection while respecting
# overlap constraints. Sort intervals by a key property (usually end time or start time)
# and greedily make selections. For maximum non-overlapping intervals, always choose
# the one that ends earliest to leave maximum room for future choices. For merging,
# sort by start time and combine overlapping intervals as you go.
#
# TYPICAL STEPS:
# 1. Sort intervals by end time (for max selection) or start time (for merging)
# 2. Initialize tracking variable (last end time, count, result array)
# 3. Iterate through sorted intervals
# 4. For each interval, check if it overlaps with last selected
# 5. If no overlap, select it; if overlap, skip or merge
# 6. Return count, merged intervals, or selected intervals
#
# Applications: Meeting rooms, activity selection, merge intervals, remove overlapping.
# ================================================================

class IntervalScheduling:
    """
    Problem: Given an array of intervals where intervals[i] = [starti, endi], return the
    minimum number of intervals you need to remove to make the rest non-overlapping.
    
    TC: O(n log n) - sorting intervals by end time
    SC: O(1) or O(log n) - depending on sorting implementation
    
    How it works:
    1. Sort intervals by end time (greedy choice: earliest ending first)
    2. Keep track of last selected interval's end time
    3. For each interval, if it starts after last end, select it (non-overlapping)
    4. Count intervals we can keep, return total - kept
    5. Greedy works: earliest ending leaves most room for future intervals
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int: # LC 435
        if not intervals:
            return 0
        
        # Sort by end time (greedy: finish earliest activities first)
        intervals.sort(key=lambda x: x[1])
        
        kept = 1  # Always keep first interval after sorting
        last_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            
            # If current interval doesn't overlap with last kept interval
            if start >= last_end:
                kept += 1
                last_end = end
            # Otherwise, skip this interval (it overlaps)
        
        # Return number of intervals we need to remove
        return len(intervals) - kept

# Example:
# intervals = [[1,2],[2,3],[3,4],[1,3]]
#
# After sorting by end time: [[1,2],[2,3],[1,3],[3,4]]
#
# Step 1: Keep [1,2], last_end = 2
# Step 2: [2,3] starts at 2 >= 2, keep it, last_end = 3
# Step 3: [1,3] starts at 1 < 3, overlaps, remove it
# Step 4: [3,4] starts at 3 >= 3, keep it, last_end = 4
#
# Kept: 3 intervals [[1,2],[2,3],[3,4]]
# Remove: 4 - 3 = 1
# Output: 1

sol = IntervalScheduling()
print("Min intervals to remove:", sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))  # 1
print("Min intervals to remove:", sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))  # 2


# ================================================================
# PATTERN 2: JUMP GAME (MAXIMIZE REACH)
# PATTERN EXPLANATION: Determine reachability or minimum steps in array where each element
# represents maximum jump length. Track the maximum position reachable at each step. Greedy
# works because if we can reach position i, we should always try to reach as far as possible
# from i - there's no benefit to stopping short. For minimum jumps, use BFS-like level
# counting to track jumps needed.
#
# TYPICAL STEPS:
# 1. Initialize max_reach = 0
# 2. For each position i in array:
#    - If i > max_reach, return False (unreachable)
#    - Update max_reach = max(max_reach, i + nums[i])
#    - If max_reach >= last index, return True (early termination)
# 3. Return True if completed loop
#
# Applications: Jump game, minimum jumps, gas station variants.
# ================================================================

class JumpGame:
    """
    Problem: You are given an integer array nums. You are initially positioned at the
    array's first index, and each element represents your maximum jump length.
    
    Return true if you can reach the last index, or false otherwise.
    
    TC: O(n) - single pass through array
    SC: O(1) - only track max reachable position
    
    How it works:
    1. Track maximum position we can reach at each step
    2. If current position is beyond max reach, it's unreachable
    3. Update max reach based on jump length at current position
    4. Greedy works: always maximize reach, no benefit to stopping short
    """
    def canJump(self, nums: List[int]) -> bool: # LC 55
        max_reach = 0
        
        for i in range(len(nums)):
            # If current position is unreachable, return False
            if i > max_reach:
                return False
            
            # Update maximum reachable position from current position
            max_reach = max(max_reach, i + nums[i])
            
            # Early termination: if we can reach the end, return True
            if max_reach >= len(nums) - 1:
                return True
        
        return True

# Example:
# nums = [2,3,1,1,4]
#
# i=0: nums[0]=2, max_reach = max(0, 0+2) = 2
# i=1: nums[1]=3, max_reach = max(2, 1+3) = 4
# i=2: max_reach = 4 >= 4 (last index), return True
#
# Can reach end!
# Output: True
#
# Example 2:
# nums = [3,2,1,0,4]
#
# i=0: max_reach = 3
# i=1: max_reach = max(3, 1+2) = 3
# i=2: max_reach = max(3, 2+1) = 3
# i=3: max_reach = max(3, 3+0) = 3
# i=4: i=4 > max_reach=3, unreachable!
# Output: False

sol = JumpGame()
print("Can jump to end:", sol.canJump([2,3,1,1,4]))  # True
print("Can jump to end:", sol.canJump([3,2,1,0,4]))  # False


# ================================================================
# PATTERN 3: TWO POINTER GREEDY
# PATTERN EXPLANATION: Optimize by choosing between two ends of array. Start with pointers
# at leftmost and rightmost positions. At each step, calculate result with current pointers
# and decide which pointer to move. Key insight: move the pointer that limits (bottlenecks)
# the result. Moving the better pointer would only make things worse, while moving the
# limiting pointer might find a better option.
#
# TYPICAL STEPS:
# 1. Initialize left = 0, right = len(array) - 1
# 2. Initialize result variable
# 3. While left < right:
#    - Calculate current result with pointers
#    - Update best result
#    - Move pointer that limits the result
# 4. Return best result
#
# Applications: Container with most water, trapping rain water, two sum in sorted array.
# ================================================================

class TwoPointerGreedy:
    """
    Problem: You are given an integer array height of length n. There are n vertical lines
    where the two endpoints of the ith line are (i, 0) and (i, height[i]).
    
    Find two lines that together with the x-axis form a container that holds the most water.
    Return the maximum amount of water a container can store.
    
    TC: O(n) - single pass with two pointers
    SC: O(1) - only pointer variables
    
    How it works:
    1. Water contained = min(height[left], height[right]) * (right - left)
    2. Height is limited by shorter line (bottleneck)
    3. Moving shorter line might find taller line and increase water
    4. Moving taller line only decreases width and can't increase water
    5. Greedy works: always move the limiting pointer
    """
    def maxArea(self, height: List[int]) -> int: # LC 11
        left, right = 0, len(height) - 1
        max_water = 0
        
        while left < right:
            # Calculate water with current pointers
            width = right - left
            current_height = min(height[left], height[right])
            current_water = width * current_height
            
            # Update maximum
            max_water = max(max_water, current_water)
            
            # Greedy choice: move the pointer with shorter height (bottleneck)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water

# Example:
# height = [1,8,6,2,5,4,8,3,7]
#
# Visual:
#     |
#     |       |               |
#     |       |       |       |       |
# |   |   |   |   |   |   |   |   |
# 0 1 2 3 4 5 6 7 8
#
# Start: left=0 (height=1), right=8 (height=7)
# Water = min(1,7) * 8 = 8
# Move left (shorter)
#
# left=1 (height=8), right=8 (height=7)
# Water = min(8,7) * 7 = 49
# Move right (shorter)
#
# left=1 (height=8), right=7 (height=3)
# Water = min(8,3) * 6 = 18 (not better)
# Continue...
#
# Maximum water = 49
# Output: 49

sol = TwoPointerGreedy()
print("Max water:", sol.maxArea([1,8,6,2,5,4,8,3,7]))  # 49
print("Max water:", sol.maxArea([1,1]))  # 1


# ================================================================
# PATTERN 4: GREEDY WITH HEAP (PRIORITY QUEUE)
# PATTERN EXPLANATION: Use heap to always process highest or lowest priority element first.
# Useful when priorities change dynamically or when scheduling tasks with frequencies/cooldowns.
# Heap provides O(log k) access to max/min element, much better than repeatedly sorting.
# Process element from heap, update its priority, and reinsert if needed.
#
# TYPICAL STEPS:
# 1. Build heap from initial elements (max heap or min heap)
# 2. While heap not empty (or until goal met):
#    - Extract highest/lowest priority element
#    - Process element
#    - Update priority if needed
#    - Reinsert into heap if more work remains
# 3. Return result (time, count, schedule, etc.)
#
# Applications: Task scheduler, meeting rooms II, merge k sorted lists, IPO.
# ================================================================

class HeapGreedy:
    """
    Problem: Given a char array tasks representing tasks and an integer n representing
    cooldown period, return the minimum number of intervals required to complete all tasks.
    Same task can't be done within n intervals.
    
    TC: O(m log m) where m = number of unique tasks (at most 26)
    SC: O(m) - heap stores unique tasks
    
    How it works:
    1. Use max heap to always schedule most frequent remaining task
    2. Schedule task, reduce its count, wait n intervals before scheduling again
    3. During cooldown, schedule other tasks or idle
    4. Greedy works: prioritizing most frequent task minimizes total time
    """
    def leastInterval(self, tasks: List[str], n: int) -> int: # LC 621
        # Count frequency of each task
        task_counts = Counter(tasks)
        
        # Build max heap (negate values for Python's min heap)
        heap = [-count for count in task_counts.values()]
        heapq.heapify(heap)
        
        time = 0
        
        while heap:
            temp = []  # Store tasks to be added back after cooldown
            
            # Try to schedule n+1 tasks (1 task + n cooldown)
            for i in range(n + 1):
                if heap:
                    count = -heapq.heappop(heap)
                    time += 1
                    
                    # If task has remaining count, store for later
                    if count > 1:
                        temp.append(-(count - 1))
            
            # Add back tasks with remaining count
            for count in temp:
                heapq.heappush(heap, count)
            
            # If heap empty, we're done (don't add idle time at end)
            if not heap:
                break
            
            # If we didn't fill all n+1 slots, we were idle
            # Add idle time to reach n+1 interval
            if len(temp) == 0:
                break
        
        return time
    
    # Simpler mathematical approach
    def leastInterval_math(self, tasks: List[str], n: int) -> int:
        # Count frequencies
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())
        
        # Count how many tasks have max frequency
        max_count = sum(1 for count in task_counts.values() if count == max_freq)
        
        # Minimum intervals = (max_freq - 1) * (n + 1) + max_count
        # OR total tasks if no idle time needed
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)

# Example:
# tasks = ["A","A","A","B","B","B"], n = 2
#
# Frequencies: A=3, B=3
# Max heap: [-3, -3]
#
# Round 1 (schedule 3 tasks: current + 2 cooldown):
#   Schedule A (count 3->2), time=1
#   Schedule B (count 3->2), time=2
#   Idle, time=3
#   Add back A (count 2), B (count 2)
#
# Round 2:
#   Schedule A (count 2->1), time=4
#   Schedule B (count 2->1), time=5
#   Idle, time=6
#   Add back A (count 1), B (count 1)
#
# Round 3:
#   Schedule A (count 1->0), time=7
#   Schedule B (count 1->0), time=8
#   Heap empty, done
#
# Output: 8
# Schedule: A -> B -> idle -> A -> B -> idle -> A -> B

sol = HeapGreedy()
print("Minimum intervals:", sol.leastInterval(["A","A","A","B","B","B"], 2))  # 8
print("Minimum intervals:", sol.leastInterval(["A","A","A","B","B","B"], 0))  # 6


# ================================================================
# PATTERN 5: GREEDY DISTRIBUTION/ASSIGNMENT
# PATTERN EXPLANATION: Match items to targets optimally by sorting both arrays and using
# two pointers. Greedy works because assigning smallest item to smallest satisfiable target
# leaves larger items for larger targets. Sort both arrays in ascending order and greedily
# match from smallest to largest.
#
# TYPICAL STEPS:
# 1. Sort both items array and targets array
# 2. Initialize two pointers i=0, j=0
# 3. While both pointers in bounds:
#    - If items[i] satisfies targets[j], make assignment, increment both
#    - Else, move to next target (current item too large)
# 4. Return count of successful assignments
#
# Applications: Assign cookies, distribute candies, task assignment with constraints.
# ================================================================

class DistributionGreedy:
    """
    Problem: Assume you are a parent trying to give cookies to children. Each child i has
    a greed factor g[i] (minimum cookie size they'll be content with). Each cookie j has
    size s[j]. You can only give one cookie to each child.
    
    Return maximum number of content children.
    
    TC: O(n log n + m log m) - sorting both arrays
    SC: O(1) - no extra space besides pointers
    
    How it works:
    1. Sort both greed factors and cookie sizes
    2. Try to satisfy each child with smallest cookie that works
    3. Greedy works: wasting small cookies on greedy children is suboptimal
    4. Match smallest available cookie to least greedy unsatisfied child
    """
    def findContentChildren(self, g: List[int], s: List[int]) -> int: # LC 455
        # Sort greed factors and cookie sizes
        g.sort()
        s.sort()
        
        child = 0  # Pointer for children
        cookie = 0  # Pointer for cookies
        
        # Try to satisfy each child with smallest suitable cookie
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                # Cookie satisfies this child
                child += 1
                cookie += 1
            else:
                # Cookie too small, try next cookie
                cookie += 1
        
        # Number of children satisfied
        return child

# Example:
# g = [1,2,3], s = [1,1]
# (children's greed factors, cookie sizes)
#
# After sorting: g = [1,2,3], s = [1,1]
#
# child=0 (greed=1), cookie=0 (size=1):
#   1 >= 1, satisfy child 0, move both pointers
#
# child=1 (greed=2), cookie=1 (size=1):
#   1 < 2, cookie too small, move cookie pointer
#
# cookie=2 (out of bounds), stop
#
# Satisfied 1 child
# Output: 1
#
# Example 2:
# g = [1,2], s = [1,2,3]
#
# After sorting: g = [1,2], s = [1,2,3]
#
# child=0 (greed=1), cookie=0 (size=1):
#   1 >= 1, satisfy, move both
#
# child=1 (greed=2), cookie=1 (size=2):
#   2 >= 2, satisfy, move both
#
# All children satisfied
# Output: 2

sol = DistributionGreedy()
print("Content children:", sol.findContentChildren([1,2,3], [1,1]))  # 1
print("Content children:", sol.findContentChildren([1,2], [1,2,3]))  # 2


# ================================================================
# PATTERN 6: CIRCULAR ARRAY/GAS STATION
# PATTERN EXPLANATION: Find valid starting position in circular array by tracking cumulative
# surplus/deficit. Key insight: if total surplus is non-negative, valid start exists. If we
# fail starting from position i and reach position j, all positions between i and j also fail.
# Next possible start is j+1. Track both total and current surplus.
#
# TYPICAL STEPS:
# 1. Initialize total_surplus = 0, current_surplus = 0, start = 0
# 2. For each position i:
#    - Add balance[i] to both totals
#    - If current_surplus < 0:
#      * Can't start from current start or any position before
#      * Set start = i + 1
#      * Reset current_surplus = 0
# 3. Return start if total_surplus >= 0, else -1
#
# Applications: Gas station, circular candy distribution.
# ================================================================

class CircularArrayGreedy:
    """
    Problem: There are n gas stations along a circular route. You have a car with unlimited
    gas tank. It costs cost[i] gas to travel from station i to station i+1.
    You begin with an empty tank at one of the stations.
    
    Given gas[] and cost[], return starting station index if you can travel around circuit
    once, otherwise return -1. Solution is guaranteed to be unique if it exists.
    
    TC: O(n) - single pass through arrays
    SC: O(1) - only track totals
    
    How it works:
    1. Track total surplus (gas - cost for all stations)
    2. Track current surplus from current starting position
    3. If current goes negative, can't start from any position up to here
    4. Try next position as new start
    5. If total >= 0, valid start exists (must be after last failure)
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int: # LC 134
        total_surplus = 0
        current_surplus = 0
        start = 0
        
        for i in range(len(gas)):
            # Net gain/loss at this station
            balance = gas[i] - cost[i]
            
            total_surplus += balance
            current_surplus += balance
            
            # If current surplus negative, can't start from here or earlier
            if current_surplus < 0:
                start = i + 1  # Try next station as start
                current_surplus = 0  # Reset for new start
        
        # Valid start exists only if total surplus is non-negative
        return start if total_surplus >= 0 else -1

# Example:
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
#
# Balance at each station: [-2, -2, -2, 3, 3]
#
# i=0: balance=-2
#   total=-2, current=-2
#   current < 0, start=1, current=0
#
# i=1: balance=-2
#   total=-4, current=-2
#   current < 0, start=2, current=0
#
# i=2: balance=-2
#   total=-6, current=-2
#   current < 0, start=3, current=0
#
# i=3: balance=3
#   total=-3, current=3
#   current >= 0, continue
#
# i=4: balance=3
#   total=0, current=6
#   current >= 0, continue
#
# total=0 >= 0, start=3 is valid
# Output: 3
#
# Verification from station 3:
# Station 3: gas=4, cost=1, have 3 left
# Station 4: gas=5, cost=2, have 3+5-2=6 left
# Station 0: gas=1, cost=3, have 6+1-3=4 left
# Station 1: gas=2, cost=4, have 4+2-4=2 left
# Station 2: gas=3, cost=5, have 2+3-5=0 left
# Back to station 3: Success!

sol = CircularArrayGreedy()
print("Starting station:", sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))  # 3
print("Starting station:", sol.canCompleteCircuit([2,3,4], [3,4,3]))  # -1
