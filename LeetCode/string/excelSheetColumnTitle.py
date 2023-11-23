# import ipdb;

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

# class Solution(object):
    # def convertToTitle(self, columnNumber):
    #     # Create an empty string for storing the characters...
    #     answer =''
    #     alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #     # Run a while loop while columnNumber is positive..
    #     while columnNumber > 0:
    #         # ipdb.set_trace()
    #         remainder = (columnNumber-1) % 26
    #         print("remainder:", remainder)
    #         char = alphabet[remainder]
    #         print("char:", char)
    #         answer = char + answer
    #         print("answer:", answer)
    #         columnNumber = (columnNumber-1)//26
    #         print("columnNumner:", columnNumber)
    #     return answer
    
class Solution(object):
    def convertToTitle(self, columnNumber):
        output = ""
        while columnNumber > 0:
            output = chr(ord('A') + (columnNumber - 1) % 26) + output
            print(ord('A'))
            print(chr(ord('A') + (columnNumber - 1) % 26))
            columnNumber = (columnNumber - 1) // 26
        return output


solution = Solution()
print(solution.convertToTitle(27))

