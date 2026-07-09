# 684. Redundant Connection

# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

# Example 1:

# 1---2
# |  /
# | /
# 3

# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# Explanation: Adding [2,3] creates cycle since 1-2-3 already connected

# Example 2:

# 2 ----- 1 --- 5
# |       |
# |       |
# 3 ----- 4

# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
# Explanation: [1,4] creates cycle in path 1-2-3-4

from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        TC: O(n) for practical purposes
            - We process n edges (one pass through the edges array)
            - Each find/union operation is nearly O(1) due to our optimizations
            - Technically O(n * α(n)) where α(n) is inverse Ackermann function
              (grows extremely slowly - effectively constant for any realistic input)
            
            Without optimizations: O(n²) in worst case
            With path compression + union by rank: O(n * α(n)) ≈ O(n)
        
        SC: O(n)
            - Parent array: stores n + 1 elements (one per node, plus index 0)
            - Rank array: stores n + 1 elements (tracks height of each tree)
            - Total: O(n) space
        """
        n = len(edges) # number of edges we have
        parent = list(range(n + 1)) # track parent of each node, initially parent is itself
        rank = [1] * (n + 1) # rank[i] = track tree height of each tree to keep trees balanced
        
        def find(node):
            """
            - Find which group this node belongs to (returns the root/leader).
            - Also flattens the tree: makes this node and all nodes on the path point directly to the root for faster future lookups.
            - Example: If 3→2→1, after find(3), both 3 and 2 point directly to 1
            """
            if parent[node] != node:
                root = find(parent[node])  # Recursively find the root
                parent[node] = root # Update this node to point to root
            return parent[node]
        
        def union(node1, node2):
            """
            - Try to connect two nodes into the same group.
            - Returns:
                False - If already in same group (adding edge would create cycle)
                True  - If successfully connected (merged two separate groups)
            - Uses "union by rank": attaches the shorter tree under the taller tree
            to keep the overall tree balanced and lookups fast.

            """
            root1 = find(node1) # find the root of each node
            root2 = find(node2)
            
            # Same root → already connected → adding edge creates cycle -> Return False
            if root1 == root2:
                return False
            
            # Union by rank: attach smaller tree under larger tree
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:  # Same rank: pick one as root, increment its rank
                parent[root2] = root1
                rank[root1] += 1 # Attaching tree of equal height makes it taller by 1
            
            return True # Return True if we attach
        
        # Process each edge
        for u, v in edges:
            if not union(u, v):  # If union fails → nodes already connected → cycle!
                return [u, v]    # This is the redundant edge -> only one edge can create the cycle in this problem so return the first one we find
        
        return []  # Shouldn't reach here based on problem constraints

sol = Solution()
print("Redundant edge:", sol.findRedundantConnection([[1,2],[1,3],[2,3]]))  # [2,3]
print("Redundant edge:", sol.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))  # [1,4]

# ====================================================================
#            EXAMPLE TRACE: edges = [[1,2],[1,3],[2,3]]
# ====================================================================

"""
Example 1: Find the redundant connection

Visual representation:
    1 -- 2
    |   /
    | /
    3

Input: edges = [[1,2], [1,3], [2,3]]
Output: [2,3]

The tree should look like:
    1 --- 2
    |
    3

But edge [2,3] creates a cycle: 1-2-3-1


==================== SETUP ====================

n = 3 (we have 3 edges, so graph has 3 nodes)
parent = [0, 1, 2, 3]  # Index 0 unused, nodes 1,2,3 point to themselves
rank = [0, 1, 1, 1]    # Index 0 unused, all trees have height 1

==================== EDGE 1: [1, 2] ====================

Processing edge [1, 2]

Step 1: Find roots
  root1 = find(1) → 1 (node 1 points to itself)
  root2 = find(2) → 2 (node 2 points to itself)

Step 2: Check if same component
  Are they in the same component? root1 == root2?
  Is 1 == 2? NO ✗
  
  Different components → Safe to connect, no cycle yet

Step 3: Union them
  rank[1] = 1, rank[2] = 1 (same rank)
  parent[2] = 1  # Make node 1 the root of node 2
  rank[1] = 2    # Increment rank of new root

State after edge [1,2]:
parent = [0, 1, 1, 3]
rank = [0, 2, 1, 1]

Visual:
    1
    |
    2       3
    ↓       ↓
    1       3

Components: {1,2} and {3}


==================== EDGE 2: [1, 3] ====================

Processing edge [1, 3]

Step 1: Find roots
  root1 = find(1) → 1 (node 1 points to itself)
  root2 = find(3) → 3 (node 3 points to itself)

Step 2: Check if same component
  Are they in the same component? root1 == root2?
  Is 1 == 3? NO ✗
  
  Different components → Safe to connect, no cycle yet

Step 3: Union them
  rank[1] = 2, rank[3] = 1 (rank[1] > rank[3])
  parent[3] = 1  # Attach smaller tree (3) under larger tree (1)

State after edge [1,3]:
parent = [0, 1, 1, 1]
rank = [0, 2, 1, 1]

Visual:
    1
   / \
  2   3

Components: {1,2,3} - ALL nodes now connected!

==================== EDGE 3: [2, 3] ====================

Processing edge [2, 3]

Step 1: Find roots
  root1 = find(2):
    parent[2] = 1 (not equal to 2)
    Recursively call find(1)
    parent[1] = 1 (equals 1, found root!)
    Return 1
  → root1 = 1

  root2 = find(3):
    parent[3] = 1 (not equal to 3)
    Recursively call find(1)
    parent[1] = 1 (equals 1, found root!)
    Return 1
  → root2 = 1

Step 2: Check if same component
  Are they in the same component? root1 == root2?
  Is 1 == 1? YES! ✓✓✓
  
  SAME ROOT! Nodes 2 and 3 are ALREADY connected!
  
  If we add edge [2,3], it creates a CYCLE:
    1 --- 2
    |    /
    |   /
    3--/
  
  Path already exists: 2 → 1 → 3
  Adding [2,3] creates cycle: 2 → 1 → 3 → 2

Step 3: Return the redundant edge
  return [2, 3]  ← This is the answer!
"""