"""
=================================================================
TRIE COMPLETE GUIDE
=================================================================

WHAT IS A TRIE?
---------------
A Trie (pronounced "try"), or Prefix Tree, is a tree-like data structure where each node
represents a single character. Paths from the root to nodes represent prefixes, and paths
that reach a node marked is_end represent complete words. All words that share a common
prefix share the same path from the root — this prefix-sharing is the key space savings.

Key characteristics:
- Root node represents the empty string
- Each edge represents one character
- Path from root to any node = a prefix shared by all words in that subtree
- is_end flag distinguishes complete words from mere prefixes
- children dict maps char -> next TrieNode (up to 26 for lowercase English)

Basic structure:
    Insert "app", "apple", "bat":
        root
        |- a -> p -> p (is_end=True)
        |             \\-> l -> e (is_end=True)
        \\- b -> a -> t (is_end=True)

When to use Trie:
- Need prefix-based operations (startsWith, autocomplete)
- Multiple strings share common prefixes
- Dictionary with insert/search/prefix-check in O(word_length)
- Wildcard pattern matching (replace '.' with try-all-children DFS)
- Multi-word search in a grid (combine with DFS + pruning)

Common Trie problem types:
- Implement Trie (insert, search, startsWith)
- Word dictionary with wildcards ('.' matches any letter)
- Word Search II (find multiple words in a grid)
- Replace words with shortest prefix
- Longest word built one character at a time

TRIE CORE PATTERNS
==================
"""

from typing import List

"""
TRIE COMPLEXITY REFERENCE
==========================

+---------------------------+------------------+------------------+
| Pattern                   | Time             | Space            |
+---------------------------+------------------+------------------+
| Insert word               | O(m)             | O(m)             |
| Search word               | O(m)             | O(1)             |
| Search prefix             | O(m)             | O(1)             |
| Wildcard search ('.')     | O(m * 26^w)      | O(m) stack       |
| Grid DFS + Trie           | O(r*c * 4^L)     | O(n * m)         |
| Replace words             | O(d + s)         | O(d)             |
+---------------------------+------------------+------------------+

m = word/pattern length, w = number of wildcards in pattern,
r/c = grid rows/cols, L = max word length, n = number of words,
d = total chars in dictionary, s = sentence length

NOTES:
- Insert creates at most m new nodes (one per character)
- Wildcard '.' tries all 26 children at each wildcard position
- Grid DFS: trie pruning stops paths early when no word shares that prefix
- Replace words: build trie O(d), scan each sentence word O(m) -> O(d+s) total
"""

"""
=============
TRIE PATTERNS
=============
"""

class TrieNode:
    def __init__(self):
        self.children = {}   # char -> TrieNode
        self.is_end = False  # True if this node ends a complete word

"""
================================================================
PATTERN 1: BASIC TRIE (INSERT, SEARCH, STARTSWITH)
PATTERN EXPLANATION: The three fundamental operations. Insert: walk the word character
by character, creating new TrieNode children as needed, then mark is_end=True at the
final node. Search: walk the word; return False if any character is missing, True only
if the final node has is_end=True. StartsWith: same as search but don't check is_end —
reaching the end of the prefix without a missing character is sufficient.

Applications: Spell checker, word validator, autocomplete prefix check.
================================================================
"""

