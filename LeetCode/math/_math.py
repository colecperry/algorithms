"""
=================================================================
MATH COMPLETE GUIDE
=================================================================

WHAT IS THE MATH CATEGORY?
---------------------------
Math problems involve number theory, arithmetic properties, and digit
manipulation rather than data structure traversal. Solutions almost
always exploit a mathematical shortcut to avoid brute force.

Core ideas:
- Use mod properties to keep intermediate values in range
- Extract digits with % 10 and // 10, rebuild numbers with * 10
- GCD via Euclidean algorithm: gcd(a, b) = gcd(b, a % b)
- Halve exponents to compute powers in O(log n)
- Simulate column-by-column arithmetic for big-number strings

When to recognize a math problem:
- Input is a plain integer or numeric string
- Problem asks about digits, primes, powers, or remainders
- Brute force would exceed 10^8 operations (time limit hint)
- Problem says "without using built-in" pow, sqrt, etc.

Common math problem types (most → least common):
- Modular arithmetic and remainders
- Digit extraction and reconstruction
- GCD, LCM, and divisibility
- Fast exponentiation and integer square root
- Big-number string arithmetic

================================
        MATH PATTERNS
================================
"""

from typing import List

# ================================================================
# PATTERN 1: DIGIT MANIPULATION
# PATTERN EXPLANATION: Extract digits with % 10 and // 10, reconstruct numbers with * 10. Building a reversed number: accumulate into a result by multiplying the running result by 10 then adding the next digit each iteration. Overflow detection: check before multiplying if result will exceed INT_MAX // 10.
#
# Applications: Reverse integer (LC 7), palindrome number (LC 9), happy number digit sum (LC 202), plus one (LC 66), add digits (LC 258).
# ================================================================

class DigitManipulationPattern:
    """
    Problem: Given a signed 32-bit integer x, return x with its digits reversed. If reversing causes overflow outside [-2^31, 2^31 - 1], return 0.

    Example:
        Input: x = 123    Output: 321
        Input: x = -123   Output: -321
        Input: x = 120    Output: 21

    Steps (Reverse Integer - LC 7):
    1. Record sign; work with abs(x)
    2. While x != 0:
       a. digit = x % 10
       b. result = result * 10 + digit
       c. x //= 10
    3. Reapply sign and check 32-bit overflow
    """
    def reverse(self, x: int) -> int:  # LC 7
        """
        - TC: O(log |x|) - one iteration per digit
        - SC: O(1) - only integer variables
        """
        INT_MAX = 2**31 - 1   # 2147483647
        INT_MIN = -(2**31)    # -2147483648

        sign = -1 if x < 0 else 1
        x = abs(x) # reverse the abs val, reapply sign at end
        result = 0

        while x != 0:
            digit = x % 10 # get last digit
            result = result * 10 + digit # update result
            x //= 10 # remove last digit with floor division

        result *= sign # reapply original sign
        return result if INT_MIN <= result <= INT_MAX else 0

    # Example trace (reverse, x=123):
    # sign=1, x=123, result=0
    #
    # Iter 1: digit=3, result=3,   x=12
    # Iter 2: digit=2, result=32,  x=1
    # Iter 3: digit=1, result=321, x=0
    #
    # 321 is within 32-bit range → return 321

sol2 = DigitManipulationPattern()
print("Reverse 123:", sol2.reverse(123))             # 321
print("Reverse -123:", sol2.reverse(-123))            # -321


# ================================================================
# PATTERN 2: GCD / LCM
# PATTERN EXPLANATION: GCD via Euclidean algorithm: repeatedly replace (a, b) with
# (b, a % b) until b == 0; the last non-zero value of a is the GCD. LCM is not a
# separate algorithm — it is derived directly from GCD: lcm(a, b) = a * b // gcd(a, b).
# The reasoning: a*b counts every prime factor from both numbers; dividing by gcd
# removes the shared factors counted twice, leaving the smallest number divisible by both.
#
# Applications: GCD of array (LC 1979), reduce fractions, any problem involving
# divisibility, common periods, or repeating structure.
# ================================================================

