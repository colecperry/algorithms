class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid > x: # mid too big
                right = mid - 1 # search left
            elif mid * mid < x: # mid too small
                left = mid + 1 # search right
            else: # exact match
                return mid

        return right
    
sol = Solution()
print(sol.mySqrt(4)) # 2
print(sol.mySqrt(8)) # 2.82