class Trie:
    """
    Problem: Implement a Trie with insert, search, and startsWith operations.

    Example:
        trie.insert("apple")
        trie.search("apple")   -> True
        trie.search("app")     -> False  (prefix only, not a complete word)
        trie.startsWith("app") -> True
        trie.insert("app")
        trie.search("app")     -> True

    Steps:
    Insert:
    1. Start at root, traverse one character at a time
    2. If character not in node.children, create a new TrieNode
    3. Move to child node; repeat for all characters
    4. Mark final node as end of word (is_end = True)

    Search:
    1. Traverse the trie following each character
    2. If any character is missing from children -> return False
    3. Return node.is_end at the end (True only for complete words)

    StartsWith:
    1. Same as search but return True once all prefix characters are traversed
    """
    def __init__(self):  # LC 208 - Implement Trie
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """TC: O(m), SC: O(m) — creates at most m new nodes"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        """TC: O(m), SC: O(1)"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        """TC: O(m), SC: O(1)"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    # Trace: insert("apple"), insert("app")
    # Trie: root -> a -> p -> p(is_end=True) -> l -> e(is_end=True)
    # search("app"):     traverse to 2nd 'p'; is_end=True  -> True ✓
    # search("appl"):    traverse to 'l';      is_end=False -> False ✓
    # startsWith("app"): traverse to 2nd 'p'; reached end  -> True ✓

trie = Trie()
trie.insert("apple")
trie.insert("app")
print("search 'apple':", trie.search("apple"))      # True
print("search 'app':", trie.search("app"))          # True
print("startsWith 'app':", trie.startsWith("app"))  # True
print("search 'appl':", trie.search("appl"))        # False


"""
================================================================
PATTERN 2: WORD DICTIONARY WITH WILDCARDS
PATTERN EXPLANATION: Extend basic trie search to support '.' as a wildcard that can
match any single character. When the current character is '.', try every child of the
current node recursively (DFS). For regular characters, follow the specific path as
usual. The recursion base case is reaching the end of the word — return node.is_end.

Applications: Word dictionary with wildcards, regex-like prefix matching.
================================================================
"""

class WordDictionary:
    """
    Problem: Design a data structure that supports addWord and search, where search
    can use '.' as a wildcard that matches any single letter.

    Example:
        addWord("bad"), addWord("dad"), addWord("mad")
        search("pad") -> False
        search(".ad") -> True   (matches "bad", "dad", or "mad")
        search("b..") -> True   (matches "bad")

    Steps:
    1. addWord: same as basic trie insert
    2. search: recursive DFS helper
       a. Base case: index == len(word) -> return node.is_end
       b. If '.': try every child node recursively; return True if any path succeeds
       c. If letter: follow that specific child; return False if missing
    """
    def __init__(self):  # LC 211
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """TC: O(m)"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        """TC: O(m) no wildcards; O(m * 26^w) with w wildcards"""
        return self._dfs(word, 0, self.root)

    def _dfs(self, word: str, index: int, node: TrieNode) -> bool:
        if index == len(word):
            return node.is_end
        char = word[index]
        if char == '.':
            return any(self._dfs(word, index + 1, child) for child in node.children.values())
        if char not in node.children:
            return False
        return self._dfs(word, index + 1, node.children[char])

    # Trace: search(".ad") with trie containing "bad","dad","mad"
    # index=0, char='.': try all root children: 'b','d','m'
    #   'b': _dfs("ad",1,node_b) -> 'a' found -> _dfs("d",2,node_a)
    #         -> 'd' found -> is_end=True ✓
    # Return True ✓

wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")
print("search 'pad':", wd.search("pad"))  # False
print("search '.ad':", wd.search(".ad"))  # True
print("search 'b..':", wd.search("b..")) # True


"""
================================================================
PATTERN 3: WORD SEARCH IN GRID (TRIE + GRID DFS)
PATTERN EXPLANATION: Build a trie from all target words, then run DFS from every cell.
At each DFS step, use the trie to prune paths that cannot lead to any word — if the
current character is not in the trie node's children, stop immediately. When a trie
node's is_end is True, a complete word has been found. Clear is_end after adding to
results to prevent duplicates. Remove exhausted leaf nodes to prune future DFS.

