# Red Black Trees are balanced binary search trees, that guarentee all tree operations have run time of O(log n) in the worst case. Red Black trees achieve this efficient run time by storing additional information, the color of a node, which can be either red of Black
"""
📌 Implementation of a Red-Black Tree in Python

🔹 Red-Black Tree Properties:
   1️⃣ Every node is either **Red** or **Black**.
   2️⃣ The root is always **Black**.
   3️⃣ Red nodes **cannot** have red children (**No Red-Red violation**).
   4️⃣ Every path from a node to its leaves must have the **same number of Black nodes**.
   5️⃣ A newly inserted node is **always Red**.

🔹 Key Operations:
    - `insert(value)`: Inserts a node and rebalances the tree.
    - `search(value)`: Searches for a node.
    - `find_min()`, `find_max()`: Finds the smallest/largest value.
    - `in_order_traversal()`: Displays elements in sorted order.
    - 'fix_insert()': When we insert a node we must maintain the Red Black Tree Properties -> if we insert a child (Red) where the parent is Red, we get a Red-Red violation
"""

# Red-Black Tree Node Class
class Node:
    def __init__(self, value, color="R"):
        """
        Initializes a new Node with a given value and color (default is Red).
        """
        self.value = value
        self.color = color  # "R" for Red, "B" for Black
        self.left = None
        self.right = None
        self.parent = None

# Red-Black Tree Class
class RedBlackTree:
    def __init__(self):
        """
        Initializes an empty Red-Black Tree with a `None` root.
        """
        self.NIL = Node(value=None, color="B")  # Sentinel NIL node (Special Node to rep None)
        self.root = self.NIL  # Initially, the tree is empty

    def search(self, value):
        """
        Searches for a node with the given value.
        Returns the node if found, otherwise returns None.
        """
        current = self.root
        while current != self.NIL and current.value != value:
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return current if current != self.NIL else None

    def find_min(self):
        """
        Returns the node with the smallest value in the tree.
        """
        current = self.root
        while current.left != self.NIL:
            current = current.left
        return current

    def find_max(self):
        """
        Returns the node with the largest value in the tree.
        """
        current = self.root
        while current.right != self.NIL:
            current = current.right
        return current

    def left_rotate(self, x):
        """
        Performs a left rotation around node `x`.
        """
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        """
        Performs a right rotation around node `y`.
        """
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, value):
        """
        Inserts a new value into the Red-Black Tree and fixes violations.
        """
        new_node = Node(value)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None # Keep track of parent (stores last valid node before hitting NIL)
        current = self.root # Start at the root

        while current != self.NIL: # Loop stops once we find NIL node (missing child)
            parent = current
            if new_node.value < current.value: # If new node's value is smaller
                current = current.left # Move left
            else:
                current = current.right # Else move right

        new_node.parent = parent # Establish parent child relationship
        if parent is None: # Check if tree is empty
            self.root = new_node  # New node becomes root
        elif new_node.value < parent.value: # Attach new node as Child
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = "R"  # New nodes are always Red
        self.fix_insert(new_node)

    def fix_insert(self, node):
        """
        Fixes Red-Black Tree violations after insertion.
        """
        # After inserting red, loop while parent == Red
        while node.parent and node.parent.color == "R": 
            if node.parent == node.parent.parent.left: # Parent's Uncle is Red
                uncle = node.parent.parent.right
                if uncle.color == "R":  # Case 1: Uncle is Red
                    node.parent.color = "B"
                    uncle.color = "B"
                    node.parent.parent.color = "R"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:  # Case 2: Node is right child
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "B"  # Case 3: Uncle is Black
                    node.parent.parent.color = "R"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "R":  # Mirror Case 1
                    node.parent.color = "B"
                    uncle.color = "B"
                    node.parent.parent.color = "R"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:  # Mirror Case 2
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "B"  # Mirror Case 3
                    node.parent.parent.color = "R"
                    self.left_rotate(node.parent.parent)

        self.root.color = "B"  # Root must always be black

    def in_order_traversal(self, node):
        """
        Performs in-order traversal (Left → Root → Right).
        """
        if node != self.NIL:
            self.in_order_traversal(node.left)
            print(f"({node.value}, {node.color})", end=" ")
            self.in_order_traversal(node.right)

    def display(self):
        """
        Prints the Red-Black Tree using in-order traversal.
        """
        print("Red-Black Tree (In-Order): ", end="")
        self.in_order_traversal(self.root)
        print("\n")


# =========================
# 🔹 Example Usage
# =========================
if __name__ == "__main__":
    rbt = RedBlackTree()

    # Insert values into the Red-Black Tree
    for value in [20, 15, 25, 10, 5, 1, 30, 35]:
        rbt.insert(value)

    # Display the tree
    rbt.display()

    # Search for elements
    print("Searching for 15:", rbt.search(15) is not None)  # ✅ True
    print("Searching for 40:", rbt.search(40) is not None)  # ❌ False

    # Find min and max values
    min_node = rbt.find_min()
    max_node = rbt.find_max()
    print("Minimum Value:", min_node.value if min_node else "Tree is empty")  # Expected: 1
    print("Maximum Value:", max_node.value if max_node else "Tree is empty")  # Expected: 35

# Expected Output:
# Red-Black Tree (In-Order): (1, R) (5, B) (10, R) (15, B) (20, B) (25, B) (30, R) (35, B) 

# Searching for 15: True
# Searching for 40: False
# Minimum Value: 1
# Maximum Value: 35