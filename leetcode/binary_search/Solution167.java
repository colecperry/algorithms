package binary_search;

// 167. Two Sum II - Input Array Is Sorted

// Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

// Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
// The tests are generated such that there is exactly one solution. You may not use the same element twice.
// Your solution must use only constant extra space. This means your algorithm must not use extra space that grows with the size of the input array. -> O(n^2) is not allowed.

// Example 1:
// Input: numbers = [2,7,11,15], target = 9
// Output: [1,2]
// Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

// Example 2:
// Input: numbers = [2,3,4], target = 6
// Output: [1,3]
// Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

// Example 3:
// Input: numbers = [-1,0], target = -1
// Output: [1,2]
// Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

import java.util.Arrays;

public class Solution167 {

    public int[] twoSum2(int[] numbers, int target) {
        int left = 0;                      // Variable left initialized to 0
        int right = numbers.length - 1;    // Variable right initialized to last index

        while (left < right) {             // Create two pointer while loop
            int sum = numbers[left] + numbers[right]; // Take the sum
            if (sum < target) {            // If the target is greater than sum
                left = left + 1;           // Move left pointer over
            } else if (sum > target) {     // If sum is greater than target
                right = right - 1;         // Move right pointer over
            } else {                       // If they are equal
                return new int[]{left + 1, right + 1}; // Return index + 1
            }
        }

        return new int[]{};                // No solution found (shouldn't happen per problem constraints)
    }

    public static void main(String[] args) {
        Solution167 solution = new Solution167();
        System.out.println(Arrays.toString(solution.twoSum2(new int[]{2, 7, 11, 15}, 9)));
        System.out.println(Arrays.toString(solution.twoSum2(new int[]{2, 3, 4}, 6)));
        System.out.println(Arrays.toString(solution.twoSum2(new int[]{-1, 0}, -1)));
        System.out.println(Arrays.toString(solution.twoSum2(new int[]{1, 3, 4, 5, 7, 11}, 9)));
    }
}