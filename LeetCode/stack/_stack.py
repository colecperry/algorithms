from typing import List

# =============================================================================
# WHAT IS A STACK?
# =============================================================================
"""
A stack is a linear data structure that follows LIFO (Last In, First Out) principle:
    - The last element added is the first one to be removed
    - Think of a stack of plates: you add/remove from the top only
    - Two main operations: push (add) and pop (remove from top)

                                VISUAL EXAMPLE:

    Operation sequence: push(1) → push(2) → push(3) → pop() 
    
    Step 1: push(1)    Step 2: push(2)    Step 3: push(3)    Step 4: pop()  
         │                  │                  │                  │                 
         │                  │                 [3] ← top           │                 
         │                 [2] ← top          [2]                [2] ← top         
        [1] ← top          [1]                [1]                [1]              
    
    Python list representation: 
    - End of list = top of stack
    - stack.append(x) = push
    - stack.pop() = pop
    - stack[-1] = peek (look at top without removing)

Array representation: stack = [1, 2, 3]
- Index 0 (bottom): 1
- Index 2 (top): 3
- Push: append to end
- Pop: remove from end
"""

# =============================================================================
# STACK ADVANTAGES
# =============================================================================
"""
- All operations (push, pop, peek) are O(1)
- Perfect for: matching pairs, tracking state, reversing order, processing nested structures
- Better than other data structures when you need LIFO access pattern

    Operation       | Stack    | Queue    | Array (unsorted)
    ----------------|----------|----------|------------------
    Push/Add        | O(1)     | O(1)     | O(1)
    Pop/Remove top  | O(1)     | O(n)*    | O(n)
    Peek top        | O(1)     | O(1)     | O(n)
    Search          | O(n)     | O(n)     | O(n)
    
    *Queue removal from front is O(1), but array-based queues may require shifting
"""

# =============================================================================
# KEY OPERATIONS
# =============================================================================
"""
1. **push(x)**: Add element to top of stack
    - Append to end of list: stack.append(x)
    - Time: O(1)

2. **pop()**: Remove and return top element
    - Remove from end of list: stack.pop()
    - Time: O(1)
    - Important: Check if stack is empty first!

3. **peek() / top()**: Look at top element without removing
    - Access last element: stack[-1]
    - Time: O(1)

4. **isEmpty()**: Check if stack is empty
    - Boolean check: len(stack) == 0 or not stack
    - Time: O(1)

5. **size()**: Get number of elements
    - Length: len(stack)
    - Time: O(1)
"""

# =============================================================================
# WHEN TO USE STACKS
# =============================================================================
"""
When stacks shine:
    - Matching pairs - Parentheses, brackets, tags
    - Tracking state - Undo/redo, browser history, function calls
    - Parsing/evaluation - Expression evaluation, syntax parsing
    - Nested structures - Tree/graph traversal (DFS), backtracking
    - Monotonic problems - Next greater/smaller element

Real-world use cases:
    - Function call stack (recursion)
    - Undo/redo functionality
    - Browser back/forward buttons
    - Expression evaluation (calculators)
    - Syntax checking (compilers)
    - Depth-first search
"""

# ============================================================================
# CORE TEMPLATE: BASIC STACK IMPLEMENTATION
# ============================================================================

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item"""
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        """Return top item without removing"""
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items in stack"""
        return len(self.items)

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f"Top: {stack.peek()}")  # 3
print(f"Pop: {stack.pop()}")   # 3
print(f"Size: {stack.size()}")  # 2

# =============================================================================
# WHAT IS A MONOTONIC STACK?
# =============================================================================
"""
A monotonic stack maintains elements in sorted order (increasing or decreasing).
When a new element breaks the order, pop elements until order is restored.

MONOTONIC DECREASING: [7, 5, 3, 1] (top is smallest)
MONOTONIC INCREASING: [1, 3, 5, 7] (top is largest)

                VISUAL EXAMPLE - MONOTONIC DECREASING STACK:

Array: [3, 7, 1, 5] - Build decreasing stack (find next GREATER elements)

Step 1: Push 3                    Stack: [3]
Step 2: 7 > 3, pop 3, push 7      Stack: [7]     (3 found its next greater: 7)
Step 3: Push 1 -> 1 < 7           Stack: [7, 1]
Step 4: 5 > 1, pop 1, push 5      Stack: [7, 5]  (1 found its next greater: 5)

Remaining [7, 5] have no next greater element

                VISUAL EXAMPLE - MONOTONIC INCREASING STACK:

Array: [5, 3, 7, 2] - Build increasing stack (find next SMALLER elements)

Step 1: Push 5                    Stack: [5]
Step 2: 3 < 5, pop 5, push 3      Stack: [3]     (5 found its next smaller: 3)
Step 3: Push 7 -> 7 > 3           Stack: [3, 7]
Step 4: 2 < 7, pop 7, push 2      Stack: [3, 2]  (7 found its next smaller: 2)
        2 < 3, pop 3              Stack: [2]     (3 found its next smaller: 2)

Remaining [2] has no next smaller element
"""

