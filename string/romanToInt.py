import ipdb;

# Roman to Integer

# Instructions
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II. Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# - I can be placed before V(5) and X(10) to make 4 and 9
# - X can be placed before L (50) and C (100) to make 40 and 90. 
# - C can be placed before D (500) and M (1000) to make 400 and 900.
# - Given a roman numeral, convert it to an integer.

# How to solve:
# Larger value comes before smaller value: Add the two values
# Smaller value comes before larger value: Subtract the smaller value from the larger






class Solution:
    def romanToInt(self, s):

# # Step 1: Create a dictionary of all roman numerals and coresponding values
        roman = { "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
                }

#         # Step 2: Create a result with the initial value of zero
        result = 0

#         # Step 3: Create a "for" loop to iterate through the characters in the "s" string which is the passed in roman numeral
        for i in range(len(s)):
#           # Does it have a character that comes after it? If yes,
#           # Is the next numeral greater than the current numeral? If yes,
            if len(s) > i+1 and roman[s[i+1]] > roman[s[i]]:
#           # Subtract the value of the numeral the current index from the result. If no,  
                result = result - roman[s[i]]
            else: 
#               # Add the value of the numberal at that index to the result
                result = result + roman[s[i]]
            print("----------")
            print("len(s):", len(s))
            print("i+1:", i+1)
            print("roman[s[i+1]: look at character after s[i]")
            print("s[i]:", s[i])
            print("result:", result)
            print("----------")

        return result
#     # ipdb.set_trace()
    
solution = Solution()
print(solution.romanToInt("MCMXCIV"))


# class Solution:
#     def romanToInt(self, s):

#         roman = { "I": 1,
#                 "V": 5,
#                 "X": 10,
#                 "L": 50,
#                 "C": 100,
#                 "D": 500,
#                 "M": 1000
#                 }

#         result = 0

#         for i in range(len(s)):
#             if len(s) > i + 1 and roman[s[i+1]] > roman[s[i]]:
#                 result = result - roman[s[i]]
#                 # ipdb.set_trace()
#             else: 
#                 result = result + roman[s[i]]
#             print("----------")
#             print("len(s):", len(s))
#             print("i+1:", i+1)
#             print("s[i+1]: look at character after s[i]")
#             print("s[i]:", s[i])
#             print("result:", result)
#             print("----------")
#         return result
    
# solution = Solution()
# print(solution.romanToInt("XIV"))

#ANOTHER SOLUTION
# sum = 0
#     for i in range(len(s)-1):
#         current = romanObj[s[i]]
#         nextvalue = romanObj[s[i+1]]
        
#         if current<nextvalue:
#             sum -= current
#         else:
#             sum += current
            
#     return (sum + romanObj[s[len(s)-1]])