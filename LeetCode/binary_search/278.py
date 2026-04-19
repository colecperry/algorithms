# 278. First Bad Version

# Topics: Binary Search

# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions
# after a bad version are also bad.

# You are given an API: bool isBadVersion(version) which returns whether a given
# version is bad. Implement a function to find the first bad version.
# You should minimize the number of calls to the API.

# Ex. 1
# Input: n = 5, bad = 4
# Output: 4
# Explanation: isBadVersion(3) -> false, isBadVersion(4) -> true -> first bad version is 4

# Ex. 2
# Input: n = 1, bad = 1
# Output: 1

bad = 4  # change this to test different cases

def isBadVersion(version: int) -> bool:
    return version >= bad

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        - TC: O(log n)
        - SC: O(1)
        """
        l, r = 1, n

        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid        # mid could be the first bad — don't exclude it
            else:
                l = mid + 1    # mid is good — first bad must be after it

        return l  # Left always points to first position that satisfies the condition after the binary search loop ends

sol = Solution()
bad = 4;  print(sol.firstBadVersion(5))   # 4
bad = 1;  print(sol.firstBadVersion(1))   # 1
bad = 1;  print(sol.firstBadVersion(10))  # 1
bad = 10; print(sol.firstBadVersion(10))  # 10