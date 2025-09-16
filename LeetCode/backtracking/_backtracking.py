"""
=================================================================
BACKTRACKING COMPLETE GUIDE
=================================================================

WHAT IS BACKTRACKING?
--------------------
Backtracking is an algorithmic approach for solving problems by exploring all possible 
solutions and abandoning ("backtracking" from) paths that cannot lead to valid solutions.

Key characteristics:
- Builds solutions incrementally by making choices
- Abandons partial solutions as soon as they're determined invalid
- Systematically explores all possibilities through DFS
- Uses recursion with state management (build up, then tear down)
- Time complexity: Often exponential O(b^d) where b=branching factor, d=depth

CORE BACKTRACKING TEMPLATE
==========================
"""

def backtrack_template(nums):
    """
    Core backtracking template - generates all permutations
    Better demonstrates the make choice → recurse → undo choice pattern
    """
    def backtrack(current_permutation, used, all_solutions):
        # Base case - found complete solution
        if len(current_permutation) == len(nums):
            all_solutions.append(current_permutation[:])  # Add copy of solution
            return
        
        # Try all possible choices at current step
        for i in range(len(nums)):
            if i not in used:  # Check if choice is valid
                # Make choice (modify state)
                current_permutation.append(nums[i])
                used.add(i)
                
                # Recurse with new state
                backtrack(current_permutation, used, all_solutions)
                
                # Backtrack (undo choice)
                current_permutation.pop()
                used.remove(i)  # Explicit state restoration
    
    all_solutions = []
    backtrack([], set(), all_solutions)
    return all_solutions

# Test the backtracking template
print("Backtracking Template - Permutations of [1,2,3]:", backtrack_template([1, 2, 3]))
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

"""
WHEN TO USE BACKTRACKING
========================

Use backtracking when:
- Need to find ALL possible solutions (not just one)
- Need to explore a decision tree exhaustively
- Have constraints that can eliminate branches early
- Problem involves permutations, combinations, or arrangements
- Can build solutions incrementally

Common problem types:
- Generate all permutations/combinations
- Solve puzzles (N-Queens, Sudoku)
- Find all paths in trees/graphs
- Subset/partition problems
- String/pattern generation

ESSENTIAL BACKTRACKING PATTERNS
===============================
"""

# ================================================================
# PATTERN 1: TREE PATH COLLECTION
# LC 257 - Binary Tree Paths
# PATTERN EXPLANATION:
# Collect all possible paths by building path incrementally during traversal.
# Key insight: Build path going down, copy when complete, backtrack going up.
# Applications: All root-to-leaf paths, path sum variations, tree serialization.
# ================================================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root):
    """
    Find all root-to-leaf paths in binary tree
    Time: O(N * H) where N=nodes, H=height
    Space: O(H) for recursion + O(N * H) for storing paths
    
    How it works:
    1. Add current node to path as we traverse down
    2. When we reach leaf, save complete path to results
    3. Backtrack by removing current node when returning up
    4. This ensures path is built/torn down correctly for each branch
    """
    def backtrack(node, current_path, all_paths):
        if not node:
            return
        
        # Make choice - add current node to path
        current_path.append(str(node.val))
        
        # Base case - reached leaf node
        if not node.left and not node.right:
            all_paths.append("->".join(current_path))  # Save complete path
        else:
            # Recurse on children
            backtrack(node.left, current_path, all_paths)
            backtrack(node.right, current_path, all_paths)
        
        # Backtrack - remove current node from path
        current_path.pop()  # Critical: undo the choice made above
    
    all_paths = []
    backtrack(root, [], all_paths)
    return all_paths

# Test tree paths
#       1
#      / \
#     2   3
#      \
#       5
paths_root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
print("All root-to-leaf paths:", binaryTreePaths(paths_root))
# Output: ['1->2->5', '1->3']

# ================================================================
# PATTERN 2: PERMUTATION GENERATION  
# LC 46 - Permutations
# PATTERN EXPLANATION:
# Generate all possible arrangements by choosing unused elements at each step.
# Key insight: Track used elements, explore all remaining choices recursively.
# Applications: All arrangements, scheduling problems, ordering sequences.
# ================================================================

def permute(nums):
    """
    Generate all permutations of given numbers
    Time: O(N! * N), Space: O(N) for recursion
    
    How it works:
    1. At each step, choose from remaining unused numbers
    2. Mark choice as used and recurse with remaining numbers
    3. Backtrack by unmarking the choice
    4. This generates all possible orderings
    """
    def backtrack(current_permutation, used, all_permutations):
        # Base case - used all numbers
        if len(current_permutation) == len(nums):
            all_permutations.append(current_permutation[:])  # Copy permutation
            return
        
        # Try each unused number
        for i in range(len(nums)):
            if i not in used:
                # Make choice - pick number at index i
                current_permutation.append(nums[i])
                used.add(i)
                
                # Recurse with updated state
                backtrack(current_permutation, used, all_permutations)
                
                # Backtrack - undo choice
                current_permutation.pop()
                used.remove(i)
    
    all_permutations = []
    backtrack([], set(), all_permutations)
    return all_permutations

