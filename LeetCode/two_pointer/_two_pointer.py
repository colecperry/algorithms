from typing import List

# =============================================================================
# WHAT IS THE TWO POINTERS PATTERN?
# =============================================================================
"""
Two pointers is a technique where we use two references (pointers/indices) to 
traverse a data structure, typically an array or string. The pointers can move:
- Toward each other (opposite ends)
- In the same direction (fast/slow)
- At different speeds

The pattern transforms O(n²) brute force solutions into O(n) elegant solutions
by eliminating the need for nested loops.

Visual Example - Opposite Direction:

Array: [1, 2, 3, 4, 5, 6, 7, 8]
        ↑                    ↑
       left               right

Step 1: left = 0, right = 7
Step 2: left = 1, right = 6
Step 3: left = 2, right = 5
...continues until left >= right

Visual Example - Same Direction (Fast/Slow):

Array: [1, 2, 3, 4, 5, 6, 7, 8]
        ↑  ↑
      slow fast

Step 1: slow = 0, fast = 1
Step 2: slow = 1, fast = 3
Step 3: slow = 2, fast = 5
...fast moves faster than slow
"""

# =============================================================================
# VISUAL: O(n²) BRUTE FORCE vs O(n) TWO POINTERS
# =============================================================================
"""
PROBLEM: Find two numbers that sum to 9

Array: [2, 3, 4, 5, 6, 7]
Target: 9

════════════════════════════════════════════════════
BRUTE FORCE - O(n²): Nested loops check every pair
════════════════════════════════════════════════════

Array: [2, 3, 4, 5, 6, 7]
        ↑  ↑              Step 1: 2+3=5 ❌
        i  j

Array: [2, 3, 4, 5, 6, 7]
        ↑     ↑           Step 2: 2+4=6 ❌
        i     j

Array: [2, 3, 4, 5, 6, 7]
        ↑        ↑        Step 3: 2+5=7 ❌
        i        j

Array: [2, 3, 4, 5, 6, 7]
        ↑           ↑     Step 4: 2+6=8 ❌
        i           j

Array: [2, 3, 4, 5, 6, 7]
        ↑              ↑  Step 5: 2+7=9 ✓
        i              j

Brute Force checks ALL pairs:
(2,3), (2,4), (2,5), (2,6), (2,7)
(3,4), (3,5), (3,6), (3,7)
(4,5), (4,6), (4,7)
(5,6), (5,7)
(6,7)
Total: 15 comparisons

════════════════════════════════════════════════════
TWO POINTERS - O(n): One pass from both ends (in this case the array must be sorted)
════════════════════════════════════════════════

Array: [2, 3, 4, 5, 6, 7]
        ↑              ↑  Step 1: 2+7=9 ✓
      left          right

2+7=9  →  3+7=10  →  4+7=11  →  5+7=12  →  6+7=13  →  Stop
Total: 5 comparisons


THE DIFFERENCE GROWS WITH SIZE:
════════════════════════════════════════════════

Array Size | Brute Force O(n²) | Two Pointers O(n)
─────────────────────────────────────────────────
    10     |        45         |       10
   100     |      4,950        |      100
  1,000    |    499,500        |    1,000
 10,000    | 49,995,000        |   10,000  

# =============================================================================
# WHY USE TWO POINTERS?
# =============================================================================

Advantages:
- Space efficient: O(1) extra space for the two pointer variables (vs O(n) for additional arrays)
- Time efficient: O(n) instead of O(n²) for many problems
- Simple and elegant: Easy to understand and implement
- Versatile: Works on arrays, strings, linked lists

Common Applications:
- Finding pairs with specific properties
- Removing duplicates in-place
- Partitioning arrays
- Detecting cycles
- Merging sorted arrays
- String palindrome checks

# =============================================================================
# PATTERN TYPES
# =============================================================================
1. OPPOSITE DIRECTION (Convergent)
    - Start: one at beginning, one at end
    - Move: toward each other
    - Use: sorted arrays, palindromes, pair sums

2. SAME DIRECTION (Sequential)
    - Start: both at beginning (or close)
    - Move: in same direction or at different speeds
    - Use: remove duplicates, partition, in-place modifications

3. FAST/SLOW (Floyd's Cycle Detection)
    - Start: both at beginning
    - Move: fast moves 2x speed of slow
    - Use: cycle detection, finding middle element, linked lists

4. SLIDING WINDOW (Special Two Pointer)
    - Start: both at beginning
    - Move: expand/contract window
    - Use: subarray/substring problems with constraints
"""

