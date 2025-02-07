# Length of Last Word - #58

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

# How to solve: (Neetcode solution)
    # Eliminate white spaces from beginning and end of the array w/o using strip()
    # Start iterating from the end of the string
    # count characters until either we hit a white space or we reach the beginning of the string

    # Time complexity - worst case we have to iterate over the whole string -> O(n)
    # Space complexity - 0(1) - only use one variable for counting

# How to solve (w/ extra memory):
    # Eliminate white spaces from the beginning and end of the array using strip()
    # Use split() to split each word of the string into an array (When you use .split() without specifying a delimiter, Python automatically treats consecutive spaces as a single separator and removes empty strings from the result.)
    # Return the last word in the array

    # Time complexity - we have to iterate through the whole string once to use .split() and once again to use .strip() - > O(n)
    # Memory complexity
        # Strip() -> we have to iterate through whole original string to create a new trimmed string: O(n)
        # Split() -> When you call .split() on a string, Python creates a new list containing all the words as separate string objects. This means that in the worst case, it duplicates the original string in memory, leading to O(N) space complexity.

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

class Solution(object):
    def lengthOfLastWord(self, s):
        i = len(s) - 1 # Pointer starting at the end of the input string
        length = 0 # Variable to count the length of the last word

        while s[i] == " ": # Loop from end until we reach a non-space
            i -= 1 # Decrement the index
        
        while i >= 0 and s[i] != " ": # Continue loop as long as index >= 0 or ele != " "
            length += 1 # Increase the length each iteration
            i -= 1 # Decrement the index
        
        return length
        


    def lengthOfLastWord2(self, s):
        # strip white space (beg & end) and split the str
        words = s.strip().split()
        return len(words[-1]) # Split returns a list

my_solution = Solution()
print(my_solution.lengthOfLastWord("Hello World"))
print(my_solution.lengthOfLastWord("   fly me   to   the moon  "))
print(my_solution.lengthOfLastWord("luffy is still joyboy"))