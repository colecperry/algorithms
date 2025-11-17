# =============================================================================
# WHAT IS A STRING?
# =============================================================================
"""
A string is a sequence of characters stored in contiguous memory:
    - Immutable in Python (cannot modify in-place, must create new string)
    - Accessed by index like arrays
    - Each character has a position from 0 to len(s)-1
    - Strings are iterable (can loop through characters)

VISUAL EXAMPLE:

    String: s = "hello"
    
    Index:    0   1   2   3   4
    Chars:   'h' 'e' 'l' 'l' 'o'
    
    Negative indexing (from end):
    Index:   -5  -4  -3  -2  -1
    Chars:   'h' 'e' 'l' 'l' 'o'
    
    Access patterns:
    - s[0] = 'h' (first character)
    - s[4] = 'o' (last character)
    - s[-1] = 'o' (last character, negative index)
    - s[1:4] = "ell" (slice from index 1 to 3)
    - len(s) = 5 (length of string)

String vs List representation:
- String: "hello" → immutable sequence of characters
- List: ['h', 'e', 'l', 'l', 'o'] → mutable sequence
"""

# =============================================================================
# STRING ADVANTAGES & DISADVANTAGES
# =============================================================================
"""
Advantages:
- Fast random access: O(1) by index
- Memory efficient (contiguous storage)
- Built-in methods for common operations
- Easy to compare, concatenate, and search

Disadvantages:
- Immutable in Python (modifications create new strings)
- Concatenation in loops is O(n²) (use join() instead)
- Cannot modify individual characters directly
- Large string operations can be memory-intensive

    Operation           | String      | List
    --------------------|-------------|-------------
    Access by index     | O(1)        | O(1)
    Slice [i:j]         | O(k)*       | O(k)*
    Concatenate         | O(n+m)      | O(1) with append
    Search substring    | O(n*m)      | N/A
    Replace             | O(n)        | O(1) for single ele
    Join/Split          | O(n)        | O(n)
    
    *k = length of slice
"""

# =============================================================================
# PYTHON STRING IMMUTABILITY
# =============================================================================
"""
CRITICAL: Strings are IMMUTABLE in Python!

What this means:
- You CANNOT change a string in-place
- Every "modification" creates a NEW string
- This affects performance in loops

Example of immutability:
    s = "hello"
    s[0] = 'H'  # ❌ ERROR: 'str' object does not support item assignment
    
    # Must create new string:
    s = 'H' + s[1:]  # ✅ Creates new string "Hello"

Performance trap - BAD:
    result = ""
    for char in s:
        result += char # O(n²) - creates new str each iteration!

Performance optimization - GOOD:
    result = []
    for char in s:
        result.append(char)  # O(1) append
    result = ''.join(result)  # O(n) - single operation

Key takeaway: For string building, use LIST then JOIN!
"""

# =============================================================================
# ESSENTIAL STRING OPERATIONS
# =============================================================================
"""
1. **Indexing and Slicing**:
    s = "hello"
    s[0]        # 'h' - single character
    s[-1]       # 'o' - last character
    s[1:4]      # 'ell' - slice [start:end) (end not included)
    s[:3]       # 'hel' - from beginning to index 3
    s[2:]       # 'llo' - from index 2 to end
    s[::2]      # 'hlo' - every 2nd character
    s[::-1]     # 'olleh' - reverse string

2. **Length and Membership**:
    len(s)      # 5 - number of characters
    'e' in s    # True - check if character exists
    'x' in s    # False
    'ell' in s  # True - check if substring exists

3. **Case Conversion**:
    s.upper()       # 'HELLO' - all uppercase
    s.lower()       # 'hello' - all lowercase
    s.capitalize()  # 'Hello' - first char uppercase
    s.title()       # 'Hello World' - each word capitalized
    s.swapcase()    # 'HELLO' → 'hello', 'hello' → 'HELLO'

4. **Searching**:
    s = 'hello'
    s.find('l')         # 2 - first occurrence index (-1 if not found)
    s.rfind('l')        # 3 - last occurrence index
    s.index('l')        # 2 - like find() but raises error if not found
    s.count('l')        # 2 - number of occurrences
    s.startswith('he')  # True
    s.endswith('lo')    # True

5. **Modification (returns new string)**:
    s.replace('l', 'L')     # 'heLLo' - replace all occurrences
    s.strip()               # Remove leading/trailing whitespace
    s.lstrip() / s.rstrip() # Remove left/right whitespace
    
6. **Split and Join**:
    "a b c".split()         # ['a', 'b', 'c'] - splits string into list of substrings by whitespace
    "a,b,c".split(',')      # ['a', 'b', 'c'] - split by delimiter
    ' '.join(['a','b','c']) # 'a b c' - join list into string split by delimiter
    ''.join(['h','i'])      # 'hi' - join without separator

7. **Character Checks**:
    s.isalpha()     # True if all alphabetic
    s.isdigit()     # True if all digits
    s.isalnum()     # True if all alphanumeric
    s.isspace()     # True if all whitespace
    s.islower()     # True if all lowercase
    s.isupper()     # True if all uppercase
"""