# =============================================================================
# TIME & SPACE COMPLEXITY
# =============================================================================
"""
| Operation                    | Time        | Space | Notes                        |
|------------------------------|-------------|-------|------------------------------|
| Opposite direction traverse  | O(n)        | O(1)  | Each element visited once    |
| Same direction traverse      | O(n)        | O(1)  | Each element visited once    |
| Fast/slow cycle detection    | O(n)        | O(1)  | Fast pointer visits 2x       |
| Sliding window               | O(n)        | O(1)  | Each element enter/exit once |

Key Insight: Even though we have two pointers, we still only traverse the 
data structure once, making it O(n) time complexity.
"""

# =============================================================================
# WHEN TO USE TWO POINTERS
# =============================================================================
"""
Use two pointers when:
✓ Problem involves sorted array/list
✓ Need to find pairs or triplets with specific properties
✓ Need to modify array in-place
✓ Problem asks about subarrays/substrings
✓ Need to detect cycles in linked list
✓ Need to find middle of sequence
✓ Need to partition array based on condition

Don't use two pointers when:
✗ Need to track multiple elements simultaneously (use hash map)
✗ Order doesn't matter and you need frequency counts (use Counter)
✗ Need to find all combinations (might need backtracking)
✗ Data structure doesn't support index access (like trees)
"""

# =============================================================================
# TWO POINTER PATTERNS - COMPREHENSIVE GUIDE
# =============================================================================

# ================================================================
# PATTERN 1: OPPOSITE DIRECTION - CONVERGING (Meet in Middle)
# PATTERN EXPLANATION: Start pointers at both ends, move toward center, compare/swap elements.
# Key insight: Process from extremes inward, skip invalid elements, validate symmetry.
# Applications: Palindrome validation, string reversal, character swapping, array reversal.
# ================================================================

# PROBLEM 1: LC 125 - Valid Palindrome
# Skip non-alphanumeric, compare from both ends moving inward

class Pattern1(object):
    '''
        # Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases. A palindrome is a string that reads the same forward and backward.

        # Example 1:
        # Input: s = "A man, a plan, a canal: Panama"
        # Output: true
        # Explanation: "amanaplanacanalpanama" is a palindrome

        # TC:
        #     - Single pass through string -> O(n)
        #     - Each character visited at most once by left or right pointer
        #     - isalnum() and lower() operations -> O(1)
        #     - Total -> O(n)
        # SC:
        #     - O(1) -> only using two pointer variables (left, right)
        #     - No additional data structures needed
    '''
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1 # Create left and right pointers
        while l < r:
            # Skip non-alphanumeric characters by 
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            # Compare characters (case-insensitive)
            elif s[l].lower() != s[r].lower(): # If not equal, return False
                return False
            else: # If they are equal move pointers
                l += 1
                r -= 1
        return True
    
solution = Pattern1()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))

# ================================================================
# PATTERN 2: OPPOSITE DIRECTION - OPTIMIZATION (Greedy Decision)
# PATTERN EXPLANATION: Start at both ends, strategically move pointer that improves result.
# Key insight: Make greedy decision about which pointer to move based on optimization goal.
# Applications: Container with water, trapping rain water, min/max problems on sorted arrays.
# ================================================================

# PROBLEM 1: LC 11 - Container With Most Water
# Move pointer with shorter height (limiting factor)

