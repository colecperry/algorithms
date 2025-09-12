from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val # Node value
        self.left = left # Left child
        self.right = right # Right child

def BFS(root):
    current = root # Create a current pointer
    queue = deque() # Create an empty deque as our queue
    results = [] # Create an empty results list
    queue.append(current) # Append the current node to the queue to start
    while len(queue) > 0: # Run a while loop as long as there are items in the queue
        current = queue.popleft() # Pop the first item off the queue and assign to current 
        results.append(current.val) # Append current's value to the results list
        if current.left is not None: # If there is a node to the left of current
            queue.append(current.left) # Append it to the queue
        if current.right is not None: # Repeat for the right node
            queue.append(current.right)
    return results # Return the BFS List of nodes

def BFS_level_based(root):
    current = root # Create a current pointer
    if not current:
        return []
    queue = deque([current]) # Create a deque initialized with the root
    results = [] # Create an empty results list
    while queue: # While there are nodes to process
        level_size = len(queue) # Get the number of nodes at the current level
        level_values = [] # Store the values at this level
        for _ in range(level_size): # Loop through all nodes at the current level
            node = queue.popleft() # Pop the first node
            level_values.append(node.val) # Add its value to level list
            if node.left is not None: # Append left child
                queue.append(node.left)
            if node.right is not None: # Append right child
                queue.append(node.right)
        results.append(level_values) # Add level list to results
    return results # Return list of levels

def BFS_tuple_based(root):
    current = root # Create a current pointer
    if not current:
        return []
    queue = deque([(current, 0)]) # Initialize deque with tuple (node, level)
    results = [] # Create an empty results list
    while queue: # While there are nodes to process
        node, level = queue.popleft() # Pop node and its level
        if len(results) <= level: # If this level hasn't been added yet
            results.append([])
        results[level].append(node.val) # Add node value to the corresponding level
        if node.left is not None: # Append left child with incremented level
            queue.append((node.left, level + 1))
        if node.right is not None: # Append right child with incremented level
            queue.append((node.right, level + 1))
    return results # Return list of levels

# Example tree:
#       47
#      /  \
#    21    76
#   / \    / \
# 18 27  52 82

root = TreeNode(47)
root.left = TreeNode(21, TreeNode(18), TreeNode(27))
root.right = TreeNode(76, TreeNode(52), TreeNode(82))

print("Standard BFS (flat list):", BFS(root))
print("Level-based BFS (list of levels):", BFS_level_based(root))
print("Tuple-based BFS (list of levels):", BFS_tuple_based(root))
