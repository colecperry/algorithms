from collections import defaultdict

# Graph class to represent a directed graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = defaultdict(list)  # Adjacency list representation of the graph
        self.color = ['white'] * vertices  # Initializing all nodes to 'white' (undiscovered)
        self.predecessor = [None] * vertices  # Predecessor array
        self.discovery_time = [-1] * vertices  # Discovery time of each node
        self.finish_time = [-1] * vertices  # Finish time of each node
        self.time = 0  # Global time counter to assign timestamps

    # Add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Depth-First Search (DFS)
    def dfs(self, v, stack=None):
        self.color[v] = 'gray'  # Mark the node as discovered
        self.discovery_time[v] = self.time
        self.time += 1  # Increment global time
        for neighbor in self.graph[v]:
            if self.color[neighbor] == 'white':  # If the neighbor is undiscovered
                self.predecessor[neighbor] = v  # Mark the predecessor
                self.dfs(neighbor, stack)
        self.color[v] = 'black'  # Mark the node as fully processed
        self.finish_time[v] = self.time
        self.time += 1  # Increment global time
        if stack is not None:
            stack.append(v)  # Add to the finish stack for reverse DFS order

    # Get the transposed graph
    def transpose(self):
        transposed_graph = Graph(self.V)
        for u in self.graph:
            for v in self.graph[u]:
                transposed_graph.add_edge(v, u)
        return transposed_graph

    # Function to find and print all SCCs
    def kosaraju_scc(self):
        stack = []
        # Step 1: Perform DFS on the original graph to fill the stack
        for i in range(self.V):
            if self.color[i] == 'white':
                self.dfs(i, stack)
        
        # Step 2: Get the transposed graph
        transposed_graph = self.transpose()

        # Step 3: Perform DFS on the transposed graph in the order defined by the finish stack
        transposed_graph.color = ['white'] * self.V  # Reset color array for transposed graph
        sccs = []
        
        while stack:
            node = stack.pop()
            if transposed_graph.color[node] == 'white':
                scc = []
                transposed_graph.dfs(node, scc)
                sccs.append(scc)
        
        return sccs

# Example usage:
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(1, 0)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    sccs = g.kosaraju_scc()

    print("Strongly Connected Components are:")
    for scc in sccs:
        print(scc)
    
    # Print discovery and finish times for each node
    print("\nDiscovery Times: ", g.discovery_time)
    print("Finish Times: ", g.finish_time)
    print("Predecessors: ", g.predecessor)