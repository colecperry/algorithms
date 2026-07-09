"""
=================================================================
STACK COMPLETE GUIDE
=================================================================

WHAT IS A STACK?
----------------
A stack is a linear data structure that follows LIFO (Last In, First Out) — the
last element pushed is the first to be popped, like a stack of plates. In Python,
a list naturally serves as a stack: append() pushes to the top and pop() removes
from the top, both in O(1).

Key characteristics:
- LIFO access: last pushed element is first popped
- push: stack.append(x) — O(1)
- pop: stack.pop() — O(1)
- peek: stack[-1] — O(1)
- All operations at the top only

When to use Stack:
- Matching/validating nested structures (parentheses, brackets)
- Next greater/smaller element problems (monotonic stack)
- Expression evaluation (RPN, infix with precedence)
- Decoding nested encodings (level-saving context)
- Building strings with cancellation rules (adjacent removal)

Common Stack problem types:
- Valid parentheses / bracket matching
- Daily temperatures / next warmer day (monotonic stack)
- Evaluate Reverse Polish Notation
- Decode String / nested encodings
- Remove adjacent duplicates in string

STACK CORE PATTERNS
===================
"""

from typing import List

"""
STACK COMPLEXITY REFERENCE
===========================

+---------------------------+------------------+------------------+
| Pattern                   | Time             | Space            |
+---------------------------+------------------+------------------+
| Matching Pairs            | O(n)             | O(n)             |
| Monotonic Stack           | O(n) amortized   | O(n)             |
| Expression Evaluation     | O(n)             | O(n)             |
| Nested Structure Decode   | O(n)             | O(n)             |
| String Construction       | O(n)             | O(n)             |
+---------------------------+------------------+------------------+

n = input length (string length or number of tokens)

NOTES:
- Matching Pairs: each char pushed once, popped at most once -> O(n)
- Monotonic Stack: each element pushed and popped at most once -> O(n) amortized
- Nested Decode: n refers to the length of the DECODED string (can be > input length)
- String Construction: each char pushed once, popped at most once
"""

"""
===============
STACK PATTERNS
===============
"""

"""
================================================================
PATTERN 1: MATCHING PAIRS (PARENTHESES / BRACKET VALIDATION)
PATTERN EXPLANATION: Push opening symbols onto the stack. When a closing symbol appears,
check if the stack top holds its matching opener — if yes, pop and continue; if no,
return False. The LIFO property ensures that the most recent unmatched opener is always
at the top, naturally handling nested structures. An empty stack at the end means
every opener was properly closed.

Applications: Valid parentheses, HTML tag matching, balanced bracket expressions.
================================================================
"""

class MatchingPairs:
    """
    Problem: Given a string of brackets '(', ')', '{', '}', '[', ']', determine
    if the brackets are validly matched and nested.

    Example:
        s = "([])"  -> True
        s = "([)]"  -> False (wrong nesting order)
        s = "((("   -> False (unclosed openers)

    Steps:
    1. Map each closing bracket to its expected opening bracket
    2. For each character:
       a. If closing: check stack top matches expected opener; pop if yes, return False if no
       b. If opening: push onto stack
    3. Return True only if stack is empty (no unmatched openers remain)
    """
    def isValid(self, s: str) -> bool:  # LC 20
        """
        TC: O(n) - single pass through string
        SC: O(n) - worst case all opening brackets (e.g., "(((((")
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0

    # Trace: s = "([])"
    # '(': push -> stack=['(']
    # '[': push -> stack=['(','[']
    # ']': mapping[']']='[', top='[' ✓ -> pop -> stack=['(']
    # ')': mapping[')']='(', top='(' ✓ -> pop -> stack=[]
    # Stack empty -> True ✓

sol = MatchingPairs()
print("Valid:", sol.isValid("()[]{}"))  # True
print("Valid:", sol.isValid("([)]"))   # False
print("Valid:", sol.isValid("{[]}"))   # True


"""
================================================================
PATTERN 2: MONOTONIC STACK (NEXT GREATER / SMALLER ELEMENT)
PATTERN EXPLANATION: Maintain a stack in strictly decreasing (or increasing) order.
When a new element breaks the order (is greater than the top for a decreasing stack),
pop elements until order is restored. Each popped element has found its "next greater"
element — the current one that broke the order. Since each element is pushed and popped
at most once, total time is O(n) amortized.

