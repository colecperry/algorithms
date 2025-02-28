# 290. Word Pattern

# Topics: Hash Table, String

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.

# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Explanation:
# The bijection can be established as:
# 'a' maps to "dog".
# 'b' maps to "cat".

# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

# How to Solve: (Two dictionary approach):
    # Create two dictionaries, one to map chars to words and one to map words to chars
    # Use split to turn the string into an array of words (default seperator is whitespace)
    # Check for early termination -> If the lengths don't match
    # Iterate through the chars and words
        # Check if we have seen this character before -> if yes, does the character to word mapping equal the current word for this iteration? If no, return False
        # Check if we have seen this word  before -> since we did not enter the first if statement, we know that this is a new char. If we have seen this word before, we know it's already mapped to a another char so we return False
    # Add mappings for both dicts
    # Return True if we get through whole iteration

    # Time Complexity: O(N)
    # - Splitting the string `s` into words: O(N)
    # - Iterating through the pattern and words: O(N)
    # - Dictionary lookups and insertions: O(1) on average, done N times → O(N)
    # - Overall: O(N), where N is the length of the pattern (or number of words in `s`).

    # Space Complexity: O(N)
    # - Storing `char_to_word` dictionary: O(N) (at most N unique characters)
    # - Storing `word_to_char` dictionary: O(N) (at most N unique words)
    # - Storing `words` list from `s.split()`: O(N)
    # - Overall: O(N) additional space.



from collections import defaultdict

def wordPattern(pattern, s):
    char_to_word = {}  # Maps pattern characters to words
    word_to_char = {}  # Maps words to pattern characters

    words = s.split()  # Split sentence into words
    
    if len(words) != len(pattern):  # Early exit if lengths don't match
        return False

    for char, word in zip(pattern, words):  # Iterate through pattern and words together
        # Check if we have seen this char before
        if char in char_to_word:
            if char_to_word[char] != word: # Char -> word mapping != curr word
                return False

        # Check if we have seen this word before
        elif word in word_to_char: # and know it's a new char
            return False  # We know this new word is already mapped to an existing char

        # Establish new mappings
        char_to_word[char] = word
        word_to_char[word] = char
    return True


print(wordPattern("abba", "dog cat cat dog"))
print(wordPattern("abba", "dog cat cat fish"))
print(wordPattern("aaaa", "dog cat cat dog"))

print(wordPattern("abca", "dog cat dog dog"))  # Expected Output: False
