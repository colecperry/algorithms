# 66. Plus One

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# Example 1: 
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2: 
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3: 
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

class Solution(object):
    def plusOne(self, digits):
        """
        TC: O(n) where n is the length of digits
            - O(n) to join digits into string
            - O(n) to parse string to integer
            - O(n) to convert integer back to string
            - O(n) to build result list
            Total: O(n)
        
        SC: O(n) where n is the length of digits
            - O(n) to hold temp string from join before turning to an int
            - O(n) to hold temp string from str(ds) before turning back to a list
            - O(n) for output list
            Total auxiliary space: O(n)
        """
        ds = int(''.join(str(d) for d in digits)) # Turn the arr into a string of digits then to an int
        ds = ds + 1 # Add one
        return [int(i) for i in str(ds)] # Use a list comprehension to turn the int back into a list of string digits then to an int

solution = Solution()
print(solution.plusOne([1, 2, 3]))
