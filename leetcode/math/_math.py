"""
=================================================================
MATH COMPLETE GUIDE
=================================================================

WHAT IS THE MATH CATEGORY?
---------------------------
Math problems involve number theory, arithmetic properties, and digit manipulation rather than data structure traversal. Solutions almost always exploit a mathematical shortcut to avoid brute force.

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

"""
MATH COMPLEXITY REFERENCE
===========================

+------------------------------------+----------------------+--------------+
| Pattern                            | Time                 | Space        |
+------------------------------------+----------------------+--------------+
| Digit Manipulation                 | O(log n)             | O(1)         |
| GCD / LCM                          | O(n + log(min(a,b))) | O(1)         |
| Prime Sieve                        | O(n log log n)       | O(n)         |
| Fast Exponentiation / Integer Sqrt | O(log n)             | O(1)         |
| String-Based Big-Number Arithmetic | O(max(m, n))         | O(max(m, n)) |
+------------------------------------+----------------------+--------------+

n = magnitude of the primary input for that pattern (digit count for Digit
Manipulation, array length for GCD/LCM, upper bound for Prime Sieve, exponent for
Fast Exponentiation), m = length of the second string for String-Based Big-Number
Arithmetic, a/b = the two values a GCD is being computed over

WHAT EACH PATTERN IS:
- Digit Manipulation: peel a number apart one digit at a time using remainder and
  division, then rebuild a new number the same way in reverse.
- GCD / LCM: repeatedly replace a pair of numbers with a smaller pair (the second
  number and the remainder of dividing them) until one hits zero — the last nonzero
  number is the greatest common divisor, and the least common multiple falls out of
  a one-line formula built from it.
- Prime Sieve: start by assuming every number could be prime, then cross off every
  multiple of each prime you find, so anything left unmarked at the end must be prime.
- Fast Exponentiation / Integer Square Root: compute a big power by repeatedly
  squaring the base and cutting the exponent in half, instead of multiplying one
  factor at a time; integer square root applies the same halving idea via binary search.
- String-Based Big-Number Arithmetic: treat numbers that are too big (or off-limits
  to convert) as plain text, and add or multiply them the way you would by hand on
  paper, one column or digit-pair at a time.

NOTES:
- Digit Manipulation: the digit count of x is O(log x), and each iteration strips one
  digit -> O(log n) time; only a few scalar variables -> O(1) space
- GCD/LCM: O(n) to scan the array for min/max, then the Euclidean algorithm shrinks
  the pair by at least half every two steps -> O(log min(a,b)); no extra storage ->
  O(1) space
- Prime Sieve: each composite is marked exactly once by its smallest prime factor;
  the classic sieve summation bounds total marking work at O(n log log n); the
  is_prime array is O(n) space
- Fast Exponentiation: the exponent is halved every iteration -> O(log n) iterations;
  only the running result and base are kept -> O(1) space
- String Arithmetic: single pass over the longer of the two strings -> O(max(m, n));
  the result string grows to the same size -> O(max(m, n)) space
"""

"""
================================================================
PATTERN 1: DIGIT MANIPULATION
PATTERN EXPLANATION: Extract digits with % 10 and // 10, reconstruct numbers with * 10. Building a reversed number: accumulate into a result by multiplying the running result by 10 then adding the next digit each iteration. Overflow detection: check before multiplying if result will exceed INT_MAX // 10.

Applications: Reverse integer (LC 7), palindrome number (LC 9), happy number digit sum (LC 202), plus one (LC 66), add digits (LC 258).
================================================================
"""

class DigitManipulationPattern:
    """
    Giveaway: "return x with its digits reversed" plus an explicit overflow
    check against a 32-bit range — needing to peel off and rebuild individual
    digits (not the number as a whole) is what signals % 10 / // 10 digit
    extraction instead of string-reversal tricks.

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

"""
================================================================
PATTERN 2: GCD / LCM
PATTERN EXPLANATION: GCD via Euclidean algorithm: repeatedly replace (a, b) with (b, a % b) until b == 0; the last non-zero value of a is the GCD. LCM is not a separate algorithm — it is derived directly from GCD: lcm(a, b) = a * b // gcd(a, b). The reasoning: a*b counts every prime factor from both numbers; dividing by gcd removes the shared factors counted twice, leaving the smallest number divisible by both.

Applications: GCD of array (LC 1979), reduce fractions, any problem involving
divisibility, common periods, or repeating structure.
================================================================
"""

class GCDPattern:
    """
    Giveaway: the problem asks directly for the greatest common divisor of
    specific numbers — that wording is the tell for the Euclidean algorithm
    (repeatedly replacing (a,b) with (b, a%b)) rather than checking every
    divisor up to min(a,b).

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

"""
================================================================
PATTERN 3: PRIME SIEVE
PATTERN EXPLANATION: To find all primes up to n, start by assuming every number is prime. Then for each prime p starting at 2, mark all its multiples as not prime — starting at p² because every smaller multiple was already marked by an earlier prime. Only iterate up to √n: any composite number ≤ n must have a factor ≤ √n, so all composites are guaranteed marked by then.