class Pattern2(object):    
    '''
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store. Notice that you may not slant the container.

    # Example 1:
    # Input: height = [1,8,6,2,5,4,8,3,7]
    # Visual representation:
    #   8      |              |
    #   7      |              |     |
    #   6      |  |           |     |
    #   5      |  |     |     |     |
    #   4      |  |     |     |     |
    #   3      |  |     |  |  |     |
    #   2      |  |     |  |  |  |  | 
    #   1      |  |  |  |  |  |  |  | 
    #   0 __|__|__|__|__|__|__|__|__|__
    #       0  1  2  3  4  5  6  7  8  (indices)
    # Output: 49
    # Explanation: The vertical lines are at indices 1 and 8 with heights 8 and 7.
    # Area = min(8, 7) * (8 - 1) = 7 * 7 = 49

    # TC:
    #     - Single pass through array -> O(n)
    #     - Each element visited at most once
    #     - Area calculation and comparison -> O(1)
    #     - Total -> O(n)
    # SC:
    #     - O(1) -> only using two pointer variables (left, right) and max_area
    #     - No additional data structures needed
    '''
    def maxArea(self, height):
        max_area = 0 # Create variable to track area
        l, r = 0, len(height) - 1 # Create two pointers at each end of the array

        while l < r: # Loop until they meet
            area = min(height[l], height[r]) * (r-l) # Calculate the water area
            max_area = max(area, max_area) # Update the max area
            if height[l] < height[r]: # Move on from pointer that has a smaller value
                l += 1                # This maximizes the potential area
            else:
                r -= 1

        return max_area

my_solution = Pattern2()
print(my_solution.maxArea([1,8,6,2,5,4,8,3,7]))

# ================================================================
# PATTERN 3: SAME DIRECTION (Slow = Write, Fast = Read)
# PATTERN EXPLANATION: Fast pointer explores, slow pointer tracks write position.
# Key insight: Slow marks boundary, fast finds valid elements to move to slow position.
# Applications: Remove duplicates, remove elements, partition, subsequence matching.
# ================================================================

# PROBLEM 1: LC 26 - Remove Duplicates from Sorted Array
# Slow = next unique position, fast = explorer

class Pattern3(object):
    '''
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

    Consider the number of unique elements in nums to be k. After removing duplicates, return the number of unique elements k. The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

    Example 2:
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).

    TC:
        - O(n) - while loop scans through nums at most once per ele, comparison and assignment operations are O(1)
    SC:
        - O(1) - only need left and right pointers, in place modification of input array
    '''
    def removeDuplicates(self, nums):
        left = 1  # Slow pointer: tracks position for inserting unique ele's (first ele always unique)
        right = 1  # Fast pointer: scans for unique elements
        
        while right < len(nums):
            if nums[right] != nums[right-1]:  # If we find unique ele with right 
                nums[left] = nums[right]  # Copy newly found unique ele to left position
                left += 1  # Advance left once we copy next unique ele
            right += 1  # Always advance right
        
        return left # left stops in the next "write" position, which is k, not k-1

answer = Pattern3()
print(answer.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

# ================================================================
# PATTERN 4: FAST/SLOW (Different Speeds or Fixed Offset)
# PATTERN EXPLANATION: Pointers move at different rates or maintain fixed gap.
# Key insight: Speed difference or gap creates useful properties (cycle detection, nth from end).
# Applications: Cycle detection, find middle, nth from end, linked list problems.
# ================================================================

# PROBLEM 2: LC 19 - Remove Nth Node From End of List
# Create fixed gap of n, move together

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Pattern4(object):
    '''
    # Given the head of a linked list, remove the nth node from the end of the list and return its head.

    # Example 1:
    #                        L        R
    # Input: head = 0 [1, 2, 3, 4, 5], n = 2 -> n = 2 means the second node from the end of the list
    # Output: [1,2,3,5]

    TC: 
        - O(n) -> iterate through list once to create gap of n nodes & until R pointer reaches end of list
    SC:
        - O(1) -> only hold L and R pointers
    '''
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head) # Create dummy node with it's next set to head
        left = dummy # Create L ptr starting at the dummy node
        right = head  # Set R ptr to the head

        for _ in range(n): # Create gap of n nodes 
            right = right.next

        while right: # Move until R ptr reaches the end
            left = left.next
            right = right.next

        left.next = left.next.next # Delete the nth node from end

        return dummy.next

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

