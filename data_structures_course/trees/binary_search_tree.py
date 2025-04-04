# Binary Search Tree - a tree where nodes are organized in a sorted order to make it easier to search. At every node, you are guarenteed that all nodes rooted at the left child are smaller than the current node value, and all nodes rooted at the right child are greater than the current node value

class Node:
    def __init__(self, value, parent=None): # Each node tracks val, l, r, parent
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, value):
        return self._search(self.root, value)
    
    def _search(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)
    
    def search_iterative(self, value):
        current = self.root
        while current is not None and current.value != value:
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return current
    
    # Min node is always the left most node b/c the left subtree always contains values less than parent node
    def find_min(self):
        current = self.root
        while current and current.left: # Iterate left until before None
            current = current.left
        return current
    
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    # Max node is always the right most node b/c the right subtree always contains values greater than parent node
    def find_max(self):
        current = self.root # Set current ptr
        while current and current.right: # Iterate right to before None
            current = current.right # Move right
        return current
    
    def _find_max(self, node):
        while node.right:
            node = node.right
        return node
    
    # A node’s successor is the smallest value greater than the node.
        # If the node has a right subtree → The successor is the leftmost (smallest) node in the right subtree.
        # If the node has no right subtree → The successor is the first ancestor where the node is in the left subtree.
    def find_successor(self, node):
        if node.right:
            return self._find_min(node.right)
        parent = node.parent # Get parent node
        while parent and node == parent.right: # Iterate until node in L subtree
            node = parent # Move node up
            parent = parent.parent # Move parent up
        return parent
    
        #               50
        #             /   \
        #            /     \
        #           30     70
        #          /  \   /  \
        #         20  40 60  80
        #
    
    # A predecessor is the largest value smaller than the given node's value
        # If the node has a left subtree, the predecessor is the maximum node in that left subtree 
        # If the node has no left subtree, the predecessor is the first ancestor where the node is in the right subtree 
    def find_predecessor(self, node): # Pass in node you want predecessor to
        if node.left: # check if node has left subtree
            return self._find_max(node.left) # Find max in left subtree
        parent = node.parent # Get node's parent
        while parent and node == parent.left: # Iterate until node is in R subtree
            node = parent # Set curr node to parent
            parent = parent.parent # Move parent node up (Iterate up the tree)
        return parent # Return the parent node (first ancestor in R subtree)
    
    #               50
    #             /   \
    #            /     \
    #           30     70
    #          /  \   /  \
    #         20  40 60  80
    #
    
    def insert(self, value):
        if self.root is None: # If no root
            self.root = Node(value) # Create new node and set to root
        else: 
            self._insert(self.root, value) # Call _insert()

    def _insert(self, current, value): # Recursive
        if value < current.value: # Compare val for new node to current node
            if current.left is None: # If left spot open
                current.left = Node(value, current) # Set node->l, parent->curr
            else: # Recurse left
                self._insert(current.left, value)
        else: # If val for insert > curr node val
            if current.right is None: # If right spot open
                current.right = Node(value, current) # Set node->r, parent->curr
            else: # Recurse right
                self._insert(current.right, value)

    def insert_iterative(self, value):
        current = self.root # Set current ptr to root
        parent = None
        while current is not None: # Loop until None
            parent = current # Keep track of parent before we move left or right
            if value < current.value: # If val <
                current = current.left # Move left
            else: # If val >
                current = current.right # Move right
        
        new_node = Node(value, parent) # Create new node with val&parent
        if parent is None: # Edge case for root
            self.root = new_node
        elif value < parent.value: # Decide connection from parent
            parent.left = new_node # Connect NN to left
        else:
            parent.right = new_node # Connect NN to right

    # Three cases:
        # If node node we are removing has no children -> simply remove it by modifying it's parents
        # If node we're removing has one child, we elevate it's child to take it's position
        # If node we're removing has two children, we need to find node it's successor
    def delete(self, value):
        node = self.search(value) # Get the actual node
        if node is None:
            return
        
        if node.left is None and node.right is None: # Leaf node
            self._transplant(node, None)
        elif node.left is None: # One right child
            self._transplant(node, node.right) # Swap node with right child
        elif node.right is None: # One left child
            self._transplant(node, node.left) # Swap node with left child
        else: # two children
            successor = self._find_min(node.right) # Find the successor
            if successor.parent != node:
                self._transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self._transplant(node, successor) # Swap node to delete with successor
            successor.left = node.left # Connect new node's left
            successor.left.parent = successor
            #
            #                 50
            #              /      \
            #             /        \
            #            /          \
            #           30          70
            #          /  \        /  \
            #         20  40      60  80
            #          \         /
            #           25      55
            #
    # target node is node we are removing
    def _transplant(self, target_node, replacement_node):
        if target_node.parent is None: # target == root
            self.root = replacement_node
        elif target_node == target_node.parent.left: # If node to remove is parent's left node
            target_node.parent.left = replacement_node # Update connection
        else: # If node to remove is parent's right node
            target_node.parent.right = replacement_node # Replace node
        if replacement_node is not None: # Update parent of replacement node
            replacement_node.parent = target_node.parent

    def print_sorted(self):
        self._in_order_traversal(self.root)
        print()

    def _in_order_traversal(self, node):
        if node is not None:
            self._in_order_traversal(node.left)
            print(node.value, end=' ')
            self._in_order_traversal(node.right)

# Example usage:
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert_iterative(80)

bst.print_sorted()  # Output: 20 30 40 50 60 70 80

max = bst.find_max() 
print(f"Maximum value in the given tree is:", max.value) # Output = 80

node_40 = bst.search(40)
node_50 = bst.search(50)
node_60 = bst.search(60)

pred = bst.find_predecessor(node_50) # Case 1 
pred2 = bst.find_predecessor(node_60) # Case 2

suc = bst.find_successor(node_50) # Case 1
suc2 = bst.find_successor(node_40) # Case 2

bst.insert_iterative(25)
print("BST after iterative addition")
bst.print_sorted()

bst.insert(55)
print("BST after recursive addition")
bst.print_sorted()

bst.delete(25) # Case 1 -> no childeren
print("BST after deletion of node 25")
bst.print_sorted()

bst.delete(60) # Case 2 -> one child
print("BST after deletion of node 60")
bst.print_sorted()

bst.delete(70) # Case 3 -> two children

