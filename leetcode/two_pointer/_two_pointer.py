"""
=================================================================
TWO POINTERS COMPLETE GUIDE
=================================================================

WHAT IS THE TWO POINTERS PATTERN?
----------------------------------
Two pointers is a technique where we use two indices to traverse a data structure,
typically an array or string. The pointers can move toward each other, in the same
direction at different speeds, or maintain a fixed gap — depending on the problem.

Key characteristics:
- Uses two index variables to traverse data structure
- Reduces O(n^2) brute force to O(n) by avoiding nested loops
- Often works on sorted arrays (sorted order enables intelligent decisions)
- Usually O(1) extra space

TIME COMPLEXITY ADVANTAGE:
--------------------------
Example: Find pair with target sum in sorted array of size n
- Brute force: nested loops check every pair -> O(n^2)
- Two pointers: converge from both ends, one step per pointer -> O(n)

Example: Remove duplicates from sorted array in-place
- Brute force: for each element, shift remaining elements -> O(n^2)
- Two pointers: slow tracks write position, fast explores -> O(n)

Example: Find triplet with target sum (3Sum)
- Brute force: three nested loops -> O(n^3)
- Two pointers: fix one element, two pointers for rest -> O(n^2)

Movement patterns:
- Opposite direction: start at both ends, converge toward center
- Same direction: both move left-to-right at different speeds (slow/fast)
- Fixed gap: maintain constant distance between pointers

When to use Two Pointers:
- Problem involves sorted array and pair/triplet finding
- Need to modify array in-place (slow/fast pointer)
- Detect cycles or find middle in linked list (fast/slow)
- Merge multiple sorted arrays (one pointer per array)

NEED SORTED ARRAY:
------------------
- Two Sum / 3Sum / k-Sum: pointer movement depends on value comparison
- Closest pair to target: move based on comparison with target
- Merging sorted structures: compare heads, advance smaller

DON'T NEED SORTING:
-------------------
- Fast/slow pointers (cycle detection, find middle)
- Same-direction partition (remove duplicates, move zeros)
- Palindrome checking (must preserve original order)

TWO POINTERS CORE PATTERNS
============================
"""

from typing import List, Optional

"""
TWO POINTERS COMPLEXITY REFERENCE
===================================

+---------------------------+------------------+------------------+
| Pattern                   | Time             | Space            |
+---------------------------+------------------+------------------+
| Opposite Direction        | O(n)             | O(1)             |
| Same Direction / Partition| O(n)             | O(1)             |
| Fast / Slow               | O(n)             | O(1)             |
| K-Sum (3Sum)              | O(n^2)           | O(1) or O(n)     |
| Multi-Array Merge         | O(m + n)         | O(1)             |
+---------------------------+------------------+------------------+

n = array/list length, m/n = lengths of two arrays being merged

WHAT EACH PATTERN IS:
- Opposite Direction: one pointer starts at each end and they move toward each other,
  used on sorted data to find a pair without checking every combination.
- Same Direction / Partition: a slow pointer marks where to write next and a fast
  pointer scans ahead, used to compact/rearrange an array in place.
- Fast / Slow: two pointers move at different speeds through the same structure
  (often a linked list), used to detect cycles or find the middle.
- K-Sum (3Sum): fix one element, then run the opposite-direction pattern on the rest
  to find pairs that combine with it to hit the target.
- Multi-Array Merge: one pointer per sorted array, always advancing whichever one
  points at the smaller value, to merge them in order.

NOTES:
- Opposite direction: each pointer moves at most n steps total -> O(n)
- Same direction: fast visits each element once, slow only writes -> O(n)
- Fast/slow: fast moves 2x speed; in worst case traverses 2n steps -> O(n)
- 3Sum: O(n log n) sort + O(n) outer x O(n) two pointers = O(n^2)
- Multi-array merge: each element written once to its final position -> O(m+n)
"""

"""
====================
TWO POINTER PATTERNS
====================
"""

