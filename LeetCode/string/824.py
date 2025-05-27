# 824. Goat Latin

# Topics: String

# You are given a string sentence that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

# We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:

# If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
# For example, the word "apple" becomes "applema".

# If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
# For example, the word "goat" becomes "oatgma".

# Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
# For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.
# Return the final sentence representing the conversion from sentence to Goat Latin.

# Example 1:
# Input: sentence = "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

# Example 2:
# Input: sentence = "The quick brown fox jumped over the lazy dog"
# Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

# How to Solve: 
    # Split the sentence into a list of words using spaces as separators
    # Initialize an empty list to store the transformed Goat Latin words
    # Loop through each word along with its index in the list
    #   - If the word starts with a vowel (case-insensitive), append "ma" to the word
    #   - If it starts with a consonant, move the first letter to the end and then append "ma" by creating a new word with string slicing
    #   - Then append a number of "a" characters equal to the word's position (starting from 1)
    #   - Add the resulting word to the result list
    # Join all transformed words back into a single string with spaces between them

    # Time Complexity: O(n), where n is the total number of characters in the sentence
    # - Each word is processed once and transformed in linear time relative to its length

    # Space Complexity: O(n)
    # - A new list of transformed words is created, plus additional space for string concatenations



class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'} 
        words = sentence.split() # Creates an array of words
        result = []

        for i, word in enumerate(words):
            if word[0].lower() in vowels: # If first char is a vowel
                goat_word = word + "ma" # add "ma"
            else: # If not a vowel
                goat_word = word[1:] + word[0] + "ma" # Start at second letter, add first char to end of word plus "ma"
            goat_word += "a" * (i + 1) # Add incrementing "a" to end 
            result.append(goat_word)

        return ' '.join(result) # Return as string joined by spaces


sol = Solution()
print(sol.toGoatLatin("I speak Goat Latin"))
print(sol.toGoatLatin("The quick brown fox jumped over the lazy dog"))

