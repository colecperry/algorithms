# 246. Strobogrammatic Number

# Topics: Hash Table, Two Pointer, String

# Given a string num which represents an integer, return true if num is a strobogrammatic number.

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Example 1:
# Input: num = "69"
# Output: true

# Example 2:
# Input: num = "88"
# Output: true

# Example 3:
# Input: num = "962"
# Output: false

# How to solve:
    # Iterate through nums in reverse, and append each the 180 degree version of the number to the string

# Time Complexity: O(N) because the algorithm iterates through the input string once, performing constant-time lookups and concatenations.

# Space Complexity: O(N) because a new string is created to store the transformed version of the input.

def isStrobogrammatic(num):
    my_string = ""  # Output sting
    my_dict = {   # Dict of strobogramatic nums
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6'
    }
    
    for i in range(len(num) - 1, -1, -1): # Iterate backwards
        if num[i] not in my_dict:  # If num isn't strobogrammatic
            return False 
        my_string += my_dict[num[i]]  # Use string concatenation 
    
    return my_string == num

print(isStrobogrammatic("69"))
print(isStrobogrammatic("88"))
print(isStrobogrammatic("962"))