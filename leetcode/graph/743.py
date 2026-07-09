# 743. Network Delay Time

# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
    
# Example 1:
    #        2
    #      /   \
    #   1 /     \ 1
    #    /       \
    #   1         3
    #            /
    #           / 1
    #          /
    #         4

# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2

# Example 2:
# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1

# Example 3:
# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1

from typing import List
from collections import defaultdict
import heapq

class Solution: # LC 743
    """
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

sol = Solution()
print("Network delay:", sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))  # 2
print("Network delay:", sol.networkDelayTime([[1,2,1]], 2, 1))  # 1
print("Network delay:", sol.networkDelayTime([[1,2,1]], 2, 2))  # -1

# ============================================================================
#          EXAMPLE TRACE: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# ============================================================================

"""
Problem: Find minimum time for signal to reach ALL nodes starting from node k=2

Graph visualization:
    2 (start)
   / \
  1   1
 /     \
↓       ↓
1       3
        |
        | 1
        ↓
        4

Edges (directed):
- 2 → 1 (time: 1)
- 2 → 3 (time: 1)
- 3 → 4 (time: 1)


==================== SETUP ====================

graph = {
    2: [(1, 1), (3, 1)],
    3: [(4, 1)],
    1: [],
    4: []
}

distances = {1: inf, 2: inf, 3: inf, 4: inf}
distances[2] = 0  # Starting node has distance 0

distances = {1: inf, 2: 0, 3: inf, 4: inf}

min_heap = [(0, 2)]  # (distance, node) - start at node 2 with distance 0

==================== ITERATION 1 ====================

Pop from heap: (0, 2)
  current_dist = 0
  current_node = 2

Check if stale -> Is the distance I just popped from the heap WORSE than the best distance I've already recorded for this node?
  Is current_dist (0) > distances[2] (0)? NO
  Not stale, continue processing

Current state: At node 2, distance from source = 0

Explore neighbors of node 2:
  
  Neighbor 1:
    travel_time = 1
    new_distance = current_dist + travel_time = 0 + 1 = 1
    Is new_distance (1) < distances[1] (inf)? YES
    Update: distances[1] = 1
    Push to heap: (1, 1)
  
  Neighbor 3:
    travel_time = 1
    new_distance = current_dist + travel_time = 0 + 1 = 1
    Is new_distance (1) < distances[3] (inf)? YES
    Update: distances[3] = 1
    Push to heap: (1, 3)

After iteration 1:
  distances = {1: 1, 2: 0, 3: 1, 4: inf}
  min_heap = [(1, 1), (1, 3)]


==================== ITERATION 2 ====================

Pop from heap: (1, 1)
  current_dist = 1
  current_node = 1

Check if stale:
  Is current_dist (1) > distances[1] (1)? NO
  Not stale, continue processing

Current state: At node 1, distance from source = 1

Explore neighbors of node 1:
  Node 1 has NO outgoing edges (graph[1] = [])
  Nothing to process

After iteration 2:
  distances = {1: 1, 2: 0, 3: 1, 4: inf}
  min_heap = [(1, 3)]


==================== ITERATION 3 ====================

Pop from heap: (1, 3)
  current_dist = 1
  current_node = 3

Check if stale:
  Is current_dist (1) > distances[3] (1)? NO
  Not stale, continue processing

Current state: At node 3, distance from source = 1

Explore neighbors of node 3:
  
  Neighbor 4:
    travel_time = 1
    new_distance = current_dist + travel_time = 1 + 1 = 2
    Is new_distance (2) < distances[4] (inf)? YES
    Update: distances[4] = 2
    Push to heap: (2, 4)

After iteration 3:
  distances = {1: 1, 2: 0, 3: 1, 4: 2}
  min_heap = [(2, 4)]


==================== ITERATION 4 ====================

Pop from heap: (2, 4)
  current_dist = 2
  current_node = 4

Check if stale:
  Is current_dist (2) > distances[4] (2)? NO
  Not stale, continue processing

Current state: At node 4, distance from source = 2

Explore neighbors of node 4:
  Node 4 has NO outgoing edges (graph[4] = [])
  Nothing to process

After iteration 4:
  distances = {1: 1, 2: 0, 3: 1, 4: 2}
  min_heap = []


==================== HEAP EMPTY - ALGORITHM COMPLETE ====================

Final distances from source (node 2):
  Node 1: 1
  Node 2: 0 (starting node)
  Node 3: 1
  Node 4: 2

Check if all nodes reachable:
  max_distance = max(0, 1, 1, 2) = 2
  Is max_distance == inf? NO
  All nodes are reachable!

Return: 2


==================== ANSWER EXPLANATION ====================

The signal starting from node 2 takes:
- 0 time to reach node 2 (starting point)
- 1 time to reach node 1 (direct edge: 2→1)
- 1 time to reach node 3 (direct edge: 2→3)
- 2 time to reach node 4 (path: 2→3→4)

The LAST node to receive the signal is node 4 at time 2.
Therefore, the network delay time is 2.


Signal propagation timeline:
  Time 0: Node 2 has signal
  Time 1: Nodes 1 and 3 receive signal
  Time 2: Node 4 receives signal ← Maximum time

Answer: 2
"""