# Bottom up: Solving the problem from the smallest problem first
# This code is bottom-up because it starts by solving the smallest subproblems (i.e., the Fibonacci numbers for indices 0 and 1) and then iteratively builds the solution for larger indices using the results of previously solved subproblems. This avoids redundant calculations by storing intermediate results in a list (fib_list). The iterative nature of the loop ensures that each Fibonacci number is computed exactly once, resulting in a time complexity of O(n)

counter = 0

def fib(n):
    fib_list = [0, 1] # Create a list with the first two indicies populated
    global counter

    for index in range(2, n + 1): # Start loop at second index and end before n + 1 -> (n)
        counter += 1
        next_fib = fib_list[index - 1] + fib_list[index - 2] # Add previous two values to find next fib #
        fib_list.append(next_fib) # Append the next number to the fibonacci list
    return fib_list[n]

n = 7
print('Fib of', n, '=', fib(n))
print('Counter:', counter)

