# 997. Find the Town Judge

# Topics: Array, Hash Table, Graph

# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

# Example 1:

# Input: n = 2, trust = [[1,2]]
# Output: 2
# Example 2:

# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:

# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1

# How to Solve (High Level)
    # The goal is to find the one person (if any) who is trusted by everyone else (n - 1 people) and does not trust anyone themselves.

    # We'll use an array (trust_count) to track trust behavior:
    # - If person A trusts person B, decrement A's score (they trust someone)
    # - Increment B's score (they are trusted by someone)

    # After processing the trust list:
    # - The town judge will have a trust score of exactly (n - 1)
    #   (they are trusted by everyone else and trust no one)

    # Edge case:
    # - If n == 1 and trust list is empty, the only person is the judge

    # Time Complexity: O(n + t)
    # - n for looping through people
    # - t for processing the trust list (where t is the number of trust pairs)

    # Space Complexity: O(n)
    # - We use a list of size n+1 to store trust scores (index 0 is unused)

from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: # Edge case for one person -> must be the town judge
            return 1
        trust_count = [0] * (n + 1) # trust arr -> each index stores the ith person and how many people trust them (the person that is trusted n-1 times must be judge)
        for trusting, trusted in trust: # Loop through input array
            trust_count[trusting] -= 1 # Decrement the count for the person trusting another person in the count arr
            trust_count[trusted] += 1 # Increment the person being trusted in the count arr

        for i in range(1, len(trust_count)): # Find the person in the trust count arr
            if trust_count[i] == (n - 1): # that's count is n - 1
                return i # i is the same as the person

        return -1
        
sol = Solution()
print(sol.findJudge(2, [[1,2]]))
print(sol.findJudge(3, [[1,3],[2,3]]))
print(sol.findJudge(3, [[1,3],[2,3],[3,1]]))
