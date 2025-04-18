# Purpose of the Algorithm:
# - To find a Minimum Spanning Tree (MST) — a subset of edges that connects all nodes with the smallest total edge weight, without forming any cycles. It is particularly efficient on sparse graphs.

# Kruskal's Algorithm - High-Level Steps:
# 1. Sort all edges in the graph in non-decreasing order by weight.
# 2. Initialize a Disjoint Set (Union-Find) data structure to track connected components.
# 3. Iterate over each edge (u, v, weight) in sorted order:
#    a. Use 'find' to check if u and v are in different sets (i.e., not already connected).
#    b. If they are in different sets:
#        i. Add the edge to the Minimum Spanning Tree (MST).
#        ii. Union their sets to mark them as connected.
# 4. Repeat until the MST contains (V - 1) edges or all edges have been processed.

# Time Complexity:
# - Sorting edges: O(E log E)
# - Union-Find operations: nearly O(1) each, amortized with path compression and union by rank
# - Total: O(E log E), which dominates the runtime

# Space Complexity:
# - O(V + E) for the disjoint set data structure, storing edges, and MST


class DisjointSet:
    def __init__(self, n):
        # Initially, each node is its own parent (self loop) and rank is 0
        self.parent = list(range(n))
        self.rank = [0] * n

    # Find with path compression
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    # Union by rank
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        # If they are already in the same component, do nothing
        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal(n, edges):
    # Step 1: Sort the edges by weight
    edges.sort(key=lambda edge: edge[2])  # Sort by weight (edge[2] is the weight)
    
    # Initialize the Disjoint Set (Union-Find)
    dsu = DisjointSet(n)
    
    mst = []  # To store the MST
    mst_weight = 0  # To store the total weight of the MST
    
    # Step 2: Process each edge
    for u, v, weight in edges:
        # Check if u and v are in different components
        if dsu.find(u) != dsu.find(v):
            # If they are in different components, add this edge to the MST
            mst.append((u, v, weight))
            mst_weight += weight
            dsu.union(u, v)
    
    return mst, mst_weight


# Example usage:
if __name__ == "__main__":
    # Number of vertices
    n = 4

    # List of edges as (u, v, weight)
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]

    mst, mst_weight = kruskal(n, edges)

    # Output the Minimum Spanning Tree (MST) and its weight
    print("Edges in the MST:")
    for u, v, weight in mst:
        print(f"({u}, {v}) -> {weight}")

    print(f"Total weight of the MST: {mst_weight}")