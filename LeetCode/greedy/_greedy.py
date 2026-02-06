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
- String partitioning and construction
- Activity selection
"""

from typing import List
import heapq
from collections import Counter

"""
================================================================
PATTERN 1: INTERVAL SELECTION
================================================================

PATTERN EXPLANATION: Select maximum non-overlapping intervals. This is GREEDY because:
- Multiple solutions exist, you make CHOICES at each step
- Optimizing: maximize count selected
- Greedy choice: always pick interval that ENDS earliest

KEY INSIGHT: Picking earliest-ending interval leaves most room for future selections.

Example: [[1,10], [2,3], [4,5]]
- Pick [1,10] first → only get 1 interval (bad)
- Pick [2,3] first (ends earliest) → can also pick [4,5] → 2 intervals ✓

TYPICAL STEPS:
1. Sort by END time
2. Select first interval, track last_end
3. For each remaining: if start > last_end, select it
4. Return count

RELATED: MERGE INTERVALS (LC 56) - NOT GREEDY
- Merge overlapping intervals. NOT greedy because there's only ONE correct solution (no choices - you MUST merge overlaps). Sort by START time instead of END time.

Example: [[1,3], [2,6]] → MUST merge to [1,6] (deterministic, no choice)
================================================================
"""

class IntervalSelection:
    """
    You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti. A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

    Return the length longest chain which can be formed. You do not need to use up all the given intervals. You can select pairs in any order.

    Example 1:
    Input: pairs = [[1,2],[2,3],[3,4]]
    Output: 2
    Explanation: The longest chain is [1,2] -> [3,4].

    Example 2:
    Input: pairs = [[1,2],[7,8],[4,5]]
    Output: 3
    Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
    
    How it works:
    1. Sort pairs by end time (greedy choice: earliest ending first)
    2. Always select pair that finishes earliest
    3. For each pair, if it doesn't overlap with last selected, take it
    4. Count total pairs selected
    5. Greedy works: earliest ending leaves most room for future selections
    """
    def findLongestChain(self, pairs: List[List[int]]) -> int: # LC 646
        """
        - TC: O(n log n) - sorting intervals by end time, loop through pairs
        - SC: O(1) or O(log n) - depending on sorting implementation
        """
        if not pairs:
            return 0
        
        # Sort by end time (greedy: finish earliest activities first)
        pairs.sort(key=lambda x: x[1])
        
        count = 1  # Always select first pair after sorting
        last_end = pairs[0][1] # get end of first interval
        
        for i in range(1, len(pairs)):
            start, end = pairs[i]
            
            # If current pair doesn't overlap with last selected pair
            # (pair follows: previous end < current start)
            if start > last_end:
                count += 1
                last_end = end # update end of prev interval
        
        return count

sol = IntervalSelection()
print("Longest chain:", sol.findLongestChain([[1,2],[2,3],[3,4]]))  # 2
print("Longest chain:", sol.findLongestChain([[1,2],[7,8],[4,5]]))  # 3

"""
================================================================
PATTERN 2: JUMP GAME (MAXIMIZE REACH)

PATTERN EXPLANATION: Determine reachability or minimum steps in array where each element represents maximum jump length. Track the maximum position reachable at each step. Greedy works because if we can reach position i, we should always try to reach as far as possible from i - there's no benefit to stopping short. For minimum jumps, use BFS-like level counting to track jumps needed.

TYPICAL STEPS:
1. Initialize max_reach = 0
2. For each position i in array:
   - If i > max_reach, return False (unreachable)
   - Update max_reach = max(max_reach, i + nums[i])
   - If max_reach >= last index, return True (early termination)
3. Return True if completed loop

Applications: Jump game, minimum jumps, gas station variants.
================================================================
"""

class JumpGame:
    """
    You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
    
    Return true if you can reach the last index, or false otherwise.

    Example 1:
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

    Example 2:
    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
    
    How it works:
    1. Track maximum position we can reach at each step
    2. If current position is beyond max reach, it's unreachable
    3. Update max reach based on jump length at current position
    4. Greedy works: always maximize reach, no benefit to stopping short
    """
    def canJump(self, nums: List[int]) -> bool: # LC 55
        """
        - TC: O(n) - single pass through array
        - SC: O(1) - only track max reachable position
        """
        farthest = 0 # Track the farthest index we can reach
        
        # Check each position we can actually reach
        for i in range(len(nums)):
            # If current position is beyond our reach, we're stuck
            if i > farthest:
                return False
            
            # Update the farthest position we can reach from here
            farthest = max(farthest, i + nums[i])
            
            # Early exit: if we can already reach the end
            if farthest >= len(nums) - 1:
                return True
        
        return True

sol = JumpGame()
print("Can jump to end:", sol.canJump([2,3,1,1,4]))  # True
print("Can jump to end:", sol.canJump([3,2,1,0,4]))  # False

"""
================================================================
PATTERN 3: TWO POINTER GREEDY
PATTERN EXPLANATION: Optimize by choosing between two ends of array. Start with pointers at leftmost and rightmost positions. At each step, calculate result with current pointers and decide which pointer to move. Key insight: move the pointer that limits (bottlenecks) the result. Moving the better pointer would only make things worse, while moving the limiting pointer might find a better option.

