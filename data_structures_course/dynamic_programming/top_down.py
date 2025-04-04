# Function to compute Fibonacci using top-down DP (memoization) which is usually implemented recursively which breaks the problem into smaller subproblems but we modify the solution to save the results of each subproblem

# Time Complexity Explanation:
# 
# Without Memoization (Naïve Recursion):
# - The naive recursive approach makes two recursive calls for each Fibonacci computation,
#   leading to an exponential time complexity of O(2^n).
# - This happens because the recursion tree grows exponentially, repeatedly computing 
#   the same values multiple times (e.g., fib(3) calls fib(2) and fib(1), and fib(2) is 
#   then recomputed when called from fib(4)).
#
# With Memoization (Top-Down DP):
# - The memoized approach stores previously computed Fibonacci values in the `memo` dictionary.
# - Each Fibonacci number is computed only once and then retrieved in O(1) time for future calls.
# - Since there are at most `n` unique subproblems, the time complexity reduces to O(n), 
#   making it significantly faster than O(2^n).
#
#


def fibonacci(n, memo={}):
    """
    Compute the nth Fibonacci number using recursion and memoization.

    :param n: Fibonacci index to compute.
    :param memo: Dictionary storing computed Fibonacci values.
    :return: nth Fibonacci number.
    """
    
    # Step 1: If value is already computed, return it (avoids recomputation)
    if n in memo:
        return memo[n]

    # Step 2: Base cases (Stopping conditions)
    if n == 0 or n == 1:  # Fibonacci(1) = 1
        return 1

    # Step 3: Recursive computation with memoization
    # Recurrence relation: F(n) = F(n-1) + F(n-2)
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    # Step 4: Return the computed Fibonacci number
    return memo[n]

# Example usage:
n = 4
print(f"Fibonacci({n}) =", fibonacci(n))

# ------------------------------
# DETAILED STEP-BY-STEP EXECUTION FOR fibonacci(4)
# ------------------------------
# 1. fibonacci(4) calls fibonacci(3)
# 2. fibonacci(3) calls fibonacci(2) 
# 3. fibonacci(2) calls fibonacci(1)
#    - Base case → Returns 1 to fibonacci(n - 1, memo) in fibonacci(2)
# 5. fibonacci(2) calls fibonacci(0)
#    - Base case → Returns 1 to fibonacci(n - 2, memo) in 
#      fibonacci(2)
# 6. fibonacci(2) completes and stores in {2:2} in memo → (computed as 1 + 1)
#    and returns 2 (memo[2] = 2) to fibonacci(3) for fibonacci(n - 1, memo)
# 7. fibonacci(3) unpauses and calls fibonacci(1) for fibonacci(n - 2, memo) as it was waiting for fibonacci(2) to complete
#    - Base case → Returns 1
# 8. fibonacci(3) completes and stores in {3:3} in memo → memo[3] = 3 (computed as 2 + 1) and returns memo[n] (memo[3] = 3) to fibonacci(4) for fibonacci(n - 1, memo)
# 9. fibonacci(4) calls fibonacci(2) 
#    - Found in memo → Returns memo[2] = 2 for fibonacci(n - 2, memo) -> uses memoization
# 10. fibonacci(4) completes memo → memo[4] = 5 (computed as memo[3] + memo[2]) = 3 + 2

# ------------------------------
# FINAL MEMO TABLE
# ------------------------------
# memo = {
#     2: 2,
#     3: 3,
#     4: 5
# }

# 1, 1, 2, 3, 5

# ------------------------------
# FINAL RETURN VALUE
# ------------------------------
# fibonacci(4) = 5
