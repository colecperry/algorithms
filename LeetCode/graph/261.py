# 261. Graph Valid Tree

# Topics: DFS, BFS, Graph, Union Find, Cycle Detection

# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false otherwise.

# A valid tree must satisfy two conditions:
# 1. The graph must be fully connected (all nodes are reachable from any node)
# 2. The graph must have no cycles

# Note: A tree with n nodes has exactly n - 1 edges.

# Example 1:
# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true
# Explanation: The graph forms a valid tree structure with no cycles and all nodes connected.

# Example 2:
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: false
# Explanation: The graph contains a cycle (1-2-3-1), so it's not a valid tree.

# Example 3:
# Input: n = 5, edges = [[0,1],[0,2],[0,3]]
# Output: false
# Explanation: Node 4 is not connected to the rest of the graph, so it's not fully connected.

from typing import List

class Solution:
    """
    NOTE: A valid tree must have n - 1 edges, and no cycles
    """
    def validTreeUnion(self, n: int, edges: List[List[int]]) -> bool:
        # Quick check: valid tree has exactly n-1 edges
        if len(edges) != n - 1:
            return False
        
        parent = list(range(n))  # Only need n, not n+1 (nodes are 0 to n-1)
        rank = [1] * n
        
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            
            if root1 == root2:
                return False  # Cycle detected
            
            # Union by rank
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
            
            return True
        
        # Try to union all edges
        for u, v in edges:
            if not union(u, v):
                return False  # Cycle found
        
        return True  # No cycles + n-1 edges = valid tree
    
    def valid_tree(n, edges): # Iterative DFS Solution
        if len(edges) != n - 1:
            return False
        # build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        stack = [(0, -1)]
        while stack:
            node, parent = stack.pop()
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor in visited and neighbor != parent:
                        return False
                if neighbor not in visited:
                    stack.append((neighbor, node))
        return len(visited) == n

sol = Solution()
print(sol.validTreeUnion(5, [[0,1],[0,2],[0,3],[1,4]]))  # True
print(sol.validTreeUnion(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))  # False
print(sol.validTreeUnion(5, [[0,1],[0,2],[0,3]]))  # False