# Time complexity - Remove an edge
# Adjacency List: O(N) - We have to find each vertex, iterate through the list to remove the edge
# Adjacency Matrix: O(1) Change the two boxes that share the common edge to 0's 

class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys(): # Check if both v1 and v2 exists as keys
            try:
                self.adj_list[v1].remove(v2) # At key 1, remove vertex 2
                self.adj_list[v2].remove(v1) # At key 2, remove vertex 1
            except ValueError: # For edge case if someone tries to remove an edge that doesn't exist
                pass # Ignore the error and move to the next line of code
            return True # Return true if removed
        return False # Return False if not removed

my_graph = Graph()

my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'A')

my_graph.remove_edge('A', 'B')
my_graph.remove_edge('A', 'D')

my_graph.print_graph()