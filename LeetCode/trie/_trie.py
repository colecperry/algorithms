"""
=================================================================
TRIE COMPLETE GUIDE
=================================================================

WHAT IS A TRIE?
---------------
A Trie (pronounced "try") or Prefix Tree is a tree-like data structure that stores strings
in a way that enables fast prefix-based operations. Each node represents a character, and
paths from root to nodes represent prefixes or complete words. Particularly efficient for
dictionary operations, autocomplete, and prefix matching.

Key characteristics:
- Root node is empty (represents empty string)
- Each edge represents a character
- Path from root to node = prefix
- Special marker indicates end of complete word
- Nodes can have up to 26 children (for lowercase English)
- Space-time tradeoff: uses more space for faster operations

Basic structure:
```
        root
       / | \
      a  b  c
     /   |   \
    p    a    a
   /     |     \
  p      t      t
 /             
l (end)        (end)   (end)

Words: "apple", "bat", "cat"
```

When to use Trie:
- Dictionary operations (insert, search, prefix check)
- Autocomplete/search suggestions
- Spell checking
- IP routing (longest prefix matching)
- Word games (Boggle, Scrabble validation)
- String matching with many patterns

Common Trie problem types:
- Basic operations (implement Trie)
- Prefix/suffix matching
- Word search in grid (Boggle)
- Autocomplete systems
- Word dictionary with wildcards
- Replace words (shortest prefix)
- XOR problems (binary trie)
- Stream of characters/longest word

TRIE CORE TEMPLATES
====================
"""

from typing import List, Optional
from collections import defaultdict

# ================================================================
# BASIC TRIE NODE TEMPLATE
# ================================================================
class TrieNode:
    """
    Basic Trie node with children dictionary
    """
    def __init__(self):
        self.children = {}  # Map char -> TrieNode
        self.is_end = False  # Marks end of word

# Alternative: Fixed array for children
class TrieNodeArray:
    """
    Trie node with fixed array (for lowercase English letters)
    Faster access but more memory
    """
    def __init__(self):
        self.children = [None] * 26  # a-z
        self.is_end = False

# ================================================================
# BASIC TRIE TEMPLATE
# ================================================================
class BasicTrie:
    """
    Standard Trie implementation with insert, search, startsWith
    TC: O(m) for all operations where m = word length
    SC: O(n * m) where n = number of words
    """
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """Insert word into trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word: str) -> bool:
        """Search for exact word"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def startsWith(self, prefix: str) -> bool:
        """Check if any word starts with prefix"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# ================================================================
# TRIE WITH COUNT TEMPLATE
# ================================================================
class TrieNodeWithCount:
    """Trie node that tracks word and prefix counts"""
    def __init__(self):
        self.children = {}
        self.word_count = 0    # Number of words ending here
        self.prefix_count = 0  # Number of words with this prefix

# ================================================================
# BINARY TRIE TEMPLATE (FOR XOR)
# ================================================================
class BinaryTrieNode:
    """Trie node for binary numbers (0 and 1)"""
    def __init__(self):
        self.children = [None, None]  # children[0] for 0, children[1] for 1

class BinaryTrie:
    """
    Binary trie for XOR operations
    TC: O(32) or O(log MAX_VAL) per operation
    """
    def __init__(self):
        self.root = BinaryTrieNode()
    
    def insert(self, num: int) -> None:
        """Insert number as binary string"""
        node = self.root
        for i in range(31, -1, -1):  # 32 bits, MSB first
            bit = (num >> i) & 1
            if not node.children[bit]:
                node.children[bit] = BinaryTrieNode()
            node = node.children[bit]
    
    def find_max_xor(self, num: int) -> int:
        """Find maximum XOR with any inserted number"""
        node = self.root
        max_xor = 0
        
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            # Try opposite bit for maximum XOR
            toggled = 1 - bit
            
            if node.children[toggled]:
                max_xor |= (1 << i)
                node = node.children[toggled]
            else:
                node = node.children[bit]
        
        return max_xor

"""
TIME & SPACE COMPLEXITY REFERENCE
==================================

TRIE OPERATIONS COMPLEXITY:
---------------------------
+---------------------------+------------------+------------------+
| Operation                 | Time Complexity  | Space Complexity |
+---------------------------+------------------+------------------+
| Insert word               | O(m)             | O(m)             |
| Search word               | O(m)             | O(1)             |
| Search prefix             | O(m)             | O(1)             |
| Delete word               | O(m)             | O(1)             |
| Autocomplete (k results)  | O(p + k)         | O(k)             |
| Count words with prefix   | O(p)             | O(1)             |
+---------------------------+------------------+------------------+

WHERE:
- m = length of word/pattern
- p = length of prefix
- k = number of results
- n = total number of words in trie

TRIE VS OTHER DATA STRUCTURES:
-------------------------------
+---------------------------+------------------+------------------+
| Data Structure            | Search           | Prefix Search    |
+---------------------------+------------------+------------------+
| Hash Set                  | O(m)             | O(n * m)         |
| Sorted Array              | O(m log n)       | O(m log n)       |
| Trie                      | O(m)             | O(p)             |
| Binary Search Tree        | O(m log n)       | O(m log n)       |
+---------------------------+------------------+------------------+

