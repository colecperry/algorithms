# 1790. Check if One String Swap Can Make Strings Equal

# Topics: Hash Table, String, Counting

# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

# Example 1:
# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last character of s2 to make "bank".

# Example 2:
# Input: s1 = "attack", s2 = "defend"
# Output: false
# Explanation: It is impossible to make them equal with one string swap.

# Example 3:
# Input: s1 = "kelb", s2 = "kelb"
# Output: true
# Explanation: The two strings are already equal, so no string swap operation is required.

# High-Level Idea: (Brute Force)
        # Try swapping every possible pair of characters in s1.
        # After each swap, check if the resulting string equals s2.
        # If any swap leads to equality, return True.

        # Time Complexity (TC): O(n^2 * n)
        # - O(n^2) for all (i, j) swap pairs
        # - O(n) for comparing and copying strings inside the loop

        # Space Complexity (SC): O(n)
        # - Creating a list copy of s1 each time uses O(n) space

from collections import Counter

class Solution: # Brute force O(n^2)
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: # Exit early if string are ==
            return True
        for i in range(len(s1)):
            for j in range(len(s1)):
                if i != j:
                    s1_list = list(s1)
                    s1_list[i], s1_list[j] = s1_list[j], s1_list[i] # Swap indexes
                    if s1_list == list(s2):
                        return True
        return False
    
    # High-Level Idea: (Optimal)
        # Traverse both strings together and collect all mismatched character pairs.
        # To fix with one swap:
        # - There must be exactly two mismatches.
        # - Swapping those two characters in s1 must result in s2.

        # Time Complexity (TC): O(n)
        # - Single pass over the strings using zip()

        # Space Complexity (SC): O(1) or O(2)
        # - At most two mismatches are stored in a list

    def areAlmostEqual2(self, s1: str, s2: str) -> bool: # Optimal O(n)
        if s1 == s2: # Exit early if strings are ==
            return True

        mismatches = [] # List to store the positions where characters differ

        for a, b in zip(s1, s2): # Compare characters from both strings
            if a != b:
                mismatches.append((a, b)) # Append a tuple

        # To be one swap away:
        if len(mismatches) == 2: # 1. Exactly two mismatched character pairs
            return mismatches[0] == mismatches[1][::-1] # 2. Swapping those characters in s1 would make it equal to s2

        return False # If not exactly two mismatches, it's not fixable with one swap


sol = Solution()
print(sol.areAlmostEqual2("bank", "kanb")) # true
print(sol.areAlmostEqual("attack", "defend")) # false
print(sol.areAlmostEqual("kelb", "kelb")) # true
print(sol.areAlmostEqual("abcd", "dcba")) # false