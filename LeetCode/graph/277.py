# 277. Find the Celebrity

# Topics: Two Pointers, Graph, Interactive

# Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.

# Now you want to find out who the celebrity is or verify that there is not one. You are only allowed to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

# You are given an integer n and a helper function bool knows(a, b) that tells you whether a knows b. Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.

# Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.

# Note that the n x n 2D array graph given as input is not directly available to you, and instead only accessible through the helper function knows. graph[i][j] == 1 represents person i knows person j, wherease graph[i][j] == 0 represents person j does not know person i.

# Example 1:

# Input: graph = [[1,1,0],[0,1,0],[1,1,1]]

#         0
#       ↙ ↑
#     1 ← 2

# Output: 1
# Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

# Example 2:

#       0
#       ↑ ↘
#       1 ← 2


# Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
# Output: -1
# Explanation: There is no celebrity.

# How to Solve (Brute Force):
    # Initialize an array to track a "score" for each person.
    # Each +1 means someone knows them; each -1 means they know someone else.
    # A true celebrity will end up with a score of exactly n - 1.

    # Loop over every pair of people (a, b).
    # If person a knows person b:
    #   - b is more likely to be a celebrity (increment their score)
    #   - a is less likely (decrement their score)

    # After populating scores, scan the array to find a person with score == n - 1.
    # This means they are known by everyone else, and they know no one.
    # Return that person as the celebrity.

    # If no one meets the condition, return -1 (no celebrity exists).

    # Time Complexity: O(n^2)
    # - The nested loop compares each pair of people once: O(n^2)
    # - Final loop to scan scores is O(n)

    # Space Complexity: O(n)
    # - We use an array of size n to track each person’s score

# Global graph reference
graph = []

# knows(i, j) returns True if person i knows person j
def knows(a, b):
    return graph[a][b] == 1

# BRUTE FORCE O(n^2)
def findCelebrityBrute(n):
    counts = [0] * n
    for a in range(n):
        for b in range(n):
            if a == b: # person is always going to know themselves
                continue
            if knows(a, b):
                counts[b] += 1      # increment b (known by someone)
                counts[a] -= 1      # decrement a (knows someone)
    for i in range(len(counts)):
        if counts[i] == n - 1:
            return i
        
    return -1

    # [1, 1, 0],
    # [0, 1, 0],
    # [1, 1, 1]

# How to Solve (Optimal):
    # Step 1: Assume person 0 is the celebrity candidate.
    # Iterate through the rest of the people:
    #   - If the candidate knows person i, then the candidate cannot be a celebrity.
    #     Update the candidate to person i.
    #   - Key Inisight: This loop does not guarentee that the final candidate knows no one because the candidate might still know someone before it was chosen, and we did not go back to check. What we do know is that everyone before candidate was elminiated because they knew someone

    # Step 2: Verify the candidate.
    # For every other person:
    #   - The candidate must not know them.
    #   - They must know the candidate.

    # If either condition fails, return -1 (not a celebrity).
    # If both conditions are true for all others, return the candidate.

    # Time Complexity: O(n)
    # - First loop to find a candidate takes O(n)
    # - Second loop to verify the candidate takes another O(n)

    # Space Complexity: O(1)
    # - No extra space used beyond a few variables

# Optimal O(n)
def findCelebrityOp(n):
    # Find a candidate: Eliminate anyone who cannot be the celebrity (they know someone)
    candidate = 0 # assume celebrity (candidate) is person 0 to start
    for i in range(1, n): # iterate through the rest of the people
        if knows(candidate, i): # if the candidate knows someone, they cannot be the celebrity
            candidate = i # update the candidate to the next person
    
    # Verify the candidate
    for i in range(n):
        if i != candidate: # don't check against yourself
            res_1 = knows(candidate, i) # check again from the beginning if they know anyone (accounts for people they could still know before they were selected)
            res_2 = knows(i, candidate) # check if person i knows the candidate
            if res_1 or not res_2: # Return immediately if the candidate knows anyone or if any person i doesn't know the candidate
                return -1
            
    return candidate

# Sample input graphs
example_1 = [
    [1, 1, 0],
    [0, 1, 0],
    [1, 1, 1]
]

example_2 = [
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1]
]

# Brute force on Example 1
graph = example_1
n = len(graph)
print("--- Brute Force: Example 1 ---")
print("Result:", findCelebrityBrute(n))

# Brute force on Example 2
graph = example_2
n = len(graph)
print("--- Brute Force: Example 2 ---")
print("Result:", findCelebrityBrute(n))

# Optimal on Example 1
graph = example_1
n = len(graph)
print("--- Optimal: Example 1 ---")
print("Result:", findCelebrityOp(n))

# Optimal on Example 2
graph = example_2
n = len(graph)
print("--- Optimal: Example 2 ---")
print("Result:", findCelebrityOp(n))