TYPICAL STEPS:
1. Initialize left = 0, right = len(array) - 1
2. Initialize result variable
3. While left < right:
   - Calculate current result with pointers
   - Update best result
   - Move pointer that limits the result
4. Return best result

Applications: Container with most water, trapping rain water, two sum in sorted array.
================================================================
"""

class TwoPointerGreedy:
    """
    Problem: You are given an integer array height of length n. There are n vertical lines
    where the two endpoints of the ith line are (i, 0) and (i, height[i]).
    
    Find two lines that together with the x-axis form a container that holds the most water.
    Return the maximum amount of water a container can store.

    Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49 goes from index 1 (8) to index 8 (7).
    
    How it works:
    1. Water contained = min(height[left], height[right]) * (right - left)
    2. Height is limited by shorter line (bottleneck)
    3. Moving shorter line might find taller line and increase water
    4. Moving taller line only decreases width and can't increase water
    5. Greedy works: always move the limiting pointer
    """
    def maxArea(self, height: List[int]) -> int: # LC 11
        """
        - TC: O(n) - single pass with two pointers
        - SC: O(1) - only pointer variables
        """
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

sol = TwoPointerGreedy()
print("Max water:", sol.maxArea([1,8,6,2,5,4,8,3,7]))  # 49
print("Max water:", sol.maxArea([1,1]))  # 1

"""
================================================================
PATTERN 4: GREEDY WITH HEAP (PRIORITY QUEUE)
================================================================

PATTERN EXPLANATION: Combine greedy choices with a heap to track and optimize decisions.
This is GREEDY because:
- Multiple solutions exist, you make CHOICES at each step
- Optimizing: maximize reach/minimize cost/maximize profit
- Heap maintains best candidates for optimization

KEY INSIGHT: Heap enables "retroactive greedy" - make optimistic choices, then use heap
to find and fix suboptimal past decisions when constraints are violated.

Why not just greedy without heap?
- Greedy alone: might need future information you don't have yet
- Heap solution: make optimistic choices, use heap to retroactively optimize

TYPICAL STEPS:
1. Process elements sequentially (or sort first)
2. Make optimistic greedy choices
3. Use heap to track choices that can be "swapped" or "revised"
4. When constraint violated, use heap to find and fix worst past choice
5. Repeat until all elements processed

