package binary_search;

// 278. First Bad Version

// Topics: Binary Search

// You are a product manager and currently leading a team to develop a new product.
// Unfortunately, the latest version of your product fails the quality check.
// Since each version is developed based on the previous version, all the versions
// after a bad version are also bad.

// You are given an API: bool isBadVersion(version) which returns whether a given
// version is bad. Implement a function to find the first bad version.
// You should minimize the number of calls to the API.

// Ex. 1
// Input: n = 5, bad = 4
// Output: 4
// Explanation: isBadVersion(3) -> false, isBadVersion(4) -> true -> first bad version is 4

// Ex. 2
// Input: n = 1, bad = 1
// Output: 1

// -----------------------
// 💡 How to Solve:
// -----------------------

// Binary search on the version range 1 to n.
// If the mid version is bad, the first bad version is at mid or earlier — move right pointer to mid.
// If the mid version is good, the first bad version must be after mid — move left pointer to mid + 1.
// When left == right, we've found the first bad version.

// Key insight: we're not searching for a value in an array — we're searching for
// the boundary between good and bad versions. This is the classic "binary search
// on answer space" pattern.
// Left always points to the first position that satisfies the condition after the loop ends.

// -----------------------
// ⏱️ Time Complexity:
// -----------------------

// O(log n) — we halve the search space on every iteration

// -----------------------
// 📦 Space Complexity:
// -----------------------

// O(1) — only two pointers, no extra space used


public class Solution278 {

    static int bad = 4; // change this to test different cases

    static boolean isBadVersion(int version) {
        return version >= bad;
    }

    public int firstBadVersion(int n) {
        int l = 1, r = n;

        while (l < r) {
            int mid = l + (r - l) / 2; // avoids integer overflow vs (l + r) / 2
            if (isBadVersion(mid)) {
                r = mid;       // mid could be the first bad — don't exclude it
            } else {
                l = mid + 1;   // mid is good — first bad must be after it
            }
        }

        return l;              // l == r, both point to the first bad version
    }

    public static void main(String[] args) {
        solution_278 sol = new solution_278();

        bad = 4;  System.out.println(sol.firstBadVersion(5));   // 4
        bad = 1;  System.out.println(sol.firstBadVersion(1));   // 1
        bad = 1;  System.out.println(sol.firstBadVersion(10));  // 1
        bad = 10; System.out.println(sol.firstBadVersion(10));  // 10
    }
}