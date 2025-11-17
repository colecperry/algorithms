"""
=================================================================
GRAPH ALGORITHMS COMPLETE GUIDE
=================================================================

WHAT ARE GRAPH ALGORITHMS?
--------------------------
Graph algorithms solve problems on data structures consisting of nodes (vertices) and edges (connections).
Graphs can represent relationships, networks, dependencies, and many real-world scenarios.

Key graph representations:
- Adjacency List: {node: [neighbors]} - most common, space efficient
- Adjacency Matrix: 2D array where matrix[i][j] = 1 if edge exists
- Edge List: List of [node1, node2] pairs

Common graph types:
- Directed vs Undirected
- Weighted vs Unweighted
- Cyclic vs Acyclic (DAG)
- Connected vs Disconnected

GRAPH CORE TEMPLATES
====================
"""

from collections import deque, defaultdict
from typing import List
import heapq

# ================================================================
# DFS TEMPLATE (RECURSIVE)
# ================================================================
def dfs_recursive(graph, start):
    """
    Basic recursive DFS for graph traversal
    TC: O(V + E) - visit each vertex once, explore each edge once
    SC: O(V) - visited set + recursion stack depth
    """
    visited = set()
    result = []
    
    def dfs(node):
        if node in visited:
            return
        
        visited.add(node)
        result.append(node)
        
        # Explore all neighbors
        for neighbor in graph[node]:
            dfs(neighbor)
    
    dfs(start)
    return result

# ================================================================
# DFS TEMPLATE (ITERATIVE)
# ================================================================
def dfs_iterative(graph, start):
    """
    Iterative DFS using explicit stack
    TC: O(V + E)
    SC: O(V) - visited set + stack
    """
    if start not in graph:
        return []
    
    stack = [start]
    visited = set([start])
    result = []
    
    while stack:
        node = stack.pop()  # LIFO - Last In First Out
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    
    return result

# ================================================================
# BFS TEMPLATE
# ================================================================
def bfs_graph(graph, start):
    """
    BFS for shortest path in unweighted graph
    TC: O(V + E)
    SC: O(V) - visited set + queue
    """
    if start not in graph:
        return []
    
    queue = deque([start])
    visited = set([start])
    result = []
    
    while queue:
        node = queue.popleft()  # FIFO - First In First Out
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