Key decision: decreasing stack -> finds next GREATER; increasing stack -> finds next SMALLER.

Applications: Daily temperatures, next greater element, stock span, largest rectangle.
================================================================
"""

class MonotonicStack:
    """
    Problem: Given an array of daily temperatures, return an array where answer[i]
    is the number of days you have to wait after day i for a warmer temperature.
    If no warmer day exists, answer[i] = 0.

    Example:
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        Output: [1, 1, 4, 2, 1, 1, 0, 0]

    Steps:
    1. Initialize result array of zeros, empty stack (stores indices)
    2. For each index i:
       a. While stack not empty AND temperatures[stack[-1]] < temperatures[i]:
          - Pop prev_day; answer[prev_day] = i - prev_day (days waited)
       b. Push i onto stack
    3. Indices remaining in stack never found a warmer day -> stay 0
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:  # LC 739
        """
        TC: O(n) - each index pushed and popped at most once
        SC: O(n) - stack stores indices
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []  # Monotonic decreasing by temperature value

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_day = stack.pop()
                answer[prev_day] = i - prev_day
            stack.append(i)

        return answer

    # Trace: temps = [73, 74, 75, 71, 69, 72, 76, 73]
    # i=0 (73): stack=[0]
    # i=1 (74): 74>73 -> pop 0, answer[0]=1; stack=[1]
    # i=2 (75): 75>74 -> pop 1, answer[1]=1; stack=[2]
    # i=3 (71): 71<75, push -> stack=[2,3]
    # i=4 (69): 69<71, push -> stack=[2,3,4]
    # i=5 (72): 72>69 -> pop 4, answer[4]=1; 72>71 -> pop 3, answer[3]=2; stack=[2,5]
    # i=6 (76): 76>72 -> pop 5, answer[5]=1; 76>75 -> pop 2, answer[2]=4; stack=[6]
    # i=7 (73): 73<76, push -> stack=[6,7]
    # Remaining [6,7] -> answer stays 0
    # Output: [1,1,4,2,1,1,0,0] ✓

sol = MonotonicStack()
print("Daily Temps:", sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1,1,4,2,1,1,0,0]


"""
================================================================
PATTERN 3: EXPRESSION EVALUATION (RPN / CALCULATOR)
PATTERN EXPLANATION: In Reverse Polish Notation (postfix), operators come after their
operands. Stack holds intermediate results: push numbers, and when an operator appears,
pop two operands, compute the result, and push it back. The final answer is the single
element remaining in the stack. Pop order matters for subtraction and division: pop b
first (top), then a (below), and compute a op b.

Applications: Evaluate RPN, basic calculator, expression parsing.
================================================================
"""

class ExpressionEval:
    """
    Problem: Evaluate the value of an arithmetic expression in Reverse Polish Notation.
    Valid operators: '+', '-', '*', '/'. Division truncates toward zero.

    Example:
        tokens = ["2","1","+","3","*"] -> (2+1)*3 = 9
        tokens = ["4","13","5","/","+"] -> 4+(13/5) = 4+2 = 6

    Steps:
    1. For each token:
       a. If number: push int(token) onto stack
       b. If operator: pop b (second), pop a (first), compute a op b, push result
    2. Return stack[0] — the final computed value
    """
    def evalRPN(self, tokens: List[str]) -> int:  # LC 150
        """
        TC: O(n) - process each token once
        SC: O(n) - stack holds intermediate results
        """
        stack = []

        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                b = stack.pop()
                a = stack.pop()
                if token == '+':   stack.append(a + b)
                elif token == '-': stack.append(a - b)
                elif token == '*': stack.append(a * b)
                else:              stack.append(int(a / b))  # Truncate toward zero
            else:
                stack.append(int(token))

        return stack[0]

    # Trace: tokens = ["2","1","+","3","*"]
    # "2": stack=[2]
    # "1": stack=[2,1]
    # "+": pop b=1, pop a=2; push 2+1=3; stack=[3]
    # "3": stack=[3,3]
    # "*": pop b=3, pop a=3; push 3*3=9; stack=[9]
    # Output: 9 ✓

sol = ExpressionEval()
print("Eval RPN:", sol.evalRPN(["2","1","+","3","*"]))    # 9
print("Eval RPN:", sol.evalRPN(["4","13","5","/","+"]))   # 6


"""
================================================================
PATTERN 4: NESTED STRUCTURE DECODING (SAVE AND RESTORE CONTEXT)
PATTERN EXPLANATION: When entering a deeper nesting level (opening bracket), push the
current accumulated state onto the stack and reset. When exiting (closing bracket), pop
the saved state and combine it with the current level's result. The stack acts as a
save/restore mechanism for multi-level nesting, building the result inside-out.

