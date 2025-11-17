"""
=================================================================
STACK COMPLETE GUIDE
=================================================================

WHAT IS A STACK?
----------------
A stack is a linear data structure that follows LIFO (Last In, First Out) principle.
The last element added is the first one to be removed, like a stack of plates.

Key characteristics:
- LIFO access: Last In, First Out
- Push: Add element to top (O(1))
- Pop: Remove element from top (O(1))
- Peek: Look at top without removing (O(1))
- All operations at one end only (the "top")

Visual representation:
    Operation: push(1) → push(2) → push(3) → pop()
    
    Step 1:     Step 2:     Step 3:     Step 4:
       │           │          [3] ← top      │
       │          [2] ← top   [2]           [2] ← top
      [1] ← top   [1]         [1]           [1]

Python implementation:
- List as stack: stack = []
- Push: stack.append(x)
- Pop: stack.pop()
- Peek: stack[-1]
- Empty check: not stack or len(stack) == 0

When to use Stack:
- Matching pairs (parentheses, brackets)
- Tracking state or history
- Parsing and evaluation
- Nested structures
- Reversing order
- DFS traversal

When NOT to use Stack:
- Need FIFO access (use queue)
- Need random access (use array/list)
- Need to access bottom elements frequently

Common stack problem types:
- Matching pairs and validation
- Next greater/smaller element (monotonic stack)
- Expression evaluation
- Nested structure decoding
- String construction with removal
- Backtracking state management

STACK CORE TEMPLATES
====================
"""

from typing import List, Optional

# ================================================================
# BASIC STACK TEMPLATE
# ================================================================
def basic_stack_template():
    """
    Basic stack operations using Python list
    
    TC: All operations O(1)
    SC: O(n) for stack storage
    
    OPERATIONS:
    - push: stack.append(x)
    - pop: stack.pop()
    - peek: stack[-1]
    - isEmpty: not stack or len(stack) == 0
    - size: len(stack)
    """
    stack = []
    
    # Push elements
    stack.append(1)
    stack.append(2)
    stack.append(3)
    
    # Peek at top (don't remove)
    top = stack[-1]  # 3
    
    # Pop from top
    removed = stack.pop()  # 3
    
    # Check if empty
    is_empty = not stack  # False
    
    # Get size
    size = len(stack)  # 2
    
    return stack

