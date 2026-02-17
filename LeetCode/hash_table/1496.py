class ComplexKeysPattern:
    """
    Given string of moves (N/S/E/W), check if path crosses itself.
    
    Example:
        Input: path = "NES"
        Output: False
        (0,0) → N → (0,1) → E → (1,1) → S → (1,0)
        
        Input: path = "NESWW"  
        Output: True
        Returns to (0,0)
    
    TC: O(n) where n = len(path)
    SC: O(n) to store visited coordinates
    """
    def isPathCrossing(self, path: str) -> bool:  # LC 1496
        visited = {(0, 0)}  # Start position - tuple key!
        x, y = 0, 0  # Track current position
        
        # Direction mappings
        moves = {
            'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'W': (-1, 0)
        }
        
        for direction in path:
            # Move to new position
            dx, dy = moves[direction]
            x, y = x + dx, y + dy
            
            # Check if we've been here before
            if (x, y) in visited:
                return True
            
            # Mark as visited
            visited.add((x, y))
        
        return False

# Example trace:
# path = "NESWW"
#
# Start: visited = {(0,0)}, pos = (0,0)
#
# 'N': pos = (0,1), visited = {(0,0), (0,1)}
# 'E': pos = (1,1), visited = {(0,0), (0,1), (1,1)}
# 'S': pos = (1,0), visited = {(0,0), (0,1), (1,1), (1,0)}
# 'W': pos = (0,0), (0,0) in visited! → return True ✓

sol = ComplexKeysPattern()
print(sol.isPathCrossing("NES"))    # False
print(sol.isPathCrossing("NESWW"))  # True