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

# Global graph reference
graph = []

# knows(i, j) returns True if person i knows person j
def knows(a, b):
    return graph[a][b] == 1

# BRUTE FORCE O(n^2)
def findCelebrityBrute(n):
    """
    # Time Complexity: O(n^2)
    # - The nested loop compares each pair of people once: O(n^2)
    # - Final loop to scan scores is O(n)

    # Space Complexity: O(n)
    # - We use an array of size n to track each person's score
    """
    # Track a "celebrity score" for each person
    # Score increases when someone knows them (+1)
    # Score decreases when they know someone (-1)
    # Celebrity score = (n-1) known by - (0) knows = n-1
    counts = [0] * n
    
    # Check all pairs of people
    for a in range(n):
        for b in range(n):
            if a == b:  # Skip self (person always knows themselves)
                continue
            
            if knows(a, b):
                counts[b] += 1  # b is known by a (good for b)
                counts[a] -= 1  # a knows someone (bad for a)
    
    # Find person with score n-1
    # Celebrity: everyone (n-1 people) knows them = +n-1
    #            they know nobody = 0 decrements
    #            Total score = n-1
    for i in range(len(counts)):
        if counts[i] == n - 1:
            return i
        
    return -1  # No celebrity found


# Optimal O(n)
def findCelebrityOp(n):
    """
    - TC: O(n) -> first loop to find candidate, second to verify, each fn call to knows() is O(1)
    - SC: O(1) -> no extra space
    """
    # Find a candidate: Eliminate anyone who cannot be the celebrity (they know someone)
    candidate = 0 # assume celebrity (candidate) is person 0 to start
    for i in range(1, n): # iterate through the rest of the people
        if knows(candidate, i): # if the candidate knows someone, they cannot be the celebrity
            candidate = i # update the candidate to the next person
    
    # Verify the candidate
    for i in range(n):
        if i != candidate: # don't check against yourself
            res_1 = knows(candidate, i) # check again from the beginning if they know anyone (accounts for people they could still know before they were selected) (False if candidate is celeb)
            res_2 = knows(i, candidate) # check if person i knows the candidate (True if candidate is celebrity)
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
print("Result:", findCelebrityBrute(n))

# Brute force on Example 2
graph = example_2
n = len(graph)
print("Result:", findCelebrityBrute(n))

# Optimal on Example 1
graph = example_1
n = len(graph)
print("Result:", findCelebrityOp(n)) # 1

# Optimal on Example 2
graph = example_2
n = len(graph)
print("Result:", findCelebrityOp(n)) # -1