# ================================================================
# UNION FIND TEMPLATE
# ================================================================
class UnionFind:
    """
    Union Find (Disjoint Set Union) for dynamic connectivity
    TC: O(α(n)) per operation (practically constant) with path compression + union by rank
    SC: O(n) - parent and rank arrays
    """
    def __init__(self, n):
        self.parent = list(range(n))  # Each node is its own parent initially
        self.rank = [1] * n  # Track tree height for union by rank
    
    def find(self, x):
        """Find root with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Flatten tree
        return self.parent[x]
    
    def union(self, x, y):
        """Union two sets, return True if they were separate"""
        root_x, root_y = self.find(x), self.find(y)
        
        if root_x == root_y:
            return False  # Already connected
        
        # Union by rank: attach smaller tree under larger tree
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True
    
    def connected(self, x, y):
        """Check if two elements are in the same set"""
        return self.find(x) == self.find(y)

# ================================================================
# TOPOLOGICAL SORT TEMPLATE (KAHN'S ALGORITHM)
# ================================================================
def topological_sort(n, edges):
    """
    Kahn's algorithm for topological ordering
    TC: O(V + E)
    SC: O(V + E) - graph and in-degree array
    
    Returns empty list if cycle detected
    """
    # Build graph and calculate in-degrees
    graph = defaultdict(list)
    in_degree = [0] * n
    
    for u, v in edges:  # u -> v means u must come before v
        graph[u].append(v)
        in_degree[v] += 1  # v has one more dependency
    
    # Start with nodes having no incoming edges (no dependencies)
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        # Reduce in-degree for neighbors (remove dependency)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:  # All dependencies satisfied
                queue.append(neighbor)
    
    # If all nodes processed, valid topological order exists
    return result if len(result) == n else []

# ================================================================
# DIJKSTRA'S ALGORITHM TEMPLATE
# ================================================================
def dijkstra(graph, start, n):
    """
    Dijkstra's shortest path for weighted graphs (positive weights only)
    TC: O((V + E) log V) with min-heap
    SC: O(V) - distances array + heap
    
    graph format: {node: [(neighbor, weight), ...]}
    Returns: distances array from start to all nodes
    """
    distances = [float('inf')] * n
    distances[start] = 0
    
    # Min-heap: (distance, node) - always process closest node first
    heap = [(0, start)]
    
    while heap:
        curr_dist, node = heapq.heappop(heap)
        
        # Skip if we've found a better path already
        if curr_dist > distances[node]:
            continue
        
        # Explore neighbors and try to find shorter paths
        for neighbor, weight in graph[node]:
            new_dist = curr_dist + weight
            
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    
    return distances

# Test the templates
test_graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2, 4],
    4: [3]
}

#     0
#    / \
#   1   2
#    \ /
#     3
#     |
#     4

print("DFS (recursive):", dfs_recursive(test_graph, 0))
print("DFS (iterative):", dfs_iterative(test_graph, 0))
print("BFS:", bfs_graph(test_graph, 0))

# Test Union Find
uf = UnionFind(5)
uf.union(0, 1)
uf.union(1, 2)
print("0 and 2 connected?", uf.connected(0, 2))  # True
print("0 and 3 connected?", uf.connected(0, 3))  # False

# Test Topological Sort
edges = [[0, 1], [0, 2], [1, 3], [2, 3]]
print("Topological order:", topological_sort(4, edges))  # [0, 1, 2, 3] or [0, 2, 1, 3]

# Test Dijkstra
weighted_graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
print("Shortest distances from 0:", dijkstra(weighted_graph, 0, 4))  # [0, 3, 1, 4]

"""
TIME & SPACE COMPLEXITY REFERENCE
==================================

GRAPH REPRESENTATION:
--------------------
Adjacency List: {node: [neighbors]}
  - Space: O(V + E) - store each vertex once, each edge once
  - Edge lookup: O(degree of node) - must scan neighbor list
  - Best for: Sparse graphs where E << V² (few edges relative to nodes)
  - Example: Social networks (most people know few others)

Adjacency Matrix: 2D array where matrix[i][j] = 1 if edge exists
  - Space: O(V²) - must store entry for every possible edge
  - Edge lookup: O(1) - direct array access
  - Best for: Dense graphs where E ≈ V² (many edges)
  - Example: Complete graphs, distance matrices

ALGORITHM COMPLEXITY:
--------------------
+----------------------+------------------+------------------+
| Algorithm            | Time Complexity  | Space Complexity |
+----------------------+------------------+------------------+
| DFS (recursive)      | O(V + E)         | O(V)             |
| DFS (iterative)      | O(V + E)         | O(V)             |
| BFS                  | O(V + E)         | O(V)             |
| Union Find           | O(α(n))          | O(n)             |
| Topological Sort     | O(V + E)         | O(V + E)         |
| Dijkstra (min-heap)  | O((V+E) log V)   | O(V)             |
| Bellman-Ford         | O(V * E)         | O(V)             |
| Floyd-Warshall       | O(V³)            | O(V²)            |
+----------------------+------------------+------------------+

WHERE:
- V = number of vertices (nodes)
- E = number of edges
- α(n) = inverse Ackermann function (practically constant, < 5 for any realistic n)

COMPLEXITY NOTES:
----------------
1. DFS/BFS: O(V + E) - Linear time
   - Visit each vertex exactly once: O(V)
   - Explore each edge exactly once: O(E)
   - Combined: O(V + E)
   
   Space considerations:
   - Visited set stores V nodes: O(V)
   - DFS recursion stack depth can reach O(V) in worst case (long chain)
   - BFS queue can hold O(V) nodes worst case (all nodes at same level)