COMMON TRIE PATTERNS COMPLEXITY:
---------------------------------
+---------------------------+------------------+------------------+
| Pattern                   | Time Complexity  | Space Complexity |
+---------------------------+------------------+------------------+
| Basic Trie                | O(m)             | O(n * m)         |
| Word Search (Grid + Trie) | O(rows*cols*4^L) | O(n * m)         |
| Autocomplete              | O(p + k*m)       | O(n * m)         |
| Dictionary with Wildcard  | O(m * 26^w)      | O(n * m)         |
| Replace Words             | O(d + s)         | O(d)             |
| Binary Trie (XOR)         | O(log MAX)       | O(n * log MAX)   |
+---------------------------+------------------+------------------+

WHERE:
- m = average word length
- n = number of words
- p = prefix length
- k = number of results
- L = max word length in grid
- w = number of wildcards
- d = dictionary size
- s = sentence length
- MAX = maximum value in array

COMPLEXITY NOTES:
-----------------
1. Basic Trie Operations: O(m) time
   - Insert: traverse m characters, create nodes if needed
   - Search: traverse m characters, check is_end
   - Prefix: traverse p characters, don't check is_end
   
   Space per word: O(m) in worst case (no shared prefixes)
   Total space: O(n * m) worst case, better with shared prefixes
   
   Why O(m)? Each character requires one node traversal/creation

2. Trie Space Optimization:
   - Worst case: O(ALPHABET_SIZE * n * m) if using arrays
   - Average case: Much better due to prefix sharing
   - HashMap children: O(actual_children) per node
   - Array children: O(26) per node (faster but more space)
   
   Example: ["apple", "app", "apply"]
   - Separate: 5 + 3 + 5 = 13 nodes
   - Trie: Only 7 unique prefix nodes (app-l-y, app-l-e, app)

3. Word Search in Grid (Boggle): O(rows * cols * 4^L)
   - Start DFS from each cell: O(rows * cols)
   - At each cell, try 4 directions: O(4^L) per path
   - L = maximum word length
   - Trie pruning significantly reduces practical complexity
   
   Without Trie: O(rows * cols * 4^L * n * m)
   With Trie: O(rows * cols * 4^L) - check n words in one pass

4. Autocomplete: O(p + k * m)
   - Find prefix node: O(p)
   - DFS to collect k words: O(k * m)
   - m = average word length
   
   Better than iterating all words: O(n * m)
   Trie allows focused search in prefix subtree

5. Dictionary with Wildcards: O(m * 26^w)
   - For each wildcard: try all 26 letters
   - w wildcards: 26^w possibilities
   - m characters to check
   
   Example: "a.c" → try "aac", "abc", "acc", ..., "azc" (26 options)
   Without wildcards: O(m)
   With w wildcards: O(m * 26^w)

6. Binary Trie (XOR): O(log MAX_VAL)
   - Insert/Search: O(32) = O(log MAX_VAL) for 32-bit integers
   - Each bit requires one node
   - Space: O(n * log MAX_VAL) for n numbers
   
   Why useful? Find max XOR in O(log MAX) vs O(n^2) brute force
   Each number stored as 32-bit path in trie

7. Replace Words (Shortest Prefix): O(d + s)
   - Build trie from dictionary: O(d) where d = total chars
   - Process sentence: O(s) where s = sentence length
   - For each word: O(m) to find shortest prefix
   
   Total: O(d + s)
   Without trie: O(d * s) - check each word against all roots

8. Trie vs HashMap:
   - Trie wins: Prefix operations, ordered traversal, memory with shared prefixes
   - HashMap wins: Exact match only, less memory with no shared prefixes
   - Trie space: O(ALPHABET * n * m) worst case
   - HashMap space: O(n * m) always

WHEN TO USE TRIE:
-----------------
Use Trie when:
- Need prefix-based operations (startsWith, autocomplete)
- Multiple words share common prefixes
- Dictionary with many words
- Pattern matching with wildcards
- Finding longest common prefix
- XOR maximum problems (binary trie)

Don't use Trie when:
- Only exact match needed (use HashMap)
- Few words, no shared prefixes
- Memory constrained (Trie uses more space)
- Single word operations (Trie overkill)

SPACE-TIME TRADEOFFS:
--------------------
Trie trades space for time:
- More space: O(ALPHABET * n * m) vs O(n * m) for set
- Faster prefix operations: O(p) vs O(n * m)
- Shared prefixes save space in practice