# =============================================================================
# MONOTONIC STACK ADVANTAGES
# =============================================================================
"""
1. **Solves "next greater/smaller" problems in O(n) time**
   - Brute force: O(n²) with nested loops
   - Monotonic stack: O(n) - each element is pushed/popped at most once

2. **Clean and predictable**
   - Simple while loop for popping
   - No worst-case quadratic behavior
   - Clear invariant to maintain

Common applications:
- Next greater/smaller element
- Temperature waits, stock spans
- Histogram areas, building views
"""

# =============================================================================
# TIME & SPACE COMPLEXITY
# =============================================================================
"""
TIME: O(n) amortized
- Each element pushed once: n operations
- Each element popped at most once: n operations
- Total: 2n = O(n)

SPACE: O(n)
- Worst case: all elements stay (e.g., [5,4,3,2,1] in decreasing stack) -> O(n)
- Best case: O(1) if elements constantly pop

| Operation          | Time | Space |
|--------------------|------|-------|
| Process n elements | O(n) | O(n)  |
| Push/Pop           | O(1) | -     |
"""

# =============================================================================
# WHEN TO USE MONOTONIC STACKS
# =============================================================================
"""
USE when you see:
✓ "Find next/previous element that is greater/smaller"
✓ "How many days until warmer temperature?"
✓ "Nearest element with property X"
✓ Problems that seem O(n²) but need O(n)
"""

# ============================================================================
# CORE TEMPLATE: MONOTONIC DECREASING STACK
# Use when: Finding next GREATER element
# ============================================================================

def monotonic_decreasing_template(arr):
    """
    Maintains stack where values are in DECREASING order (top is smallest)
    When we find an element GREATER than top, pop all smaller elements
    """
    stack = []  # Can store values or indices depending on problem
    
    for i, num in enumerate(arr):
        # Found num greater than top of stack (top is smallest)
        while stack and num > stack[-1]:
            smaller = stack.pop() # Pop all elements SMALLER than current
            # smaller has found its "next greater element" (num)
            # Do something with this relationship
        
        stack.append(num)  # Or append index i
    
    return stack

print(monotonic_decreasing_template([5, 3, 8, 2, 1, 6, 4])) # [8, 6, 4]

# ============================================================================
# CORE TEMPLATE: MONOTONIC INCREASING STACK  
# Use when: Finding next SMALLER element
# ============================================================================

def monotonic_increasing_template(arr):
    """
    Maintains stack where values are in INCREASING order (top is largest)
    When we find an element SMALLER than top, pop all larger elements
    """
    stack = []  # Can store values or indices depending on problem
    
    for i, num in enumerate(arr):
        # Found num less than top of stack (top is largest)
        while stack and num < stack[-1]:
            larger = stack.pop() # Pop all elements LARGER than current
            # larger has found its "next smaller element" (num)
            # Do something with this relationship
        
        stack.append(num)  # Or append index i
    
    return stack

print(monotonic_increasing_template([3, 5, 2, 7, 8, 6, 1, 4])) # [1, 4]

# =============================================================================
                        # COMMON STACK PATTERNS
# =============================================================================

# ================================================================
# PATTERN 1: MATCHING PAIRS (Parentheses/Brackets Validation)
# PATTERN EXPLANATION: Use stack to match opening/closing symbols in correct order
# Key insight: 
#   - Push opening symbols onto stack
#   - When closing symbol appears, check if it matches top of stack
#   - Stack empty at end = all pairs matched correctly
# Applications: Valid parentheses, HTML tag matching, balanced expressions
# Time Complexity: O(n) - single pass through string
# Space Complexity: O(n) - worst case all opening symbols
# ================================================================

# PROBLEM 1: LC 20 - Valid Parentheses
# Key Insight: Stack naturally tracks most recent unmatched opening bracket