2. Union Find: O(α(n)) per operation - Amortized near-constant time
   - α(n) is inverse Ackermann function - grows incredibly slowly
   - α(10^80) ≈ 4, so effectively constant for all practical purposes
   
   Why it's fast:
   - Path compression: flattens tree during find, making future finds faster
   - Union by rank: keeps trees balanced by attaching smaller to larger
   - Without these optimizations: O(log n) average, O(n) worst case
   
   Best for: Dynamic connectivity where edges added over time

3. Topological Sort: O(V + E) - Only works on DAGs
   - Works only on Directed Acyclic Graphs (no cycles allowed)
   - Process each node once: O(V)
   - Check each edge once: O(E)
   
   Cycle detection:
   - If result.length < n, cycle exists (some nodes never reach in-degree 0)
   - Kahn's algorithm naturally detects cycles
   
   Common use: Task scheduling, build systems, course prerequisites

4. Dijkstra: O((V + E) log V) - Efficient single-source shortest path
   - Requires NON-NEGATIVE edge weights (fails with negative weights)
   - Each node processed once: O(V)
   - Each edge relaxed once: O(E)
   - Each heap operation: O(log V)
   - Combined: O((V + E) log V)
   
   When to use:
   - Finding shortest path from one node to all others
   - Weighted graphs with non-negative weights
   - GPS navigation, network routing
   
   For dense graphs (E ≈ V²): becomes O(V² log V)

5. Graph Space Complexity:
   - Sparse graphs (E ≈ V): O(V + E) ≈ O(V)
     Example: Tree with V nodes has E = V-1 edges
   
   - Dense graphs (E ≈ V²): O(V + E) ≈ O(V²)
     Example: Complete graph with V nodes has E = V(V-1)/2 edges

WHEN TO USE EACH ALGORITHM:
---------------------------
DFS: 
  - Explore all paths, backtracking problems
  - Detect cycles in directed graphs
  - Find connected components
  - Topological sort (DFS-based version)

BFS: 
  - Shortest path in unweighted graphs (guarantees minimum distance)
  - Level-by-level processing
  - Minimum steps/moves problems

Union Find: 
  - Dynamic connectivity (edges added over time)
  - Cycle detection in undirected graphs
  - Grouping elements into sets
  - Kruskal's MST algorithm

Topological Sort: 
  - Order tasks with dependencies
  - Course scheduling (prerequisites)
  - Build systems (compile order)
  - Only works on DAGs (no cycles)

Dijkstra: 
  - Single-source shortest path in weighted graphs
  - NON-NEGATIVE weights only
  - GPS/navigation systems
  - Network routing