"""
================================================================
PATTERN 1: OPPOSITE DIRECTION (CONVERGING FROM BOTH ENDS)
PATTERN EXPLANATION: Start with one pointer at index 0 and one at index n-1. At each
step, examine the sum (or comparison) of the two pointed values and move the appropriate
pointer inward. If the sum is too small, move left right (to get a larger value). If
too large, move right left. Because the array is sorted, this always makes progress
toward the answer without missing any valid pair.

Applications: Two sum in sorted array, pair finding, container with most water.
================================================================
"""

class OppositeDirection:
    """
    Giveaway: the array is explicitly stated as already sorted, and you need a pair
    that adds up to a target — sortedness means a sum that's too small or too large
    tells you exactly which pointer to move, letting one linear sweep from both ends
    replace checking every pair.

    Problem: Given a 1-indexed sorted array numbers and a target, find two numbers
    that add up to target. Return their 1-indexed positions.

    Example:
        numbers = [2, 7, 11, 15], target = 9
        2 + 7 = 9 -> Output: [1, 2]

    Steps:
    1. Initialize left=0, right=len(numbers)-1
    2. While left < right:
       a. If numbers[left] + numbers[right] == target -> return [left+1, right+1]
       b. If sum < target -> move left right (need larger sum)
       c. If sum > target -> move right left (need smaller sum)
    3. Return [] if no pair found
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:  # LC 167
        """
        TC: O(n) - each pointer moves at most n times total
        SC: O(1) - only two pointer variables
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return []

    # Trace: numbers=[2,7,11,15], target=9
    # left=0 (2), right=3 (15): sum=17 > 9 -> right=2
    # left=0 (2), right=2 (11): sum=13 > 9 -> right=1
    # left=0 (2), right=1 (7):  sum=9  == 9 -> return [1,2] ✓

sol = OppositeDirection()
print("Two Sum:", sol.twoSum([2, 7, 11, 15], 9))  # [1, 2]
print("Two Sum:", sol.twoSum([2, 3, 4], 6))        # [1, 3]


"""
================================================================
PATTERN 2: SAME DIRECTION / PARTITION (SLOW WRITES, FAST EXPLORES)
PATTERN EXPLANATION: Both pointers start at the same side and move in the same direction.
The slow pointer tracks the next valid write position; the fast pointer explores ahead
to find elements that belong in the valid region. When fast finds a valid element, write
it to the slow position and advance slow. This enables in-place array modification
without extra space.

Applications: Remove duplicates, remove elements, move zeros, partition by condition.
================================================================
"""

class SameDirection:
    """
    Giveaway: "remove duplicates in-place" from a sorted array means duplicates are
    always adjacent, so you only ever need to compare an element to its immediate
    predecessor while writing survivors to a compacting position — that in-place,
    no-extra-space requirement is what points to a slow write / fast read pointer
    pair instead of building a new list.

    Problem: Given a sorted array nums, remove duplicates in-place so each unique element
    appears only once. Return the number of unique elements k. The first k elements of
    nums should contain the unique elements in their original order.

    Example:
        nums = [0,0,1,1,1,2,2,3,3,4]
        After: nums = [0,1,2,3,4,_,_,_,_,_]
        Output: 5

    Steps:
    1. slow=1 (first element always unique, start writing at index 1)
    2. For each fast from 1 to end:
       a. If nums[fast] != nums[fast-1] -> unique element found
       b. Write nums[fast] to nums[slow]; slow += 1
    3. Return slow (count of unique elements)
    """
    def removeDuplicates(self, nums: List[int]) -> int:  # LC 26
        """
        TC: O(n) - single pass with fast pointer
        SC: O(1) - in-place modification
        """
        if not nums:
            return 0

        slow = 1

        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1

        return slow

    # Trace: nums = [0,0,1,1,2]
    # slow=1, fast=1: 0==0 skip
    # fast=2: 1!=0 -> write nums[1]=1, slow=2  -> [0,1,1,1,2]
    # fast=3: 1==1 skip
    # fast=4: 2!=1 -> write nums[2]=2, slow=3  -> [0,1,2,1,2]
    # Output: slow=3, nums[:3]=[0,1,2] ✓

