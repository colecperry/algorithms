"""
=================================================================
STRING COMPLETE GUIDE
=================================================================

WHAT IS A STRING?
-----------------
A string is an immutable sequence of characters. In Python, strings cannot be modified
in-place — every "modification" creates a new string object. This makes string building
via concatenation in a loop O(n^2); the solution is to collect characters in a list and
join at the end.

Key characteristics:
- Immutable: cannot modify characters in-place (s[0] = 'x' raises TypeError)
- Indexed: O(1) access by position
- Iterable: loop character by character with for char in s
- Slicing: s[i:j] creates a new string in O(k), where k = j - i

Python string essentials:
    s.lower() / s.upper()           # case conversion
    s.isalnum() / s.isalpha()       # character classification
    s.split() / ' '.join(words)     # tokenize / reassemble
    ord('a') = 97, chr(97) = 'a'   # ASCII conversion
    Counter(s)                      # character frequency map
    sorted(s)                       # sort characters (returns list)

When to use String patterns:
- Comparing or grouping words by their character composition (anagram problems)
- Checking string symmetry (palindromes)
- Rearranging words within a sentence (parsing/manipulation)
- Compressing repeated characters (run-length encoding)

Common String problem types:
- Anagram detection and grouping (character frequency)
- Palindrome validation
- Word reversal and sentence manipulation
- String compression and encoding

STRING CORE PATTERNS
=====================
"""

from typing import List
from collections import defaultdict

"""
STRING COMPLEXITY REFERENCE
============================

+---------------------------+------------------+------------------+
| Pattern                   | Time             | Space            |
+---------------------------+------------------+------------------+
| Character Frequency       | O(n * k)         | O(n * k)         |
| Palindrome Check          | O(n)             | O(1)             |
| String Parsing            | O(n)             | O(n)             |
| String Compression        | O(n)             | O(1) extra       |
+---------------------------+------------------+------------------+

For Character Frequency: n = number of strings, k = average string length
For all others: n = single string length

NOTES:
- Character frequency: sort each string O(k log k) or build freq tuple O(k); n strings -> O(n*k)
- Palindrome: two pointers meet in the middle -> single O(n) pass, no extra space
- String parsing: split + reverse + join each O(n); list of words is the only extra space
- Compression: in-place read/write with two pointers -> O(1) extra space
"""

"""
===============
STRING PATTERNS
===============
"""

"""
================================================================
PATTERN 1: CHARACTER FREQUENCY / ANAGRAM GROUPING
PATTERN EXPLANATION: Use character frequency as a signature to identify and group
related strings. Two strings are anagrams if and only if their character frequency
arrays are identical. Build a hashmap keyed by the frequency tuple (a tuple of 26
counts, one per letter a-z); all strings with the same key are anagrams of each other.

Applications: Group anagrams, valid anagram, find all anagrams, ransom note.
================================================================
"""

class CharFrequency:
    """
    Problem: Given an array of strings, group all anagrams together.

    Example:
        strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    Steps:
    1. For each string, compute its frequency signature:
       a. Create a count array of 26 zeros (one slot per letter a-z)
       b. Increment count[ord(char) - ord('a')] for each character
       c. Convert to tuple (tuples are hashable; lists are not)
    2. Group strings by their signature in a defaultdict(list)
    3. Return all groups as a list
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  # LC 49
        """
        TC: O(n * k) where n = number of strings, k = max string length
        SC: O(n * k) - stores all strings grouped in the hashmap
        """
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            groups[tuple(count)].append(s)

        return list(groups.values())

    # Trace: strs = ["eat", "tea", "ate"]
    # "eat": count[e]=1,count[a]=1,count[t]=1 -> tuple(...1..1..1...) -> key K1
    # "tea": same character counts -> key K1
    # "ate": same character counts -> key K1
    # groups = {K1: ["eat","tea","ate"]}
    # Output: [["eat","tea","ate"]] ✓

sol = CharFrequency()
print("Group Anagrams:", sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


"""
================================================================
PATTERN 2: PALINDROME CHECK (TWO POINTERS ON STRING)
PATTERN EXPLANATION: Place one pointer at the start and one at the end. Move both
inward simultaneously, comparing characters at each step. Skip non-alphanumeric
characters before comparing (convert to lowercase for case-insensitive check).
If all compared characters match, the string is a palindrome. O(n) time, O(1) space.

