# 133. Clone Graph

# Topics: Hash Table, DFS, BFS, Graph

# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }

# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

# Ex. 1
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

# Ex. 2
# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

# Ex. 3
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.

# -----------------------
# 💡 How to Solve:
# -----------------------

# The goal is to make a deep copy of an undirected graph.
# Each node has a value and a list of neighbors.
# We must create a new graph with the same structure, where:
# - Each original node is cloned once
# - Each neighbor relationship is preserved

# Use DFS or BFS to traverse the graph.
# Keep a dictionary (visited) to map original nodes to their cloned copies.
# As you visit each node:
#   1. Clone it (if not already cloned)
#   2. Recursively or iteratively clone its neighbors
#   3. Append the cloned neighbors to the cloned node’s neighbor list
# Finally, return the cloned copy of the original input node.

# -----------------------
# ⏱️ Time Complexity:
# -----------------------

# O(N + E), where:
# - N is the number of nodes
# - E is the number of edges
# Every node and every edge is visited exactly once.

# -----------------------
# 📦 Space Complexity:
# -----------------------

# O(N), for:
# - The visited dictionary storing N cloned nodes
# - The recursion stack (DFS) or queue (BFS), which may hold up to O(N) nodes


from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: # Edge case if the graph is empty
            return None 
        
        visited = {node : Node(node.val)} # dictionary to keep track of node's we've already cloned (origional node : cloned node), add the first node in
        queue = deque([node]) # Initialize the deque with iterable object (original node)

        while queue: # BFS traversal for exploring the existing graph (existing graph)
            v = queue.popleft() # pop node from existing graph/queue
            for u in v.neighbors: # Iterate through each neighbor of the original node
                if u not in visited: # If not yet visited
                    visited[u] = Node(u.val) # Create a new cloned node and map it to the original node in the visited dictionary
                    queue.append(u) # Add the neighbor (original node) to explore later
                clone_v, clone_u = visited[v], visited[u] # get cloned version of the node objects (curr node and neighbor)
                clone_v.neighbors.append(clone_u) # Add cloned neighbor to cloned node's neighbors list
        return visited[node] # return cloned version of the original input node in visited dict
    
sol = Solution()

# Create all 4 nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Define neighbors (undirected, so both sides connect)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

print(sol.cloneGraph(node1)) # [[2,4],[1,3],[2,4],[1,3]]

node_1 = Node(1)
print(sol.cloneGraph(node_1)) # [[]]

node_2 = None
print(sol.cloneGraph(node_2)) # None