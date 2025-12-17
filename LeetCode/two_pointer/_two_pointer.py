"""
=================================================================
TWO POINTERS COMPLETE GUIDE
=================================================================

WHAT IS THE TWO POINTERS PATTERN?
---------------------------------
Two pointers is a technique where we use two references (pointers/indices) to traverse a data structure, typically an array or string. The pointers can move in various ways to efficiently solve problems that would otherwise require nested loops.

Key characteristics:
- Uses two index variables to traverse data structure
- Reduces O(n²) brute force to O(n) in many cases
- Eliminates need for nested loops
- Often works on sorted or partially sorted data
- Usually requires O(1) extra space

TIME COMPLEXITY ADVANTAGE:
-------------------------
Brute Force vs Two Pointers:

Example: Find pair with target sum in sorted array of size n
- Brute Force: Check every pair with nested loops
  TC: O(n²) - outer loop n times, inner loop n times
  For each pair (i,j), check if arr[i] + arr[j] == target
  
- Two Pointers (array must be sorted): Start at ends, converge based on sum 
  TC: O(n) - each pointer moves at most n times total
  Single pass, pointers meet in middle
  
Speedup: O(n²) → O(n)
For n=1000: 1,000,000 comparisons → 1,000 comparisons (1000x faster!)

Example: Remove duplicates from sorted array in-place
- Brute Force: For each element, shift remaining elements
  TC: O(n²) - n elements, each requires O(n) shifting
  
- Two Pointers: Slow tracks write position, fast explores
  TC: O(n) - single pass, each element visited once
  
Speedup: O(n²) → O(n)

Example: Find triplet with target sum (3Sum)
- Brute Force: Three nested loops to check all triplets
  TC: O(n³) - check all n³ combinations
  
- Two Pointers: Fix one element, use two pointers for remaining
  TC: O(n²) - outer loop O(n), inner two pointers O(n)
  
Speedup: O(n³) → O(n²)
For n=1000: 1,000,000,000 operations → 1,000,000 operations (1000x faster!)

KEY INSIGHT: Two pointers avoids redundant work by:
1. Making intelligent movement decisions (not checking all pairs)
2. Using sorted order to eliminate impossible candidates
3. Processing each element limited number of times (not nested iteration)
4. Converging from both ends or maintaining fixed relationship

Movement patterns:
- Opposite direction: Start at both ends, move toward center
- Same direction: Both move left-to-right, at same or different speeds
- Fixed gap: Maintain constant distance between pointers

When to use Two Pointers:
- Problem involves sorted array/string
- Need to find pairs or triplets with specific properties
- Need to modify array in-place
- Detect cycles or find middle element
- Merge multiple sorted structures

When NOT to use Two Pointers:
- Need to track multiple elements (use hash map)
- Order doesn't matter and need frequency counts
- Need all combinations (use backtracking)
- Data structure doesn't support index access (like trees)

NEED SORTED ARRAY:
------------------
✓ Two Sum / 3Sum / k-Sum problems
    - Must know: left→right = increasing values
    - Decision: sum too small? move left. sum too large? move right.

✓ Finding pairs with target sum/difference
    - Need predictable value ordering

✓ Merging sorted arrays
    - Compare heads, build sorted result

✓ Closest pair to target
    - Move pointers based on comparison to target

Rule: Need sorting when pointer movement depends on VALUE COMPARISON and knowing which direction has larger/smaller values.


DON'T NEED SORTING:
-------------------
✓ Fast/Slow pointers (linked lists)
    - Cycle detection, find middle, nth from end
    - Based on structure/speed, not values

✓ Same-direction partition
    - Remove duplicates, move zeros, partition by condition
    - Grouping elements, order doesn't matter

✓ Palindrome checking
    - Must preserve original order!

✓ Container with water, trapping rain water
    - Use heights/indices as given

Rule: Don't need sorting when pointer movement is based on POSITION, STRUCTURE, or CONDITIONS unrelated to sorted order.


KEY INSIGHT:
-----------
SORTED = Can make intelligent decisions about which direction to move based on value comparisons
NOT SORTED = Movement based on position, structure, or other logic

# ==============================================
#             TWO POINTERS PATTERNS
# ============================================== 
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

# ================================================================
# PATTERN 1: OPPOSITE DIRECTION (CONVERGING)
# PATTERN EXPLANATION: Start with pointers at both ends of array and move them toward the center. Make decisions at each step about which pointer to move based on the problem's goal - either finding a match, optimizing a value, or validating a property. Continue until pointers meet. Common in sorted arrays where you can eliminate half the search space at each step.
#
# TYPICAL STEPS:
# 1. Initialize left=0, right=len(arr)-1
# 2. While left < right:
#    - Calculate/compare values at both pointers
#    - If condition met, return result
#    - Decide which pointer to move (or both)
#    - Move pointer(s) inward
# 3. Return result after pointers meet
#
# Applications: Two sum in sorted array, pair finding, palindrome validation, container optimization.
# ================================================================
"""
from typing import List, Optional

