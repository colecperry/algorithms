# 682. Baseball Game

# Topics: Array, Stack, Simulation

# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record. You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

# An integer x : Record a new score of x.
# '+': Record a new score that is the sum of the previous two scores.
# 'D': Record a new score that is the double of the previous score.
# 'C': Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.

# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.


# Example 1:
# Input: ops = ["5","2","C","D","+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.
# Example 2:

# Input: ops = ["5","-2","4","C","D","9","+","+"]
# Output: 27
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "-2" - Add -2 to the record, record is now [5, -2].
# "4" - Add 4 to the record, record is now [5, -2, 4].
# "C" - Invalidate and remove the previous score, record is now [5, -2].
# "D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
# "9" - Add 9 to the record, record is now [5, -2, -4, 9].
# "+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
# "+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
# The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
# Example 3:

# Input: ops = ["1","C"]
# Output: 0
# Explanation:
# "1" - Add 1 to the record, record is now [1].
# "C" - Invalidate and remove the previous score, record is now [].
# Since the record is empty, the total sum is 0.

# How to solve:
    # Use else case for integer -> so we don't have to use isdigit()
        # If int add to the stack
    # If we get a C, we pop last ele from the stack
    # If we get a D, take ele at the top of the stack, double it, and add it to the stack
    # If we get +, we take two prev ele's, add them, and add it to the stack


class Solution(object):
    def calPoints(self, operations):
        stack = []
        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2]) # Append sum of prev two ele's
            elif op == 'D': 
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
            else: # Must be an integer
                stack.append(int(op)) # Add ele as an int (guarentees we have int's to work with in our other operations)

        return sum(stack)


my_solution = Solution()
ops1 = ["5","2","C","D","+"]
ops2 = ["5","-2","4","C","D","9","+","+"]
ops3 = ["1","C"]
print(my_solution.calPoints(ops1))
print(my_solution.calPoints(ops2))
print(my_solution.calPoints(ops3))
