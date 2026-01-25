# 17. Letter Combinations of a Phone Number

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# ┌─────────────────────────────────────────────┐
# │                                             │
# │   ╭───────╮   ╭───────╮   ╭───────╮         │
# │   │ 1     │   │ 2 abc │   │ 3 def │         │
# │   ╰───────╯   ╰───────╯   ╰───────╯         │
# │                                             │
# │   ╭───────╮   ╭───────╮   ╭───────╮         │
# │   │ 4 ghi │   │ 5 jkl │   │ 6 mno │         │
# │   ╰───────╯   ╰───────╯   ╰───────╯         │
# │                                             │
# │   ╭───────╮   ╭───────╮   ╭───────╮         │
# │   │ 7 pqrs│   │ 8 tuv │   │ 9 wxyz│         │
# │   ╰───────╯   ╰───────╯   ╰───────╯         │
# │                                             │
# │   ╭───────╮   ╭───────╮   ╭───────╮         │
# │   │   *   │   │ 0  _  │   │   #   │         │
# │   ╰───────╯   ╰───────╯   ╰───────╯         │
# │                                             │
# └─────────────────────────────────────────────┘

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
# Input: digits = "2"
# Output: ["a","b","c"]

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """
        TC: O(4^n * n)
            - for char in phone[...]     → branches 4 ways, n levels = 4^n total calls
            - result.append(path)        → copies string of length n = O(n) per combination

        SC: O(n)
            - backtrack(index + 1, ...)  → recursion goes n levels deep = O(n) stack
            - path + char                → path grows to length n = O(n) storage
        """
        if not digits: # Edge Case -> empty string
            return []
        
        phone = {
            '2': 'abc', 
            '3': 'def', 
            '4': 'ghi', 
            '5': 'jkl',
            '6': 'mno', 
            '7': 'pqrs', 
            '8': 'tuv', 
            '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index, path):
            # Base case: we've processed all digits
            if index == len(digits):
                result.append(path)
                return
            
            current_digit = digits[index] # Get the digit of the curr index

            # Try each letter for the current digit
            for char in phone[current_digit]:
                backtrack(index + 1, path + char) # Go to next index, concat char -> we do not need a backtrack call because prev callstack has the previous string as the path since we update each call
        
        backtrack(0, "") # start at index 0, path is a string

        return result
        

sol = Solution()
print(sol.letterCombinations("23")) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(sol.letterCombinations("2")) # ["a","b","c"]

# ============================================
# VISUALIZATION FOR LETTER COMBINATIONS: digits = "23"
# ============================================
#
# phone = {'2': 'abc', '3': 'def'}
#
#                              backtrack(index=0, path="")
#                                      digit = '2'
#                   /                      |                      \
#               TRY 'a'                 TRY 'b'                 TRY 'c'
#                 /                        |                        \
#            path="a"                  path="b"                  path="c"
#            index=1                   index=1                   index=1 
#            digit='3'                 digit='3'                 digit='3'
#          /     |     \             /     |     \             /     |     \
#       'd'     'e'    'f'        'd'     'e'    'f'        'd'     'e'    'f'
#        |       |      |          |       |      |          |       |      |
#      "ad"    "ae"   "af"       "bd"    "be"   "bf"       "cd"    "ce"   "cf"
#        ✓       ✓      ✓          ✓       ✓      ✓          ✓       ✓      ✓
#      SAVE    SAVE   SAVE       SAVE    SAVE   SAVE       SAVE    SAVE   SAVE
#
#
# Result: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
#
# Key: index controls which digit we're processing
#   index=0 → process '2' → try 'a', 'b', 'c'
#   index=1 → process '3' → try 'd', 'e', 'f'
#   index=2 → len(digits) reached → SAVE result
#
# No "start" index needed (unlike combinations) because:
#   - We're not choosing FROM the same pool
#   - Each level has its OWN set of choices (different digit)
#   - Order matters: "ad" and "da" would be different (if digits were "32")