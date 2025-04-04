"""
GRAPH DEPTH-FIRST SEARCH (DFS) - Big Picture, Code Walkthrough, and Complexity

------------------------
🔍 BIG PICTURE SUMMARY:
------------------------
Depth-First Search (DFS) is a graph traversal algorithm that explores as far as possible along each branch before backtracking. It helps uncover the structure of a graph by assigning each node a discovery time (when first visited) and a finish time (when all its descendants are explored).

------------------------
⚙️ HOW THIS CODE WORKS:
------------------------
- Each node has attributes to track its:
    - color (White: unvisited, Gray: visiting, Black: done)
    - discovery and finish timestamps
    - predecessor (who discovered it)
- The `dfs()` method loops over all nodes. If a node is unvisited (`White`), it calls `dfs_visit()`.
- `dfs_visit()`:
    - Marks the node as Gray and records its discovery time.
    - Recursively visits all unvisited neighbors, updating time.
    - After visiting all neighbors, marks the node as Black and records its finish time.
- Timestamps help reconstruct the DFS forest and understand traversal order.

------------------------
⏱ TIME & SPACE COMPLEXITY:
------------------------
Let:
    n = number of nodes (vertices)
    m = number of edges

⏰ TIME COMPLEXITY: O(n + m)
- Each node is visited once → O(n)
- Each edge is explored once (in a directed graph) → O(m)
- Total work = O(n + m)

💾 SPACE COMPLEXITY: O(n + m)
- O(n) for node objects and metadata (color, predecessor, timestamps)
- O(m) for adjacency lists (stored in each node's neighbor list)
- Recursive stack space in worst-case = O(n) (if the graph is a single long chain)

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.color = 'White'  # Node's color: White (unvisited), Gray (visiting), Black (visited)
        self.predecessor = None  # What node led to this one in DFS
        self.discovered = None  # When this node was first visited
        self.finished = None  # When we finished exploring this node
        self.neighbors = []  # List of adjacent (connected) nodes

    def add_neighbor(self, neighbor): # Appends another node obj to this node's adj list
        self.neighbors.append(neighbor)


class Graph:
    def __init__(self):
        self.nodes = {} # Dict: value -> Node object

    def add_node(self, value): # Adds a new node (if not already present) to graph
        if value not in self.nodes:
            self.nodes[value] = Node(value) # Add node obj to dict

    def add_edge(self, from_value, to_value): # Connects a directed edge
        if from_value not in self.nodes:
            self.add_node(from_value) # Add node to nodes dict
        if to_value not in self.nodes:
            self.add_node(to_value) # Add node to nodes dict
        self.nodes[from_value].add_neighbor(self.nodes[to_value]) # Add neighbor to node's list of neighbors

    def dfs(self):
        time = 0 # Tracks when nodes are discovered and finished
        for node in self.nodes.values(): # Starts DFS from all unvisited (white) nodes
            if node.color == 'White':
                time = self.dfs_visit(node, time)

    def dfs_visit(self, node, time):
        node.color = 'Gray' # Mark the node as discovered
        node.discovered = time # Set node's discovery time
        time += 1 # Increments the time for next node discovered
        
        # Explore all the neighbors
        for neighbor in node.neighbors:
            if neighbor.color == 'White': # If neighbor unvisited
                neighbor.predecessor = node # Set neighbor's pred
                time = self.dfs_visit(neighbor, time) # Recursively visit neighbors of current neighbor (pass current time at neighbor and get back updated time after exploring entire subtree)
        
        # After visiting all neighbors, mark the node as fully explored
        node.color = 'Black'
        node.finished = time # Set finish time to time after exploring entire subtree
        time += 1 # Increment time again for next node
        return time # Return starting time of next node


    def print_node_info(self):
        for node in self.nodes.values():
            print(f"Node {node.value}:")
            print(f"  Color: {node.color}")
            print(f"  Predecessor: {node.predecessor.value if node.predecessor else None}")
            print(f"  Discovered: {node.discovered}")
            print(f"  Finished: {node.finished}")
            print("-----")


# Example usage
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)

# Perform DFS traversal
graph.dfs()

# Print node information
graph.print_node_info()