class ValidParentheses:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid.
    
    An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.
    
    Example 1:
    Input: s = "()"
    Output: true
    
    Example 2:
    Input: s = "()[]{}"
    Output: true
    
    Example 3:
    Input: s = "(]"
    Output: false
    
    Example 4:
    Input: s = "([)]"
    Output: false
    Explanation: The brackets are interleaved incorrectly
    
    TC: O(n) - iterate through string once
    SC: O(n) - worst case all opening brackets
    """
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { # match closing bracket to opening bracket
            ')':'(',
            '}': '{', 
            ']': '['
            }
        
        for char in s:
            if char in mapping:  # Char is closing bracket
                # Check if stack empty or top (opening) doesn't match
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()  # Match found, remove opening bracket
            else:  # Char is opening bracket
                stack.append(char)
        
        # Valid only if all brackets matched (stack empty)
        return len(stack) == 0

sol = ValidParentheses()
print(sol.isValid("()"))        # True
print(sol.isValid("()[]{}"))    # True
print(sol.isValid("(]"))        # False
print(sol.isValid("([)]"))      # False

# ================================================================
# PATTERN 2: MONOTONIC STACK (Next Greater/Smaller Element)
# PATTERN EXPLANATION: Maintain stack in sorted order to find next greater/smaller elements
# Key insight:
#   - Stack stores elements in monotonic (one-directional) order
#   - When new element breaks the order, pop elements → they've found their answer
#   - Each element pushed/popped exactly once → O(n) time
#   
#   For NEXT GREATER: use DECREASING stack (smaller elements on top)
#     → When current > stack top: pop (those found their next greater)
#   For NEXT SMALLER: use INCREASING stack (larger elements on top)
#     → When current < stack top: pop (those found their next smaller)
#
# Why it works: Stack maintains "candidates" that haven't found their answer yet
# Applications: Next greater/smaller, stock span, largest rectangle, temperature waits
# Time Complexity: O(n) - each element pushed and popped at most once
# Space Complexity: O(n) - stack storage
# ================================================================

# PROBLEM 2: LC 739 - Daily Temperatures
# Key Insight: Monotonic decreasing stack - pop when we find warmer temperature

class DailyTemperatures:
    """
    Given an array of integers temperatures represents the daily temperatures, 
    return an array answer such that answer[i] is the number of days you have 
    to wait after the ith day to get a warmer temperature. If there is no 
    future day for which this is possible, keep answer[i] == 0 instead.
    
    Example 1:
    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]
    Explanation:
    - Day 0 (73°): Next warmer is day 1 (74°) → wait 1 day
    - Day 1 (74°): Next warmer is day 2 (75°) → wait 1 day
    - Day 2 (75°): Next warmer is day 6 (76°) → wait 4 days
    - Day 3 (71°): Next warmer is day 5 (72°) → wait 2 days
    - Day 4 (69°): Next warmer is day 5 (72°) → wait 1 day
    - Day 5 (72°): Next warmer is day 6 (76°) → wait 1 day
    - Day 6 (76°): No warmer day → 0
    - Day 7 (73°): No warmer day → 0
    
    Strategy:
    1. Use monotonic DECREASING stack (store indices)
    2. Stack holds indices of days waiting for warmer temperature
    3. When current temp > stack top temp:
        - Pop index from stack (it found its answer!)
        - Calculate days waited = current_index - popped_index
    4. Always push current index onto stack
    
    Visualization for [73,74,75,71,69,72,76,73]:
    
    i=0, T=73: stack=[0]
    i=1, T=74: 74>73, pop 0, answer[0]=1-0=1, stack=[1]
    i=2, T=75: 75>74, pop 1, answer[1]=2-1=1, stack=[2]
    i=3, T=71: 71<75, stack=[2,3]
    i=4, T=69: 69<71, stack=[2,3,4]
    i=5, T=72: 72>69, pop 4, answer[4]=5-4=1
                72>71, pop 3, answer[3]=5-3=2
                72<75, stack=[2,5]
    i=6, T=76: 76>72, pop 5, answer[5]=6-5=1
                76>75, pop 2, answer[2]=6-2=4
                stack=[6]
    i=7, T=73: 73<76, stack=[6,7]
    
    Remaining in stack (6,7) have no warmer days → answer[6]=0, answer[7]=0
    
    TC: O(n) - each index pushed and popped at most once
    SC: O(n) - stack can store up to n indices
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n 
        stack = []  # Stores indices - maintains DECREASING temperature order
        
        for i, temp in enumerate(temperatures):            
            # While current temp is warmer than stack top:
            # Pop those days - they found their answer (today is their warmer day!)
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index  # Days waited = today - that day
            
            # Add current day to stack (it's now waiting for a warmer day)
            stack.append(i)
        
        # Days still in stack never found warmer weather (already 0)
        return answer

