# 208. Implement Trie (Prefix Tree)

# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:
    # - Trie() Initializes the trie object.
    # - void insert(String word) Inserts the string word into the trie.
    # - boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    # - boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

# Example 1:
    # Input
    # ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    # [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    # Output
    # [null, null, true, false, true, null, true]

    # Explanation
    # Trie trie = new Trie();
    # trie.insert("apple");
    # trie.search("apple");   // return True
    # trie.search("app");     // return False
    # trie.startsWith("app"); // return True
    # trie.insert("app");
    # trie.search("app");     // return True

class Trie:

    def __init__(self):
        self.children = {}  # dict that stores next letters where the key=char and the value=Trie (node that char leads to)
        self.is_end = False # flag tells us whether this node marks the end of a complete word
    
    def insert(self, word):
        # STEP 1: Start from root -> TrieNode we made with __init__
        node = self
        
        # STEP 2: Create path for each character
        for char in word:
            if char not in node.children:  # Check if that letter is in the children
                node.children[char] = Trie()  # If not, add the letter to the dict (create new node)
            node = node.children[char]  # Move to next node
        
        # STEP 3: Mark end of word
        node.is_end = True
    
    def search(self, word):
        # STEP 1: Traverse to end of word
        node = self  # Start at root node
        for char in word:
            if char not in node.children:  # Check if char is there
                return False
            node = node.children[char]  # Move to next node
        
        return node.is_end  # Verify it's a complete word (not just prefix)
    
    def startsWith(self, prefix):
        # STEP 1: Traverse the prefix
        node = self  # Start at root node
        for char in prefix:
            if char not in node.children:  # Check if char is there
                return False
            node = node.children[char]  # Move to next node
        
        return True  # Prefix exists if we successfully traversed
        


trie = Trie()
print(trie.insert("apple"))
print(trie.search("apple")) # True
print(trie.search("app"))   # False
print(trie.startsWith("app")) # True
print(trie.insert("app"))
print(trie.search("app"))   # True
