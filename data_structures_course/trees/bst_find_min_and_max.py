class Node:
    def __init__(self, value):
        self.value = value  # Each node has a value
        self.left = None  # Pointer to left child
        self.right = None  # Pointer to right child

class BinarySearchTree:
    def __init__(self):
        self.root = None  # Initialize root to None

    def __r_insert(self, current, value):
        """ Recursively inserts a value into the BST. """
        if current is None:  # Base case
            return Node(value)  # Create a new node
        if value < current.value:  # If value is smaller, go left
            current.left = self.__r_insert(current.left, value)
        elif value > current.value:  # If value is larger, go right
            current.right = self.__r_insert(current.right, value)
        return current  # Duplicates will just return

    def r_insert(self, value):
        """ Public insert method to handle the empty tree case. """
        if self.root is None:  # If tree is empty, set root
            self.root = Node(value)
        else:
            self.__r_insert(self.root, value)

    def __r_contains(self, current, value):
        """ Recursively checks if a value exists in the BST. """
        if current is None:
            return False  # Value not found
        if value == current.value:
            return True  # Value found
        if value < current.value:
            return self.__r_contains(current.left, value)  # Search left
        return self.__r_contains(current.right, value)  # Search right

    def r_contains(self, value):
        """ Public method to check if the tree contains a value. """
        return self.__r_contains(self.root, value)

    def find_min(self):
        """ Returns the node with the smallest value in the BST. """
        current = self.root
        while current and current.left:
            current = current.left  # Keep going left
        return current

    def find_max(self):
        """ Returns the node with the largest value in the BST. """
        current = self.root
        while current and current.right:
            current = current.right  # Keep going right
        return current


# =========================
# 🔹 Example Usage
# =========================
my_tree = BinarySearchTree()  # Create a BST instance

# Insert nodes
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

# Search for values
print('BST Contains 27:', my_tree.r_contains(27))  # ✅ True
print('BST Contains 17:', my_tree.r_contains(17))  # ❌ False

# Find Min & Max
min_node = my_tree.find_min()
max_node = my_tree.find_max()

print('Minimum value in BST:', min_node.value if min_node else "Tree is empty")  # Expected: 18
print('Maximum value in BST:', max_node.value if max_node else "Tree is empty")  # Expected: 82