Optimization techniques:
- Use HashMap for children (save space)
- Use array for children (faster access)
- Compress path (radix tree)
- Reference counting for deletion
"""

"""
TRIE PATTERNS
=============
"""

# ================================================================
# PATTERN 1: BASIC TRIE (INSERT, SEARCH, PREFIX)
# PATTERN EXPLANATION: Implement fundamental trie operations for dictionary management.
# Insert adds words character by character, creating nodes as needed. Search checks for
# complete words by verifying is_end flag. StartsWith checks for prefix by traversing
# without requiring is_end. Foundation for all other trie patterns.
#
# TYPICAL STEPS:
# Insert:
# 1. Start at root, iterate through characters
# 2. If character not in children, create new node
# 3. Move to child node
# 4. Mark last node as end of word
#
# Search:
# 1. Traverse trie following characters
# 2. If character missing, return False
# 3. At end, check if node is marked as word end
#
# Prefix:
# 1. Traverse trie following characters
# 2. If reach end of prefix successfully, return True
#
# Applications: Dictionary, spell checker, word validator, prefix search.
# ================================================================

class Trie:
    """
    Problem: Implement a trie with insert, search, and startsWith operations.
    
    Example:
        Trie trie = new Trie()
        trie.insert("apple")
        trie.search("apple")   → true
        trie.search("app")     → false
        trie.startsWith("app") → true
        trie.insert("app")
        trie.search("app")     → true
    
    TC: O(m) for all operations where m = word length
    SC: O(n * m) where n = number of words
    
    How it works:
    1. Each node has children map and is_end flag
    2. Insert: create path of nodes for each character
    3. Search: follow path, check is_end at end
    4. StartsWith: follow path for prefix, don't check is_end
    """
    def __init__(self):  # LC 208 - Implement Trie
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """Insert word into trie"""
        node = self.root
        
        for char in word:
            # Create node if doesn't exist
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to child
            node = node.children[char]
        
        # Mark end of word
        node.is_end = True
    
    def search(self, word: str) -> bool:
        """Search for exact word"""
        node = self.root
        
        for char in word:
            # Character not found
            if char not in node.children:
                return False
            node = node.children[char]
        
        # Check if complete word
        return node.is_end
    
    def startsWith(self, prefix: str) -> bool:
        """Check if any word starts with prefix"""
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        # Don't need to check is_end (just prefix)
        return True

# Example trace:
# Insert "apple":
#   root -> a -> p -> p -> l -> e (is_end=True)
#
# Insert "app":
#   root -> a -> p -> p (is_end=True, reuse existing path)
#
# Trie structure:
#         root
#          |
#          a
#          |
#          p
#          |
#          p (is_end=True for "app")
#          |
#          l
#          |
#          e (is_end=True for "apple")
#
# search("apple"): traverse to 'e', is_end=True → True
# search("app"): traverse to second 'p', is_end=True → True
# search("appl"): traverse to 'l', is_end=False → False
# startsWith("app"): traverse to second 'p', exists → True

    def longestCommonPrefix(self, strs: List[str]) -> str:  # LC 14
        """
        Problem: Find longest common prefix among array of strings.
        
        Example:
            Input: ["flower","flow","flight"]
            Output: "fl"
        
        TC: O(n * m) where n = number of strings, m = length
        SC: O(n * m) for trie
        
        Using Trie approach:
        1. Insert all strings into trie
        2. Traverse from root while:
           - Node has only one child
           - Node is not end of word
        3. Return characters collected
        """
        if not strs:
            return ""
        
        # Build trie
        trie = Trie()
        for s in strs:
            trie.insert(s)
        
        # Find common prefix
        node = trie.root
        prefix = []
        
        while True:
            # Stop if more than one branch or end of word
            if len(node.children) != 1 or node.is_end:
                break
            
            # Get single child
            char = list(node.children.keys())[0]
            prefix.append(char)
            node = node.children[char]
        
        return ''.join(prefix)

# Alternative: Without trie (simpler for this problem)
    def longestCommonPrefix_simple(self, strs: List[str]) -> str:
        """
        TC: O(n * m)
        SC: O(1)
        """
        if not strs:
            return ""
        
        # Compare character by character
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            for s in strs[1:]:
                # Reached end of string or different character
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
        
        return strs[0]

trie = Trie()
trie.insert("apple")
print("Search 'apple':", trie.search("apple"))  # True
print("Search 'app':", trie.search("app"))  # False
print("StartsWith 'app':", trie.startsWith("app"))  # True
trie.insert("app")
print("Search 'app':", trie.search("app"))  # True
print("Longest Common Prefix:", trie.longestCommonPrefix(["flower","flow","flight"]))  # "fl"


# ================================================================
# PATTERN 2: WORD SEARCH WITH TRIE (GRID DFS + TRIE)
# PATTERN EXPLANATION: Combine trie with DFS on 2D grid to find multiple words efficiently.
# Build trie from word list, then DFS from each cell, using trie to prune invalid paths
# early. Significantly faster than searching for each word individually. Classic application
# for word games like Boggle.
#
# TYPICAL STEPS:
# 1. Build trie from all words
# 2. For each cell in grid:
#    a. Start DFS with root of trie
#    b. Check if current character in trie children
#    c. If yes, continue DFS to neighbors
#    d. If current node is end of word, add to result
#    e. Mark cell visited, recurse, unmark (backtrack)
# 3. Prune: stop DFS if character not in trie
#
# Applications: Boggle, word search in grid, finding multiple patterns in text.
# ================================================================

class WordSearchTrie:
    """
    Problem: Find all words from dictionary that can be formed in a 2D board.
    Words can be constructed from letters of sequentially adjacent cells (horizontal/vertical).
    Same cell cannot be used twice in one word.
    
    Example:
        board = [['o','a','a','n'],
                 ['e','t','a','e'],
                 ['i','h','k','r'],
                 ['i','f','l','v']]
        words = ["oath","pea","eat","rain"]
        
        Output: ["eat","oath"]
        
        "eat": e(0,0) -> a(0,1) -> t(1,1)
        "oath": o(0,0) -> a(0,1) -> t(1,1) -> h(1,2)
    
    TC: O(m*n*4^L) where L = max word length
        Without trie: O(m*n*4^L * k*L) where k = number of words
    SC: O(k*L) for trie where k = number of words
    
    How it works:
    1. Build trie from word list (prune invalid paths early)
    2. DFS from each cell, following valid trie paths
    3. When reach end of word in trie, add to result
    4. Mark cells visited during path, unmark when backtrack
    """
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:  # LC 212
        # Build trie from words
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
            node.word = word  # Store word at end node
        
        rows, cols = len(board), len(board[0])
        result = []
        
        def dfs(r, c, node):
            """DFS with trie pruning"""
            # Get current character
            char = board[r][c]
            
            # Check if character in trie
            if char not in node.children:
                return
            
            # Move to next trie node
            next_node = node.children[char]
            
            # Found complete word
            if next_node.is_end:
                result.append(next_node.word)
                next_node.is_end = False  # Avoid duplicates
            
            # Mark visited
            board[r][c] = '#'
            
            # Explore 4 directions
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and 
                    board[nr][nc] != '#'):
                    dfs(nr, nc, next_node)
            
            # Backtrack
            board[r][c] = char
            
            # Optimization: remove leaf nodes to prune trie
            if not next_node.children:
                del node.children[char]
        
        # Start DFS from each cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        return result

# Example trace:
# board = [['o','a','a','n'],
#          ['e','t','a','e'],
#          ['i','h','k','r'],
#          ['i','f','l','v']]
# words = ["oath","pea","eat","rain"]
#
# Trie structure:
#     root
#    / | \ \
#   o  p  e  r
#   |  |  |  |
#   a  e  a  a
#   |  |  |  |
#   t  a  t  i
#   |        |
#   h        n
#
# DFS from (0,0) with 'o':
#   'o' in trie → continue
#   Try neighbors: (0,1)='a', (1,0)='e'
#   Go to (0,1) with 'a':
#     'a' in trie children of 'o' → continue
#     Try neighbors: (0,2)='a', (1,1)='t'
#     Go to (1,1) with 't':
#       't' in children of 'a' → continue
#       Try neighbors: (1,2)='a', (2,1)='h'
#       Go to (2,1) with 'h':
#         'h' in children of 't' → is_end=True
#         Found "oath"! Add to result
#
# Pruning benefit: If we tried path starting with 'x', 
# DFS stops immediately since 'x' not in trie root

sol = WordSearchTrie()
board = [['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']]
print("Word Search II:", sol.findWords(board, ["oath","pea","eat","rain"]))  # ["oath","eat"]


# ================================================================
# PATTERN 3: AUTOCOMPLETE / PREFIX MATCHING
# PATTERN EXPLANATION: Collect all words with given prefix from trie. Navigate to prefix
# node, then DFS to collect all complete words in that subtree. Efficient for typeahead,
# search suggestions, and autocomplete systems. Can limit results or rank by frequency.
#
# TYPICAL STEPS:
# 1. Navigate to prefix node in trie
# 2. If prefix not found, return empty
# 3. DFS from prefix node collecting words:
#    a. If current node is end of word, add to results
#    b. Recursively visit all children
#    c. Build word as you traverse
# 4. Optional: sort by frequency/rank, limit results
#
# Applications: Autocomplete, search suggestions, typeahead, prefix matching.
# ================================================================

class AutocompleteTrie:
    """
    Problem: Design autocomplete system that returns top 3 suggestions
    after each character typed.
    
    Example:
        Input: sentences = ["i love you","island","iroman","i love leetcode"]
               times = [5,3,2,2]
        
        User types "i":
        Output: ["i love you","island","i love leetcode"]
        (top 3 by frequency)
        
        User types " ":
        Output: ["i love you","i love leetcode"]
    
    TC: O(p + k*m) where p = prefix length, k = results, m = avg word length
    SC: O(n*m) for trie
    
    How it works:
    1. Build trie with frequency counts
    2. For each character, navigate to prefix node
    3. DFS from prefix node to collect all words
    4. Sort by frequency and return top k
    """
    def __init__(self, sentences: List[str], times: List[int]):  # LC 642
        self.root = TrieNode()
        self.root.sentences = {}  # Store (sentence, frequency) at each node
        self.current_prefix = ""
        
        # Build trie with frequencies
        for sentence, time in zip(sentences, times):
            self._add_sentence(sentence, time)
    
    def _add_sentence(self, sentence: str, time: int):
        """Add sentence to trie with frequency"""
        node = self.root
        
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
                node.children[char].sentences = {}
            node = node.children[char]
            
            # Update frequency at this prefix node
            if sentence in node.sentences:
                node.sentences[sentence] += time
            else:
                node.sentences[sentence] = time
    
    def input(self, c: str) -> List[str]:
        """Process character input and return top 3 suggestions"""
        if c == '#':
            # End of sentence, add to trie
            self._add_sentence(self.current_prefix, 1)
            self.current_prefix = ""
            return []
        
        # Build current prefix
        self.current_prefix += c
        
        # Navigate to prefix node
        node = self.root
        for char in self.current_prefix:
            if char not in node.children:
                return []  # Prefix not found
            node = node.children[char]
        
        # Get all sentences with this prefix
        sentences = node.sentences
        
        # Sort by frequency (desc) then lexicographically
        sorted_sentences = sorted(sentences.items(), 
                                 key=lambda x: (-x[1], x[0]))
        
        # Return top 3
        return [sentence for sentence, _ in sorted_sentences[:3]]

# Example trace:
# sentences = ["i love you","island","iroman","i love leetcode"]
# times = [5,3,2,2]
#
# After building trie:
#         root
#          |
#          i
#         / \
#        ' ' s
#        |   |
#       love land
#       ...
#
# At node 'i':
#   sentences = {"i love you": 5, "island": 3, "iroman": 2, "i love leetcode": 2}
#
# input('i'):
#   Navigate to 'i' node
#   Get all sentences: sorted by (-freq, name)
#   Return top 3: ["i love you", "island", "i love leetcode"]
#
# input(' '):
#   Navigate to 'i' -> ' ' node
#   sentences = {"i love you": 5, "i love leetcode": 2}
#   Return: ["i love you", "i love leetcode"]

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:  # LC 1268
        """
        Problem: Return top 3 lexicographically minimal products after each character.
        
        Example:
            products = ["mobile","mouse","moneypot","monitor","mousepad"]
            searchWord = "mouse"
            
            Output: [
                ["mobile","moneypot","monitor"],  # prefix "m"
                ["mobile","moneypot","monitor"],  # prefix "mo"
                ["mouse","mousepad"],             # prefix "mou"
                ["mouse","mousepad"],             # prefix "mous"
                ["mouse","mousepad"]              # prefix "mouse"
            ]
        
        TC: O(n*m + k*L) where n = products, m = length, k = prefix length, L = results
        SC: O(n*m) for trie
        """
        # Build trie
        root = TrieNode()
        for product in products:
            node = root
            for char in product:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
            node.product = product
        
        result = []
        node = root
        
        # Process each prefix
        for char in searchWord:
            if node and char in node.children:
                node = node.children[char]
                # DFS to collect up to 3 products
                products_found = []
                self._collect_products(node, products_found, 3)
                result.append(sorted(products_found)[:3])
            else:
                node = None  # Prefix not found
                result.append([])
        
        return result
    
    def _collect_products(self, node, products, limit):
        """DFS to collect products from subtree"""
        if len(products) >= limit:
            return
        
        if node.is_end:
            products.append(node.product)
        
        # Visit children in alphabetical order
        for char in sorted(node.children.keys()):
            self._collect_products(node.children[char], products, limit)

# Alternative simpler solution using sorting:
    def suggestedProducts_simple(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        TC: O(n log n + k*n) where k = searchWord length
        SC: O(1) excluding output
        """
        products.sort()
        result = []
        prefix = ""
        
        for char in searchWord:
            prefix += char
            # Filter products starting with prefix
            suggestions = [p for p in products if p.startswith(prefix)]
            result.append(suggestions[:3])
        
        return result

