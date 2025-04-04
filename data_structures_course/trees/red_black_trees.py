# Red-Black Trees are balanced binary search trees, that guarentee all tree operations have a run time of O(log(n)) in the worst case. Red Black trees achieve this efficient run time by storing additional information, the color of a node, which can be either red or black. They must satisfy the following conditions:
    # - Every node in the tree is either red or black
    # - The root is black
    # - Every leaf (NIL node) is black
    # - If a node is red, then both it's children are black (no consecutive red nodes)
    # - For every node, all simple paths from the node to it's descendant leaves contain the same number of black nodes

# Left pivot visually -> used when the right child of a node is causing a violation

    # Before left rotation              After left rotation
    #        10 (Black)                           20 (Black)
    #          \                                /    \
    #          20 (Red)                        10(R) 30(R)
    #            \                              
    #            30 (Red)                      
    #
# Steps:
# 1. Pivot Node = 10  (The node being rotated)
# 2. New Parent = 20  (Right child of pivot node 10, moves up)
# 3. Middle Subtree = None  (There is no middle subtree in this case)
# 4. Update parent links:
#    - 20 takes 10's place as the new root.
#    - 10 moves down as the left child of 20.
#    - 30 remains as the right child of 20.
# 5. Recolor to restore Red-Black properties:
#    - 20 becomes Black.
#    - 10 and 30 become Red.

# Right pivot visually -> used when the left child of a node is causing a violation
    # Before right rotation              After left rotation
    #         20(B)                            10(B)
    #        /                                /    \
    #       10(R)                           5(R)  20(R)
    #      /                                     
    #     5(R)                                    
    #
# Steps:
# 1. Pivot Node = 20  (The node being rotated)
# 2. New Parent = 10  (Left child of pivot node 20, moves up)
# 3. Middle Subtree = None  (There is no middle subtree in this case)
# 4. Update parent links:
#    - 10 takes 20's place as the new root.
#    - 20 moves down as the right child of 10.
#    - 5 remains as the left child of 10.
# 5. Recolor to restore Red-Black properties:
#    - 10 becomes Black.
#    - 5 and 20 become Red.


import random

class Node:
    def __init__(self, value, color="red", parent=None):
        """
        Initializes a node with a given value, color (default is red), and parent reference.
        """
        self.value = value
        self.color = color  # Nodes can be "red" or "black"
        self.left = None
        self.right = None
        self.parent = parent

