# 168. Excel Sheet Column Title

# Topics - Math, String

# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...

# Example 1: 
# Input: columnNumber = 1
# Output: "A"

# Example 2: 
# Input: columnNumber = 28
# Output: "AB"

# Example 3: 
# Input: columnNumber = 701
# Output: "ZY"

    
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        
        while columnNumber > 0:
            # Convert from 1-indexed (Excel) to 0-indexed (programming)
            columnNumber -= 1
            
            # Find letter position: 0=A, 1=B, 2=C, ..., 25=Z
            letter_index = columnNumber % 26
            
            # Convert index to actual letter
            letter = chr(ord('A') + letter_index)
            result.append(letter)
            
            # Move to the next digit position (like dividing by 10 in base-10)
            columnNumber //= 26
        
        # We built right-to-left, so reverse to get correct order
        return ''.join(reversed(result))

solution = Solution()
print(solution.convertToTitle(28))  # Output: "AB"

