from collections import deque
from typing import List

class GraphBFS:
    """
    Problem: A gene string is an 8-character string from 'A', 'C', 'G', 'T'.
    To mutate from startGene to endGene, change one character at a time.
    Each intermediate mutation must be in the bank. Return minimum mutations needed, or -1.

    Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    Output: 2
    
    How it works:
    1. Treat each gene as a node in implicit graph
    2. Generate neighbors by changing one character to A/C/G/T
    3. Only consider neighbors that exist in bank
    4. BFS finds shortest path from start to end gene
    5. Return number of mutations (path length - 1)
    """
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int: # LC 433
        """
        TC: O(N * M * 4) where N = bank size, M = gene length (8)
        For each gene, try 4 possible characters at each position
        SC: O(N) - visited set and queue store genes from bank
        """
        if endGene not in bank:  # Target must be reachable (in bank)
            return -1
        
        bank_set = set(bank)  # Convert to set for O(1) lookup 
        visited = {startGene}  # Track explored genes to avoid cycles
        queue = deque([(startGene, 0)])  # BFS queue: (current_gene, mutation_count)
        genes = ['A', 'C', 'G', 'T']  # Possible characters for gene string
        
        def get_neighbors(gene):
            """
            Generate next states (neighbors) by trying all single-character mutations. This is the "implicit" part - we create edges on-the-fly based on rules.
            """
            neighbors = [] # list of neighbors -> one char different than input
            for i in range(len(gene)):  # Try mutating each position
                for char in genes:  # Try each possible character
                    if char != gene[i]:  # Skip if same char
                        neighbor = gene[:i] + char + gene[i+1:]  # Build new gene string
                        if neighbor in bank_set:  # Only valid if exists in bank
                            neighbors.append(neighbor)
            return neighbors
        
        # Standard BFS loop
        while queue:
            gene, mutations = queue.popleft()
            
            # Early termination: reached target
            if gene == endGene:
                return mutations
            
            # Explore all valid next states (one mutation away)
            for next_gene in get_neighbors(gene):
                if next_gene not in visited:  # Haven't explored this gene yet
                    visited.add(next_gene)  # Mark as explored
                    queue.append((next_gene, mutations + 1))  # Add to queue with incremented count
        
        return -1  # Exhausted all possibilities, no path exists

# Start: "AACCGGTT"
# End:   "AACCGGTA"
# Bank: ["AACCGGTA"]
#
# Mutation: AACCGGTT → AACCGGTA (change one character)
# Mutations needed: 1

sol = GraphBFS()
print(sol.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))  # 1
print(sol.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]))  # 2
print(sol.minMutation("AACCGGTT", "AACCGGTA", []))  # -1
