# ================================================================
# PATTERN 7: ALL PATHS COLLECTION - BACKTRACKING
# LC 257 - Binary Tree Paths
# PATTERN EXPLANATION:
# This pattern collects all possible paths from root to leaves.
# Key insight: Use path copying for backtracking - each recursive call gets its own path copy.
# When reaching a leaf, add the complete path to results.
# ================================================================

class TreePaths:
    # RECURSIVE SOLUTION
    def binaryTreePaths(self, root):
        """
        Pattern: Path collection with backtracking
        Time: O(n * h), Space: O(n * h)
        
        How it works:
        1. Build path as we traverse down
        2. When we reach a leaf, add complete path to results
        3. Use path copying (path[:]) for backtracking
        4. Each recursive call gets its own path copy
        """
        def dfs(node, path, paths):
            if not node:
                return
            
            path.append(str(node.val))
            
            # Leaf node - add complete path
            if not node.left and not node.right:
                paths.append("->".join(path))
            else:
                # Continue exploring (path[:] creates copy for backtracking)
                dfs(node.left, path[:], paths)
                dfs(node.right, path[:], paths)
        
        paths = []
        dfs(root, [], paths)
        return paths
    
    # ITERATIVE SOLUTION
    def binaryTreePathsIterative(self, root):
        """
        Pattern: Path tracking with stack of (node, path) pairs
        
        How it works:
        1. Stack stores (node, current_path_string) pairs
        2. When reaching a leaf, add path to results
        3. For non-leaf nodes, add children with extended paths
        """
        if not root:
            return []
        
        stack = [(root, str(root.val))]
        paths = []
        
        while stack:
            node, path = stack.pop()
            
            # Leaf node
            if not node.left and not node.right:
                paths.append(path)
            
            # Add children with extended paths
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
        
        return paths

# Test tree paths
paths_root = TreeNode(1)
paths_root.left = TreeNode(2)
paths_root.right = TreeNode(3)
paths_root.left.right = TreeNode(5)

tree_paths = TreePaths()
print("All paths (recursive):", tree_paths.binaryTreePaths(paths_root))
print("All paths (iterative):", tree_paths.binaryTreePathsIterative(paths_root))