class OppositeDirectionPattern:
    """
    Problem: Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target.

    Return the indices (1-indexed) of the two numbers.
    
    How it works:
    1. Start with pointers at both ends
    2. Calculate sum of values at both pointers
    3. If sum too small, move left right (increase sum)
    4. If sum too large, move right left (decrease sum)
    5. If sum equals target, found the pair
    
    Why it works:
    - Array is sorted, so left has smaller values, right has larger
    - Moving left increases sum, moving right decreases sum
    - This allows us to "navigate" to the target sum efficiently
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]: # LC 167
        """
        - TC: O(n) - single pass with two pointers moving inwards
        - SC: O(1) - only two pointer variables
        """
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # Return 1-indexed
            elif current_sum < target:
                left += 1  # Need larger sum
            else:
                right -= 1  # Need smaller sum
        
        return []  # No solution (shouldn't happen per problem constraints)

# Example:
# numbers = [2,7,11,15], target = 9
#
# Step 1: left=0 (2), right=3 (15)
#   Sum = 2 + 15 = 17 > 9
#   Move right left
#
# Step 2: left=0 (2), right=2 (11)
#   Sum = 2 + 11 = 13 > 9
#   Move right left
#
# Step 3: left=0 (2), right=1 (7)
#   Sum = 2 + 7 = 9 ✓
#   Found pair!
#
# Output: [1, 2] (1-indexed)

sol = OppositeDirectionPattern()
print("Two sum:", sol.twoSum([2,7,11,15], 9))  # [1,2]
print("Two sum:", sol.twoSum([2,3,4], 6))  # [1,3]

"""
================================================================
PATTERN 2: SAME DIRECTION (PARTITION/WRITE)
PATTERN EXPLANATION: Both pointers move in the same direction, with one (slow) tracking the write/boundary position and the other (fast) exploring to find valid elements. Slow pointer marks where the next valid element should be written, while fast pointer scans ahead. This pattern enables in-place modifications without extra space.

TYPICAL STEPS:
1. Initialize slow=0 (or 1), fast=0 (or 1)
2. While fast < len(arr):
   - Check if arr[fast] is valid
   - If valid, write to arr[slow] and increment slow
   - Always increment fast
3. Return slow (new length) or modified array

