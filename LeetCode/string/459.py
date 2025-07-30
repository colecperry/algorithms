# 459. Repeated Substring Pattern

# Topics: String, String Matching

# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

# Example 1:
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.

# Example 2:
# Input: s = "aba"
# Output: false

# Example 3:
# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

# How to Solve: O(n^2)
    # Step 1: Get the total length of the string (let's call it n)
    # We'll try different substring lengths from 1 up to n // 2 (since a repeat must occur at least twice)

    # Step 2: For each candidate length i from 1 to n // 2:
    #   - Use 'n % i == 0' to check if the string's length can be evenly divided by i
    #     → This means the full string could be made by repeating a substring of length i
        #     → Example: if n = 6 and i = 2, then 6 % 2 == 0 → a substring of length 2 could repeat 3 times
    #
    #   - If it divides evenly, extract the substring of length i from the start of the string → substring = s[:i]
    #
    #   - Use 'n // i' to calculate how many times to repeat the substring to reach the full length → This is floor division: it tells you how many complete chunks of size i fit into n
        #     → Example: 6 // 2 = 3 → repeat the substring 3 times
    #
    #   - Build the full repeated string and check if it matches the original
    #     → If it matches, return True (we found a valid repeating pattern)

    # Step 3: If we loop through all possible lengths and find no valid pattern, return False

    # Time Complexity (TC): O(n^2)
    # - We iterate through up to n/2 possible substring lengths → O(n)
    # - For each evenly dividable substring, we build a repeated string and compare it to s → O(n)
    # - So worst-case total is O(n) * O(n) = O(n^2), but the outer loop iterates n//2 times and we don't go into the if block every iteration so it is closer to O(n)

    # Space Complexity (SC): O(n)
    # - We build repeated substrings of length up to n when checking → uses O(n) temporary space


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool: # O(n)^2
        n = len(s)
        for i in range(1, n // 2 + 1): # Check all possible substring lengths
            if n % i == 0: # Check if the substring divides the length evenly
                substring = s[:i] # Get the substring
                repeat_count = n // i
                if substring * repeat_count == s: # Build full repeated string & check match
                    return True
        return False

sol = Solution()
print(sol.repeatedSubstringPattern("abab")) # True
print(sol.repeatedSubstringPattern("aba")) # False
print(sol.repeatedSubstringPattern("abcabcabcabc")) # True