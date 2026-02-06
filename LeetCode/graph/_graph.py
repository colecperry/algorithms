"""
=================================================================
GRAPH ALGORITHMS COMPLETE GUIDE
=================================================================

1. Connected Components (DFS/BFS)
2. BFS Shortest Path (Unweighted)
3. Bipartite Check
4. Toplogical Sort
5. Union Find
6. Dijkstra's Algorithm

WHAT ARE GRAPH ALGORITHMS?
--------------------------
Graph algorithms solve problems on data structures consisting of nodes (vertices) and edges (connections). Graphs can represent relationships, networks, dependencies, and many real-world scenarios.

Key graph representations:
- Adjacency List: {node: [neighbors]} - most common, space efficient
- Adjacency Matrix: 2D array where matrix[i][j] = 1 if edge exists
- Edge List: List of [node1, node2] pairs

Common graph types:
- Directed vs Undirected -> one way vs two way connections
- Weighted vs Unweighted -> edges have costs vs no costs
- Cyclic vs Acyclic (DAG) -> has cycles vs no cycles
- Connected vs Disconnected -> every node can reach every other node vs isolated

GRAPH CORE TEMPLATES
====================
"""

from collections import deque, defaultdict
from typing import List
import heapq

# ==========================================
# DFS TEMPLATE (RECURSIVE)
# ==========================================
def dfs_recursive(graph, start):
    """
    TC: O(V + E) - visit each vertex and each edge once
    SC: O(V)
        - Visited set holds all verticies
        - Worst case recursion stack depth O(V) for a linear chain, recursion unwinds once we have no more neighbors to visit/all neighbors have been visited
        - Result list holds V elements
    """
    visited = set()
    result = []
    
    def dfs(node):
        if node in visited: # have we been here?
            return
        
        visited.add(node) # if we haven't ->
        result.append(node)
        
        # Explore all neighbors
        for neighbor in graph[node]:
            dfs(neighbor)
    
    dfs(start)
    return result

# ========================================
# DFS TEMPLATE (ITERATIVE)
# ========================================
def dfs_iterative(graph, start):
    """
    TC: O(V + E) - explore each vertex and edge once
    SC: O(V)
        - Worst case stack holds V verticies to explore (star graph)
        - Visited set holds all verticies
        - Result list holds V elements
    """
    if start not in graph:
        return []
    
    stack = [start] # DFS uses a stack
    visited = set([start])
    result = []
    
    while stack:
        node = stack.pop()  # LIFO - Last In First Out
        result.append(node)
        
        # explore only unvisited neighbors
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
    - TC: O(V + E) - visit each vertex and edge once
    - SC: O(V) 
        - Queue worst case holds V elements (star graph)
        - Visisted set holds V elements
        - Result list holds V elements
    """
    if start not in graph:
        return []
    
    queue = deque([start]) # BFS uses a deque
    visited = set([start])
    result = []
    
    while queue:
        node = queue.popleft()  # FIFO - First In First Out
        result.append(node)
        
        # explore only unvisited neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

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

"""
================================================================
PATTERN 1: CONNECTED COMPONENTS (DFS/BFS)

PATTERN EXPLANATION: Find separate groups of connected nodes. Run DFS/BFS from each unvisited node to mark its entire group. The number of times you start DFS/BFS = the number of groups (components).

TYPICAL STEPS:
1. Initialize visited tracking (set or array)
2. Initialize component count
3. For each unvisited node:
   - Increment component count (found new component)
   - Run DFS/BFS to mark all connected nodes as visited
4. Return component count or component assignments

