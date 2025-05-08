# 243. Shortest Word Distance

# Topics - Array, String

# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.


# Example 1:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
# Output: 3

# Example 2:
# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
# Output: 1

# How to Solve (High Level)
    # 1. Initialize two variables to track the most recent indices of word1 and word2.
    #    - These will help us calculate distances as we iterate through the list.
    # 2. Initialize a variable to store the shortest distance found so far, starting with a large 
    #    number (e.g., float('inf')).
    # 3. Loop through the list of words, one by one:
    #    a. If the current word matches word1, update word1's index.
    #    b. If the current word matches word2, update word2's index.
    #    c. If both indices have been set (i.e., both words have been seen at least once),
    #       calculate the absolute difference between the indices.
    #    d. Update the shortest distance if this difference is smaller -> each time we find either
    #       word, we are comparing it to the most recent position of the other, which guarentees we 
    #       we are looking at the current potential shortest distance between current word and other
    # 4. After processing the list, return the shortest distance found.

    # Time Complexity (TC): O(n)
    # - We loop through the list of words exactly once.
    # - n is the number of words in wordsDict.

    # Space Complexity (SC): O(1)
    # - We use a constant amount of extra space (for indices and the distance variable).
    # - No additional space is needed proportional to input size.


from typing import List

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        shortest_distance = float('inf')  # Initialize shortest distance with a large number
        word_1_idx, word_2_idx = -1, -1   # Track the latest indices of word1 and word2, -1 means not found yet

        # Loop through each word in the list along with its index
        for i, word in enumerate(wordsDict):
            if word == word1:
                word_1_idx = i  # Update word1's latest index
            elif word == word2:
                word_2_idx = i  # Update word2's latest index

            # If both words have been seen at least once
            if word_1_idx != -1 and word_2_idx != -1:
                # Calculate the distance between them and update the minimum if smaller
                distance = abs(word_1_idx - word_2_idx)
                shortest_distance = min(shortest_distance, distance)

        return shortest_distance  # Return the smallest distance found

sol = Solution()
print(sol.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"))
print(sol.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"))