Applications: Remove duplicates, remove elements, move zeros, partition array.
================================================================
"""

class SameDirectionPattern:
    """
    Problem: Given an integer array nums sorted in non-decreasing order, remove duplicates in-place such that each unique element appears only once. Return the number of unique elements k. First k elements of nums should contain unique elements in order.
    
    How it works:
    1. Slow pointer tracks where to write next unique element
    2. Fast pointer explores array looking for unique elements
    3. When fast finds unique element (different from previous), write to slow position
    4. Slow advances only when we write a unique element
    
    Why it works:
    - Array is sorted, so duplicates are adjacent
    - Slow maintains boundary between processed and unprocessed
    - Fast finds next unique, slow marks where to place it
    """
    def removeDuplicates(self, nums: List[int]) -> int: # LC 26
        """
        - TC: O(n) - single pass through array with fast pointer
        - SC: O(1) - in-place modification, only pointer vars
        """
        if not nums: # Edge Case -> empty array has 0 unique ele
            return 0
        
        slow = 1  # Write position for next unique element (first element always unique)
        
        for fast in range(1, len(nums)):  # Explore from index 1
            # If curr ele different from prev, it's unique
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]  # Write unique ele
                slow += 1  # Move write position
        
        return slow  # Number of unique elements

# Example:
# nums = [0,0,1,1,1,2,2,3,3,4]
#
# Initial: slow=1, fast=1
# nums = [0,0,1,1,1,2,2,3,3,4]
#         s f
#
# fast=1: nums[1]=0 == nums[0]=0, skip
#
# fast=2: nums[2]=1 != nums[1]=0, unique!
#   Write nums[1]=1: [0,1,1,1,1,2,2,3,3,4]
#   slow=2
#
# fast=3: nums[3]=1 == nums[2]=1, skip
# fast=4: nums[4]=1 == nums[3]=1, skip
#
# fast=5: nums[5]=2 != nums[4]=1, unique!
#   Write nums[2]=2: [0,1,2,1,1,2,2,3,3,4]
#   slow=3
#
# Continue...
# Final: [0,1,2,3,4,_,_,_,_,_]
# Output: 5

sol = SameDirectionPattern()
test_nums = [0,0,1,1,1,2,2,3,3,4]
print("Unique count:", sol.removeDuplicates(test_nums))  # 5
print("Modified array:", test_nums[:5])  # [0,1,2,3,4]

"""
================================================================
PATTERN 3: FAST/SLOW (DIFFERENT SPEEDS)
PATTERN EXPLANATION: Two pointers start at same position but move at different speeds. Slow moves 1 step at a time, fast moves 2 steps. If there's a cycle, fast will eventually catch up to slow (they'll meet). If no cycle, fast reaches end first. Also used to find middle element (when fast reaches end, slow is at middle) or maintain fixed gap.

TYPICAL STEPS (Cycle Detection):
1. Initialize slow=head, fast=head
2. While fast and fast.next exist:
   - Move slow one step: slow = slow.next
   - Move fast two steps: fast = fast.next.next
   - If slow == fast, cycle detected
3. If fast reaches null, no cycle

Applications: Cycle detection, find middle, find nth from end, happy number.
================================================================
"""

class FastSlowPattern:
    """
    Problem: Given head of linked list, determine if it has a cycle. A cycle exists if a node can be reached again by following next pointers.
    
    How it works (Floyd's Cycle Detection):
    1. Slow pointer moves 1 step, fast moves 2 steps
    2. If cycle exists, fast will eventually catch slow (meet in cycle)
    3. If no cycle, fast reaches end (null) first
    
    Why it works:
    - In cycle, fast gains 1 step on slow per iteration
    - Eventually fast catches up (like runners on circular track)
    - If no cycle, fast reaches end in n/2 steps
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool: # LC 141
        """
        - TC: O(n) - fast pointer visits at most 2n nodes before meeting slow or reaching end
        - SC: O(1) - only two pointer variables
        """
        if not head or not head.next: # Empty LL or one node
            return False
        
        slow = head 
        fast = head
        
        while fast and fast.next: 
            slow = slow.next          # Move 1 step
            fast = fast.next.next     # Move 2 steps
            
            if slow == fast:          # Pointers met
                return True
        
        return False  # Fast reached end, no cycle

# Example with cycle:
# List: 3 → 2 → 0 → -4 ↩ (connects back to 2)
#
# Step 1: slow=3, fast=3
# Step 2: slow=2, fast=0
# Step 3: slow=0, fast=2
# Step 4: slow=-4, fast=-4  ← They meet!
# Output: True
#
# Example without cycle:
# List: 1 → 2 → 3 → 4 → null
#
# Step 1: slow=1, fast=1
# Step 2: slow=2, fast=3
# Step 3: slow=3, fast=null (fast.next doesn't exist)
# Output: False

# Alternative: Find middle element
class FindMiddleExample:
    """Shows fast/slow for finding middle"""
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]: # LC 876
        slow = head
        fast = head
        
        # When fast reaches end, slow is at middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