Applications: Friend circles, network connectivity, island counting, clustering.
================================================================
"""

class ConnectedComponents:
    """
    Problem: There are n cities. Some are connected, some are not. If city a connects to city b, and city b connects to city c, then a indirectly connects to c.
    
    A province is a group of directly or indirectly connected cities. Given an n x n matrix isConnected where isConnected[i][j] = 1 if cities i and j are connected, return the total number of provinces.

    # Example 1
    - Input: isConnected = [
    [1,1,0],
    [1,1,0],
    [0,0,1]
    ]
    - Output: 2
    
    How it works:
    1. Treat each city as a node in the graph
    2. For each unvisited city, start DFS to explore entire province
    3. Mark all reachable cities in same province as visited
    4. Each new starting city represents a new province
    """
    def findCircleNumDFS(self, isConnected: List[List[int]]) -> int: # LC 547
        """
        - TC: O(n²) - iterate n cities * check n neighbors per city = visit all n² cells once
        - SC: O(n) - visited array stores n cities + recursion stack max depth n (worst case: linear chain)
        """
        n = len(isConnected)
        visited = set()
        provinces = 0 # result
        
        def dfs(city):
            """Mark all cities in the same province as visited"""
            visited.add(city) # Mark city as visited
            
            # Check all other cities for direct connections
            for neighbor in range(n):
                # If cities are connected and neighbor not yet visited
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)  # Explore neighbor's connections
        
        # Try starting DFS from each city
        for city in range(n):
            if city not in visited:
                provinces += 1  # Found a new province
                dfs(city)  # Mark all cities in this province
        
        return provinces
    
    def findCircleNumBFS(self, isConnected: List[List[int]]) -> int:
        """
        TC: O(n²) - check all n² matrix cells once
        SC: O(n) - visited set holds n ele's, queue worst case holds n cities at once (all cities connected to one city -> star graph)
        """
        n = len(isConnected)
        visited = set()
        provinces = 0
        
        for city in range(n): # Explore each city (vertex)
            if city not in visited:
                provinces += 1
                
                # BFS to explore all cities in this province
                queue = deque([city])
                visited.add(city)
                
                while queue:
                    curr = queue.popleft() # get current city
                    
                    # keep exploring connected, unvisited cities
                    for neighbor in range(n): 
                        if isConnected[curr][neighbor] == 1 and neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
        
        return provinces

# Example:
# isConnected = [[1,1,0], City 0 connects to city 1, City 0 connected to itself
#                [1,1,0], City 1 connects to city 0, City 1 connected to itself
#                [0,0,1]] City 2 is isolated
#
# Province 1: cities 0 and 1 (connected)
# Province 2: city 2 (isolated)
# Output: 2

sol = ConnectedComponents()
print("Provinces:", sol.findCircleNumDFS([[1,1,0],[1,1,0],[0,0,1]]))  # 2
print("Provinces:", sol.findCircleNumBFS([[1,1,0],[1,1,0],[0,0,1]]))  # 2

"""
================================================================
PATTERN 2: BFS SHORTEST PATH (UNWEIGHTED)

PATTERN EXPLANATION: Find the shortest path (minimum steps/distance) from a source to a target in an unweighted graph. BFS guarantees the shortest path because it explores nodes level by level - the first time we reach the target is always via the shortest route.

TYPICAL STEPS:
1. Initialize queue with (node, distance) starting at 0
2. Mark starting node as visited
3. While queue not empty:
   - Pop current node and distance
   - If reached target, return distance
   - Explore all unvisited neighbors
   - Add neighbors to queue with distance + 1
4. If target never reached, return -1

