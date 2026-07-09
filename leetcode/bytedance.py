# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

# Example 1:
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.

def combination_recursive(n, k):
    """
    Recursive approach to generate combinations
    """
    # Base Cases
    if k == 0:
        return [[]]  # One way to choose 0 elements: empty combination
    if k > n or n <= 0:
        return []    # No way to choose k elements from fewer than k elements
    if k == n:
        return [list(range(1, n + 1))]  # Only one way: choose all elements
    
    # Recursive case: either include n or don't include n
    # Case 1: Include n in the combination
    with_n = combination_recursive(n - 1, k - 1)
    for combo in with_n:
        combo.append(n)
    
    # Case 2: Don't include n in the combination
    without_n = combination_recursive(n - 1, k)
    
    return with_n + without_n

def combination_backtrack(n, k):
    """
    Alternative recursive approach using backtracking
    Often more intuitive and efficient
    """
    result = []
    
    def backtrack(start, current_combination):
        # Base case: if we have k numbers, add to result
        if len(current_combination) == k:
            result.append(current_combination[:])  # Make a copy
            return
        
        # Try all numbers from start to n
        for i in range(start, n + 1):
            # Choose: add current number
            current_combination.append(i)
            
            # Explore: recurse with next starting position
            backtrack(i + 1, current_combination)
            
            # Unchoose: backtrack
            current_combination.pop()
    
    backtrack(1, [])
    return result

def test_combinations():
    print("Testing with n=4, k=2:")
    print("Recursive:", combination_recursive(4, 2))
    print("Backtracking:", combination_backtrack(4, 2))
    print()
    
    print("Testing with n=1, k=1:")
    print("Recursive:", combination_recursive(1, 1))
    print("Backtracking:", combination_backtrack(1, 1))
    print()
    
    print("Testing with n=5, k=3:")
    print("Recursive:", combination_recursive(5, 3))
    print("Backtracking:", combination_backtrack(5, 3))

if __name__ == "__main__":
    test_combinations()


# Question 4 of 4
# Submitted
# 0:00:00
# +
# 0:00:33
# You are developing a new programming language. You believe that ordinary dictionaries are boring, so you've decided to add a cool feature to make your language unique!

# You want the cool feature to be able to perform two types of queries. With two integer arrays, a and b, the two types of queries are as follows:

# If the query is of the form [0, i, x], then add x to a[i] (а[i] should be assigned the value of a[i] + x).
# If the query is of the form [1, x], then find the total number of pairs of indices i and j such that a[i] + b[j] = x.
# You will be given the arrays of integers a and b, as well as queries, an array of queries in either of the forms described above. Your task is to implement this cool feature, perform the given queries and return an array of the results of the queries of the type [1, x].

# Example

# For a = [1, 4], b = [1, 2, 3], and queries = [[1, 5], [0, 0, 2], [1, 5]], the output should be solution(a, b, queries) = [1, 2].

# The arrays look like this initially:
# a = [1, 4] and b = [1, 2, 3]

# For the query [1, 5], there's only one way to form a sum of 5 using an element from each array: 5 = 4 + 1 = a[1] + b[0]. So the result is 1.

# The query [0, 0, 2] adds 2 to the value of a[0], so the arrays now look like this:
# a = [3, 4] and b = [1, 2, 3]

# For the final query [1, 5], there are now two ways to form a sum of 5 using an element from each array: 5 = 3 + 2 = a[0] + b[1] and 5 = 4 + 1 = a[1] + b[0]. So the result is 2.

# Since the two queries of type [1, x] gave results of 1 and 2 respectively, the answer is [1, 2].

# For a = [2, 3], b = [1, 2, 2], and queries = [[1, 4], [0, 0, 1], [1, 5]], the output should be solution(a, b, queries) = [3, 4].

# The arrays look like this initially:
# a = [2, 3] and b = [1, 2, 2]

# For the query [1, 4], there are three ways to form a sum of 4 using an element from each array: 4 = 2 + 2 = a[0] + b[1], 4 = 2 + 2 = a[0] + b[2], and 4 = 3 + 1 = a[1] + b[0]. So the result is 3.

# The query [0, 0, 1] adds 1 to the value of a[0], so the arrays now look like this:
# a = [3, 3] and b = [1, 2, 2]

# For the final query [1, 5] there are now 4 ways to form a sum of 5 using an element from each array: 5 = 3 + 2 = a[0] + b[1], 5 = 3 + 2 = a[0] + b[2], 5 = 3 + 2 = a[1] + b[1], and 5 = 3 + 2 = a[1] + b[2]. So the result is 4.

# Since the two queries of type [1, x] gave results of 3 and 4 respectively, the answer is [3, 4].

# Input/Output

# [execution time limit] 4 seconds (py3)

# [memory limit] 1 GB

# [input] array.integer a

# An array of integers.

# Guaranteed constraints:
# 1 ≤ a.length ≤ 5 · 104,
# 0 ≤ a[i] ≤ 108.

# [input] array.integer b

# An array of integers.

# Guaranteed constraints:
# 1 ≤ b.length ≤ 103,
# 0 ≤ b[i] ≤ 108.

# [input] array.array.integer queries

# An array of queries, where queries[i][0] represents the type of query, and the other elements represent the parameters of the query (i and x for type 0, and just x for type 1).

# For queries of the type [0, i, x], it is guaranteed that 0 ≤ i < a.length and 0 ≤ x ≤ 105.
# For queries of the type [1, x], it is guaranteed that 0 ≤ x ≤ 3 · 108.

# Guaranteed constraints:
# 1 ≤ query.length ≤ 103.

# [output] array.integer

# The outputs of the queries of the type [1, x], in the order they are given in the input.