# ================================================================
# MATCHING PAIRS TEMPLATE
# ================================================================
def matching_pairs_template(s, pairs):
    """
    Template for matching opening/closing symbols
    
    TC: O(n) - single pass through string
    SC: O(n) - worst case all opening symbols
    
    WHEN TO USE:
    - Validate parentheses/brackets
    - Match opening and closing tags
    - Check balanced expressions
    
    PATTERN:
    1. Create mapping of closing → opening symbols
    2. For each character:
       - If opening: push to stack
       - If closing: check if matches stack top, pop if yes
    3. Stack should be empty if all matched
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:  # Closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:  # Opening bracket
            stack.append(char)
    
    return not stack

# ================================================================
# EXPRESSION EVALUATION TEMPLATE
# ================================================================
def evaluate_expression_template(tokens, operators):
    """
    Template for evaluating postfix expressions
    
    TC: O(n) - process each token once
    SC: O(n) - stack holds intermediate results
    
    WHEN TO USE:
    - Evaluate RPN (Reverse Polish Notation)
    - Calculator problems
    - Expression parsing
    
    PATTERN:
    1. For each token:
       - If number: push to stack
       - If operator: pop operands, compute, push result
    2. Return final result (top of stack)
    """
    stack = []
    
    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            result = compute(a, token, b)
            stack.append(result)
        else:
            stack.append(int(token))
    
    return stack[0]

# ================================================================
# NESTED STRUCTURE TEMPLATE
#
# WHAT IS A STACK NESTED STRUCTURE?
#     A stack nested structure handles data that can be embedded within itself, 
#     like Russian nesting dolls. Each opening bracket '[' creates a new "level" 
#     of nesting that must be resolved from innermost to outermost. The stack 
#     tracks the context at each nesting level, allowing us to:
#     - Save our current progress when entering a nested level
#     - Restore previous context when exiting a nested level
#     - Build the result from inside-out as we close brackets
# ================================================================
def nested_structure_template(s):
    """
    Template for decoding nested structures
    
    TC: O(n) where n = decoded output length
    SC: O(n) - stack depth for nesting levels
    
    WHEN TO USE:
    - Decode nested strings
    - Parse nested structures
    - Handle multiple nesting levels
    
    PATTERN:
    1. Stack stores context at each level
    2. On opening: push current state, reset
    3. On closing: pop state, combine with current
    4. Build result level by level
    """
    stack = []
    current = ""
    num = 0
    
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '[':
            stack.append((current, num))
            current = ""
            num = 0
        elif char == ']':
            prev_str, count = stack.pop()
            current = prev_str + count * current
        else:
            current += char
    
    return current

# ================================================================
# STRING CONSTRUCTION TEMPLATE
# ================================================================
def string_construction_template(s):
    """
    Template for building strings with adjacent removal
    
    TC: O(n) - each character processed once
    SC: O(n) - stack storage
    
    WHEN TO USE:
    - Remove adjacent duplicates
    - Build strings with cancellation rules
    - Simplify expressions
    
    PATTERN:
    1. For each character:
       - If matches stack top: pop (removal/cancellation)
       - Else: push to stack
    2. Join stack to form result string
    """
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Remove adjacent duplicate
        else:
            stack.append(char)
    
    return ''.join(stack)


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
✓ "Find next/previous element that is greater/smaller" ***
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

"""
COMPLEXITY QUICK REFERENCE
==========================

Stack Operation Complexities:
- Push: O(1) - append to end
- Pop: O(1) - remove from end
- Peek: O(1) - access last element
- Search: O(n) - must scan entire stack

Why Stack is Efficient:
- All core operations are O(1)
- No shifting required (unlike queue with arrays)
- Simple implementation with arrays/lists
- Perfect for LIFO access patterns

Pattern Complexities:
1. Matching Pairs: O(n) time, O(n) space
2. Monotonic Stack: O(n) time, O(n) space (amortized - each element push/pop once)
3. Expression Evaluation: O(n) time, O(n) space
4. Nested Structure: O(n) time, O(n) space (n = decoded length)
5. String Construction: O(n) time, O(n) space

Amortized Analysis (Monotonic Stack):
- Each element pushed once: n pushes
- Each element popped once: n pops
- Total: 2n operations over n elements
- Amortized: O(1) per element, O(n) total

Space Analysis:
- Best case: O(1) when stack stays small
- Worst case: O(n) when all elements pushed
- Matching pairs: O(n) worst case (all opening brackets)
- Monotonic stack: O(n) worst case (monotonic input)