# sol = AutocompleteTrie(["i love you","island","iroman","i love leetcode"], [5,3,2,2])
# print(sol.input('i'))   # ["i love you","island","i love leetcode"]
# print(sol.input(' '))   # ["i love you","i love leetcode"]

sol2 = AutocompleteTrie([], [])
print("Suggested Products:", sol2.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))


# ================================================================
# PATTERN 4: WORD DICTIONARY WITH WILDCARDS
# PATTERN EXPLANATION: Support wildcard characters (usually '.') that match any letter.
# During search, when encountering wildcard, try all possible children instead of specific
# character. Requires recursive DFS to explore all branches. More complex than basic trie
# search due to branching factor of wildcards.
#
# TYPICAL STEPS:
# 1. Insert: Same as basic trie
# 2. Search with wildcards:
#    a. If regular character: follow that child
#    b. If wildcard: try all children recursively
#    c. If at end of word: check is_end flag
# 3. Use DFS/recursion for wildcard handling
#
# Applications: Pattern matching, regex-like search, flexible word lookup.
# ================================================================

class WordDictionary:
    """
    Problem: Design data structure that supports adding words and searching
    with wildcard '.' that matches any letter.
    
    Example:
        addWord("bad")
        addWord("dad")
        addWord("mad")
        search("pad") → false
        search("bad") → true
        search(".ad") → true
        search("b..") → true
    
    TC: O(m) for add, O(m * 26^w) for search where w = wildcards
    SC: O(n * m) for trie
    
    How it works:
    1. Add: Standard trie insertion
    2. Search: When hit '.', try all 26 possible children
    3. Use DFS to explore all branches for wildcards
    """
    def __init__(self):  # LC 211
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        """Add word to dictionary"""
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end = True
    
    def search(self, word: str) -> bool:
        """Search word (can include '.' wildcard)"""
        return self._search_helper(word, 0, self.root)
    
    def _search_helper(self, word: str, index: int, node: TrieNode) -> bool:
        """Recursive helper for wildcard search"""
        # Reached end of word
        if index == len(word):
            return node.is_end
        
        char = word[index]
        
        if char == '.':
            # Wildcard: try all possible children
            for child in node.children.values():
                if self._search_helper(word, index + 1, child):
                    return True
            return False
        else:
            # Regular character: follow specific path
            if char not in node.children:
                return False
            return self._search_helper(word, index + 1, node.children[char])