sol = DailyTemperatures()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
print(sol.dailyTemperatures([30,40,50,60]))  # [1,1,1,0]
print(sol.dailyTemperatures([30,60,90]))  # [1,1,0]

# ================================================================
# PATTERN 3: EXPRESSION EVALUATION (Postfix/Prefix/Infix)
# PATTERN EXPLANATION: Use stack to evaluate mathematical expressions
# Key insight:
#   - Stack holds operands (numbers)
#   - When operator encountered, pop operands, compute, push result
#   - Natural fit for postfix (reverse polish notation)
#   - Can handle precedence and parentheses for infix
# Applications: Calculator, evaluate RPN, basic calculator with parentheses
# Time Complexity: O(n) - process each token once
# Space Complexity: O(n) - stack storage
# ================================================================

# PROBLEM 3: LC 150 - Evaluate Reverse Polish Notation
# Key Insight: Stack holds intermediate results, operators pop and compute

class EvalRPN:
    """
    You are given an array of strings tokens that represents an arithmetic 
    expression in Reverse Polish Notation (postfix notation).
    
    Valid operators are '+', '-', '*', and '/'. Each operand may be an integer 
    or another expression. Division between two integers should truncate toward zero.
    
    Example:
    Input: tokens = ["2","1","+","3","*"]
    Output: 9
    Explanation: ((2 + 1) * 3) = 9
    
    How it works:
    - Numbers: push onto stack
    - Operator: pop two operands, compute, push result
    
    Step-by-step for ["2","1","+","3","*"]:
    1. "2": stack=[2]
    2. "1": stack=[2,1]
    3. "+": pop 1,2, compute 2+1=3, stack=[3]
    4. "3": stack=[3,3]
    5. "*": pop 3,3, compute 3*3=9, stack=[9]
    
    TC: O(n) - process each token once
    SC: O(n) - stack stores intermediate results
    """
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token in operators: # Operator encountered
                # Pop two operands (order matters for - and /)
                b = stack.pop()
                a = stack.pop()
                
                if token == '+': # Perform calcs
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                else:  # '/'
                    # Truncate toward zero (+ rounds down, - rounds up)
                    result = int(a / b)
                
                stack.append(result) # Push result
            else:
                stack.append(int(token)) # Push token if not an operator
        
        return stack[0]

sol = EvalRPN()
print(sol.evalRPN(["2","1","+","3","*"]))  # 9
print(sol.evalRPN(["4","13","5","/","+"]))  # 6
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # 22

# ================================================================
# PATTERN 4: NESTED STRUCTURE DECODING (DFS with State)
# PATTERN EXPLANATION: Use stack to handle nested encoding/structures
# Key insight:
#   - Stack stores context at each nesting level
#   - Opening bracket/digit: push current state, start new level
#   - Closing bracket: pop state, combine with current level
#   - Stack naturally handles arbitrary nesting depth
# Applications: Decode string, parse nested structures, directory path
# Time Complexity: O(n) where n is decoded output length
# Space Complexity: O(n) for stack depth
# ================================================================

# PROBLEM 4: LC 394 - Decode String
# Key Insight: Stack stores (count, previous_string) for each nesting level

class DecodeString:
    """
    Given an encoded string, return its decoded string.
    The encoding rule is: k[encoded_string], where the encoded_string inside 
    the square brackets is being repeated exactly k times.
    
    Example 1:
    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"
    
    Example 2:
    Input: s = "3[a2[c]]"
    Output: "accaccacc"
    Explanation: Inner "2[c]"=cc, then "3[acc]"="accaccacc"
    
    Example 3:
    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"
    
    Strategy:
    1. Use stack to store (previous_string, repeat_count) for each nesting level
    2. Build current string character by character
    3. On '[': push (current_string, current_count), reset for nested level
    4. On ']': pop (prev_string, count), combine: prev_string + count * current_string
    
    Visualization for "3[a2[c]]":
    
    char='3': count=3
    char='[': stack=[(curr_str="", count=3)], reset curr_str="", count=0
    char='a': curr_str="a"
    char='2': count=2
    char='[': stack=[("",3), ("a",2)], reset curr_str=""
    char='c': curr_str="c"
    char=']': pop ("a",2), curr_str = "a" + 2*"c" = "acc"
    char=']': pop ("",3), curr_str = "" + 3*"acc" = "accaccacc"
    
    TC: O(n) where n is length of decoded string
    SC: O(n) for stack depth
    """
    def decodeString(self, s: str) -> str:
        stack = [] # Stores (prev_string, repeat_count) for each nesting level
        curr_str = "" # Building current decoded string
        curr_num = 0 # Accumulating repeat count for next '['
        
        for char in s:
            if char.isdigit(): # Accumulate repeat count before each [
                # Build multi-digit number (e.g., "12" → 1*10 + 2 = 12)
                curr_num = curr_num * 10 + int(char)
                
            elif char == '[': # Enter new nesting level: save context & reset
                stack.append((curr_str, curr_num))
                curr_str = "" # Reset string and num for next nesting
                curr_num = 0  
                
            elif char == ']': # Exit nesting level: restore context & decode
                prev_str, num = stack.pop() # Pop prev string & repeat count
                curr_str = prev_str + (num * curr_str) # Combine: previous + (repeated current)
                
            else:
                # Regular letter: append to current string
                curr_str += char
        
        return curr_str