class GCDPattern:
    """
    Problem: Return the GCD of the smallest and largest element in nums.

    Example:
        Input: nums = [2, 5, 6, 9, 10]   Output: 2
            min=2, max=10 → gcd(2, 10) = 2

    Steps (GCD of Array - LC 1979):
    1. a, b = min(nums), max(nums)
    2. While b != 0:
       a. a, b = b, a % b
    3. Return a

    LCM extension — once you have GCD, LCM is free:
        lcm(a, b) = a * b // gcd(a, b)
    Example: lcm(4, 6) → gcd(4,6)=2 → 4*6//2 = 12
        (12 is the smallest number both 4 and 6 divide evenly into)
    """
    def findGCD(self, nums: List[int]) -> int:  # LC 1979
        """
        - TC: O(n + log min(a,b)) - O(n) to find min/max, O(log) for GCD
        - SC: O(1)
        """
        a, b = min(nums), max(nums)
        while b:
            a, b = b, a % b  # Euclidean: gcd(a,b) = gcd(b, a%b)
        return a

    # Example trace (findGCD, gcd(2, 10)):
    # a=2, b=10 → a,b = 10, 2    (2 % 10 = 2)
    # a=10, b=2 → a,b = 2, 0    (10 % 2 = 0)
    # b=0 → return 2 ✓

