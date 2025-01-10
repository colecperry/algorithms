# RECURSION
# A Function that calls itself... until it doesn't
# The process has to be the same each time
# Each process, we make the problem smaller

# Base case -> Better to make it obvious
# Needs to have a return statement

# Factorial example
# 4! =              factorial(4)             -> return 24
# 4 * 3! =          return 4 * factorial(3)  -> 4 * 6, return 24 to factorial(4)
#     3 * 2! =      return 3 * factorial(2)  -> 3 * 2, return 6 to factorial(3)
#         2 * 1! =  return 2 * factorial(1)  -> 2 * 1 = 2, return 2 to factorial(2)
#             1     return 1                 -> return 1 to factorial(1)

# Note -> on the recursive call, it does not return yet because when it is trying to calculate the return value, it makes the recursive call before it can return
# Use debugger call stack to walk through step by step

def factorial(n):
    if n == 1: # Base case
        return 1
    return n * factorial(n-1) # Function calls itself before it returns, then returns after it hits the base case

print(factorial(4))