Applications: Word Search II (Boggle), find multiple words in a grid.
================================================================
"""

class WordSearchTrie:
    """
    Problem: Given a 2D board of characters and a list of words, find all words
    that can be formed by sequentially adjacent cells (horizontal/vertical).
    Each cell may be used at most once per word.

    Example:
        board = [['o','a','a','n'],
                 ['e','t','a','e'],
                 ['i','h','k','r'],
                 ['i','f','l','v']]
        words = ["oath","pea","eat","rain"]
        Output: ["eat","oath"]

    Steps:
    1. Build trie from all words; store word string at each end node
    2. DFS from each cell (r, c) with trie root:
       a. If cell char not in trie node's children -> return (pruning)
       b. Move to child trie node; if is_end -> add word to results, clear is_end
       c. Mark cell visited (board[r][c] = '#'), recurse 4 directions, restore cell
       d. If trie node has no children left -> remove it from parent (prune leaf)
    3. Return all found words
    """
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:  # LC 212
        """
        TC: O(m*n * 4^L) where L = max word length (trie pruning reduces practical cost)
        SC: O(k * L) for trie where k = number of words
        """
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            next_node = node.children[char]
            if next_node.is_end:
                result.append(next_node.word)
                next_node.is_end = False     # Prevent duplicate adds

            board[r][c] = '#'               # Mark visited
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)
            board[r][c] = char              # Restore cell

            if not next_node.children:      # Prune exhausted leaf
                del node.children[char]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result

    # Trace: words=["eat"], board has 'e' at (1,0), 'a' at (1,1), 't' at (1,1)...
    # dfs(1,0,root): 'e' in root.children -> move to node_e
    #   board[1][0]='#'; try neighbors
    #   dfs(0,0,node_e): 'o' not in node_e.children -> return (pruned!)
    #   dfs(1,1,node_e): 'a' in node_e.children -> move to node_a
    #     ...eventually finds 'eat' -> result=["eat"] ✓

sol = WordSearchTrie()
board = [['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']]
print("Word Search II:", sol.findWords(board, ["oath","pea","eat","rain"]))


"""
================================================================
PATTERN 4: REPLACE WORDS (SHORTEST PREFIX MATCHING)
PATTERN EXPLANATION: Insert all dictionary roots into a trie. For each word in the
sentence, traverse the trie character by character. The first node encountered with
is_end=True is the shortest root — stop there and use the accumulated prefix as the
replacement. If no root is found as a prefix, keep the original word. This runs in
O(d + s) time where d is total dictionary characters and s is sentence length.

Applications: Replace words with roots, abbreviation matching, shortest prefix queries.
================================================================
"""

class ReplaceWords:
    """
    Problem: Given a dictionary of roots and a sentence, replace each word in the sentence
    with the shortest root from the dictionary that is a prefix of the word.
    If no root is a prefix, keep the original word.

    Example:
        dictionary = ["cat","bat","rat"]
        sentence = "the cattle was rattled by the battery"
        Output: "the cat was rat by the bat"

    Steps:
    1. Build trie from dictionary roots; mark each root's end node with is_end=True
    2. Split sentence into words
    3. For each word, traverse trie character by character:
       a. If current node is_end=True -> found shortest root; use prefix so far
       b. If character not in children -> no root prefix; keep original word
    4. Join replaced words back into sentence
    """
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:  # LC 648
        """
        TC: O(d + s) - build trie O(d), process sentence O(s)
        SC: O(d) - trie stores all dictionary characters
        """
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True

        result = []
        for word in sentence.split():
            node = root
            prefix = []
            replaced = False
            for char in word:
                if char not in node.children:
                    break
                node = node.children[char]
                prefix.append(char)
                if node.is_end:
                    result.append(''.join(prefix))
                    replaced = True
                    break
            if not replaced:
                result.append(word)

        return ' '.join(result)

    # Trace: dictionary=["cat","bat"], sentence="cattle battery"
    # Trie: root->c->a->t(is_end), root->b->a->t(is_end)
    # "cattle": c->a->t (is_end=True!) -> replace with "cat"
    # "battery": b->a->t (is_end=True!) -> replace with "bat"
    # Output: "cat bat" ✓

sol = ReplaceWords()
print("Replace Words:", sol.replaceWords(
    ["cat","bat","rat"], "the cattle was rattled by the battery"))
# "the cat was rat by the bat"