# ================================================================
# PATTERN 1: SLIDING WINDOW
# Strategy: Maintain a flexible window with two pointers:
#   1. Expand right pointer to include new characters
#   2. Contract left pointer when window becomes invalid
#   3. Track optimal solution while window is valid
#
# ================================================================

# PROBLEM: LC 3 - Longest Substring Without Repeating Characters
# Find longest substring with all unique characters

class LongestSubstringWithoutRepeating:
    """
    Given a string s, find the length of the longest substring without repeating characters.
    
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    
    TC: O(n)
    SC: O(k) where k is character set size
    """

    def lengthOfLongestSubstring(self, s):
        char_count = {} # Char freq's in curr window
        max_length = 0 # max len of string w/o repeating chars
        left = 0 # left ptr
        
        # STEP 1: Expand window by moving right pointer
        for right in range(len(s)):
            char = s[right]
            char_count[char] = char_count.get(char, 0) + 1
            
            # STEP 2: Contract window when condition violated (duplicate found) -> curr char has dup
            while char_count[char] > 1:
                char_count[s[left]] -= 1
                left += 1 # Shrink from L until window valid
            
            # STEP 3: Update result when window is valid
            # Window is always valid here (no duplicates)
            max_length = max(max_length, right - left + 1)
        
        return max_length

sol = LongestSubstringWithoutRepeating()
print(sol.lengthOfLongestSubstring("abcabcbb"))  # 3
print(sol.lengthOfLongestSubstring("bbbbb"))  # 1
print(sol.lengthOfLongestSubstring("pwwkew"))  # 3
print(sol.lengthOfLongestSubstring(""))  # 0

# ================================================================
# PATTERN 2: TWO POINTERS
# Strategy: Use two pointers moving toward/away from each other:
#   1. Initialize pointers at strategic positions (often opposite ends)
#   2. Move pointers based on comparison logic
#   3. Process elements while maintaining invariant
#
# Common applications: palindromes, reversals, partitioning, comparisons
# Time: Usually O(n) | Space: O(1)
# ================================================================

# PROBLEM: LC 125 - Valid Palindrome
# Check if string is palindrome (reads same forwards/backwards)

class ValidPalindrome:
    """
    Given a string s, return true if it is a palindrome, considering only 
    alphanumeric characters and ignoring cases.
    
    Input: s = "A man, a plan, a canal: Panama"
    Output: True
    Explanation: "amanaplanacanalpanama" is a palindrome.
    
    Input: s = "race a car"
    Output: False
    Explanation: "raceacar" is not a palindrome.
    
    TC: O(n) | SC: O(1)
    """
    def isPalindrome(self, s):
        # STEP 1: Initialize two pointers at opposite ends
        left = 0
        right = len(s) - 1
        
        # STEP 2: Move pointers toward each other
        while left < right:
            # Skip non-alphanumeric characters from left
            while left < right and not s[left].isalnum():
                left += 1
            
            # Skip non-alphanumeric characters from right
            while left < right and not s[right].isalnum():
                right -= 1
            
            # STEP 3: Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
            
            # Move both pointers inward
            left += 1
            right -= 1
        
        # Successfully compared all characters
        return True