When to Use Each Pattern:
1. Matching Pairs: Validation, balanced symbols
2. Monotonic Stack: Next greater/smaller, areas, spans
3. Expression Evaluation: Calculators, RPN, parsing
4. Nested Structure: Decoding, nested brackets
5. String Construction: Remove duplicates, simplify
"""

# ================================================================
# PATTERN 1: MATCHING PAIRS
# PATTERN EXPLANATION: Use stack to validate matching of opening and closing symbols.
# Push opening symbols onto stack, when closing symbol appears check if it matches stack top.
# Stack naturally tracks most recent unmatched opening symbol (LIFO property perfect for
# nested matching). Stack must be empty at end for valid input.
#
# TYPICAL STEPS:
# 1. Create mapping of closing → opening symbols
# 2. For each character:
#    - If opening symbol: push to stack
#    - If closing symbol: check if matches stack top, pop if match
#    - If no match or stack empty: invalid
# 3. After processing all characters: stack should be empty
# 4. Return true if empty, false otherwise
#
# Applications: Valid parentheses, HTML tag matching, balanced expressions, bracket validation.
# ================================================================

class MatchingPairsPattern:
    """
    Problem: Given string containing characters '(', ')', '{', '}', '[', ']', determine
    if the input string is valid. Valid means:
    - Open brackets closed by same type
    - Open brackets closed in correct order
    - Every closing bracket has corresponding opening bracket
    
    TC: O(n) - single pass through string
    SC: O(n) - worst case all opening brackets (e.g., "((((")
    
    How it works:
    1. Stack stores unmatched opening brackets
    2. When closing bracket appears, check if it matches top of stack
    3. If match: pop (pair matched), if no match: invalid
    4. LIFO property ensures most recent opening is checked first
    5. Empty stack at end means all pairs matched
    
    Why stack works:
    - Nested brackets must close in reverse order of opening
    - LIFO perfectly matches this reverse order requirement
    - Most recent unmatched opening is always at top
    """
    def isValid(self, s: str) -> bool: # LC 20
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:  # Closing bracket
                # Check if stack empty or top doesn't match
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()  # Match found, remove opening
            else:  # Opening bracket
                stack.append(char)
        
        # Valid only if all brackets matched (stack empty)
        return len(stack) == 0

# Example:
# s = "([)]"
#
# char='(': opening, push → stack=['(']
# char='[': opening, push → stack=['(', '[']
# char=')': closing, top='[' but need '(' → mismatch!
# Output: False
#
# s = "([])"
#
# char='(': push → stack=['(']
# char='[': push → stack=['(', '[']
# char=']': matches '[', pop → stack=['(']
# char=')': matches '(', pop → stack=[]
# Stack empty ✓
# Output: True

sol = MatchingPairsPattern()
print("Valid:", sol.isValid("()"))  # True
print("Valid:", sol.isValid("()[]{}"))  # True
print("Valid:", sol.isValid("(]"))  # False
print("Valid:", sol.isValid("([)]"))  # False


# ================================================================
# PATTERN 2: MONOTONIC STACK
# PATTERN EXPLANATION: Maintain stack in sorted order (monotonically increasing or decreasing). When new element breaks the order, pop elements until order restored. Popped elements have found their "answer" (next greater/smaller). Each element pushed and popped at most once, giving O(n) time. Two variants:
#
# DECREASING stack (top is smallest): finds next GREATER element
# - Pop when current > stack top
#
# INCREASING stack (top is largest): finds next SMALLER element
# - Pop when current < stack top
#
# TYPICAL STEPS (Next Greater):
# 1. Initialize stack (stores indices), result array
# 2. For each index:
#    - While current value > stack top value: pop (found next greater)
#    - Calculate answer for popped index
#    - Push current index
# 3. Remaining stack elements have no answer
#
# Applications: Daily temperatures, next greater element, stock span, largest rectangle.
# ================================================================

class MonotonicStackPattern:
    """
    BASIC APPLICATION: Daily Temperatures
    
    Problem: Given array of daily temperatures, return array where answer[i] is number
    of days until warmer temperature. If no warmer day exists, answer[i] = 0.
    
    TC: O(n) - each index pushed and popped at most once (2n operations total)
    SC: O(n) - stack stores indices
    
    How it works:
    1. Use monotonic DECREASING stack (stores indices)
    2. Stack holds indices of days waiting for warmer temperature
    3. When current temp > stack top temp:
       - Pop index (it found its answer)
       - Calculate wait = current_day - popped_day
    4. Always push current day's index
    5. Days remaining in stack never found warmer temperature
    
    Why decreasing stack:
    - Want to find next GREATER (warmer) temperature
    - Maintain decreasing order so we can detect when greater appears
    - When current > top, all smaller temps in stack found their answer
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: # LC 739
        n = len(temperatures)
        answer = [0] * n
        stack = []  # Monotonic decreasing (stores indices)
        
        for i, temp in enumerate(temperatures):
            # While current temp warmer than stack top
            while stack and temperatures[stack[-1]] < temp:
                prev_day = stack.pop()
                answer[prev_day] = i - prev_day  # Days waited
            
            stack.append(i)
        
        # Remaining in stack never found warmer day (already 0)
        return answer
    
    # ================================================================
    # ADVANCED APPLICATION: Largest Rectangle in Histogram
    # ================================================================
    def largestRectangleArea(self, heights: List[int]) -> int: # LC 84
        """
        ADVANCED: Monotonic stack for area calculation
        
        Problem: Given histogram bar heights, find largest rectangle area.
        
        TC: O(n) - each bar pushed and popped once
        SC: O(n) - stack stores indices
        
        How it works:
        1. Use monotonic INCREASING stack (stores indices)
        2. When current height < stack top height:
           - Pop index (this bar becomes height of rectangle)
           - Width = distance between current and new stack top
           - Area = popped_height * width
        3. Add sentinel 0 at end to process remaining bars
        
        Why increasing stack:
        - Want to find when bars can't extend further (next smaller)
        - Popped bar is shortest in its extendable range
        - All bars between stack_top and current were >= popped (monotonic property)
        - So rectangle with popped height spans that entire width
        """
        stack = []
        max_area = 0
        heights.append(0)  # Sentinel to flush remaining bars
        
        for i, h in enumerate(heights):
            # Pop bars taller than current (can't extend to current position)
            while stack and heights[stack[-1]] > h:
                height_idx = stack.pop()
                height = heights[height_idx]
                
                # Width = current position - previous bar position - 1
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            
            stack.append(i)
        
        return max_area