sol = SameDirection()
test = [0,0,1,1,1,2,2,3,3,4]
k = sol.removeDuplicates(test)
print("Unique count:", k, "->", test[:k])  # 5 -> [0,1,2,3,4]


"""
================================================================
PATTERN 3: FAST / SLOW (DIFFERENT SPEEDS)
PATTERN EXPLANATION: Two pointers start at the same position but move at different speeds.
Slow moves 1 step; fast moves 2 steps. If there is a cycle, fast will eventually lap slow
and they will meet inside the cycle. If no cycle, fast reaches the end first. The same
pattern finds the middle of a linked list: when fast reaches the end, slow is at the middle.

Applications: Cycle detection, find middle of linked list, find nth node from end.
================================================================
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class FastSlow:
    """
    Giveaway: "determine if it contains a cycle" in a linked list, where you can
    only follow next pointers one at a time (no random access, no set of visited
    nodes required), is the classic tell for a fast/slow pointer pair — a cycle
    means a faster pointer must eventually lap and collide with a slower one.

    Problem: Given the head of a linked list, determine if it contains a cycle.
    A cycle exists if some node can be reached again by following next pointers.

    Example:
        3 -> 2 -> 0 -> -4 -> (back to 2)  -> True
        1 -> 2 -> 3 -> null               -> False

    Steps:
    1. Initialize slow=head, fast=head
    2. While fast and fast.next exist:
       a. slow = slow.next         (1 step)
       b. fast = fast.next.next    (2 steps)
       c. If slow == fast -> cycle detected, return True
    3. fast reached null -> return False (no cycle)
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:  # LC 141
        """
        TC: O(n) - fast traverses at most 2n steps before meeting slow or reaching end
        SC: O(1) - only two pointer variables
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    # Trace: 3 -> 2 -> 0 -> -4 -> (back to 2)
    # step 1: slow=2, fast=0
    # step 2: slow=0, fast=2   (fast: 0->-4->2)
    # step 3: slow=-4, fast=-4 (fast: 2->0->-4)  <- meet! ✓
    # Return True

sol = FastSlow()
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next  # Cycle back to node 2
print("Has cycle:", sol.hasCycle(head))             # True
print("Has cycle:", sol.hasCycle(ListNode(1)))      # False


"""
================================================================
PATTERN 4: K-SUM (FIX ONE + TWO POINTERS ON REST)
PATTERN EXPLANATION: Reduce k-sum to 2-sum by fixing k-2 elements with nested loops,
then using two pointers on the remaining subarray. For 3Sum, fix one element i and
run two pointers on nums[i+1:]. Skip duplicates at each level to avoid duplicate triplets
in the output. Sort first so that two-pointer decisions (sum too big/small) are correct.

Applications: 3Sum, 4Sum, 3Sum closest, triplet problems.
================================================================
"""

class KSum:
    """
    Giveaway: needing "unique triplets" that sum to a target is one dimension more
    than a pair-sum problem — fixing one element by looping over it and then running
    the sorted two-pointer sweep on what's left is what turns a 3Sum into a
    same-target 2Sum, which the "distinct indices" and duplicate-triplet wording
    also demands sorting to skip cleanly.

    Problem: Given an integer array nums, return all unique triplets [a, b, c] such that
    a + b + c == 0 and they come from distinct indices.

    Example:
        nums = [-1, 0, 1, 2, -1, -4]
        Output: [[-1,-1,2], [-1,0,1]]

    Steps:
    1. Sort nums (enables two-pointer decisions and easy duplicate skipping)
    2. For each index i (fixing first element):
       a. Skip if nums[i] == nums[i-1] (duplicate fixed element)
       b. Set left=i+1, right=len(nums)-1
       c. While left < right:
          - If sum==0: record triplet, skip duplicate left/right values, move both
          - If sum < 0: left += 1 (need larger sum)
          - If sum > 0: right -= 1 (need smaller sum)
    3. Return result
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:  # LC 15
        """
        TC: O(n^2) - sort O(n log n) + O(n) outer * O(n) two pointers
        SC: O(1) extra (ignoring sort's O(log n) stack)
        """
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result

    # Trace: nums = [-4,-1,-1,0,1,2] (sorted)
    # i=0 (-4): left=1(-1), right=5(2): sum=-3 < 0 -> left++; ... no triplet
    # i=1 (-1): left=2(-1), right=5(2): sum=0 ✓ -> [[-1,-1,2]]
    #           skip dup left, skip dup right -> left=3(0), right=4(1)
    #           sum=0 ✓ -> [[-1,-1,2],[-1,0,1]]
    # i=2 (-1): nums[2]==nums[1] -> skip (duplicate)
    # Output: [[-1,-1,2],[-1,0,1]] ✓