"""

"""
GRAPH PATTERNS
==============
"""

from collections import deque, defaultdict
from typing import List
import heapq

# ================================================================
# PATTERN 1: CONNECTED COMPONENTS (DFS/BFS)
# PATTERN EXPLANATION: Find groups of nodes that are connected to each other but isolated
# from other groups. Each component is a maximal set of nodes where every node can reach
# every other node in the same component. Count components or identify which nodes belong
# to the same component by exploring from each unvisited node.
#
# TYPICAL STEPS:
# 1. Initialize visited tracking (set or array)
# 2. Initialize component count
# 3. For each unvisited node:
#    - Increment component count (found new component)
#    - Run DFS/BFS to mark all connected nodes as visited
# 4. Return component count or component assignments
#
# Applications: Friend circles, network connectivity, island counting, clustering.
# ================================================================

class ConnectedComponents:
    """
    Problem: There are n cities. Some are connected, some are not.
    If city a connects to city b, and city b connects to city c, then a indirectly connects to c.
    
    A province is a group of directly or indirectly connected cities.
    Given an n x n matrix isConnected where isConnected[i][j] = 1 if cities i and j are connected,
    return the total number of provinces.
    
    TC: O(n²) - visit each cell in adjacency matrix once
    SC: O(n) - visited array and recursion stack
    
    How it works:
    1. Treat each city as a node in the graph
    2. For each unvisited city, start DFS to explore entire province
    3. Mark all reachable cities in same province as visited
    4. Each new starting city represents a new province
    """
    def findCircleNum(self, isConnected: List[List[int]]) -> int: # LC 547
        n = len(isConnected)
        visited = [False] * n
        provinces = 0
        
        def dfs(city):
            """Mark all cities in the same province as visited"""
            visited[city] = True
            
            # Check all other cities for direct connections
            for neighbor in range(n):
                # If cities are connected and neighbor not yet visited
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)  # Explore neighbor's connections
        
        # Try starting DFS from each city
        for city in range(n):
            if not visited[city]:
                provinces += 1  # Found a new province
                dfs(city)  # Mark all cities in this province
        
        return provinces

# Example:
# isConnected = [[1,1,0],    City 0 connects to city 1
#                [1,1,0],    City 1 connects to city 0
#                [0,0,1]]    City 2 is isolated
#
# Province 1: cities 0 and 1 (connected)
# Province 2: city 2 (isolated)
# Output: 2

sol = ConnectedComponents()
print("Provinces:", sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))  # 2
print("Provinces:", sol.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))  # 3


# ================================================================
# PATTERN 2: TOPOLOGICAL SORT
# PATTERN EXPLANATION: Order nodes in a Directed Acyclic Graph (DAG) such that for every
# directed edge u→v, node u appears before node v in the ordering. This represents a valid
# sequence respecting all dependencies. Uses in-degree counting (Kahn's algorithm) - nodes
# with no dependencies can be processed first, then we "remove" them and update dependencies.
# Can detect cycles: if we can't process all nodes, a cycle exists.
#
# TYPICAL STEPS (Kahn's Algorithm):
# 1. Build graph and calculate in-degree for each node (count incoming edges)
# 2. Add all nodes with in-degree 0 to queue (no dependencies)
# 3. While queue not empty:
#    - Remove node from queue, add to result
#    - For each neighbor, decrement its in-degree (remove dependency)
#    - If neighbor's in-degree becomes 0, add to queue
# 4. If result contains all nodes, valid ordering exists (no cycle)
#
# Applications: Course scheduling, task ordering, build systems, dependency resolution.
# ================================================================

class TopologicalSort:
    """
    Problem: There are numCourses courses labeled 0 to numCourses-1.
    Given prerequisites where prerequisites[i] = [ai, bi], you must take course bi before ai.
    
    Return true if you can finish all courses (no circular dependencies).
    
    TC: O(V + E) - build graph O(E), process each course once O(V), check each prereq once O(E)
    SC: O(V + E) - store graph (adjacency list) and in-degree array
    
    How it works:
    1. Build directed graph: prereq -> course
    2. Count in-degree (prerequisites) for each course
    3. Start with courses having no prerequisites (in-degree = 0)
    4. Process courses and reduce in-degree of dependent courses
    5. If all courses processed, no cycle exists (can finish all)
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: # LC 207
        # Build adjacency list and track in-degrees
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)  # prereq -> course edge
            in_degree[course] += 1  # course has one more prerequisite
        
        # Initialize queue with courses that have no prerequisites
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
        
        courses_taken = 0  # Track how many courses we can complete
        
        # Process courses in topological order
        while queue:
            course = queue.popleft()
            courses_taken += 1
            
            # For each course that depends on current course
            for next_course in graph[course]:
                in_degree[next_course] -= 1  # One prerequisite satisfied
                
                # If all prerequisites now satisfied, can take this course
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        # If we took all courses, no cycle exists
        return courses_taken == numCourses

# Example 1:
# numCourses = 2, prerequisites = [[1,0]]
# Must take course 0 before course 1
# Valid order: 0 → 1
# Output: True
#
# Example 2:
# numCourses = 2, prerequisites = [[1,0],[0,1]]
# Circular dependency: 0 requires 1, 1 requires 0
# No valid order possible
# Output: False