class RedBlackTree:
    def __init__(self):
        """
        Initializes a Red-Black Tree with a sentinel NIL node (representing null leaves) -> every leaf node in must be black (Red-Black Tree property).
        """
        self.NIL = Node(value=None, color="black")  # Sentinel NIL node represents leaf node
        self.root = self.NIL  # Root starts as NIL

    def insert(self, value):
        """
        Inserts a new node into the Red-Black Tree while maintaining balance properties.
        """
        new_node = Node(value, color="red", parent=None) # New nodes initialized to red
        new_node.left = self.NIL  # Initially, set left child to NIL
        new_node.right = self.NIL  # Initially, set right child to NIL

        # Locate the correct position for the new node
        parent = None
        current = self.root # set ptr to root
        while current != self.NIL: # loop until we hit NIL node
            parent = current # Update parent before traversing
            if value < current.value: # If val we are inserting < curr's val
                current = current.left  # Move left
            elif value > current.value: # If val we are inserting > curr's val
                current = current.right  # Move right
            else:
                print(f"Duplicate value {value} ignored.")  # Ignore duplicates
                return

        # Attach the new node to the correct parent
        new_node.parent = parent # Set the new node's parent 
        if parent is None: # If the node is the root
            self.root = new_node  # First node inserted becomes the root
        elif value < parent.value: # Choose direction to attach node based on val
            parent.left = new_node
        else:
            parent.right = new_node

        # Fix any Red-Black Tree property violations
        self.insert_fixup(new_node)

    
    def insert_fixup(self, node):
        """
        Fixes Red-Black Tree violations after insertion.
        """
        while node.parent and node.parent.color == "red":
            if node.parent == node.parent.parent.left:  # Parent is left child of grandparent
                uncle = node.parent.parent.right  # Get the uncle node
                if uncle.color == "red":  # Case 1: Uncle is red -> recolor
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent  # Move up to check further violations
                else:
                    if node == node.parent.right:  # Case 2: Node is right child -> Left rotate
                        node = node.parent
                        self.left_rotate(node)
                    # Case 3: Node is left child -> Right rotate
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.right_rotate(node.parent.parent)
            else:  # Parent is right child of grandparent (mirror case)
                uncle = node.parent.parent.left # Get uncle node
                if uncle.color == "red":  # Case 1: Uncle is red -> recolor
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent  # Move up
                else: 
                    if node == node.parent.left:  # Case 2: Node is left child -> Right rotate
                        node = node.parent
                        self.right_rotate(node)
                    # Case 3: Node is right child -> Left rotate
                    node.parent.color = "black" # Set node's parent to black
                    node.parent.parent.color = "red" # Set node's grandparent to red
                    self.left_rotate(node.parent.parent)

        # Ensure the root is always black
        self.root.color = "black"

    def left_rotate(self, pivot_node):
        """
        Performs a left rotation on the given node (pivot_node).
        The right child moves up to take the place of the pivot node, the pivot node moves down to become the left child of the new root, and if the right child had a left subtree, it gets reassigned to the pivot node.
        """
        new_parent = pivot_node.right  # Step 1: Right child becomes the new parent of subtree
        
        middle_subtree = new_parent.left  # Step 2: Middle subtree (new_parent's left child)
        pivot_node.right = middle_subtree  # Step 3: Move middle subtree to pivot's right
        if middle_subtree != self.NIL:
            middle_subtree.parent = pivot_node  # Step 4: Update parent reference for middle_subtree
        
        new_parent.parent = pivot_node.parent  # Step 5: Update new parent's parent reference
        if pivot_node.parent is None:  # Step 6: If pivot_node was root, update root to new_parent
            self.root = new_parent
        elif pivot_node == pivot_node.parent.left:
            pivot_node.parent.left = new_parent  # Step 7: Update parent's left child if pivot_node was a left child
        else:
            pivot_node.parent.right = new_parent  # Step 8: Update parent's right child if pivot_node was a right child

        new_parent.left = pivot_node  # Step 9: Move pivot_node below new_parent as its left child
        pivot_node.parent = new_parent  # Step 10: Update pivot_node's parent reference


    def right_rotate(self, pivot_node):
        """
        Performs a right rotation on the given node (pivot_node).
        The left child moves up to take the place of the pivot node, the pivot node moves down to become the right child of the new root, and if the left child had a right subtree, it gets reassigned to the pivot node.
        """
        new_parent = pivot_node.left  # Step 1: Left child becomes the new parent of subtree
        
        middle_subtree = new_parent.right  # Step 2: Middle subtree (new_parent's right child)
        pivot_node.left = middle_subtree  # Step 3: Move middle subtree to pivot's left
        if middle_subtree != self.NIL:
            middle_subtree.parent = pivot_node  # Step 4: Update parent reference for middle_subtree
        
        new_parent.parent = pivot_node.parent  # Step 5: Update new parent's parent reference
        if pivot_node.parent is None:  # Step 6: If pivot_node was root, update root to new_parent
            self.root = new_parent
        elif pivot_node == pivot_node.parent.right:
            pivot_node.parent.right = new_parent  # Step 7: Update parent's right child if pivot_node was a right child
        else:
            pivot_node.parent.left = new_parent  # Step 8: Update parent's left child if pivot_node was a left child

        new_parent.right = pivot_node  # Step 9: Move pivot_node below new_parent as its right child
        pivot_node.parent = new_parent  # Step 10: Update pivot_node's parent reference


    def print_tree(self, node, indent="", last=True):
        """
        Prints the tree in a readable format.
        """
        if node != self.NIL:
            print(indent + ("└── " if last else "├── ") + f"{node.value} ({node.color})")
            indent += "    " if last else "│   "
            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)


# TESTING ALL EDGE CASES
print("\n### TESTING RED-BLACK TREE ###\n")

rbt = RedBlackTree()

# 1. Insert single value (edge case: tree with one node)
print("\n### Inserting a Single Value (Root Case) ###\n")
rbt.insert(50)
rbt.print_tree(rbt.root)

# 2. Insert multiple values in ascending order (forcing rotations)
print("\n### Inserting Ascending Order (Forces Rotations) ###\n")
for value in [60, 70, 80]:
    rbt.insert(value)
    rbt.print_tree(rbt.root)

# 3. Insert multiple values in descending order (forcing rotations)
print("\n### Inserting Descending Order (Forces Rotations) ###\n")
for value in [40, 30, 20]:
    rbt.insert(value)
    rbt.print_tree(rbt.root)

# 4. Insert random values
print("\n### Inserting Random Values ###\n")
random_values = random.sample(range(1, 100), 5)
for value in random_values:
    rbt.insert(value)
rbt.print_tree(rbt.root)

# 5. Insert duplicate values (should be ignored)
print("\n### Inserting Duplicates (Should be Ignored) ###\n")
rbt.insert(50)
rbt.insert(30)
rbt.print_tree(rbt.root)

print("\n### TESTING COMPLETED ###\n")