# Example trace:
# addWord("bad"), addWord("dad"), addWord("mad")
#
# Trie:
#       root
#      / | \
#     b  d  m
#     |  |  |
#     a  a  a
#     |  |  |
#     d  d  d
#    (e)(e)(e)
#
# search(".ad"):
#   index=0, char='.'
#   Try all children of root: 'b', 'd', 'm'
#     Try 'b': search("ad", 1, node_b)
#       index=1, char='a', found 'a' in children
#       search("d", 2, node_a)
#         index=2, char='d', found 'd' in children
#         index=3, is_end=True → return True
#   Found! return True
#
# search("b.."):
#   index=0, char='b', found
#   index=1, char='.', try all children of 'b': only 'a'
#     Try 'a': search(".", 2, node_a)
#       index=2, char='.', try all children of 'a': only 'd'
#         Try 'd': search("", 3, node_d)
#           index=3, is_end=True → return True

    def longestWord(self, words: List[str]) -> str:  # LC 720
        """
        Problem: Find longest word that can be built one character at a time
        from other words in the array.
        
        Example:
            Input: ["w","wo","wor","worl","world"]
            Output: "world"
            
            Can build: w -> wo -> wor -> worl -> world
        
        TC: O(n * m) where n = words, m = length
        SC: O(n * m) for trie
        
        How it works:
        1. Build trie from all words
        2. DFS from root, only follow paths where all prefixes are words
        3. Track longest valid word found
        """
        # Build trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
            node.word = word
        
        # DFS to find longest word
        longest = ""
        
        def dfs(node):
            nonlocal longest
            
            for char in node.children:
                child = node.children[char]
                
                # Only continue if prefix is a complete word
                if child.is_end:
                    # Update longest (prefer longer, then lexicographically smaller)
                    if len(child.word) > len(longest) or \
                       (len(child.word) == len(longest) and child.word < longest):
                        longest = child.word
                    
                    # Continue DFS
                    dfs(child)
        
        dfs(root)
        return longest

wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")
print("Search 'pad':", wd.search("pad"))  # False
print("Search '.ad':", wd.search(".ad"))  # True
print("Search 'b..':", wd.search("b.."))  # True
print("Longest Word:", wd.longestWord(["w","wo","wor","worl","world"]))  # "world"


# ================================================================
# PATTERN 5: TRIE WITH MODIFICATION (DELETE, REPLACE)
# PATTERN EXPLANATION: Extend basic trie with deletion and replacement operations. Deletion
# requires careful handling to avoid breaking other words sharing prefixes. Replace words
# with shortest prefix match (like autocorrect). Track word counts for proper deletion.
#
# TYPICAL STEPS:
# Delete:
# 1. Search for word, mark is_end = False
# 2. Remove leaf nodes if no other words use them
# 3. Stop removal when hit node with other children or is_end
#
# Replace (Shortest Prefix):
# 1. For each word, search trie for shortest prefix
# 2. If find complete word before reaching end, use that
# 3. Replace word with shortest matching prefix
#
# Applications: Dictionary with updates, autocorrect, word replacement.
# ================================================================

class TrieWithModification:
    """
    Problem 1: Implement trie with delete operation.
    
    TC: O(m) for delete
    SC: O(n * m)
    
    How it works:
    1. Mark word as not complete (is_end = False)
    2. Remove unused leaf nodes recursively
    3. Stop at nodes with other children or words
    """
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def delete(self, word: str) -> bool:
        """Delete word from trie"""
        def _delete_helper(node, word, index):
            if index == len(word):
                # Reached end of word
                if not node.is_end:
                    return False  # Word doesn't exist
                
                node.is_end = False
                # Return True if can delete this node (no children)
                return len(node.children) == 0
            
            char = word[index]
            if char not in node.children:
                return False  # Word doesn't exist
            
            child = node.children[char]
            should_delete_child = _delete_helper(child, word, index + 1)
            
            if should_delete_child:
                # Delete child node
                del node.children[char]
                # Return True if this node can also be deleted
                return not node.is_end and len(node.children) == 0
            
            return False
        
        return _delete_helper(self.root, word, 0)

# Example trace:
# Insert "apple", "app", "apply"
#
# Trie:
#     root
#      |
#      a
#      |
#      p
#      |
#      p (is_end for "app")
#     / \
#    l   l
#    |   |
#    y   e
#   (e) (e)
#
# delete("apply"):
#   Traverse to 'y': is_end=True, no children
#   Set is_end=False at 'y', can delete
#   Delete 'y' from parent 'l'
#   Node 'l' has no children, not end → can delete
#   Delete left 'l' from 'p'
#   Node 'p' still has child 'l' (for "apple") → stop
#
# Resulting trie:
#     root
#      |
#      a
#      |
#      p
#      |
#      p (is_end for "app")
#      |
#      l
#      |
#      e
#     (e)

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:  # LC 648
        """
        Problem 2: Replace words with their shortest root from dictionary.
        
        Example:
            dictionary = ["cat","bat","rat"]
            sentence = "the cattle was rattled by the battery"
            Output: "the cat was rat by the bat"
            
            "cattle" → "cat" (shortest prefix)
            "rattled" → "rat" (shortest prefix)
            "battery" → "bat" (shortest prefix)
        
        TC: O(d + s) where d = dictionary size, s = sentence length
        SC: O(d) for trie
        
        How it works:
        1. Build trie from dictionary roots
        2. For each word in sentence:
           - Search trie character by character
           - Stop at first complete word (shortest prefix)
           - If no match, keep original word
        """
        # Build trie from dictionary
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
        
        # Process each word in sentence
        words = sentence.split()
        result = []
        
        for word in words:
            # Find shortest prefix
            node = root
            prefix = []
            
            for char in word:
                if char not in node.children:
                    break
                
                node = node.children[char]
                prefix.append(char)
                
                # Found complete root (shortest prefix)
                if node.is_end:
                    break
            
            # Use prefix if found, otherwise original word
            if node.is_end:
                result.append(''.join(prefix))
            else:
                result.append(word)
        
        return ' '.join(result)