sol2 = GCDPattern()
print("GCD of [2,5,6,9,10]:", sol2.findGCD([2, 5, 6, 9, 10]))   # 2
print("LCM of 4 and 6:", 4 * 6 // sol2.findGCD([4, 6]))          # 12


# ================================================================
# PATTERN 3: FAST EXPONENTIATION & INTEGER SQUARE ROOT
# PATTERN EXPLANATION: Compute x^n in O(log n) by halving the exponent each step.
# If n is even: x^n = (x²)^(n//2). If n is odd: factor out one x, then fall into
# the even case. Track the "leftover" x factors in a running result — when n is odd,
# multiply result by x before squaring and halving. Integer sqrt is the same idea
# applied as binary search on the answer space [0, x//2].
#
# Applications: Pow(x, n) (LC 50), Sqrt(x) (LC 69), modular exponentiation,
# Super Pow (LC 372), any problem computing large powers efficiently.
# ================================================================

class FastExponentiationPattern:
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
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        while n > 0:
            if n % 2 == 1:     # Odd exponent — absorb one x factor into result
                result *= x
            x *= x             # Square the base
            n //= 2            # Halve the exponent

        return result

    # Example trace (myPow, x=2.0, n=10):
    # n=10 (even):  result=1,    x=4,   n=5
    # n=5  (odd):   result=4,    x=16,  n=2
    # n=2  (even):  result=4,    x=256, n=1
    # n=1  (odd):   result=1024, x=..., n=0
    # n=0 → stop → return 1024.0

    # Application 2: Integer Square Root
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
        if x < 2:
            return x

        lo, hi = 1, x // 2    # √x ≤ x/2 for all x ≥ 2
        result = 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid <= x:
                result = mid           # Valid candidate — try to go larger
                lo = mid + 1
            else:
                hi = mid - 1          # Too large — go smaller

        return result

    # Example trace (mySqrt, x=8):
    # lo=1, hi=4
    # mid=2: 4 ≤ 8  → result=2, lo=3
    # mid=3: 9 > 8  → hi=2
    # lo=3 > hi=2   → stop → return 2

sol4 = FastExponentiationPattern()
print("2^10:", sol4.myPow(2.0, 10))    # 1024.0
print("2^-2:", sol4.myPow(2.0, -2))    # 0.25
print("sqrt(8):", sol4.mySqrt(8))      # 2
print("sqrt(4):", sol4.mySqrt(4))      # 2


# ================================================================
# PATTERN 4: STRING-BASED BIG-NUMBER ARITHMETIC
# PATTERN EXPLANATION: When numbers exceed integer width or conversion is forbidden,
# represent them as strings and simulate grade-school column arithmetic. Addition:
# two pointers start at the rightmost digit of each string, add digit-by-digit
# carrying any overflow, then reverse the collected digits at the end. Multiplication:
# each digit pair (i, j) contributes to exactly two positions in the result array
# — p1 = i+j (carry position) and p2 = i+j+1 (current digit position).
#
# Applications: Add strings (LC 415), add binary (LC 67), multiply strings (LC 43),
# any "big number" problem where int conversion is off-limits.
# ================================================================

class StringArithmeticPattern:
    """
    Problem: Given two non-negative integers as strings, return their sum as a string.
    Must not convert inputs to integers directly.

    Example:
        Input: num1 = "456", num2 = "77"   Output: "533"
        Input: num1 = "11",  num2 = "123"  Output: "134"

    Steps (Add Strings - LC 415):
    1. i, j = last index of num1, num2; carry = 0
    2. While i >= 0 or j >= 0 or carry:
       a. val1 = int(num1[i]) if i >= 0 else 0
       b. val2 = int(num2[j]) if j >= 0 else 0
       c. total = val1 + val2 + carry
       d. Append total % 10 to result; carry = total // 10
       e. i -= 1; j -= 1
    3. Reverse result and join
    """
    def addStrings(self, num1: str, num2: str) -> str:  # LC 415
        """
        - TC: O(max(m, n)) - one pass through both strings
        - SC: O(max(m, n)) - result list
        """
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            val1 = int(num1[i]) if i >= 0 else 0
            val2 = int(num2[j]) if j >= 0 else 0
            total = val1 + val2 + carry
            result.append(str(total % 10))    # Current column digit
            carry = total // 10               # Carry to next column
            i -= 1
            j -= 1

        return "".join(reversed(result))

    # Example trace (addStrings, "456" + "77"):
    # i=2, j=1, carry=0
    #
    # Col 1: 6+7+0=13  → result=["3"], carry=1, i=1, j=0
    # Col 2: 5+7+1=13  → result=["3","3"], carry=1, i=0, j=-1
    # Col 3: 4+0+1=5   → result=["3","3","5"], carry=0, i=-1
    # reversed → "533"

    # Application 2: Multiply Strings
    def multiply(self, num1: str, num2: str) -> str:  # LC 43
        """
        Multiply two non-negative integers given as strings without converting to int.

        Example:
        Input: num1 = "123", num2 = "456"   Output: "56088"

        Strategy: Grade-school multiplication. Digit pair (i, j) contributes to
        positions p1=i+j and p2=i+j+1 in a result array of size len(num1)+len(num2).
        Accumulate all contributions in the array, then strip leading zeros.

        - TC: O(m * n) - every digit pair touched once
        - SC: O(m + n) - result array
        """
        m, n = len(num1), len(num2)
        pos = [0] * (m + n)       # Max digits in product is m+n

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1          # Carry and current positions
                total = mul + pos[p2]

                pos[p2] = total % 10                # Place current digit
                pos[p1] += total // 10              # Propagate carry

        result = "".join(str(d) for d in pos).lstrip("0")
        return result or "0"

    # Example trace (multiply, "12" * "3"):
    # m=2, n=1, pos=[0,0,0]
    #
    # i=1 (digit=2), j=0 (digit=3): mul=6, p1=1, p2=2
    #   total=6+pos[2]=6; pos[2]=6, pos[1]+=0 → pos=[0,0,6]
    # i=0 (digit=1), j=0 (digit=3): mul=3, p1=0, p2=1
    #   total=3+pos[1]=3; pos[1]=3, pos[0]+=0 → pos=[0,3,6]
    # "036".lstrip("0") = "36" ✓

sol5 = StringArithmeticPattern()
print("Add '456'+'77':", sol5.addStrings("456", "77"))      # 533
print("Multiply '123'*'456':", sol5.multiply("123", "456")) # 56088
print("Multiply '2'*'3':", sol5.multiply("2", "3"))         # 6