sol = FastSlowPattern()
# Test with cycle
cycle_head = ListNode(3)
cycle_head.next = ListNode(2)
cycle_head.next.next = ListNode(0)
cycle_head.next.next.next = ListNode(-4)
cycle_head.next.next.next.next = cycle_head.next  # Create cycle
print("Has cycle:", sol.hasCycle(cycle_head))  # True

# Test without cycle
no_cycle = ListNode(1, ListNode(2, ListNode(3)))
print("Has cycle:", sol.hasCycle(no_cycle))  # False

"""
================================================================
PATTERN 4: K-SUM (FIX + CONVERGE)
PATTERN EXPLANATION: Reduce k-sum problem to 2-sum by fixing the first k-2 elements with nested loops, then using two pointers on remaining elements. For 3-sum, fix one element and use two pointers. For 4-sum, fix two elements and use two pointers. This
reduces time complexity from O(n^k) to O(n^(k-1)).

TYPICAL STEPS (for 3-sum):
1. Sort array (required for two pointer optimization)
2. For each index i (fixing first element):
   - Skip duplicates of fixed element
   - Set left=i+1, right=len-1
   - While left < right:
     * Calculate sum with fixed element
     * If sum == target, save result, move both pointers
     * If sum < target, move left right
     * If sum > target, move right left
     * Skip duplicates while moving
3. Return all unique triplets/quadruplets

Applications: 3sum, 4sum, 3sum closest, triplet problems in sorted arrays.
================================================================
"""

class KSumPattern:
    """
    Problem: Given integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
    such that i != j != k and nums[i] + nums[j] + nums[k] = 0. (i, j, and k must be different indexes)
    
    The solution set must not contain duplicate triplets. (Cannot have the same triplet using different indicies)
    
    How it works:
    1. Sort array (enables two pointer optimization)
    2. Fix first element with loop
    3. Use two pointers to find pairs that complete triplet to target sum
    4. Skip duplicates to avoid duplicate triplets
    5. Reduces 3-sum to 2-sum problem for each fixed element
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]: # LC 15
        """
        - TC: O(n²) - sort O(n log n), then O(n) outer loop x O(n) two pointer = O(n²)
        - SC: O(1) or O(n) depending on how you count sorting space
        """
        nums.sort()  # Required for two pointer approach
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicate fixed elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two pointers for remaining elements
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0: # Case 1: found triplets
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1 # If no skips, move l and r pointers
                    right -= 1
                
                # Case 2: Sum too small
                elif current_sum < 0:
                    left += 1  # Need larger sum
                else: # Case 3: Sum too large
                    right -= 1  # Need smaller sum
        
        return result

# Example:
# nums = [-1,0,1,2,-1,-4]
#
# After sort: [-4,-1,-1,0,1,2]
#
# i=0 (fix -4):
#   left=1 (-1), right=5 (2)
#   Sum = -4 + (-1) + 2 = -3 < 0, move left
#   Continue... no valid triplet with -4
#
# i=1 (fix -1):
#   left=2 (-1), right=5 (2)
#   Sum = -1 + (-1) + 2 = 0 ✓
#   Found: [-1, -1, 2]
#   
#   Skip duplicates, move both
#   left=3 (0), right=4 (1)
#   Sum = -1 + 0 + 1 = 0 ✓
#   Found: [-1, 0, 1]
#
# i=2: Skip (duplicate -1)
# Continue...
#
# Output: [[-1,-1,2], [-1,0,1]]

sol = KSumPattern()
print("3Sum:", sol.threeSum([-1,0,1,2,-1,-4]))  # [[-1,-1,2],[-1,0,1]]
print("3Sum:", sol.threeSum([0,1,1]))  # []

"""
================================================================
PATTERN 5: MULTI-ARRAY MERGE (ONE POINTER PER ARRAY)
PATTERN EXPLANATION: Maintain one pointer for each input array. Compare elements at current pointers, select smallest/largest based on problem, and advance that pointer. Continue until all arrays exhausted. Common in merging sorted structures or finding common/union elements across multiple sorted arrays.