sol = TopologicalSort()
print("Can finish:", sol.canFinish(2, [[1,0]]))  # True
print("Can finish:", sol.canFinish(2, [[1,0],[0,1]]))  # False


# ================================================================
# PATTERN 3: UNION FIND (DISJOINT SET UNION)
# PATTERN EXPLANATION: Efficiently track and merge groups of connected elements. Maintains
# disjoint sets where each set has a representative (root/parent). Two main operations:
# Find (which set does element belong to?) and Union (merge two sets). Uses path compression
# to flatten trees during find, and union by rank to keep trees balanced. Perfect for problems
# where connectivity changes over time or we need to detect cycles.
#
# TYPICAL STEPS:
# 1. Initialize: each element is its own parent (separate set)
# 2. Find operation: follow parent pointers to root, compress path along the way
# 3. Union operation: connect roots of two sets, attach smaller tree to larger
# 4. For cycle detection: if union returns False, adding edge would create cycle
#
# Applications: Network connectivity, cycle detection, Kruskal's MST, grouping elements.
# ================================================================

class UnionFindCycle:
    """
    Problem: In an undirected graph that started as a tree with n nodes, one extra edge was added.
    A tree is a connected acyclic graph with n nodes and n-1 edges.
    
    Return an edge that can be removed to restore the tree structure.
    If multiple answers exist, return the last occurring edge.
    
    TC: O(n * α(n)) where α is inverse Ackermann (practically constant)
    SC: O(n) - parent and rank arrays
    
    How it works:
    1. Use Union Find to track connected components dynamically
    2. For each edge, check if both nodes already in same component
    3. If already connected, adding this edge creates a cycle
    4. Return the first edge that would create a cycle
    """
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]: # LC 684
        n = len(edges)
        parent = list(range(n + 1))  # Each node is its own parent initially
        rank = [1] * (n + 1)  # Track tree height for union by rank
        
        def find(node):
            """Find root with path compression"""
            if parent[node] != node:
                parent[node] = find(parent[node])  # Flatten tree on the way up
            return parent[node]
        
        def union(node1, node2):
            """Union two sets, return False if already in same set"""
            root1, root2 = find(node1), find(node2)
            
            if root1 == root2:
                return False  # Already in same set (adding edge creates cycle)
            
            # Union by rank: attach smaller tree under larger tree
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
            
            return True
        
        # Process edges in order until we find the redundant one
        for u, v in edges:
            if not union(u, v):  # If union fails, these nodes already connected
                return [u, v]  # This edge creates a cycle
        
        return []  # Should never reach here given problem constraints

# Example:
# edges = [[1,2], [1,3], [2,3]]
#
# Step 1: Add [1,2] - creates component {1,2}
# Step 2: Add [1,3] - creates component {1,2,3}
# Step 3: Add [2,3] - both already in same component, creates cycle!
# Output: [2,3]

sol = UnionFindCycle()
print("Redundant edge:", sol.findRedundantConnection([[1,2],[1,3],[2,3]]))  # [2,3]
print("Redundant edge:", sol.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))  # [1,4]


# ================================================================
# PATTERN 4: DIJKSTRA'S ALGORITHM (SHORTEST PATH)
# PATTERN EXPLANATION: Find shortest path from a source node to all other nodes in a weighted
# graph with non-negative edge weights. Greedily selects the closest unvisited node and explores
# its neighbors, updating distances if a shorter path is found. Uses a min-heap to efficiently
# get the closest node. Guarantees optimal solution because we always process nodes in order of
# their distance from source.
#
# TYPICAL STEPS:
# 1. Initialize all distances to infinity, source to 0
# 2. Add source to min-heap with distance 0
# 3. While heap not empty:
#    - Extract node with minimum distance
#    - For each neighbor, calculate new distance through current node
#    - If new distance is shorter, update and add to heap
# 4. Return distances array or specific target distance
#
# Applications: GPS navigation, network routing, shortest path in weighted graphs.
# ================================================================