sol = ValidPalindrome()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
print(sol.isPalindrome("race a car"))  # False
print(sol.isPalindrome(" "))  # True
print(sol.isPalindrome("aba"))  # True

# ================================================================
# PATTERN 3: DYNAMIC PROGRAMMING ON STRINGS
# Strategy: Build solution from subproblems:
#   1. Define dp[i][j] as solution for substring relationship
#   2. Initialize base cases (empty strings, single chars)
#   3. Fill table by comparing characters and using previous results
#
# Time: O(n*m) | Space: O(n*m) - can often optimize to O(min(n,m))
# ================================================================

# PROBLEM: LC 1143 - Longest Common Subsequence
# Find length of longest subsequence common to both strings

class LongestCommonSubsequence:
    """
    Find the length of the longest common subsequence of two strings.
    A subsequence doesn't need to be contiguous.
    
    Input: text1 = "abcde", text2 = "ace"
    Output: 3
    Explanation: The longest common subsequence is "ace" with length 3.
    
    Input: text1 = "abc", text2 = "abc"
    Output: 3
    
    TC: O(m*n) | SC: O(m*n)
    """
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        
        # Matrix DP table stores LCS from only the first "i" chars of text1 and first "j" chars of text2
        # dp[i][j] = LCS length for text1[0:i] and text2[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # STEP 2: Base cases already initialized (empty strings = 0)
        
        # STEP 3: Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    # Characters match, add 1 to whatever LCS we had without both these chars
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    # Characters don't match, take best from excluding either char
                    dp[i][j] = max(
                        dp[i-1][j],   # Exclude char from text1
                        dp[i][j-1]    # Exclude char from text2
                    )
        
        return dp[m][n]

sol = LongestCommonSubsequence()
print(sol.longestCommonSubsequence("abcde", "ace"))  # 3
print(sol.longestCommonSubsequence("abc", "abc"))    # 3
print(sol.longestCommonSubsequence("abc", "def"))    # 0

# ================================================================
# PATTERN 4: TRIE (PREFIX TREE) -> a special tree like data structure used to store and search through strings, especially when dealing with prefixes like in autocomplete or spell check

# TRIE VISUAL
    # (root)
    #  ├── c
    #  │    └── a
    #  │         ├── r (end)
    #  │         └── t (end)
    #  └── d
    #       └── o
    #            └── g (end)

#   - Each node represents a character
#   - Children stored in dictionary
#   - Each path from the root to a node represents a prefix
#   - Mark end of words with boolean flag
#
# Time: O(m) for insert/search where m is word length
# Space: O(ALPHABET_SIZE * N * M) for N words of length M
# ================================================================

# PROBLEM: LC 208 - Implement Trie
# Design data structure for efficient prefix operations

class TrieNode:
    """Node in Trie containing children and end-of-word flag"""
    def __init__(self):
        self.children = {}  # dict that stores next letters where the key=char and the value=TrieNode (node that char leads to)
        self.is_end = False # flag tells us whether this node marks the end of a complete word

class Trie:
    """
    Implement the Trie class:
    - Trie() Initializes the trie object.
    - void insert(String word) Inserts the string word into the trie.
    - boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    - boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

    Example 1:
    - Input -> ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    - Output -> [null, null, true, false, true, null, true]

    Explanation
    - Trie trie = new Trie();
    - trie.insert("apple");
    - trie.search("apple");   // return True
    - trie.search("app");     // return False
    - trie.startsWith("app"); // return True
    - trie.insert("app");
    - trie.search("app");     // return True

    TC: O(m) for all operations | SC: O(total characters stored)
    """
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        # STEP 1: Start from root -> TrieNode we made with __init__
        node = self.root
        
        # STEP 2: Create path for each character
        for char in word:
            if char not in node.children: # Check if that letter is in the children
                node.children[char] = TrieNode() # If not, add the letter to the dict
            node = node.children[char] # Move to next node
        
        # STEP 3: Mark end of word
        node.is_end = True
    
    def search(self, word):
        # STEP 1: Traverse to end of word
        node = self.root # Start at root node
        for char in word:
            if char not in node.children: # Check if char is there
                return False
            node = node.children[char] # Move to next node
        
        return node.is_end # Verify it's a complete word (not just prefix)
    
    def startsWith(self, prefix):
        # STEP 1: Traverse the prefix
        node = self.root # Start at root node
        for char in prefix:
            if char not in node.children: # Check if char is there
                return False
            node = node.children[char] # Move to next node
        
        return True # Prefix exists if we successfully traversed

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))    # True
print(trie.search("app"))      # False
print(trie.startsWith("app"))  # True
trie.insert("app")
print(trie.search("app"))      # True