Applications: Minimum steps/transformations, shortest path in graphs, word ladders, state space search.
================================================================
"""

class BFSShortestPath:
    """
    Problem: A gene string is represented by an 8-character string of 'A', 'C', 'G', 'T'. 
    A mutation is changing one character. Given a start gene, end gene, and a gene bank, 
    find the minimum number of mutations needed to mutate from start to end. 
    Each mutation must result in a gene from the bank. If no mutation sequence exists, return -1.
    
    # Example
    - Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    - Output: 2
    - Explanation: AACCGGTT → AACCGGTA → AAACGGTA
    
    How it works:
    1. Treat each gene as a node in an implicit graph
    2. Two genes are connected if they differ by exactly 1 character
    3. Use BFS to find shortest path (minimum mutations)
    4. Only genes in the bank are valid intermediate steps
    """
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int: # LC 433
        """
        TC: O(N * M * 4) where N = bank size, M = gene length (8)
            - BFS processes up to worst case N genes (visit each gene in the bank before getting to our end gene)
            - For each gene: loop M (len of gene) positions * try 4 characters
        SC: O(N)
            - Queue worst case holds N genes when many bank genes are 1 mutation from current gene (star pattern)
            - Visited set stores up to N genes (only add if it's in the bank)
        """
        # End gene must be in bank to be reachable
        if endGene not in bank:
            return -1
        
        bank_set = set(bank) # set of mutations allowed
        visited = {startGene} # mutations we have visited
        queue = deque([(startGene, 0)])  # BFS queue: (current_gene, # mutations)
        genes = ['A', 'C', 'G', 'T']
        
        while queue:
            current_gene, mutations = queue.popleft()
            
            # Found the target gene
            if current_gene == endGene:
                return mutations
            
            # Try all possible single-character mutations
            for i in range(8):  # Gene has 8 characters
                for gene_char in genes:  # Try each of 4 possible characters
                    # Skip if same character (not a mutation)
                    if gene_char == current_gene[i]:
                        continue
                    
                    # Create mutated gene: replace character at position i
                    mutated_gene = current_gene[:i] + gene_char + current_gene[i+1:]
                    
                    # Check if mutation is valid (in bank) and unvisited
                    if mutated_gene in bank_set and mutated_gene not in visited:
                        visited.add(mutated_gene)
                        queue.append((mutated_gene, mutations + 1)) # num of mutations ++
        
        return -1  # No valid mutation sequence found

# Visual Example:
# start = "AACCGGTT"
# end = "AAACGGTA"
# bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
#
# BFS exploration:
# Level 0: "AACCGGTT" (start)
# Level 1: "AACCGGTA" (1 mutation: T→A at position 7)
# Level 2: "AAACGGTA" (2 mutations: C→A at position 2) - FOUND!
# Output: 2

sol = BFSShortestPath()
print("Min mutations:", sol.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))  # 2

"""
================================================================
PATTERN 3: BIPARTITE CHECK (GRAPH COLORING)
PATTERN EXPLANATION: Dating app analogy - imagine men and women where:
- ✅ Man can match Woman (different groups)
- ❌ Man cannot match Man (same group)
- ❌ Woman cannot match Woman (same group)

A bipartite graph follows the same rule: nodes split into two groups (A and B) where all edges connect different groups, never nodes within the same group.

Solution: Use 2-coloring. Assign nodes to groups as you traverse with BFS/DFS - if a node is Group A, all neighbors must be Group B, and vice versa. If two connected nodes end up in the same group, it's NOT bipartite.

TYPICAL STEPS:
1. Initialize color array (0 = uncolored, 1 = color A, -1 = color B)
2. For each uncolored node (handles disconnected components):
   - Color it with color A
   - BFS/DFS to color all connected nodes
   - Try to color neighbors with opposite color
   - If neighbor already has same color, not bipartite
3. Return true if successfully colored entire graph

Applications: Matching problems, scheduling conflicts, team assignments.
================================================================
"""

class BipartiteCheck:
    """
    Problem: Given an undirected graph, return true if the graph is bipartite.
    A graph is bipartite if nodes can be partitioned into two independent sets A and B such that every edge connects a node in A to a node in B (no edges within a set).
    
    Graph is given as adjacency list where graph[i] is array of nodes adjacent to node i.

    Example 1:
    Input: graph = [[1,3],[0,2],[1,3],[0,2]]
    Output: true
    Explanation: Can partition into sets {0, 2} and {1, 3}

    Example 2:
    Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    Output: false
    Explanation: Cannot partition nodes into two independent sets
    
    How it works:
    1. Use 2-coloring technique: assign each node to group 0 or 1
    2. Start by assigning any unvisited node to group 0
    3. Assign all its neighbors to group 1 (opposite group)
    4. If a neighbor is already in the same group, graph is NOT bipartite
    5. Repeat for all components (graph may be disconnected)
    """
    def isBipartite(self, graph: List[List[int]]) -> bool: # LC 785
        """
        TC: O(V + E) - visit each node once, check each edge once
        SC: O(V) - color array stores n nodes, queue worst case O(V) (star graph)
        """
        n = len(graph)
        color = [-1] * n  # -1 = unassigned, 0 = group A, 1 = group B
        
        # Handle disconnected components: try each node as a starting point - if we have a connected graph, bfs will explore all edges on first loop
        for start in range(n):
            if color[start] != -1:  # Already colored from previous BFS (skip)
                continue
            
            # BFS to assign this component
            queue = deque([start])
            color[start] = 0  # Assign to group 0
            
            while queue:
                node = queue.popleft()
                
                # Check all neighbors of current node
                for neighbor in graph[node]:
                    # Neighbor not yet assigned to a color
                    if color[neighbor] == -1:
                        # Mark as opposite color -> trick toggles b/t 0 & 1
                        color[neighbor] = 1 - color[node] 
                        queue.append(neighbor)
                    # Neighbor can't be same color as current node
                    elif color[neighbor] == color[node]:
                        return False  # Conflict! Connected nodes can't be in same group (color)
        return True

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
# Visual:  0 --- 1      Cannot partition - triangle 0-1-2 requires 3 colors
#          | \ / |
#          |  X  |
#          | / \ |
#          3 --- 2
# Output: False (not bipartite)

sol = BipartiteCheck()
print("Is bipartite:", sol.isBipartite([[1,3],[0,2],[1,3],[0,2]]))  # True
print("Is bipartite:", sol.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))  # False

"""
================================================================
PATTERN 4: TOPOLOGICAL SORT
PATTERN EXPLANATION: Find an order to complete tasks when some tasks depend on others (Task A must finish before Task B can start). 

Real-world example: Course prerequisites
- Take CS101 before CS201
- Take CS201 before CS301
- Valid order: CS101 → CS201 → CS301

Algorithm (Kahn's):
1. Count prerequisites for each task (in-degree) -> number of incoming edges to a node usually with an array, build the graph if needed
2. Start with tasks that have 0 prerequisites and add them to a queue
3. "Complete" those tasks, reduce prerequisite count for dependent tasks
4. If completing that task unlocks any other tasks, add to the queue and repeat until all tasks done
5. If tasks remain but all have prerequisites → circular dependency (impossible)

Applications: Course scheduling, task ordering, build systems, dependency resolution.
================================================================
"""

class TopologicalSort:
    """
    Problem: There are numCourses courses labeled 0 to numCourses-1.
    Given prerequisites where prerequisites[i] = [ai, bi], you must take course bi before ai.
    
    Return true if you can finish all courses (no circular dependencies).

    Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0. So it is possible.

    Example 2:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
    
    How it works:
    1. Build directed graph: prereq -> course
    2. Count in-degree (prerequisites) for each course
    3. Start with courses having no prerequisites (in-degree = 0)
    4. Process courses and reduce in-degree of dependent courses
    5. If all courses processed, no cycle exists (can finish all)
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: # LC 207
        """
        TC: O(V + E)
            - Build graph and in-degree: O(E) - iterate through all prereqs
            - Initialize queue: O(V) - check all courses for in-degree == 0
            - Process queue: O(V) - each course dequeued once
            - Update neighbors: O(E) - each edge traversed once via graph[course]
            - Total: O(E) + O(V) + O(V) + O(E) = O(V + E)

        SC: O(V + E)
            - Graph (adjacency list): O(E) - stores all prerequisite edges
            - In-degree array: O(V) - one entry per course
            - Queue: O(V) worst case - all courses with no prereqs at start
        """
        # Graph tracks nodes and their edges (prereq -> course)
        graph = defaultdict(list)
        # Tracks num of prereq's a course has
        in_degree = [0] * numCourses 
        
        # Step 1: Build graph and in degree array
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Step 2: Initialize queue with courses w/ no prereq's
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
        
        courses_taken = 0  # Total courses we can complete
        
        # Step 3: Process courses in topological order
        while queue:
            course = queue.popleft()
            courses_taken += 1
            
            # Look at what courses we unlock
            for next_course in graph[course]:
                in_degree[next_course] -= 1  # One prerequisite satisfied
                
                # If all prereqs satisfied, take the course
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        # If we took all courses, no cycle exists
        return courses_taken == numCourses

sol = TopologicalSort()
print("Can finish:", sol.canFinish(2, [[1,0]]))  # True
print("Can finish:", sol.canFinish(2, [[1,0],[0,1]]))  # False

"""
================================================================
PATTERN 5: UNION FIND (DISJOINT SET UNION)
PATTERN EXPLANATION: Efficiently manage separate groups and detect when connecting elements would create a cycle.

Think of it like islands and bridges:
- Start: Each person is their own island (separate groups)
- Union: Build a bridge connecting two islands → they become one landmass
- Find: Which landmass does this person belong to?
- Cycle detection: If two people are already on the same landmass,  building another bridge between them creates a redundant loop

Real-world example: Social network connections
┌─────────────────────────────────────────────────────────────┐
│ Initial state: Everyone separate                            │
│   [1]  [2]  [3]  [4]  [5]                                   │
│                                                             │
│ Connect 1-2: Merge into one group                           │
│   [1,2]  [3]  [4]  [5]                                      │
│                                                             │
│ Connect 3-4: Merge into another group                       │
│   [1,2]  [3,4]  [5]                                         │
│                                                             │
│ Connect 2-3: Bridge the two groups                          │
│   [1,2,3,4]  [5]                                            │
│                                                             │
│ Try to connect 1-4: CYCLE! They're already connected        │
│   Path already exists: 1→2→3→4                              │
│   Adding direct 1-4 edge creates redundant connection       │
└─────────────────────────────────────────────────────────────┘


Algorithm:
1. Initialize: each element is its own parent (separate group)
2. Find: follow parent pointers to root (with path compression to flatten)
3. Union: merge two groups by connecting their roots (use rank to keep balanced)
4. For cycle detection: if both nodes have same root, adding edge creates cycle

Key optimizations:
- Path compression: flatten tree during find operations
- Union by rank: attach smaller tree under larger to keep balanced

Applications: Network connectivity, cycle detection, grouping elements, Kruskal's MST.
================================================================
"""

class UnionFindCycle: # LC 684
    """
    In a graph that started as a tree with n nodes, one extra edge was added. Return the edge that can be removed to restore the tree structure. If multiple answers exist, return the last occurring edge.
    
    Example 1:

    1---2
    |  /
    | /
    3

    Input: edges = [[1,2],[1,3],[2,3]]
    Output: [2,3]
    Explanation: Adding [2,3] creates cycle since 1-2-3 already connected
    
    Example 2:

    2 ----- 1 --- 5
    |       |
    |       |
    3 ----- 4

    Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    Output: [1,4]
    Explanation: [1,4] creates cycle in path 1-2-3-4
    
    How it works:
    1. Process edges in order using Union Find
    2. For each edge, check if nodes already in same component (same root)
    3. If same component, adding edge creates cycle → return it
    4. Otherwise, union the two components
    """
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
            
            # Same root → already connected → adding edge creates cycle
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
            
            return True
        
        # Process each edge
        for u, v in edges:
            if not union(u, v):  # If union fails → nodes already connected → cycle!
                return [u, v]    # This is the redundant edge -> only one edge can create the cycle in this problem so return the first one we find
        
        return []  # Shouldn't reach here based on problem constraints

sol = UnionFindCycle()
print("Redundant edge:", sol.findRedundantConnection([[1,2],[1,3],[2,3]]))  # [2,3]
print("Redundant edge:", sol.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))  # [1,4]


"""
================================================================
PATTERN 6: DIJKSTRA'S ALGORITHM (SHORTEST PATH)
PATTERN EXPLANATION: Find shortest path from source to all nodes in weighted graph.

Real-world example: GPS navigation
- Start at your location
- Find shortest time to every destination
- Always explore closest unvisited location first

Algorithm:
1. Initialize all distances to infinity, source to 0
2. Use min-heap to always process closest unprocessed node
3. For each node, explore neighbors and update distances if shorter path found
4. Mark node as processed (never revisit with longer path)
5. Continue until all reachable nodes processed

Key insight: Greedy approach works because we process nodes in distance order. Once we process a node, we've found its shortest path (can't improve it later).

Requirements: Non-negative edge weights only (negative weights break greedy property).

Applications: GPS routing, network packet routing, shortest path in weighted graphs.
================================================================
"""

class DijkstraShortestPath: # LC 743
    """
    You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
    
    We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

           2
         /   \
      1 /     \ 1
       /       \
      1         3
               /
              / 1
             /
            4
    
    Example 1:
    Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
    Output: 2
    Explanation: 
    - Node 2 (source): 0 time
    - Node 1: 1 time (direct from 2)
    - Node 3: 1 time (direct from 2)
    - Node 4: 2 time (2→3→4)
    Max time is 2
    
    Example 2:
    Input: times = [[1,2,1]], n = 2, k = 2
    Output: -1
    Explanation: Node 1 unreachable from node 2
    
    How it works:
    1. Build weighted graph from edge list
    2. Run Dijkstra from source node k
    3. Find maximum distance (last node to receive signal)
    4. If any node unreachable (distance = infinity), return -1
    """

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Find minimum time for signal to reach all nodes using Dijkstra's algorithm.
        
        TC: O((V + E) log V)
            - Build graph: O(E) where E = number of edges
            - Dijkstra's: O((V + E) log V) where V = number of nodes
              - Each node processed once: O(V log V)
              - Each edge relaxed once: O(E log V)
        
        SC: O(V + E)
            - Graph adjacency list: O(E) - stores all edges
            - Distances dict: O(V) - stores distance to each node
            - Min-heap: O(V) - at most all nodes in heap
        """
        # Step 1: Build adjacency list representation of graph
        # graph[node] = [(neighbor, travel_time), ...]
        graph = defaultdict(list)
        for source, target, time in times:
            graph[source].append((target, time))
        
        # Step 2: Initialize distances - all start at infinity except source
        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[k] = 0  # Starting node has distance 0
        
        # Step 3: Min-heap for Dijkstra's - always process closest unvisited node, Format: (distance_from_source, node)
        min_heap = [(0, k)]  # Start at node k with distance 0
        
        # Step 4: Dijkstra's algorithm
        while min_heap:
            current_dist, current_node = heapq.heappop(min_heap)
            
            # Optimization: skip if we already found a shorter path to this node -> multiple nodes can be added to heap w/ diff distances
            if current_dist > distances[current_node]:
                continue
            
            # Explore all neighbors of current node
            for neighbor, travel_time in graph[current_node]:
                # Total distance from source to neighbor = current distance to this node + travel time it's neigbor we're processing
                total_dist_from_source = current_dist + travel_time
                
                # If this path is shorter, update distance and add to heap
                if total_dist_from_source < distances[neighbor]:
                    distances[neighbor] = total_dist_from_source
                    heapq.heappush(min_heap, (total_dist_from_source, neighbor))
        
        # Step 5: Check if all nodes are reachable (must reach all)
        max_distance = max(distances.values())
        
        # If any node still at infinity, it's unreachable
        if max_distance == float('inf'):
            return -1
        
        # Return max distance (time for signal to reach ALL nodes)
        return max_distance

sol = DijkstraShortestPath()
print("Network delay:", sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))  # 2
print("Network delay:", sol.networkDelayTime([[1,2,1]], 2, 1))  # 1
print("Network delay:", sol.networkDelayTime([[1,2,1]], 2, 2))  # -1