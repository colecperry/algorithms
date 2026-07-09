class Solution:
    def mySqrt(self, x: int) -> int:  # LC 69
        """
        Return floor(√x) without using built-in sqrt.

        Example:
        Input: x = 8   Output: 2   (√8 ≈ 2.828, floor = 2)
        Input: x = 4   Output: 2

        Strategy: Binary search on the answer space [1, x//2].
        Track the last valid candidate — the largest k where k² ≤ x.

        - TC: O(log x), SC: O(1)
        """
        if x == 0:
            return 0
        if x == 1:
            return 1
        l = 0
        r = x - 1
        while l <= r :
            mid = (r + l)//2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                r = mid - 1
            else:
                l = mid + 1
        return r
sol4 = Solution()
print("sqrt(8):", sol4.mySqrt(8))      # 2
print("sqrt(4):", sol4.mySqrt(4))      # 2
