// 496. Next Greater Element I

// The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

// You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

// For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

// Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

// Example 1:
// Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
// Output: [-1,3,-1]

// Example 2:
// Input: nums1 = [2,4], nums2 = [1,2,3,4]
// Output: [3,-1]

package stack;

import java.util.*;

public class Solution496 {
    /**
     * TC: O(N + M) -> loop through nums2 once to build the map, loop through nums1 once to build the result
     * SC: O(M) -> dict and stack both hold at most M elements from nums2
     */
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> nextGreater = new HashMap<>(); // Map num: next greater ele
        Deque<Integer> stack = new ArrayDeque<>(); // Monotonic decreasing stack -> in Java, use a Deque when implementing a stack

        // Step 1: Build the "next greater" mapping for nums2 -> Mono decreasing stack
        for (int num : nums2) {
            // Pop all smaller elements - current num is their next greater
            while (!stack.isEmpty() && num > stack.peek()) { 
                int smallerNum = stack.pop();       // pop the smaller element
                nextGreater.put(smallerNum, num);  // current num is its next greater
            }
            stack.push(num); // push current num, maintaining decreasing order
        }

        // Build result for nums1
        int[] result = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            result[i] = nextGreater.getOrDefault(nums1[i], -1); // if not in map, -1
        }

        return result;
    }

    public static void main(String[] args) {
        Solution496 sol = new Solution496();
        System.out.println(Arrays.toString(sol.nextGreaterElement(new int[]{4,1,2}, new int[]{1,3,4,2}))); // [-1, 3, -1]
        System.out.println(Arrays.toString(sol.nextGreaterElement(new int[]{2,4}, new int[]{1,2,3,4})));   // [3, -1]
        System.out.println(Arrays.toString(sol.nextGreaterElement(new int[]{1,3}, new int[]{3,2,1,4})));   // [4, 4]
    }
}