class DijkstraShortestPath:
    """
    Problem: You are given a network of n nodes labeled 1 to n. Also given times, a list of
    travel times as directed edges times[i] = (ui, vi, wi) where ui is source, vi is target,
    and wi is the time for a signal to travel from source to target.
    
    Send a signal from node k. Return the minimum time for all nodes to receive the signal.
    If impossible, return -1.
    
    TC: O((V + E) log V) - each node processed once (V), each edge relaxed once (E), heap operations (log V)
    SC: O(V + E) - graph storage O(V+E), distances array O(V), heap O(V)
    
    How it works:
    1. Build weighted graph from edge list
    2. Use Dijkstra to find shortest path from source to all nodes
    3. Return maximum distance (time for last node to receive signal)
    """
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int: # LC 743
        # Build adjacency list: node -> [(neighbor, weight), ...]
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Initialize distances to all nodes as infinity
        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[k] = 0  # Distance to source is 0
        
        # Min-heap: (distance, node) - always process closest node first
        heap = [(0, k)]
        
        while heap:
            curr_dist, node = heapq.heappop(heap)
            
            # Skip if we've already found a shorter path to this node
            if curr_dist > distances[node]:
                continue
            
            # Explore all neighbors and try to find shorter paths
            for neighbor, weight in graph[node]:
                new_dist = curr_dist + weight
                
                # If found shorter path, update distance and add to heap
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))
        
        # Find maximum distance (time for last node to receive signal)
        max_dist = max(distances.values())
        
        # If any node unreachable, return -1
        return max_dist if max_dist != float('inf') else -1

# Example:
# times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
#
# Graph: 2 → 1 (weight 1)
#        2 → 3 (weight 1)
#        3 → 4 (weight 1)
#
# Distances from node 2:
# - Node 2: 0 (source)
# - Node 1: 1 (direct)
# - Node 3: 1 (direct)
# - Node 4: 2 (through node 3)
# Output: 2 (max distance)

sol = DijkstraShortestPath()
print("Network delay:", sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))  # 2
print("Network delay:", sol.networkDelayTime([[1,2,1]], 2, 1))  # 1
print("Network delay:", sol.networkDelayTime([[1,2,1]], 2, 2))  # -1


# ================================================================
# PATTERN 5: BACKTRACKING (ALL PATHS)
# PATTERN EXPLANATION: Find ALL possible paths or solutions, not just one optimal path.
# Systematically explores all possibilities by making choices, recursing to explore that
# choice, then undoing the choice (backtracking) to try other options. Different from
# standard DFS which stops after finding one solution - backtracking exhaustively searches
# the entire solution space.
#
# TYPICAL STEPS:
# 1. Start with empty path from source
# 2. Add current node to path
# 3. If reached target, save path to results
# 4. Otherwise, recursively try all neighbors
# 5. Remove current node from path (backtrack)
# 6. Return all collected paths
#
# Applications: All paths between nodes, combinations, permutations, puzzle solving.
# ================================================================

class AllPaths:
    """
    Problem: Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n-1,
    find all possible paths from node 0 to node n-1 and return them in any order.
    
    The graph is given as graph[i] is a list of all nodes you can visit from node i.
    
    TC: O(2^V * V) - in worst case (complete graph), exponential paths, each path length V
    SC: O(V) - recursion depth and current path storage
    
    How it works:
    1. Use backtracking to explore all possible paths
    2. Add current node to path and check if reached target
    3. Recursively explore all neighbors
    4. Backtrack by removing current node to try other paths
    """
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]: # LC 797
        n = len(graph)
        target = n - 1
        result = []
        
        def backtrack(node, path):
            """Explore all paths starting from current node"""
            # Add current node to path
            path.append(node)
            
            # Base case: reached target, save this path
            if node == target:
                result.append(path[:])  # Make a copy of current path
            else:
                # Explore all neighbors
                for neighbor in graph[node]:
                    backtrack(neighbor, path)
            
            # Backtrack: remove current node to try other paths
            path.pop()
        
        backtrack(0, [])  # Start from node 0 with empty path
        return result