Applications: Count Primes (LC 204), any problem asking for prime counts or
prime membership up to a bound.
================================================================
"""

import math

class PrimeSievePattern:
    """
    Giveaway: "return the number of primes strictly less than n" — needing prime
    status for every number up to a bound, not just testing one specific number,
    is what signals sieving out multiples once instead of trial-dividing each
    number individually.

    Problem: Given an integer n, return the number of prime numbers strictly less than n.
    
    NOTE: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

    Example:
        Input: n = 10   Output: 4   (primes: 2, 3, 5, 7)
        Input: n = 1    Output: 0

    Steps (Prime Sieve Algorithm):
    1. If n < 2, return 0
    2. is_prime = [True] * n; mark 0 and 1 as False
    3. For i from 2 to √n (inclusive): 
       a. If is_prime[i]:
          b. For j from i*i to n, step i: is_prime[j] = False
    4. Return sum(is_prime)

    NOTE: isqrt(n) returns the largest integer whose square doesn't exceed n
    Ex. isqrt(10) → 3 because 3² = 9 ≤ 10, and 4² = 16 is too big
    """
    def countPrimes(self, n: int) -> int:  # LC 204
        """
        - TC: O(n log log n) - sieve eliminates each composite once
        - SC: O(n) - boolean array of size n
        """
        if n < 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False   # 0 and 1 are not prime

        for i in range(2, math.isqrt(n) + 1): #isqrt is integer square root fn
            if is_prime[i]: # get all multiples of each prime
                for j in range(i * i, n, i): # Find all multiples of i starting at i² 
                    is_prime[j] = False

        return sum(is_prime)

    # Example trace (countPrimes, n=10):
    # is_prime = [F, F, T, T, T, T, T, T, T, T]  (indices 0-9)
    #
    # i=2: mark 4, 6, 8     → [F,F,T,T,F,T,F,T,F,T]
    # i=3: mark 9           → [F,F,T,T,F,T,F,T,F,F]
    # i=√10 = 3 → stop
    #
    # sum = 4 (indices 2,3,5,7) ✓

sol5 = PrimeSievePattern()
print("Count primes < 10:", sol5.countPrimes(10))   # 4
print("Count primes < 1:", sol5.countPrimes(1))     # 0

"""
================================================================
PATTERN 4: FAST EXPONENTIATION & INTEGER SQUARE ROOT
PATTERN EXPLANATION: Compute x^n in O(log n) by halving the exponent each step. If n is even: x^n = (x²)^(n//2). If n is odd: factor out one x, then fall into the even case. Track the "leftover" x factors in a running result — when n is odd, multiply result by x before squaring and halving. Integer sqrt is the same idea applied as binary search on the answer space [0, x//2].

Applications: Pow(x, n) (LC 50), Sqrt(x) (LC 69), modular exponentiation,
Super Pow (LC 372), any problem computing large powers efficiently.
================================================================
"""

class FastExponentiationPattern:
    """
    Giveaway: "implement pow(x, n)" where n can be large — computing a big power
    efficiently, implying naive repeated multiplication is too slow, is the
    signal for halving the exponent via repeated squaring instead of multiplying
    x by itself n times.

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
    
sol = FastExponentiationPattern()
print(sol.myPow(2.0, 10))   # 1024.0
print(sol.myPow(2.0, -2))   # 0.25

# Example trace (myPow, x=2.0, n=10):
# n=10 (even):  result=1,    x=4,   n=5
# n=5  (odd):   result=4,    x=16,  n=2
# n=2  (even):  result=4,    x=256, n=1
# n=1  (odd):   result=1024, x=..., n=0
# n=0 → stop → return 1024.0

"""
================================================================
PATTERN 5: STRING-BASED BIG-NUMBER ARITHMETIC
PATTERN EXPLANATION: When numbers exceed integer width or conversion is forbidden, represent them as strings and simulate grade-school column arithmetic. Addition: two pointers start at the rightmost digit of each string, add digit-by-digit carrying any overflow, then reverse the collected digits at the end. Multiplication: each digit pair (i, j) contributes to exactly two positions in the result array — p1 = i+j (carry position) and p2 = i+j+1 (current digit position).

Applications: Add strings (LC 415), add binary (LC 67), multiply strings (LC 43),
any "big number" problem where int conversion is off-limits.
================================================================
"""

class StringArithmeticPattern:
    """
    Giveaway: numbers are given as strings with an explicit "must not convert
    inputs to integers directly" — that ban, combined with needing an exact
    digit-by-digit sum, is what signals simulating grade-school column
    arithmetic instead of using built-in int conversion.

    Problem: Given two non-negative integers as strings, return their sum as a string. Must not convert inputs to integers directly.

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
        i, j = len(num1) - 1, len(num2) - 1 # ptrs at end of each str
        carry = 0 # carry for sums >= 10
        result = [] # collect digits in reverse order

        # continue until both strings are exhausted and no carry remains
        while i >= 0 or j >= 0 or carry: 
            val1 = int(num1[i]) if i >= 0 else 0
            val2 = int(num2[j]) if j >= 0 else 0
            total = val1 + val2 + carry # sum curr digits + carry
            result.append(str(total % 10)) # Current column digit
            carry = total // 10            # Carry to next column
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

sol5 = StringArithmeticPattern()
print("Add '456'+'77':", sol5.addStrings("456", "77"))      # 533

