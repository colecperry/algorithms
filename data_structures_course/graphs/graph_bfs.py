# Breadth First Search is an algorithm that discovers all verticies at distance k from s before discovering any vertex at k+1
# BFS is a graph traversal algorithm that:
    # - Starts from a source vertex
    # - Visits neighbors layer by layer (closest first, then their neighbors, etc)
    # - Uses a queue to keep track of what to visit next

# Code in detail:
    # Reset graph by setting all verticies to white (undiscovered), dist to "inf", and predecessor to None
    # Prep the source node by getting the node object from the verticies dict and set color to gray (discovered by not explored), dist to 0 (source node's dist is always 0)
    # Create a queue starting with the source node and begin BFS loop
        # Pop the left node off the queue
        # Loop through the popped node's neighbors in the adjacency list
        # If the neighbor is white (unvisited), turn it's color to grey (discovered), set distance to one more than current node, add it's predecessor, and append the node to the queue to be explored
    # Once we finish looping through all the neighbors, turn the current node black (fully explored)

# Time Complexity: O(n + m)
    # - n = number of vertices
    # - m = number of edges
    # - Each vertex is enqueued and dequeued at most once: O(n)
    # - All edges from all adjacency lists are scanned once: O(m)
    # - So total time is linear in the size of the graph: O(n + m)

# Space Complexity: O(n + m)
    # - O(n) space for vertex attributes (color, distance, predecessor)
    # - O(m) space for adjacency list
    # - O(n) space for the queue in the worst case
    # - Overall space is dominated by the graph representation: O(n + m)

from collections import deque

class Vertex:
    def __init__(self, name): # Each node has a:
        self.name = name  # Identifier of each node (ex. "A")
        self.color = "white" # Used to track discovery status -> "white" = unvisited, "gray" = discovered by not fully explored, "black" = fully explored
        self.predecessor = None # Tracks vertex that led to this one
        self.distance = float("inf") # Number of edges from the source

    def __repr__(self):
        return f"Vertex({self.name}, color={self.color}, distance={self.distance}, predecessor={self.predecessor})"

class Graph:
    def __init__(self):
        self.vertices = {} # Stores all node objects (name -> node obj)
        self.adjacency_list = {} # Stores connections between nodes

    def add_vertex(self, name):
        if name not in self.vertices: # Check if vertex exists
            vertex = Vertex(name) # Init vertex (node)
            self.vertices[name] = vertex # add key (name) and value (vertex obj) to verticies dict
            self.adjacency_list[name] = [] # Create empty adjacency list for new vertex

    def add_edge(self, src, dest):
        if src not in self.vertices: # Check if src vertex exists
            self.add_vertex(src) # If not add the vertex
        if dest not in self.vertices: # Check if dest vertex exists
            self.add_vertex(dest) # If not add the vertex
        self.adjacency_list[src].append(self.vertices[dest]) # Append dest node to src node's adj dict
        self.adjacency_list[dest].append(self.vertices[src])  # Undirected graph adj list goes both directions

    def bfs(self, source):
        if source not in self.vertices: # Make sure src exists
            raise ValueError("Source vertex not found in the graph")
        # Loop through values (vertex obj's) in verticies dict
        for vertex in self.vertices.values(): # Reset graph
            vertex.color = "white" # Set all verticies to color = white, distance = inf, pred = None
            vertex.distance = float("inf")
            vertex.predecessor = None
        
        source_vertex = self.vertices[source] # Get source vertex object from verticies dict
        source_vertex.color = "gray" # Prep the src node
        source_vertex.distance = 0 
        source_vertex.predecessor = None
        
        queue = deque([source_vertex]) # Create a deque with the source vertex obj
        
        while queue: # Begin BFS loop
            current_vertex = queue.popleft() # Get next vertex to explore
            for neighbor in self.adjacency_list[current_vertex.name]: # Loop through each neighbor of node
                if neighbor.color == "white": # Process unvisited neighbors
                    neighbor.color = "gray" # Turn to discovered
                    neighbor.distance = current_vertex.distance + 1 # Set distance to 1 more than current vertex
                    neighbor.predecessor = current_vertex.name # Add curr vertex as neighbors predecessor
                    queue.append(neighbor) # Append the neighbor to queue to be explored
            
            current_vertex.color = "black" # Mark as done

    def display_vertices(self):
        for vertex in self.vertices.values():
            print(vertex)

# Example usage
graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "E")
graph.add_edge("D", "E")
graph.add_edge("E", "F")

graph.bfs("A")
graph.display_vertices()