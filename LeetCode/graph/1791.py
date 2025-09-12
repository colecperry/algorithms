# 1791. Find Center of Star Graph

# Topics: Graph

# There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

# Example 1:
#                     4
#                     |
#                     2
#                   /   \
#                  1     3
#
#
# Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2
# Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

# Example 2:
# Input: edges = [[1,2],[5,1],[1,3],[1,4]]
# Output: 1

# How to solve:
    # - In a star graph, all edges connect to one central node.
    # - Therefore, the center node must appear in every edge.
    # - By comparing just the first two edges, we can identify the common node.
    #   That node is guaranteed to be the center.

    # Time Complexity: O(1)
    # - We only look at the first two edges, so the runtime is constant.

    # Space Complexity: O(1)
    # - No extra space is used beyond a few variables.


from typing import List

from collections import Counter

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
    # Compare the nodes in the first two edges
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]: # check if the center is the 1st node in the 1st index (appears twice in first 2 indexes)
            return edges[0][0]
        return edges[0][1] # if not, it must be the second node in the first index

    def findCenter2(self, edges: List[List[int]]) -> int: # Counter solution
            count = Counter()
            
            # Count how many times each node appears
            for a, b in edges:
                count[a] += 1
                count[b] += 1
            
            # The center will appear n - 1 times (in every edge)
            n = len(edges) + 1  # total number of nodes
            for node, freq in count.items():
                if freq == n - 1:
                    return node


sol = Solution()
print(sol.findCenter([[1,2],[2,3],[4,2]]))
print(sol.findCenter([[1,2],[5,1],[1,3],[1,4]]))