# Example trace:
# dictionary = ["cat","bat","rat"]
# sentence = "the cattle was rattled by the battery"
#
# Trie:
#     root
#    / | \
#   c  b  r
#   |  |  |
#   a  a  a
#   |  |  |
#   t  t  t
#  (e)(e)(e)
#
# Process "cattle":
#   c → a → t (is_end=True, stop)
#   Found "cat", use it
#
# Process "rattled":
#   r → a → t (is_end=True, stop)
#   Found "rat", use it
#
# Process "battery":
#   b → a → t (is_end=True, stop)
#   Found "bat", use it
#
# Result: "the cat was rat by the bat"

triem = TrieWithModification()
triem.insert("apple")
triem.insert("app")
print("Delete 'app':", triem.delete("app"))  # True
print("Replace Words:", triem.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))


# ================================================================
# PATTERN 6: BINARY TRIE (XOR PROBLEMS)
# PATTERN EXPLANATION: Use trie to store binary representation of numbers for XOR operations.
# Each node has two children (0 and 1 bit). Insert numbers as 32-bit binary paths. To find
# maximum XOR, greedily choose opposite bits when possible. Achieves O(log MAX_VAL) per
# operation instead of O(n²) brute force.
#
# TYPICAL STEPS:
# Insert:
# 1. Convert number to binary (32 bits)
# 2. Traverse/create path from MSB to LSB
# 3. Create nodes for 0 and 1 as needed
#
# Find Max XOR:
# 1. For given number, traverse trie
# 2. At each bit: try opposite bit (for max XOR)
# 3. If opposite exists, take it; else take same
# 4. Build result XOR value bit by bit
#
# Applications: Maximum XOR pair, XOR queries with range, bit manipulation problems.
# ================================================================

class MaximumXORTrie:
    """
    Problem 1: Find maximum XOR of two numbers in array.
    
    Example:
        Input: nums = [3,10,5,25,2,8]
        Output: 28
        
        Explanation: 5 XOR 25 = 28
        5  = 00101
        25 = 11001
        XOR= 11100 = 28
    
    TC: O(n * 32) = O(n) where n = number of elements
    SC: O(n * 32) = O(n) for trie
    
    How it works:
    1. Insert all numbers as binary paths in trie
    2. For each number, find maximum XOR:
       - Try opposite bit at each position
       - Opposite bit gives 1 in XOR result
       - Track maximum XOR found
    """
    def findMaximumXOR(self, nums: List[int]) -> int:  # LC 421
        root = BinaryTrieNode()
        
        # Insert all numbers
        for num in nums:
            node = root
            for i in range(31, -1, -1):  # 32 bits, MSB first
                bit = (num >> i) & 1
                if not node.children[bit]:
                    node.children[bit] = BinaryTrieNode()
                node = node.children[bit]
        
        # Find maximum XOR
        max_xor = 0
        
        for num in nums:
            node = root
            current_xor = 0
            
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                # Try opposite bit for maximum XOR
                toggled = 1 - bit
                
                if node.children[toggled]:
                    # Opposite bit exists, use it (XOR = 1)
                    current_xor |= (1 << i)
                    node = node.children[toggled]
                else:
                    # Must use same bit (XOR = 0)
                    node = node.children[bit]
            
            max_xor = max(max_xor, current_xor)
        
        return max_xor

