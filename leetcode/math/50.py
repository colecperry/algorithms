class Solution:
    """
    Problem: Implement pow(x, n), which computes x raised to the power n.

    Example:
        Input: x = 2.0, n = 10   Output: 1024.0
        Input: x = 2.0, n = -2   Output: 0.25

    Steps (Pow(x,n) - LC 50):
    1. Handle negative n: x = 1/x, n = -n
    2. result = 1.0
    3. While n > 0:
       a. If n is odd: result *= x  (absorb one factor before halving)
       b. x = x * x                 (square the base)
       c. n //= 2                   (halve the exponent)
    4. Return result
    """
    def myPow(self, x: float, n: int) -> float:  # LC 50
        """
        - TC: O(log n) - halve n each iteration
        - SC: O(1) - iterative
        """
        negative = n < 0
        n = abs(n)

        result = 1.0
        while n > 0:
            if n % 2 == 1: # Odd exponent — absorb one x factor into result
                result *= x # Update result with the "leftover" x
            x *= x             # Square the base each iteration
            n //= 2            # Halve the exponent each iteration

        return 1 / result if negative else result
    
sol = Solution()
print(sol.myPow(2.0, 10))   # 1024.0
print(sol.myPow(2.0, -2))   # 0.25

# Example trace (myPow, x=2.0, n=10):
# n=10 (even):  result=1,    x=4,   n=5
# n=5  (odd):   result=4,    x=16,  n=2
# n=2  (even):  result=4,    x=256, n=1
# n=1  (odd):   result=1024, x=..., n=0
# n=0 → stop → return 1024.0