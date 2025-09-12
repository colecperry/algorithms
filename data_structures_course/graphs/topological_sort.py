# Topological Sort: a linear ordering of a directed acylclic graph such that, if graph G contains an edge (u,v), then vertex u appears before v in ordering
    # - Use DFS to explore the graph
    # - When a node is fully finished (Black - all it's children have been explored), we add it to the stack
    # - At the end, we reverse the stack to get the topological order

# Code:
# - Each node is a `Node` object with metadata: color, discovery/finish time, predecessor, and neighbors.
# - `add_edge()` builds a directed graph by connecting nodes.
# - `topological_sort()` performs DFS from all unvisited (White) nodes:
    # - Marks nodes as Gray when discovered and Black when fully explored.
    # - Records discovery and finish times for learning/debugging purposes.
    # - Once a node and its entire subtree are explored, its value is added to a stack.
# - The stack is reversed at the end to get the correct topological order.

# -----------------------------
# ⏱ TIME & SPACE COMPLEXITY
# -----------------------------
# Let:
#   - n = number of nodes (vertices)
#   - m = number of edges

# ⏰ TIME COMPLEXITY: O(n + m)
# - Each node is visited once → O(n)
# - Each edge is explored once → O(m)
# - Total work is proportional to size of input graph → O(n + m)

# 💾 SPACE COMPLEXITY: O(n + m)
# - O(n) for node metadata (color, timestamps, predecessors)
# - O(m) for adjacency lists stored in each node
# - O(n) for the result stack
# - Recursive call stack in worst-case = O(n)

class Node:
    def __init__(self, value):
        self.value = value
        self.color = 'White'  # Node's color: White (unvisited), Gray (visiting), Black (visited)
        self.predecessor = None  # Prev node in DFS path
        self.discovered = None  # Timestamp when node is discovered
        self.finished = None  # Timestamp when node's exploration is finished
        self.neighbors = []  # List of adjacent nodes

    def add_neighbor(self, neighbor): # Adds a directed edge from this node to a neighbor
        self.neighbors.append(neighbor)


class Graph:
    def __init__(self):
        self.nodes = {} # value -> Node object

    def add_node(self, value): # Adds a new vertex or node to the graph
        if value not in self.nodes:
            self.nodes[value] = Node(value)

    def add_edge(self, from_value, to_value): # Adds a directed edge from "from_value" to "to_value"
        if from_value not in self.nodes:
            self.add_node(from_value) # Add a new node to the graph
        if to_value not in self.nodes:
            self.add_node(to_value) # Add a new node to the graph
        self.nodes[from_value].add_neighbor(self.nodes[to_value]) # Add directed edge to node's neighbors list

    def dfs_visit(self, node, time, result_stack):
        # Discover the node
        node.color = 'Gray' # Mark the node as discovered
        node.discovered = time # Set node's discovery time
        time += 1 # Increment the time for the next node discovered
        
        # Explore all the neighbors
        for neighbor in node.neighbors:
            if neighbor.color == 'White': # If the neighbor is unvisited
                neighbor.predecessor = node # Set the neighbor's predecessor
                time = self.dfs_visit(neighbor, time, result_stack) # Recursively visit neighbors of current neighbor (pass current time at neighbor and get back updated time after exploring entire subtree)
        
        node.color = 'Black' # Mark node as fully explored
        node.finished = time # Set finish time to time after exploring entire subtree
        time += 1 # Increment time for next node
        
        # Push node to result stack as it's completely explored
        result_stack.append(node.value)
        return time

    def topological_sort(self):
        time = 0 # Initialize time and result stack
        result_stack = []
        
        # Perform DFS on all unvisited nodes
        for node in self.nodes.values():
            if node.color == 'White':
                time = self.dfs_visit(node, time, result_stack)
        
        # Reverse the result stack to get the topological order
        result_stack.reverse()
        return result_stack

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
graph.add_edge(3, 4)


# Perform topological sorting
topological_order = graph.topological_sort()

# Print topological sort result
print("Topological Sort Order:", topological_order)

# Optionally, print node information for debugging
graph.print_node_info()