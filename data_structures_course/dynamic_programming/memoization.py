# Need these use dynamic programming:
# 1. Overlapping subproblems -> Repeating subproblems
    # Subproblems are breaking parts of a problem into smaller parts, solving those, and putting it back together to solve the overall problem. 
    # Overlapping subproblems are having subproblems that repeat. These subproblems are identical. Since we know the result of these subproblems, when we encounter this problem again, we can store the result of the operation in advance.

# 2: Optimized Substructure -> If you have the optimal solution for each subproblem 1, 2, and 3, that will give you the optimal solution to the overall problem. If this is not true, you cannot use dynamic programming to solve.

# Fibonacci example
# 1. Overlapping subproblems -> Both fib(2) and fib(3) call fib(1) recursively. Both fib(3) and fib(4) call fib (2) recursively.
# 2. Optimized substructure -> Because the solution to F(n) depends on optimal solutions for F(n - 1) and F(n - 2)
# Big O of this function is O(2^n)

counter = 0 # Used to show how inefficient this function is, then we will use dynamic programming to make it for efficient with memoization. 

def fib(n): 
    global counter # Add this line for the inside of the function to see global variable
    counter += 1 # Count the number of function calls
    if n == 0 or n == 1: # Base case
        return n # Return 0 or 1
    return fib(n - 1) + fib(n - 2)

n = 7
print("\nFib of", n, "=", fib(n))
print('\nCounter: ', counter)

n = 30
print("\nFib of", n, "=", fib(n))
print('\nCounter: ', counter)

# 41 function calls for n = 7
# 832,040 function calls for n = 30

# Using memoization -> Each recursive call's result for fib2(n) is stored in a list, so if we encounter it we can return without going through the whole recursive function call again
# Big O: O(n)

memo = [None] * 100 # Initialize a list with 100 indexes with None
counter2 = 0 # Count the number of function calls

def fib2(n): 
    global counter2
    counter2 += 1

    if memo[n] is not None: # If the number is in the list (Not equal to initialization of "None")
        return memo[n] # Return the value

    if n == 0 or n == 1: # Base case
        return n # Return 0 or 1
    
    memo[n] = fib2(n - 1) + fib2(n - 2) #Recursive call fib for the previous 2 numbers, add, and add to list
    return memo[n] # Return the result of addition

n = 7
print("\nFib of", n, "=", fib2(n)) # fib2(n) returns the 7th fibonacci number, 13
print('\nCounter: ', counter2)

n = 30
print("\nFib of", n, "=", fib2(n))
print('\nCounter: ', counter2)