# Example:
# graph = [[1,2],[3],[3],[]]
#
# Visual:  0 → 1 → 3
#          ↓       ↑
#          2 ------┘
#
# All paths from 0 to 3:
# - [0, 1, 3]
# - [0, 2, 3]
# Output: [[0,1,3],[0,2,3]]

sol = AllPaths()
print("All paths:", sol.allPathsSourceTarget([[1,2],[3],[3],[]]))  # [[0,1,3],[0,2,3]]
print("All paths:", sol.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))  # [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]


# ================================================================
# PATTERN 6: BIPARTITE CHECK (GRAPH COLORING)
# PATTERN EXPLANATION: Determine if a graph can be colored with 2 colors such that no two
# adjacent nodes have the same color. Equivalent to checking if graph can be split into two
# independent sets. Uses BFS/DFS to assign colors: start with one color, alternate colors
# as you traverse. If you ever try to color a node that's already colored with the wrong
# color, the graph is not bipartite.
#
# TYPICAL STEPS:
# 1. Initialize color array (0 = uncolored, 1 = color A, -1 = color B)
# 2. For each uncolored node (handles disconnected components):
#    - Color it with color A
#    - BFS/DFS to color all connected nodes
#    - Try to color neighbors with opposite color
#    - If neighbor already has same color, not bipartite
# 3. Return true if successfully colored entire graph
#
# Applications: Matching problems, scheduling conflicts, team assignments.
# ================================================================

class BipartiteCheck:
    """
    Problem: Given an undirected graph, return true if the graph is bipartite.
    A graph is bipartite if nodes can be partitioned into two independent sets A and B
    such that every edge connects a node in A to a node in B.
    
    Graph is given as adjacency list where graph[i] is array of nodes adjacent to node i.
    
    TC: O(V + E) - visit each node once, check each edge once
    SC: O(V) - color array and queue
    
    How it works:
    1. Try to color graph with 2 colors using BFS
    2. Start by coloring a node with color 1
    3. Color all its neighbors with opposite color (-1)
    4. If we try to color a node that's already colored differently, not bipartite
    5. Handle disconnected components by trying to color all uncolored nodes
    """
    def isBipartite(self, graph: List[List[int]]) -> bool: # LC 785
        n = len(graph)
        color = [0] * n  # 0 = uncolored, 1 = color A, -1 = color B
        
        # Try to color each component (graph might be disconnected)
        for start in range(n):
            if color[start] != 0:  # Already colored from another component
                continue
            
            # BFS to color this component
            queue = deque([start])
            color[start] = 1  # Start with color A
            
            while queue:
                node = queue.popleft()
                
                # Try to color all neighbors with opposite color
                for neighbor in graph[node]:
                    if color[neighbor] == 0:  # Neighbor not colored yet
                        color[neighbor] = -color[node]  # Opposite color
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:  # Same color as current
                        return False  # Not bipartite - adjacent nodes same color
        
        return True  # Successfully colored entire graph

# Example 1:
# graph = [[1,3],[0,2],[1,3],[0,2]]
#
# Visual:  0 -- 1      Can partition into {0,2} and {1,3}
#          |    |      All edges go between the two sets
#          3 -- 2
# Output: True (bipartite)
#
# Example 2:
# graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
#
# Visual:  0 -- 1      Cannot partition - triangle 0-1-2 requires 3 colors
#          |\ / |
#          | X  |
#          |/ \ |
#          3 -- 2
# Output: False (not bipartite)

sol = BipartiteCheck()
print("Is bipartite:", sol.isBipartite([[1,3],[0,2],[1,3],[0,2]]))  # True
print("Is bipartite:", sol.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))  # False


