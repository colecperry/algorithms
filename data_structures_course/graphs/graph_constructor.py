# Graphs:
# Have a vertex or verticies (a node or point in the graph)
# Between the verticies are edges (connections)
# Each vertex can have edges with mutiple or other verticies
# You can have weighted edges, bi-directional (no arrows), or directional (one way arrow)

# How to represent a graph:
# Adjacency Matrix - is a 2D matrix with all nodes as rows and columns. For example, if you have a graph with nodes A,B,C,D, and E, you would have rows and columns with A,B,C,D, and E. One column needs to represent the starting node, and the other should represent the node it has an edge with (to account for one directional edges). In each box, if they have an edge connection, store 1, if not, store 0, if they have a weight, store the weight. 

# Adjacency List - It is a dictionary with the starting node as the key and the nodes it has an edge with as the value (single value or list of values for multiple edges). We will use this because from a storage perspective, you don't have to store the 0's, which works better with large data sets.

# Big O
# Matrix space complexity - each verticy has to store every connection it is not connected to O(V)^2
# List space complexity - only stores the verticies that is it connected to O(V+E)

class Graph:
    def __init__(self):
        self.adj_list = {} # Use an empty dict for the adj list
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex]) # Print key (vertex) and value
    
my_graph = Graph()
