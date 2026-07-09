package array;


// 56. Merge Intervals

// Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

// Example 1:
// Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
// Output: [[1,6],[8,10],[15,18]]
// Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

// Example 2:
// Input: intervals = [[1,4],[4,5]]
// Output: [[1,5]]
// Explanation: Intervals [1,4] and [4,5] are considered overlapping.

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution56 {

    /**
     * TC: O(n log n) - dominated by sorting
     * SC: O(n) - output array (or O(log n) for sorting if we don't count output)
     */
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]); // sort by start

        List<int[]> result = new ArrayList<>();
        int prevStart = intervals[0][0]; // get initial start
        int prevEnd = intervals[0][1];   // get initial end

        for (int i = 1; i < intervals.length; i++) { // iterate from i=1
            int currStart = intervals[i][0];
            int currEnd = intervals[i][1];

            if (prevEnd >= currStart) { // INTERVALS OVERLAP
                prevEnd = Math.max(prevEnd, currEnd); // update end pointer -> use max() for edge case where interval is fully contained
            } else { // INTERVALS DO NOT OVERLAP
                result.add(new int[]{prevStart, prevEnd}); // add merged interval to result
                prevStart = currStart; // move pointers
                prevEnd = currEnd;
            }
        }

        result.add(new int[]{prevStart, prevEnd}); // append last interval

        return result.toArray(new int[0][]);
    }

    public static void main(String[] args) {
        Solution56 sol = new Solution56();
        System.out.println(Arrays.deepToString(sol.merge(new int[][]{{1,3},{2,6},{8,10},{15,18}}))); // [[1,6],[8,10],[15,18]]
        System.out.println(Arrays.deepToString(sol.merge(new int[][]{{1,4},{4,5}}))); // [[1,5]]
        System.out.println(Arrays.deepToString(sol.merge(new int[][]{{1,4},{2,3}}))); // [[1,4]] -> fully contained edge case
    }
}