# ================================================================
# PATTERN 5: HASHMAP / CHARACTER FREQUENCY
# Strategy: Use HashMap to track and compare character counts:
#   1. Count character frequencies with Counter or dict
#   2. Use frequency pattern as key for grouping/matching
#   3. Common in anagram, substring, grouping problems
#
# Time: O(n*k) where k is avg string length | Space: O(n*k)
# ================================================================

# PROBLEM: LC 49 - Group Anagrams
# Group strings that are anagrams of each other

from collections import defaultdict

class GroupAnagrams:
    """
    Given an array of strings, group the anagrams together.
    
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    
    Input: strs = [""]
    Output: [[""]]
    
    Input: strs = ["a"]
    Output: [["a"]]
    
    TC: O(n*k) where n is number of strings, k is max string length
    SC: O(n*k)
    """
    def groupAnagrams(self, strs):
        # STEP 1: Create hashmap to group anagrams
        # Key = character frequency pattern, Value = list of strings
        anagram_groups = defaultdict(list)
        
        # STEP 2: Process each string
        for s in strs:
            # STEP 3: Create frequency signature for the string
            # Count each character (a-z) to create unique key
            count = [0] * 26  # 26 lowercase letters
            
            for char in s:
                count[ord(char) - ord('a')] += 1 # Convert letter to ASCII number (0-25)
            
            # STEP 4: Use frequency tuple as dictionary key
            key = tuple(count) # key in dict is a tuple of our freq count (list can't be key in python)
            anagram_groups[key].append(s) # Append the word s to that freq tuple
        
        # STEP 5: Return all grouped anagrams
        return list(anagram_groups.values())

sol = GroupAnagrams()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# [["eat","tea","ate"], ["tan","nat"], ["bat"]]

# ================================================================
# PATTERN 6: BACKTRACKING ON STRINGS
# Strategy: Explore all possibilities through recursive decision tree:
#   1. Make a choice at current position
#   2. Recursively explore remaining choices
#   3. Backtrack (undo choice) and try next option
#
# Common applications: string generation, permutations, combinations, partitioning
# Time: Usually O(b^n) where b is branching factor, n is depth
# Space: O(n) for recursion stack
# ================================================================

# PROBLEM: LC 17 - Letter Combinations of a Phone Number
# Generate all possible letter combinations from phone number digits

class LetterCombinations:
    """
    Given a string containing digits 2-9, return all possible letter 
    combinations that the number could represent (like old phone keypads).
    
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    
    Input: digits = ""
    Output: []
    
    Input: digits = "2"
    Output: ["a","b","c"]
    
    TC: O(4^n) where n is number of digits (worst case: 7,9 have 4 letters)
    SC: O(n) for recursion stack
    """
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        # STEP 1: Define digit-to-letter mapping
        phone_map = {
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
        
        def backtrack(index, current_combo):
            # STEP 2: Base case - reached end of digits
            if index == len(digits):
                result.append(current_combo)
                return
            
            # STEP 3: Get letters for current digit
            current_digit = digits[index]
            letters = phone_map[current_digit]
            
            # STEP 4: Try each letter choice
            for letter in letters:
                # Make choice: add letter to combination
                backtrack(index + 1, current_combo + letter)
                # Backtrack happens automatically (no explicit undo needed here)
        
        # Start backtracking from index 0 with empty combination
        backtrack(0, "")
        return result

sol = LetterCombinations()
print(sol.letterCombinations("23"))
# ["ad","ae","af","bd","be","bf","cd","ce","cf"]

print(sol.letterCombinations(""))    # []
print(sol.letterCombinations("2"))   # ["a","b","c"]
print(sol.letterCombinations("234")) # 27 combinations