Applications: Resource allocation, task scheduling, k-way merges, capital optimization.
================================================================
"""

class HeapGreedy:
    """
    Problem: You are climbing buildings. To go from building i to i+1:
    - If heights[i+1] <= heights[i]: free (going down or same)
    - If heights[i+1] > heights[i]: need bricks OR a ladder for the climb
    
    Bricks: Use (heights[i+1] - heights[i]) bricks for the climb
    Ladders: Skip any climb (unlimited height), but you have limited ladders
    
    Return the furthest building index you can reach.
    
    Example 1:
    Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
    Output: 4
    Explanation: Starting at 0, you can reach 4:
    - 0→1: down (free)
    - 1→2: climb 5, use ladder
    - 2→3: down (free)  
    - 3→4: climb 3, use bricks (5-3=2 left)
    - 4→5: climb 5, need 5 bricks but only have 2 ❌
    
    How it works:
    1. Greedy strategy: Save ladders for BIGGEST climbs (but we don't know future!)
    2. Solution: Use ladders OPTIMISTICALLY, track in min heap
    3. When out of ladders, swap SMALLEST ladder-climb for bricks (heap gives us this)
    4. This ensures ladders end up on the biggest climbs
    5. Greedy works: retrospectively optimizing ensures optimal resource allocation
    """
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int: # LC 1642
        """
        TC: O(n * log(ladders)) where n = number of buildings
            - Iterate through n-1 gaps between buildings: O(n)
            - For each gap with a climb:
                - heappush: O(log k) where k = heap size
                - heappop: O(log k)
            - Heap size is bounded by (ladders + 1) since we pop when exceeding
            - Therefore: O(n * log(ladders))
    
        SC: O(ladders)
            - Min heap stores at most (ladders + 1) elements temporarily
            - After popping, heap maintains exactly 'ladders' elements
            - No other data structures scale with input size
        """
        # Min heap tracks climbs where we've used ladders
        # Stores the HEIGHT of each climb, smallest on top
        ladder_climbs = []
        
        for i in range(len(heights) - 1):
            climb_height = heights[i + 1] - heights[i]
            
            # No resources needed for going down or staying level
            if climb_height <= 0:
                continue
            
            # Use a ladder for this climb (optimistic choice)
            heapq.heappush(ladder_climbs, climb_height)
            
            # If we've used more ladders than available
            if len(ladder_climbs) > ladders:
                # Swap the smallest ladder-climb for bricks instead (min heap)
                # This keeps ladders on the biggest climbs
                smallest_climb = heapq.heappop(ladder_climbs)
                bricks -= smallest_climb
                
                # Can't proceed without enough bricks
                if bricks < 0:
                    return i
        
        # Successfully reached the last building
        return len(heights) - 1

# Example walkthrough:
# heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
#
# i=0: 4→2, climb=-2, going down (skip)
# i=1: 2→7, climb=5, use ladder → heap=[5], ladders_used=1
# i=2: 7→6, climb=-1, going down (skip)
# i=3: 6→9, climb=3, use ladder → heap=[3,5], ladders_used=2
#      But we only have 1 ladder! Swap smallest:
#      Pop 3 from heap, use bricks instead → bricks=5-3=2, heap=[5]
# i=4: 9→14, climb=5, use ladder → heap=[5,5], ladders_used=2
#      But we only have 1 ladder! Swap smallest:
#      Pop 5 from heap, use bricks instead → bricks=2-5=-3 ❌
#      Not enough bricks! Return i=4
#
# Output: 4 (can reach building at index 4)
#
# Why greedy works:
# By always swapping smallest ladder-climb for bricks, we ensure ladders
# end up on the BIGGEST climbs. Since ladders can handle any height but
# bricks are limited, this minimizes brick usage and maximizes reach.

sol = HeapGreedy()
print("Furthest building:", sol.furthestBuilding([4,2,7,6,9,14,12], 5, 1))  # 4
print("Furthest building:", sol.furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2))  # 7
print("Furthest building:", sol.furthestBuilding([14,3,19,3], 17, 0))  # 3

"""
================================================================
PATTERN 5: GREEDY DISTRIBUTION/ASSIGNMENT
PATTERN EXPLANATION: Match items to targets optimally by sorting both arrays and using
two pointers. Greedy works because assigning smallest item to smallest satisfiable target
leaves larger items for larger targets. Sort both arrays in ascending order and greedily
match from smallest to largest.

TYPICAL STEPS:
1. Sort both items array and targets array
2. Initialize two pointers i=0, j=0
3. While both pointers in bounds:
   - If items[i] satisfies targets[j], make assignment, increment both
   - Else, move to next target (current item too large)
4. Return count of successful assignments

Applications: Assign cookies, distribute candies, task assignment with constraints.
================================================================
"""

class DistributionGreedy:
    """
    Problem: Assume you are a parent trying to give cookies to children. Each child i has
    a greed factor g[i] (minimum cookie size they'll be content with). Each cookie j has
    size s[j]. You can only give one cookie to each child.
    
    Return maximum number of content children.
    
    How it works:
    1. Sort both greed factors and cookie sizes
    2. Try to satisfy each child with smallest cookie that works
    3. Greedy works: wasting small cookies on greedy children is suboptimal
    4. Match smallest available cookie to least greedy unsatisfied child
    """
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        TC: O(n log n + m log m) where n = len(g), m = len(s)
            - Sorting greed factors: O(n log n)
            - Sorting cookie sizes: O(m log m)
            - Iterating through cookies: O(m)
            - Dominated by sorting: O(n log n + m log m)
    
        SC: O(n + m)
            - Python's sort uses O(n) and O(m) auxiliary space worst case
            - Child pointer: O(1)
        """
        # Sort greed factors and cookie sizes
        g.sort()
        s.sort()
        
        child = 0  # Pointer for children (tracks next child to satisfy)
        
        # Try each cookie in order (smallest to largest)
        for cookie_size in s:
            # If current cookie satisfies current child's greed
            if child < len(g) and cookie_size >= g[child]:
                child += 1  # Move to next child
        
        # Number of children satisfied
        return child

sol = DistributionGreedy()
print("Content children:", sol.findContentChildren([1,2,3], [1,1]))  # 1
print("Content children:", sol.findContentChildren([1,2], [1,2,3]))  # 2

"""
================================================================
PATTERN 6: STRING PARTITIONING (GREEDY EXTENSION)
PATTERN EXPLANATION: Partition string or array into optimal segments by tracking boundaries
and greedily extending partitions. Key insight: once we see a character, we must include
all its occurrences in current partition. Track the furthest position we must reach before
closing current partition, then start new partition.

TYPICAL STEPS:
1. Precompute last occurrence of each character/element
2. Initialize partition start and end boundaries
3. For each position:
   - Update partition end to max(end, last_occurrence[char])
   - If reached partition end, close partition and start new one
4. Return list of partition sizes or boundaries

Applications: Partition labels, split array into consecutive subsequences, string construction.
================================================================
"""

class StringPartitioning:
    """
    Problem: You are given a string s. Partition s into as many parts as possible so that
    each letter appears in at most one part. Return a list of integers representing the
    size of these parts.
    
    How it works:
    1. Precompute last occurrence index for each character
    2. Track current partition boundary (end)
    3. For each character, GREEDY CHOICE: immediately commit to extending current partition 
       to include its last occurrence (no backtracking, no trying alternatives)
    4. Keep extending until we reach partition boundary, then close it (all chars complete)
    5. Why greedy works: once we see a character, we MUST include all its occurrences in 
       current partition. Extending to furthest occurrence guarantees this while maximizing 
       number of partitions (we close as soon as possible)
    """
    def partitionLabels(self, s: str) -> List[int]:
        """
        Example: "ababcbacadefegdehijhklij"
                -> [9, 7, 8]
        
        - TC: O(n) - two passes (one for last occurrence, one for partitioning)
        - SC: O(1) - hash map stores at most 26 characters
        """
        # Store last occurrence of each character
        # Key insight: Once we reach a char's last occurrence, we'll NEVER see it again
        # This tells us when it's safe to close a partition (all chars in it are complete)
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i  # Overwrites previous value if char seen before
        
        result = []
        partition_start = 0
        partition_end = 0
        
        for i, char in enumerate(s):
            # Greedy choice -> If I see a character, I immediately commit to extending my current partition to include ALL occurrences of that character.
            partition_end = max(partition_end, last_occurrence[char])
            
            # When we reach partition boundary, all chars are complete
            if i == partition_end:
                result.append(partition_end - partition_start + 1)
                partition_start = i + 1
        
        return result

# Example:
# s = "ababcbaca"
#
# last_occurrence = {'a': 8, 'b': 5, 'c': 7}
# partition_start = 0
# partition_end = 0

# i=0, char='a':
#     partition_end = max(0, 8) = 8     -> Must go to index 8 to include all 'a's
#     i (0) != partition_end (8)        -> Can't close partition yet
    
# i=1, char='b':
#     partition_end = max(8, 5) = 8     -> Still need to reach 8 (already extended)
#     i (1) != partition_end (8)
    
# i=2, char='a':
#     partition_end = max(8, 8) = 8     -> Already planning to go to 8
#     i (2) != partition_end (8)
    
# i=3, char='b':
#     partition_end = max(8, 5) = 8
#     i (3) != partition_end (8)
    
# i=4, char='c':
#     partition_end = max(8, 7) = 8     -> Still need to reach 8
#     i (4) != partition_end (8)
    
# i=5, char='b':
#     partition_end = max(8, 5) = 8
#     i (5) != partition_end (8)
    
# i=6, char='a':
#     partition_end = max(8, 8) = 8
#     i (6) != partition_end (8)
    
# i=7, char='c':
#     partition_end = max(8, 7) = 8
#     i (7) != partition_end (8)
    
# i=8, char='a':
#     partition_end = max(8, 8) = 8
#     i (8) == partition_end (8)        -> ✓ Reached the boundary!
#     result.append(9)                   -> Partition size = 8 - 0 + 1 = 9
#     partition_start = 9                -> Next partition starts here

sol = StringPartitioning()
print("Partition sizes:", sol.partitionLabels("ababcbacadefegdehijhklij"))  # [9, 7, 8]
print("Partition sizes:", sol.partitionLabels("eccbbbbdec"))  # [10]