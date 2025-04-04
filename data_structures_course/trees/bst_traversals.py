class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None: # If tree is empty
            self.root = Node(key) # Create node with key (value) and assign to root
        else: # If tree not empty
            self._insert_recursive(self.root, key) # Call recursive fn
    
    def _insert_recursive(self, node, key): # Takes in root and key (val)
        if key < node.value: # If val we are inserting < root
            if node.left is None: # Check if left slot is open
                node.left = Node(key) # Create new node and assign to left
            else: # If slot not open
                self._insert_recursive(node.left, key) # Recurse left
        else: # If val we are inserting > root
            if node.right is None: # Check if right slot is open
                node.right = Node(key) # Create new node and assign to right
            else: # If slot not open
                self._insert_recursive(node.right, key) # Recurse right
    
    # Process the left subtree first, the the parent node, then the right subtree
    def inorder_traversal(self, node=None): 
        if node is None:
            node = self.root # Set node to the root
        result = [] # Array stores the in order traversal
        if node.left: # If there is a left node
            result += self.inorder_traversal(node.left) # Traverse left first then concatenate lists after returning
        result.append(node.value) # Append curr node after left subtree processed
        if node.right: # If there is a right node
            result += self.inorder_traversal(node.right) # Traverse right first and concatenate lists after returning
        return result # Return result array to prev call stack (concatenate lists)
    

    # Process the node first, then it's left, then it's right subtrees
    def preorder_traversal(self, node=None):
        if node is None:
            node = self.root # Set node to the root
        result = [node.value] # Process current node first
        if node.left: # If there is a left node
            result += self.preorder_traversal(node.left) # Traverse left and concatenate lists after returning (add curr node to front)
        if node.right: # If there is a right node
            result += self.preorder_traversal(node.right) # Traverse right and concatenate lists after returning (add current node to front)
        return result # Return result arr to prev call stack
    
    #         10
    #        /  \
    #       /    \
    #      5     15
    #     / \
    #    2   7
    #
    
    # Process left and right subtrees first, then parent node
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root # Set node to root
        result = [] # Create empty results arr
        if node.left: # Keep going left
            result += self.postorder_traversal(node.left) # Traverse left and concatenate lists
        if node.right: # Then go right
            result += self.postorder_traversal(node.right) # Traverse right and concatenate lists
        result.append(node.value) # Process current node after l and r subtrees processed
        return result
    
    def search(self, key):
        return self._search_recursive(self.root, key) # Call fn with root & key
    
    def _search_recursive(self, node, key):
        if node is None or node.value == key: # Check is curr node is none or if the curr node is the node we are searching for
            return node
        if key < node.value: # If node we are search for is less than curr node
            return self._search_recursive(node.left, key) # Recurse left
        return self._search_recursive(node.right, key) # Recurse right

# Example usage
bt = BinarySearchTree()
bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(2)
bt.insert(7)

#         10
#        /  \
#       /    \
#      5     15
#     / \
#    2   7
#

print("Inorder Traversal:", bt.inorder_traversal())
print("Preorder Traversal:", bt.preorder_traversal())
print("Postorder Traversal:", bt.postorder_traversal())
print("Search for 7:", bt.search(7) is not None)
print("Search for 20:", bt.search(20) is not None)