sol = DecodeString()
print(sol.decodeString("3[a]2[bc]"))     # "aaabcbc"
print(sol.decodeString("3[a2[c]]"))      # "accaccacc"
print(sol.decodeString("2[abc]3[cd]ef")) # "abcabccdcdcdef"

# ================================================================
# PATTERN 5: HISTOGRAM/RECTANGLE PROBLEMS (Area Calculation)
# PATTERN EXPLANATION: Use monotonic stack to calculate maximum areas
# Key insight:
#   - Use monotonic INCREASING stack (stores indices)
#   - When current < stack top: pop and calculate area using popped as height
#   - Width = current_index - stack_top_after_pop - 1
#   - Popped element is the shortest bar in this rectangle
#   - Works because monotonic property guarantees all bars to right were >= popped height
# Applications: Largest rectangle, maximal rectangle in matrix, trapping water
# Time Complexity: O(n) - each element pushed/popped once
# Space Complexity: O(n) - stack storage
# ================================================================

# PROBLEM 5: LC 84 - Largest Rectangle in Histogram
# Key Insight: Monotonic increasing stack + calculate area when popping

class LargestRectangle:
    """
    Given an array of integers heights representing the histogram's bar height 
    where the width of each bar is 1, return the area of the largest rectangle 
    in the histogram.
    
    Example:
    Input: heights = [2,1,5,6,2,3]
    Output: 10
    Explanation: The largest rectangle has height 5 and width 2 (bars at index 2,3)
    
    Visualization:
         6
       5 █
       █ █
       █ █   3
       █ █ 2 █
     2 █ █ █ █
     █ 1 █ █ █
    
    The rectangle with height 5 spans indices 2-3 (width=2), area = 5*2 = 10
    
    Strategy:
    1. Use monotonic INCREASING stack (store indices)
    2. When current height < stack top height:
        - Pop index (this bar is the height of rectangle)
        - Calculate width: current_index - stack_top_after_pop - 1
        - Calculate area: popped_height * width
    3. Add sentinel value 0 at end to process remaining bars
    
    Why it works:
    - Popped bar is shortest in its range
    - All bars between stack_top and current were >= popped (monotonic property)
    - So popped bar extends across that entire width
    
    Visualization for [2,1,5,6,2,3]:
    
    i=0, h=2: stack=[0]
    i=1, h=1: 1<2, pop 0, width=1-(-1)-1=1, area=2*1=2, stack=[1]
    i=2, h=5: stack=[1,2]
    i=3, h=6: stack=[1,2,3]
    i=4, h=2: 2<6, pop 3, width=4-2-1=1, area=6*1=6
              2<5, pop 2, width=4-1-1=2, area=5*2=10 ← max!
              stack=[1,4]
    i=5, h=3: stack=[1,4,5]
    i=6, h=0: Process remaining bars...
    
    TC: O(n) - each bar pushed and popped at most once
    SC: O(n) - stack stores indices
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Store indices
        max_area = 0
        heights.append(0)  # Sentinel to process remaining bars
        
        for i, h in enumerate(heights):
            # Pop bars taller than current (they can't extend further)
            while stack and heights[stack[-1]] > h:
                height_index = stack.pop()
                height = heights[height_index]
                
                # Width = distance to current minus distance to previous bar
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            
            stack.append(i)
        
        return max_area

sol = LargestRectangle()
print(sol.largestRectangleArea([2,1,5,6,2,3]))  # 10
print(sol.largestRectangleArea([2,4]))  # 4
print(sol.largestRectangleArea([1,1]))  # 2