"""
Bottom-Up Dynamic Programming approach to compute Fibonacci numbers.

This approach avoids recursion by having some natural size of the problem and builds the solution iteratively from smaller subproblems to larger ones. It optimally stores results in a table (list)
to prevent redundant calculations, reducing the time complexity to O(n).

Benefits of Bottom-Up DP:
- Avoids recursion overhead.
- Uses an iterative loop to compute results efficiently.
- Saves all computed Fibonacci numbers in a list for direct access.
"""

"""
### How Bottom-Up DP Reduces Time Complexity:

# Naïve Recursive Approach:
#   fib(n) = fib(n-1) + fib(n-2)
#   Each call branches into two more calls → O(2^n) exponential time

# Example Recursion Tree for n = 5:
#       fib(5)
#      /      \
#  fib(4)    fib(3)
#   /   \     /   \
# fib(3) fib(2) fib(2) fib(1)
#  /  \    /  \
# fib(2) fib(1) fib(1) fib(0)

# Notice that fib(2) and fib(3) are recomputed multiple times.

# Bottom-Up DP Approach:
# Instead of recursion, we build an array iteratively:
#   dp[0] = 0
#   dp[1] = 1
#   dp[2] = dp[1] + dp[0] = 1
#   dp[3] = dp[2] + dp[1] = 2
#   dp[4] = dp[3] + dp[2] = 3
#   dp[5] = dp[4] + dp[3] = 5
#   ...
# Unlike recursion, which redundantly recalculates subproblems, this approach stores previously computed values in a list and directly accesses them in O(1) time
# Each value is computed **only once**, giving us a total of O(n) time complexity.
"""

def fibonacci(n):
    """
    Compute the nth Fibonacci number using a bottom-up DP approach.
    :param n: The Fibonacci number to compute.
    :return: The nth Fibonacci number.
    """
    
    # Base cases: 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Step 1: Create a DP table to store Fibonacci values
    dp = [0] * (n + 1)  # Initialize array with zeros
    dp[0] = 0  # Fibonacci(0) = 0
    dp[1] = 1  # Fibonacci(1) = 1
    
    # Step 2: Iteratively compute Fibonacci numbers from 2 to n
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # Bottom-up formula -> we already have the vals instead of computing each time
    
    # Step 3: Return the nth Fibonacci number
    return dp[n]

# Example usage:
n = 8
print(f"Fibonacci({n}) =", fibonacci(n))