sol = KSum()
print("3Sum:", sol.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
print("3Sum:", sol.threeSum([0, 1, 1]))               # []


"""
================================================================
PATTERN 5: MULTI-ARRAY MERGE (ONE POINTER PER ARRAY)
PATTERN EXPLANATION: Maintain one pointer for each input array. Compare the elements
at the current pointers, select the appropriate one (largest for reverse fill), and
advance that pointer. Continue until all pointers are exhausted. For merging into an
existing array, fill from the back to avoid overwriting unprocessed elements.

Applications: Merge sorted arrays, array intersection, merge intervals.
================================================================
"""

class MultiArrayMerge:
    """
    Giveaway: merging two already-sorted arrays "in-place" into the one with extra
    trailing zero slots means you can't safely write from the front (you'd overwrite
    unread values) — that in-place constraint on pre-sorted inputs is what points to
    a pointer per array filling backward from the end, rather than a fresh merged
    list.

    Problem: You are given two sorted arrays nums1 (length m+n, last n slots are zeros)
    and nums2 (length n). Merge nums2 into nums1 in-place in sorted order.

    Example:
        nums1 = [1,2,3,0,0,0], m=3
        nums2 = [2,5,6], n=3
        Output: [1,2,2,3,5,6]

    Steps:
    1. p1 = m-1 (last real element in nums1)
       p2 = n-1 (last element in nums2)
       p3 = m+n-1 (last position in merged nums1)
    2. While p1 >= 0 and p2 >= 0:
       a. If nums1[p1] > nums2[p2]: write nums1[p1] at p3, p1 -= 1
       b. Else: write nums2[p2] at p3, p2 -= 1
       c. p3 -= 1
    3. Copy any remaining nums2 elements (nums1 elements already in place)
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:  # LC 88
        """
        TC: O(m + n) - each element written exactly once
        SC: O(1) - in-place modification with three pointer variables
        """
        p1 = m - 1
        p2 = n - 1
        p3 = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 -= 1
            else:
                nums1[p3] = nums2[p2]
                p2 -= 1
            p3 -= 1

        while p2 >= 0:
            nums1[p3] = nums2[p2]
            p2 -= 1
            p3 -= 1

    # Trace: nums1=[1,2,3,0,0,0] m=3, nums2=[2,5,6] n=3
    # p1=2(3), p2=2(6), p3=5: 6>3 -> nums1[5]=6, p2=1, p3=4
    # p1=2(3), p2=1(5), p3=4: 5>3 -> nums1[4]=5, p2=0, p3=3
    # p1=2(3), p2=0(2), p3=3: 3>2 -> nums1[3]=3, p1=1, p3=2
    # p1=1(2), p2=0(2), p3=2: 2==2 -> nums1[2]=2(nums2), p2=-1, p3=1
    # p2 < 0, done
    # nums1 = [1,2,2,3,5,6] ✓

sol = MultiArrayMerge()
nums1 = [1,2,3,0,0,0]
sol.merge(nums1, 3, [2,5,6], 3)
print("Merged:", nums1)  # [1,2,2,3,5,6]