TYPICAL STEPS:
1. Initialize pointer for each array (i=0, j=0, etc.)
2. While pointers within bounds:
   - Compare elements at current pointers
   - Select element based on criteria (min for merge, equal for intersection)
   - Add to result if applicable
   - Advance pointer of selected element
3. Handle remaining elements from arrays
4. Return merged result

Applications: Merge sorted arrays, array intersection, merge intervals.
================================================================
"""

class MultiArrayPattern:
    """
    Problem: You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing number of elements in each.
    
    Merge nums1 and nums2 into single sorted array stored in nums1. nums1 has length m+n where first m elements are actual values and last n are zeros (placeholders).

    Example 1:
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
    
    How it works:
    1. Use three pointers: p1 for nums1 values, p2 for nums2 values, p3 for merge position
    2. Start from END of arrays (merge backwards to avoid overwriting)
    3. Compare nums1[p1] and nums2[p2], place larger at nums1[p3]
    4. Move pointer of selected element and merge position pointer
    5. Copy remaining nums2 elements if any (nums1 elements already in place)
    
    Why backwards:
    - nums1 has space at end for merged result
    - Merging forward would overwrite nums1 values
    - Merging backward fills empty space without overwriting
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None: # LC 88
        """
        - TC: O(m + n) - process all elements from both arrays exactly once
        - SC: O(1) - in-place modification, only three pointer variables
        """
        p1 = m - 1  # Pointer for last element in nums1
        p2 = n - 1  # Pointer for last element in nums2
        p3 = m + n - 1  # Pointer for last position in merged array
        
        # Merge from back to front
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]: # Ele in nums1 is bigger
                nums1[p3] = nums1[p1] # Write that ele to merged array WRITE spot
                p1 -= 1
            else: # Ele in nums2 is bigger
                nums1[p3] = nums2[p2] # Write that ele to merged array
                p2 -= 1
            p3 -= 1 # Move write spot
        
        # Copy remaining nums2 elements (if any)
        # Don't need to copy nums1 - already in correct position
        while p2 >= 0:
            nums1[p3] = nums2[p2]
            p2 -= 1
            p3 -= 1

# Example:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6], n = 3
#
# Start: p1=2 (3), p2=2 (6), p3=5
#   nums1[2]=3, nums2[2]=6
#   6 > 3, place 6 at p3
#   nums1 = [1,2,3,0,0,6], p2=1, p3=4
#
# p1=2 (3), p2=1 (5), p3=4
#   5 > 3, place 5 at p3
#   nums1 = [1,2,3,0,5,6], p2=0, p3=3
#
# p1=2 (3), p2=0 (2), p3=3
#   3 > 2, place 3 at p3
#   nums1 = [1,2,3,3,5,6], p1=1, p3=2
#
# p1=1 (2), p2=0 (2), p3=2
#   2 == 2, place nums2[2] at p3
#   nums1 = [1,2,2,3,5,6], p2=-1, p3=1
#
# p2 < 0, done
# Output: [1,2,2,3,5,6]

sol = MultiArrayPattern()
sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3) # [1,2,2,3,5,6]
sol.merge([4,5,6,0,0,0], 3, [1,2,3], 3) # [1,2,3,4,5,6]