Applications: Decode string, parse nested expressions, directory paths.
================================================================
"""

class NestedDecode:
    """
    Problem: Given an encoded string where k[s] means string s repeated k times,
    decode and return the full string. Encodings can be nested.

    Example:
        s = "3[a2[c]]"
        Inner: 2[c] -> "cc"
        Outer: 3["a" + "cc"] = 3["acc"] -> "accaccacc"
        Output: "accaccacc"

    Steps:
    1. Track curr_str (current decoded segment) and curr_num (pending repeat count)
    2. On digit: accumulate multi-digit numbers (curr_num = curr_num * 10 + digit)
    3. On '[': push (curr_str, curr_num) onto stack; reset both to "" / 0
    4. On ']': pop (prev_str, count); curr_str = prev_str + count * curr_str
    5. On letter: append to curr_str
    """
    def decodeString(self, s: str) -> str:  # LC 394
        """
        TC: O(n) where n = length of decoded output
        SC: O(n) - stack depth proportional to nesting levels
        """
        stack = []
        curr_str = ""
        curr_num = 0

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                stack.append((curr_str, curr_num))
                curr_str, curr_num = "", 0
            elif char == ']':
                prev_str, count = stack.pop()
                curr_str = prev_str + count * curr_str
            else:
                curr_str += char

        return curr_str

    # Trace: s = "3[a2[c]]"
    # '3': curr_num=3
    # '[': push ("",3); curr_str="", curr_num=0 -> stack=[("",3)]
    # 'a': curr_str="a"
    # '2': curr_num=2
    # '[': push ("a",2); curr_str="", curr_num=0 -> stack=[("",3),("a",2)]
    # 'c': curr_str="c"
    # ']': pop ("a",2); curr_str="a" + 2*"c" = "acc" -> stack=[("",3)]
    # ']': pop ("",3); curr_str="" + 3*"acc" = "accaccacc" -> stack=[]
    # Output: "accaccacc" ✓

sol = NestedDecode()
print("Decoded:", sol.decodeString("3[a]2[bc]"))  # "aaabcbc"
print("Decoded:", sol.decodeString("3[a2[c]]"))   # "accaccacc"


"""
================================================================
PATTERN 5: STRING CONSTRUCTION (ADJACENT REMOVAL / CANCELLATION)
PATTERN EXPLANATION: Build a result string using the stack as a buffer. When adding a
character, check the stack top: if it matches the current character, they cancel (pop);
otherwise, push the character. This naturally handles cascading cancellations — removing
one pair can expose a new adjacent pair. Join the remaining stack to get the result.

Applications: Remove adjacent duplicates, backspace string compare, simplify path.
================================================================
"""

class StringConstruction:
    """
    Problem: Given a string s, repeatedly remove adjacent duplicate letters until
    no adjacent duplicates remain. Return the final string.

    Example:
        s = "abbaca" -> remove "bb" -> "aaca" -> remove "aa" -> "ca"
        Output: "ca"

        s = "azxxzy" -> remove "xx" -> "azzy" -> remove "zz" -> "ay"
        Output: "ay"

    Steps:
    1. Initialize empty stack
    2. For each character:
       a. If stack not empty AND stack top == current char: pop (cancel the pair)
       b. Otherwise: push current char
    3. Join and return remaining stack characters
    """
    def removeDuplicates(self, s: str) -> str:  # LC 1047
        """
        TC: O(n) - each character pushed at most once and popped at most once
        SC: O(n) - stack stores result characters
        """
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)

    # Trace: s = "azxxzy"
    # 'a': stack=['a']
    # 'z': stack=['a','z']
    # 'x': stack=['a','z','x']
    # 'x': top='x' == 'x' -> pop -> stack=['a','z']
    # 'z': top='z' == 'z' -> pop -> stack=['a']   <- cascading removal!
    # 'y': stack=['a','y']
    # Output: "ay" ✓

sol = StringConstruction()
print("Remove Dups:", sol.removeDuplicates("abbaca"))  # "ca"
print("Remove Dups:", sol.removeDuplicates("azxxzy"))  # "ay"
