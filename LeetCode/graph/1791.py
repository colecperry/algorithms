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

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a, b = edges[0] # Destructure first edge
        c, d = edges[1] # Destructure second edge

        # Check if 'a' is in the second edge
        if a == c or a == d:
            return a
        else:
            return b  # Otherwise, 'b' must be the center



sol = Solution()
print(sol.findCenter([[1,2],[2,3],[4,2]]))
print(sol.findCenter([[1,2],[5,1],[1,3],[1,4]]))