sol = Pattern4()
print(sol.removeNthFromEnd(head, 2))

# ================================================================
# PATTERN 5: FIXED + TWO CONVERGING (3-Way Pointer / K-Sum)
# PATTERN EXPLANATION: Fix one pointer, use two others in opposite direction on sorted array.
# Key insight: Reduce 3Sum to 2Sum by fixing first element, then two-pointer for remaining.
# Applications: 3Sum, 4Sum, triplet problems on sorted arrays.
# ================================================================

# PROBLEM 1: LC 16 - 3Sum Closest

# LC 16 - 3Sum Closest (CLEANER for learning the pattern)

class Pattern5(object):
    """
    Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

    Return the sum of the three integers.

    You may assume that each input would have exactly one solution.

    Example 1:
    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

    TC:
        - O(n log n) -> timsort
        - O(n^2) -> iterate through each ele in nums, and iterate through again with l and r pointers
        - Total -> O(n^2)
    SC:
        - O(log n) -> python's timsort uses extra space (not in place)
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() # Sort array (required for two pointer logic)
        closest_sum = float('inf') # Track closest sum of three ele
        
        # Fix first ele i (leave room for l & r pointers after i)
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1 # 2 ptrs for remaining ele's
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest if this sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move ptrs based on whether sum too small or large
                if current_sum < target: # sum too small
                    left += 1
                elif current_sum > target: # sum too big
                    right -= 1
                else:
                    return current_sum  # Exact match
        
        return closest_sum
    
sol = Pattern5()
print(sol.threeSumClosest([-1,2,1,-4], 1)) # 2

# ================================================================
# PATTERN 6: MULTI-ARRAY MERGE (One Pointer Per Array)
# PATTERN EXPLANATION: Maintain pointer for each array, compare and merge based on values.
# Key insight: Use multiple pointers across different data structures, merge by comparison.
# Applications: Merge sorted arrays, merge k sorted lists, merge intervals.
# ================================================================

# PROBLEM 1: LC 88 - Merge Sorted Array
# Three pointers: one for each array + one for result position

class Pattern6(object):
    """
    # You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

    # Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    # The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

    # Example 1:

    # Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    # Output: [1,2,2,3,5,6]
    # Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    # The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

    TC:
        - O(m + n) -> main loop runs at most m + n iterations, cleanup loop runs at most n iterations
    SC:
        - O(1) -> only need three pointer variables, in place modification of nums1
    """
    def merge(self, nums1, m, nums2, n):
        p1 = m - 1  # Pointer for nums1's m elements
        p2 = n - 1  # Pointer for nums2' n elements
        p3 = len(nums1) - 1  # Pointer for the merged array (nums1)
        
        # Merge nums1 and nums2 starting from the largest values
        while p1 >= 0 and p2 >= 0:
            if nums2[p2] > nums1[p1]: # Compare ele's
                nums1[p3] = nums2[p2] # Set merged ele
                p2 -= 1
            else:
                nums1[p3] = nums1[p1]
                p1 -= 1
            p3 -= 1 # always decrease merged arr ptr
        
        # Copy remaining elements from nums2 if any because they are smaller than everything we've placed. Don't need to check nums1 (p1) because these ele's are already in nums1 at their correct position
        while p2 >= 0:
            nums1[p3] = nums2[p2]
            p2 -= 1
            p3 -= 1

        return nums1

my_solution = Pattern6()
print(my_solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(my_solution.merge([4,5,6,0,0,0], 3, [1,2,3], 3))