# Example (Daily Temperatures):
# temps = [73,74,75,71,69,72,76,73]
#
# i=0 (73): stack=[0]
# i=1 (74): 74>73, pop 0, answer[0]=1, stack=[1]
# i=2 (75): 75>74, pop 1, answer[1]=1, stack=[2]
# i=3 (71): 71<75, stack=[2,3]
# i=4 (69): 69<71, stack=[2,3,4]
# i=5 (72): 72>69, pop 4, answer[4]=1
#           72>71, pop 3, answer[3]=2
#           stack=[2,5]
# i=6 (76): 76>72, pop 5, answer[5]=1
#           76>75, pop 2, answer[2]=4
#           stack=[6]
# i=7 (73): 73<76, stack=[6,7]
#
# Output: [1,1,4,2,1,1,0,0]
#
# Example (Histogram):
# heights = [2,1,5,6,2,3]
#
# Visual:
#     6
#   5 █
#   █ █     3
#   █ █   2 █
# 2 █ █   █ █
# █ 1 █   █ █
#
# Largest rectangle: height=5, width=2, area=10
# Output: 10

sol = MonotonicStackPattern()
print("Daily temps:", sol.dailyTemperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
print("Largest rectangle:", sol.largestRectangleArea([2,1,5,6,2,3]))  # 10


# ================================================================
# PATTERN 3: EXPRESSION EVALUATION
# PATTERN EXPLANATION: Use stack to evaluate mathematical expressions, particularly Reverse
# Polish Notation (postfix). Stack holds operands (numbers), when operator encountered pop
# two operands, compute result, push back. Natural fit for postfix notation where operators
# come after operands. Can extend to handle infix with precedence.
#
# TYPICAL STEPS (RPN):
# 1. For each token in expression:
#    - If number: push to stack
#    - If operator: pop two operands (order matters!)
#    - Compute: second_operand operator first_operand
#    - Push result back to stack
# 2. Final result is only element left in stack
#
# Applications: Evaluate RPN, basic calculator, expression parsing, operator precedence.
# ================================================================

class ExpressionPattern:
    """
    Problem: Evaluate value of arithmetic expression in Reverse Polish Notation (RPN).
    Valid operators: '+', '-', '*', '/'. Each operand may be integer or another expression.
    Division truncates toward zero.
    
    TC: O(n) - process each token exactly once
    SC: O(n) - stack holds intermediate results
    
    How it works:
    1. Stack holds numbers (operands)
    2. When operator encountered:
       - Pop second operand (b)
       - Pop first operand (a)
       - Compute: a operator b (order matters for - and /)
       - Push result back
    3. Final result is top of stack
    
    Why RPN uses stack:
    - Operators come after operands
    - Stack provides operands in reverse order naturally
    - No parentheses needed (order is implicit)
    - Each operation reduces two numbers to one
    """
    def evalRPN(self, tokens: List[str]) -> int: # LC 150
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token in operators:
                # Pop two operands (order matters!)
                b = stack.pop()  # Second operand
                a = stack.pop()  # First operand
                
                # Compute result
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                else:  # '/'
                    result = int(a / b)  # Truncate toward zero
                
                stack.append(result)
            else:
                # Number: push to stack
                stack.append(int(token))
        
        return stack[0]  # Final result

# Example:
# tokens = ["2","1","+","3","*"]
# Represents: (2 + 1) * 3
#
# Token "2": stack=[2]
# Token "1": stack=[2,1]
# Token "+": pop 1,2, compute 2+1=3, stack=[3]
# Token "3": stack=[3,3]
# Token "*": pop 3,3, compute 3*3=9, stack=[9]
#
# Output: 9
#
# Example 2:
# tokens = ["4","13","5","/","+"]
# Represents: 4 + (13 / 5)
#
# Token "4": stack=[4]
# Token "13": stack=[4,13]
# Token "5": stack=[4,13,5]
# Token "/": pop 5,13, compute 13/5=2, stack=[4,2]
# Token "+": pop 2,4, compute 4+2=6, stack=[6]
#
# Output: 6

sol = ExpressionPattern()
print("Eval RPN:", sol.evalRPN(["2","1","+","3","*"]))  # 9
print("Eval RPN:", sol.evalRPN(["4","13","5","/","+"]))  # 6


# ================================================================
# PATTERN 4: NESTED STRUCTURE DECODING
# PATTERN EXPLANATION: Use stack to decode strings with nested encoding patterns. Stack
# stores context (previous state) at each nesting level. When entering new level (opening
# bracket), push current context and reset. When exiting level (closing bracket), pop
# context and combine with current level's result. Handles arbitrary nesting depth.
#
# TYPICAL STEPS:
# 1. Initialize stack, current_string, current_number
# 2. For each character:
#    - If digit: accumulate into current_number
#    - If '[': push (current_string, current_number), reset both
#    - If ']': pop (prev_string, count), combine: prev + count * current
#    - If letter: append to current_string
# 3. Return current_string (fully decoded)
#
# Applications: Decode string, parse nested structures, directory paths, expression trees.
# ================================================================

class NestedStructurePattern:
    """
    Problem: Given encoded string, return decoded string. Encoding rule: k[encoded_string]
    means encoded_string repeated k times. Can have nested encodings.
    
    TC: O(n) where n = length of decoded string (can be larger than input)
    SC: O(n) - stack depth proportional to nesting levels
    
    How it works:
    1. Stack stores (previous_string, repeat_count) for each nesting level
    2. Build current string character by character
    3. On '[': save current context to stack, reset for nested level
    4. On ']': pop context, decode current level: prev_string + count * current_string
    5. Continue building outward from innermost to outermost
    
    Why stack works:
    - Each nesting level needs to remember context
    - Inner levels decode first, then outer levels multiply
    - LIFO matches the nesting structure perfectly
    """
    def decodeString(self, s: str) -> str: # LC 394
        stack = []  # Stores (string_so_far, repeat_count)
        curr_str = ""
        curr_num = 0
        
        for char in s:
            if char.isdigit():
                # Accumulate multi-digit numbers
                curr_num = curr_num * 10 + int(char)
            
            elif char == '[':
                # Enter new nesting level: save context
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            
            elif char == ']':
                # Exit nesting level: restore context and decode
                prev_str, count = stack.pop()
                curr_str = prev_str + count * curr_str
            
            else:
                # Regular letter: append to current
                curr_str += char
        
        return curr_str

# Example:
# s = "3[a2[c]]"
#
# char='3': curr_num=3
# char='[': push ("",3), reset → stack=[("",3)]
# char='a': curr_str="a"
# char='2': curr_num=2
# char='[': push ("a",2), reset → stack=[("",3), ("a",2)]
# char='c': curr_str="c"
# char=']': pop ("a",2), curr_str = "a" + 2*"c" = "acc"
#          → stack=[("",3)]
# char=']': pop ("",3), curr_str = "" + 3*"acc" = "accaccacc"
#          → stack=[]
#
# Output: "accaccacc"
#
# Example 2:
# s = "2[abc]3[cd]ef"
#
# Process "2[abc]": → "abcabc"
# Process "3[cd]": → "cdcdcd"
# Append "ef": → "abcabccdcdcdef"
# Output: "abcabccdcdcdef"

sol = NestedStructurePattern()
print("Decoded:", sol.decodeString("3[a]2[bc]"))  # "aaabcbc"
print("Decoded:", sol.decodeString("3[a2[c]]"))  # "accaccacc"
print("Decoded:", sol.decodeString("2[abc]3[cd]ef"))  # "abcabccdcdcdef"


# ================================================================
# PATTERN 5: STRING CONSTRUCTION (ADJACENT REMOVAL)
# PATTERN EXPLANATION: Build string using stack where adjacent duplicates cancel each other.
# When adding character, check if it matches stack top. If yes, pop (removal/cancellation).
# If no, push character. Stack naturally handles cascading removals where removing one pair
# creates new adjacent pair. Join stack at end to form final string.
#
# TYPICAL STEPS:
# 1. Initialize empty stack
# 2. For each character:
#    - If stack not empty AND top matches current: pop (cancel pair)
#    - Else: push current character
# 3. Join stack elements to form final string
# 4. Return result
#
# Applications: Remove adjacent duplicates, backspace string compare, simplify path.
# ================================================================

class StringConstructionPattern:
    """
    Problem: Given string s consisting of lowercase letters, repeatedly remove adjacent
    duplicate letters. Keep removing until no more adjacent duplicates.
    Return final string after all such removals.
    
    TC: O(n) - process each character once
    SC: O(n) - stack stores characters of result string
    
    How it works:
    1. Stack builds result string character by character
    2. When adding character, check if it matches top
    3. If match: pop (adjacent duplicates removed)
    4. If no match: push (add to result)
    5. Cascading removal happens automatically (stack property)
    
    Why stack works:
    - After removing pair, previous character becomes adjacent to next
    - Stack top is always the last unmatched character
    - Removal can trigger more removals (cascading)
    - LIFO naturally handles this cascade
    """
    def removeDuplicates(self, s: str) -> str: # LC 1047
        stack = []
        
        for char in s:
            # If current matches top, remove both (adjacent duplicates)
            if stack and stack[-1] == char:
                stack.pop()
            else:
                # No match, add to stack
                stack.append(char)
        
        return ''.join(stack)

# Example:
# s = "abbaca"
#
# char='a': stack=['a']
# char='b': stack=['a','b']
# char='b': matches top, pop → stack=['a']
# char='a': matches top, pop → stack=[]
# char='c': stack=['c']
# char='a': stack=['c','a']
#
# Output: "ca"
#
# Example 2 (Cascading):
# s = "azxxzy"
#
# char='a': stack=['a']
# char='z': stack=['a','z']
# char='x': stack=['a','z','x']
# char='x': matches top, pop → stack=['a','z']
# char='z': matches top, pop → stack=['a']  ← Cascade!
# char='y': stack=['a','y']
#
# Output: "ay"
#
# Notice: Removing 'xx' exposed 'zz', which also got removed

sol = StringConstructionPattern()
print("Remove duplicates:", sol.removeDuplicates("abbaca"))  # "ca"
print("Remove duplicates:", sol.removeDuplicates("azxxzy"))  # "ay"