Applications: Valid palindrome, palindrome number, longest palindromic substring.
================================================================
"""

class PalindromeCheck:
    """
    Problem: Given a string s, return True if it is a palindrome after converting to
    lowercase and removing all non-alphanumeric characters.

    Example:
        s = "A man, a plan, a canal: Panama" -> "amanaplanacanalpanama" -> True
        s = "race a car" -> "raceacar" -> False

    Steps:
    1. Initialize left=0, right=len(s)-1
    2. While left < right:
       a. Skip non-alphanumeric from left (left += 1 while not isalnum)
       b. Skip non-alphanumeric from right (right -= 1 while not isalnum)
       c. Compare s[left].lower() vs s[right].lower(); return False if different
       d. Move both pointers inward (left += 1, right -= 1)
    3. Return True (all pairs matched)
    """
    def isPalindrome(self, s: str) -> bool:  # LC 125
        """
        TC: O(n) - each pointer moves at most n/2 times
        SC: O(1) - only two pointer variables
        """
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

    # Trace: s = "A man, a plan, a canal: Panama"
    # Effective chars: "amanaplanacanalpanama"
    # left=0 'A', right=29 'a' -> 'a'=='a' ✓ -> left=1, right=28
    # left=1 ' ' -> skip; right=28 -> 'm'
    # left=2 'm', right=28 'm' -> 'm'=='m' ✓ -> ...
    # All pairs match -> True ✓

sol = PalindromeCheck()
print("Palindrome:", sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
print("Palindrome:", sol.isPalindrome("race a car"))                       # False


"""
================================================================
PATTERN 3: STRING PARSING / WORD MANIPULATION
PATTERN EXPLANATION: Tokenize the string into words with split(), apply transformations
(filter, reverse, reorder), then reassemble with join(). Python's split() with no argument
splits on any whitespace AND automatically strips leading/trailing spaces and collapses
multiple spaces between words. The split/filter/join pipeline is the idiomatic approach
for sentence-level string manipulation.

Applications: Reverse words in a string, reorder sentence, capitalize words.
================================================================
"""

class StringParsing:
    """
    Problem: Given an input string s, reverse the order of words. A word is a sequence
    of non-space characters. The output should have no leading/trailing spaces and
    exactly one space between words.

    Example:
        s = "  the sky is blue  "
        Words: ["the","sky","is","blue"]
        Reversed: ["blue","is","sky","the"]
        Output: "blue is sky the"

    Steps:
    1. s.split() — splits on any whitespace, strips edges, collapses internal spaces
       Result: ["the","sky","is","blue"]
    2. [::-1] — reverse the list of words
    3. ' '.join(...) — reassemble with single spaces
    """
    def reverseWords(self, s: str) -> str:  # LC 151
        """
        TC: O(n) - split O(n) + reverse O(w) + join O(n)
        SC: O(n) - list of words
        """
        return ' '.join(s.split()[::-1])

    # Trace: s = "  the sky is blue  "
    # s.split()  -> ["the", "sky", "is", "blue"]  (strips + splits on whitespace)
    # [::-1]     -> ["blue", "is", "sky", "the"]
    # ' '.join   -> "blue is sky the" ✓

sol = StringParsing()
print("Reverse Words:", sol.reverseWords("  the sky is blue  "))  # "blue is sky the"
print("Reverse Words:", sol.reverseWords("a good   example"))     # "example good a"


"""
================================================================
PATTERN 4: STRING COMPRESSION (IN-PLACE READ/WRITE POINTERS)
PATTERN EXPLANATION: Use two pointers on the same character array: a read pointer i
scans groups of identical characters, and a write pointer tracks where to write the
compressed output. Count consecutive identical characters, write the character and its
count (only if count > 1) to the write position. Since the write pointer never overtakes
the read pointer, this runs in O(1) extra space.

Applications: String compression, run-length encoding, remove duplicates in-place.
================================================================
"""

class StringCompression:
    """
    Problem: Given an array of characters chars, compress it in-place using run-length
    encoding. Groups of consecutive identical characters are replaced by the character
    followed by the group length (omit length if group size is 1). Return new length.

    Example:
        chars = ['a','a','b','b','c','c','c']
        Compressed: ['a','2','b','2','c','3'] -> Output: 6

        chars = ['a']
        Output: 1 (single char, no count appended)

    Steps:
    1. write=0 (write position), i=0 (read position)
    2. While i < len(chars):
       a. Record chars[i] as the current character
       b. Count consecutive occurrences: advance i while chars[i] == current char
       c. Write the character to chars[write], write += 1
       d. If count > 1: write each digit of str(count) to chars[write]
    3. Return write (new length)
    """
    def compress(self, chars: List[str]) -> int:  # LC 443
        """
        TC: O(n) - single pass through chars
        SC: O(1) - only pointer variables (modifies chars in-place)
        """
        write = 0
        i = 0

        while i < len(chars):
            char = chars[i]
            count = 0

            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1

            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write

    # Trace: chars = ['a','a','b','b','c','c','c']
    # i=0: char='a', count=2 (i moves to 2)
    #   write chars[0]='a', write=1; count>1 -> write chars[1]='2', write=2
    # i=2: char='b', count=2 (i moves to 4)
    #   write chars[2]='b', write=3; write chars[3]='2', write=4
    # i=4: char='c', count=3 (i moves to 7)
    #   write chars[4]='c', write=5; write chars[5]='3', write=6
    # return 6 ✓
    # chars = ['a','2','b','2','c','3']

sol = StringCompression()
chars = ['a','a','b','b','c','c','c']
new_len = sol.compress(chars)
print("Compressed length:", new_len, "->", chars[:new_len])  # 6 -> ['a','2','b','2','c','3']
chars2 = ['a']
print("Compressed length:", sol.compress(chars2))  # 1
