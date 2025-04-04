class FordFulkerson:
    def __init__(self, graph, source, sink):
        self.graph = graph  # Graph represented as an adjacency matrix
        self.source = source
        self.sink = sink
        self.n = len(graph)  # Number of nodes
        self.residual_graph = [row[:] for row in graph]  # Create a copy of the original graph for residual capacities
        self.flow = [[0] * self.n for _ in range(self.n)]  # Initialize flow to 0

    # Helper method to perform DFS and find an augmenting path
    def dfs(self, u, visited, parent):
        visited[u] = True
        if u == self.sink:
            return True  # We found an augmenting path
        for v in range(self.n):
            if not visited[v] and self.residual_graph[u][v] > 0:  # There is available capacity
                parent[v] = u  # Track the parent to reconstruct the path
                if self.dfs(v, visited, parent):
                    return True
        return False

    # Ford-Fulkerson method to calculate the maximum flow
    def ford_fulkerson(self):
        max_flow = 0
        parent = [-1] * self.n  # Array to store the path
        while True:
            visited = [False] * self.n
            if not self.dfs(self.source, visited, parent):
                break  # No more augmenting path found, we are done

            # Find the maximum flow through the path found by DFS
            path_flow = float('Inf')
            s = self.sink
            while s != self.source:
                path_flow = min(path_flow, self.residual_graph[parent[s]][s])
                s = parent[s]

            # Update residual graph and reverse flow
            v = self.sink
            while v != self.source:
                u = parent[v]
                self.residual_graph[u][v] -= path_flow
                self.residual_graph[v][u] += path_flow
                v = parent[v]

            max_flow += path_flow

        return max_flow


# Example usage
graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

source = 0
sink = 5
ff = FordFulkerson(graph, source, sink)
max_flow = ff.ford_fulkerson()

print("The maximum flow is:", max_flow)
