# 69. Sqrt(x)

# Topics - Math, Binary Search

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

# How to solve: (Binary Search)
    # Since we can't use sqrt function, try exploring all integers. The square root of a number x must be between 0 and x//2 (since the answer rounds down) -> initialize our left and right pointers to l = 0 and r = x // 2
    # Create binary search loop, calculate mid, and calculate the mid squared (the num we are comparing to X)
    # Finish three scenarios when comparing mid squared to X and decrease search space
    # Because of the binary search condition l <= r, the loop will stop when r becomes greater than l. So when the loop terminates the right pointer ends up pointing at the largest integer for which r^2 <= x. 

# Runtime Complexity: O(log x)
# - The algorithm uses binary search on the range [0, x//2]. 
#   Since each iteration halves the search space, the number of iterations is logarithmic in x.
#
# Space Complexity: O(1)
# - Only a fixed number of variables are used, regardless of the input size.


def mySqrt(x):
    if x == 0: # Edge case if x == 0, return right away
        return 0
    if x == 1: # Edge case if x == 1
        return 1
    
    l = 0 # Initialize l and r pointers
    r = x // 2

    while l <= r : # Binary Search Loop
        mid = l + (r - l) //2 # Calculate mid point (floor)
        num = mid * mid # Calculate mid squared -> The num we are squaring
        if num == x: # If we found the number
            return mid # Return the sqrt
        elif num > x: # If num we calculate is greater than integer X (Too big)
            r = mid - 1 # Search the left side
        else: # Else number is too small
            l = mid + 1 # Search the right side
    return r # Once while loop condition terminates, R ends up pointing at the largest int where r^2 <= x 


print(mySqrt(4)) # Expected output: 2
print(mySqrt(8)) # Expected output: 2