# Example trace:
# nums = [3, 10, 5]
# Binary:
# 3  = 00011
# 10 = 01010
# 5  = 00101
#
# Insert 3 (00011):
#   Bit 4(0): create node.children[0]
#   Bit 3(0): create node.children[0]
#   Bit 2(0): create node.children[0]
#   Bit 1(1): create node.children[1]
#   Bit 0(1): create node.children[1]
#
# Find max XOR with 10 (01010):
#   Bit 4(0): try bit 1? No → use bit 0, XOR bit = 0
#   Bit 3(1): try bit 0? Yes! → use bit 0, XOR bit = 1
#   Bit 2(0): try bit 1? Yes! (from 5) → use bit 1, XOR bit = 1
#   Bit 1(1): try bit 0? Yes! (from 3) → use bit 0, XOR bit = 1
#   Bit 0(0): try bit 1? Yes! (from 3,5) → use bit 1, XOR bit = 1
#   
#   current_xor = 01111 = 15
#   10 XOR 5 = 15 ✓

    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:  # LC 1707
        """
        Problem 2: Maximum XOR with constraint (values <= m).
        
        Example:
            nums = [0,1,2,3,4]
            queries = [[3,1],[1,3],[5,6]]
            
            Query [3,1]: max XOR of 3 with nums[i] <= 1
                Can use 0,1 → max(3^0=3, 3^1=2) = 3
            Query [1,3]: max XOR of 1 with nums[i] <= 3
                Can use 0,1,2,3 → max(1^0=1, 1^1=0, 1^2=3, 1^3=2) = 3
            
            Output: [3,3,7]
        
        TC: O(n log n + q * 32) where q = queries
        SC: O(n * 32) for trie
        
        How it works:
        1. Sort nums and queries by value
        2. Process queries in order
        3. Insert nums <= m into trie before each query
        4. Find max XOR using trie
        """
        # Sort nums
        nums.sort()
        
        # Sort queries but keep original indices
        indexed_queries = [(m, x, i) for i, (x, m) in enumerate(queries)]
        indexed_queries.sort()
        
        root = BinaryTrieNode()
        result = [-1] * len(queries)
        nums_idx = 0
        
        for m, x, original_idx in indexed_queries:
            # Insert all nums <= m
            while nums_idx < len(nums) and nums[nums_idx] <= m:
                num = nums[nums_idx]
                node = root
                
                for i in range(31, -1, -1):
                    bit = (num >> i) & 1
                    if not node.children[bit]:
                        node.children[bit] = BinaryTrieNode()
                    node = node.children[bit]
                
                nums_idx += 1
            
            # If no valid nums inserted, return -1
            if nums_idx == 0:
                continue
            
            # Find max XOR with x
            node = root
            current_xor = 0
            
            for i in range(31, -1, -1):
                bit = (x >> i) & 1
                toggled = 1 - bit
                
                if node.children[toggled]:
                    current_xor |= (1 << i)
                    node = node.children[toggled]
                else:
                    node = node.children[bit]
            
            result[original_idx] = current_xor
        
        return result

sol = MaximumXORTrie()
print("Maximum XOR:", sol.findMaximumXOR([3,10,5,25,2,8]))  # 28
print("Maximize XOR:", sol.maximizeXor([0,1,2,3,4], [[3,1],[1,3],[5,6]]))  # [3,3,7]


# ================================================================
# SUMMARY OF TRIE PATTERNS
# ================================================================
"""
Pattern 1 - Basic Trie (Insert, Search, Prefix):
  - Fundamental trie operations
  - O(m) for all operations
  - Use for: Dictionary, spell checker, prefix lookup
  - Example: LC 208 (Implement Trie), LC 14 (Longest Common Prefix)

Pattern 2 - Word Search with Trie (Grid DFS + Trie):
  - Combine trie with grid DFS for multi-word search
  - Trie prunes invalid paths early
  - Use for: Boggle, word games, multi-pattern matching
  - Example: LC 212 (Word Search II)

Pattern 3 - Autocomplete / Prefix Matching:
  - Collect all words with given prefix
  - DFS from prefix node
  - Use for: Search suggestions, typeahead, autocomplete
  - Example: LC 642 (Autocomplete System), LC 1268 (Search Suggestions)

Pattern 4 - Word Dictionary with Wildcards:
  - Support wildcard characters (.) in search
  - Try all children for wildcards
  - Use for: Pattern matching, flexible search
  - Example: LC 211 (Add and Search Word), LC 720 (Longest Word)

Pattern 5 - Trie with Modification:
  - Delete words, replace with prefixes
  - Careful handling of shared paths
  - Use for: Dictionary updates, autocorrect, word replacement
  - Example: LC 648 (Replace Words), Trie deletion

Pattern 6 - Binary Trie (XOR Problems):
  - Store numbers as binary paths
  - Find maximum XOR efficiently
  - Use for: XOR queries, bit manipulation
  - Example: LC 421 (Maximum XOR), LC 1707 (Maximum XOR with Constraints)

Master these 6 patterns and you'll handle 80-90% of Trie problems on LeetCode!

KEY TAKEAWAYS:
--------------
1. Trie trades space for time on prefix operations
2. Insert/Search/Prefix all O(m) where m = word length
3. Use HashMap children for flexibility, array for speed
4. Trie + Grid DFS powerful for multi-word search
5. Wildcards require trying all branches (exponential with wildcards)
6. Binary trie enables O(log MAX) XOR operations
7. Mark is_end to distinguish complete words from prefixes
8. Store extra data (frequency, word) at nodes for extensions
9. DFS from prefix node collects all matching words
10. Prune trie by removing leaf nodes during deletion

WHEN TO USE TRIE:
-----------------
✓ Use Trie when:
  - Multiple prefix operations needed
  - Dictionary with shared prefixes
  - Autocomplete/search suggestions
  - Multi-pattern matching
  - Word games (Boggle, Scrabble)
  - XOR problems (binary trie)

✗ Don't use Trie when:
  - Only exact match needed (use HashMap)
  - Few words, no shared prefixes
  - Memory constrained
  - Single word operations
  - Suffix operations (use suffix tree/array)

SPACE-TIME TRADEOFFS:
--------------------
Trie vs HashMap:
- Trie: O(ALPHABET * n * m) space, O(m) prefix operations
- HashMap: O(n * m) space, O(m) exact match, O(n * m) prefix

Optimization:
- Use HashMap children: saves space
- Use array children: faster access
- Compress paths: radix tree
- Lazy deletion: mark nodes instead of removing
"""