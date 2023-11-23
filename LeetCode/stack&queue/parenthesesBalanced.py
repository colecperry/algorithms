# Stack: Parentheses Balanced ( ** Interview Question)
# Check to see if a string of parentheses is balanced or not.

# By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis in the correct
# order. For example, the string "((()))" has three pairs of balanced parentheses, so it is a balanced string. 
# On the other hand, the string "(()))" has an imbalance, as the last two parentheses do not match, so it is not
# balanced.  Also, the string ")(" is not balanced because the close parenthesis needs to follow the open
# parenthesis.

# Your program should take a string of parentheses as input and return True if it is balanced, or False if it
# is not. In order to solve this problem, use a Stack data structure.

# Function name:
# is_balanced_parentheses

# Remember: this is not a method within the Stack class, this is a separate function.  Indent all the way to
# the left.

# This will use the Stack class we created in these coding exercises:
    # Implement Stack Using List
    # Push for Stack That Uses Lists
    # Pop for Stack That Uses Lists

class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()



def is_balanced_parentheses(string):
    stack = Stack() # Create a new stack using the Stack class
    for s in string: # Iterate through each character in the input string
        if s == '(': # If the current character is an opening parentheses,
            stack.push(s) # push it onto the stack using the push method
        elif s == ')': # If the character is a closing parentheses,
            if stack.is_empty() or stack.pop() != '(': # Check if the stack is empty or if the next item in the
                return False # stack is not an open parentheses. If either of these conditions are true, return
                            # False because the parentheses are not balanced. 
    return stack.is_empty() # If the stack is empty, the run the 'is_empty' function which returns True if
                            # the length is zero, and false if not





def test_is_balanced_parentheses():
    try:
        assert is_balanced_parentheses('((()))') == True
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        assert is_balanced_parentheses('()') == True
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')

    try:
        assert is_balanced_parentheses('(()())') == True
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        assert is_balanced_parentheses('(()') == False
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        assert is_balanced_parentheses('())') == False
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

    try:
        assert is_balanced_parentheses(')(') == False
        print('Test case 6 passed')
    except AssertionError:
        print('Test case 6 failed')

    try:
        assert is_balanced_parentheses('') == True
        print('Test case 7 passed')
    except AssertionError:
        print('Test case 7 failed')

    try:
        assert is_balanced_parentheses('()()()()') == True
        print('Test case 8 passed')
    except AssertionError:
        print('Test case 8 failed')

    try:
        assert is_balanced_parentheses('(())(())') == True
        print('Test case 9 passed')
    except AssertionError:
        print('Test case 9 failed')

    try:
        assert is_balanced_parentheses('(()()())') == True
        print('Test case 10 passed')
    except AssertionError:
        print('Test case 10 failed')

    try:
        assert is_balanced_parentheses('((())') == False
        print('Test case 11 passed')
    except AssertionError:
        print('Test case 11 failed')

test_is_balanced_parentheses()