# Test permutations
print("Permutations of [1,2,3]:", permute([1, 2, 3]))
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# ================================================================
# PATTERN 3: SUBSET GENERATION
# LC 78 - Subsets  
# PATTERN EXPLANATION:
# Generate all possible subsets by deciding include/exclude for each element.
# Key insight: At each element, make binary choice - include it or skip it.
# Applications: Power set generation, subset sum, partition problems.
# ================================================================

def subsets(nums):
    """
    Generate all possible subsets (power set)
    Time: O(2^N * N), Space: O(N) for recursion
    
    How it works:
    1. For each element, make two recursive calls:
        - One including the current element
        - One excluding the current element
    2. Base case reached when processed all elements
    3. This creates all 2^N possible combinations
    """
    def backtrack(index, current_subset, all_subsets):
        # Base case - processed all elements
        if index == len(nums):
            all_subsets.append(current_subset[:])  # Copy current subset
            return
        
        # Choice 1: Include current element
        current_subset.append(nums[index])
        backtrack(index + 1, current_subset, all_subsets)
        current_subset.pop()  # Backtrack
        
        # Choice 2: Exclude current element  
        backtrack(index + 1, current_subset, all_subsets)
    
    all_subsets = []
    backtrack(0, [], all_subsets)
    return all_subsets

# Test subsets
print("All subsets of [1,2,3]:", subsets([1, 2, 3]))
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# ================================================================
# PATTERN 4: MATRIX BACKTRACKING WITH STATE RESTORATION
# LC 79 - Word Search
# PATTERN EXPLANATION:
# Search in 2D space by exploring all directions with proper state management.
# Key insight: Mark cells as visited, explore neighbors, then unmark (restore state).
# Applications: Word search, pathfinding, maze solving, flood fill variations.
# ================================================================

def exist(board, word):
    """
    Find if word exists in 2D character grid
    Time: O(M*N*4^L) where M,N=board dimensions, L=word length
    Space: O(L) for recursion depth
    
    How it works:
    1. Try starting from each cell in the board
    2. For each start, use DFS to match word character by character
    3. Mark visited cells to avoid reuse in current path
    4. Backtrack by restoring original cell value
    5. Explore all 4 directions from each cell
    """
    def backtrack(row, col, index):
        # Base case - found complete word
        if index == len(word):
            return True
        
        # Check bounds, character match, and if already visited
        if (row < 0 or row >= len(board) or 
            col < 0 or col >= len(board[0]) or 
            board[row][col] != word[index] or
            board[row][col] == '#'):  # '#' marks visited
            return False
        
        # Make choice - mark cell as visited
        original_char = board[row][col]
        board[row][col] = '#'  # Temporarily mark as visited
        
        # Explore all 4 directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
        found = False
        for dr, dc in directions:
            if backtrack(row + dr, col + dc, index + 1):
                found = True
                break  # Early termination once word is found
        
        # Backtrack - restore original character
        board[row][col] = original_char  # Critical: restore state
        
        return found
    
    # Try starting from each cell
    for i in range(len(board)):
        for j in range(len(board[0])):
            if backtrack(i, j, 0):
                return True
    
    return False

# Test word search
test_board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'], 
    ['A', 'D', 'E', 'E']
]
print("Word 'ABCCED' exists:", exist(test_board, "ABCCED"))  # True
print("Word 'SEE' exists:", exist(test_board, "SEE"))       # True  
print("Word 'ABCB' exists:", exist(test_board, "ABCB"))     # False

"""
COMMON BACKTRACKING MISTAKES
============================

1. **Forgetting to backtrack**: Always undo changes after recursion
    ❌ current_path.append(node.val); recurse(); # Missing pop()
    ✅ current_path.append(node.val); recurse(); current_path.pop()

2. **Modifying shared state**: Use copies when storing solutions  
    ❌ all_solutions.append(current_solution)  # Shares reference
    ✅ all_solutions.append(current_solution[:])  # Makes copy

3. **Incorrect base cases**: Handle both success and failure conditions
    ❌ if len(path) == target: return  # Missing return value
    ✅ if len(path) == target: solutions.append(path[:])

4. **Not restoring state**: Essential for matrix/board problems
    ❌ board[r][c] = '#'; recurse(); # Missing restoration  
    ✅ temp = board[r][c]; board[r][c] = '#'; recurse(); board[r][c] = temp

5. **Inefficient choice generation**: Use constraints to prune early
    ❌ for choice in all_possible_choices:  # May include invalid
    ✅ for choice in valid_choices_only:   # Pre-filter choices

WHEN TO USE BACKTRACKING VS OTHER APPROACHES
===========================================

Use BACKTRACKING when:
- Need ALL solutions, not just one optimal
- Can prune invalid branches early
- Solution built incrementally with choices
- Exploring permutations/combinations/arrangements

Use DYNAMIC PROGRAMMING when:
- Looking for optimal solution
- Overlapping subproblems exist  
- Can store and reuse partial results

Use GREEDY when:
- Local optimal choices lead to global optimum
- Don't need to explore all possibilities
- Can make irrevocable decisions

Use BFS when:
- Need shortest path/minimum steps
- Exploring level by level makes sense
- All edges have equal weight
"""