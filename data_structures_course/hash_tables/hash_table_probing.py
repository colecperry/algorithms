"""
📌 Hash Table Implementation using Open Addressing (Linear Probing)

🔹 Features:
    - `insert(key)`: Inserts a key using linear probing.
    - `search(key)`: Searches for a key in the hash table.
    - `delete(key)`: Deletes a key (marks it as "DELETED"). 

🔹 Linear Probing:
    - If a collision occurs, probe the next available slot.
    - If the table is full, insertion fails.
    - Deleted keys are marked as `"DELETED"` to preserve search sequence
    - If we earlier had a collision and marked the key as None instead of "Deleted", we would hit none in our search sequence before we found our ele

🔹 Time Complexity:
   - **Best Case:** O(1) (Direct placement)
   - **Worst Case:** O(n) (Full table, worst clustering)
   - **Average Case:** O(1) with a low load factor

"""

class LinearProbingHashTable:
    def __init__(self, size=7):
        """
        Initializes the hash table with a fixed size.
        Uses `None` for empty slots and "DELETED" for deleted keys.
        """
        self.size = size
        self.table = [None] * size
        self.deleted = "DELETED"

    def _hash(self, key):
        """
        Hash function: Computes an index using modulo operation.
        """
        return key % self.size

    def insert(self, key):
        """
        Inserts a key using linear probing.
        If a collision occurs, finds the next available slot.
        """
        index = self._hash(key)  # Compute initial index
        i = 0  # Probing counter

        # Linear probing: Find next available slot
        while self.table[(index + i) % self.size] not in (None, self.deleted): # See if it's in Tuple or basically if it's == None
            i += 1
            if i == self.size:  # If table is full
                print(f"Error: Hash table is full. Cannot insert {key}.")
                return
        
        self.table[(index + i) % self.size] = key  # Insert key

    def search(self, key):
        """
        Searches for a key using linear probing.
        Returns the index if found, else None.
        """
        index = self._hash(key)
        i = 0

        # Linear probing: Search for the key
        while self.table[(index + i) % self.size] is not None:
            if self.table[(index + i) % self.size] == key:
                return f"Found {key} at index {(index + i) % self.size}"
            i += 1
            if i == self.size:  # If table is full cycle
                break
        
        return f"{key} not found"

    def delete(self, key):
        """
        Deletes a key using linear probing.
        Instead of removing it, marks the slot as "DELETED" to maintain search sequence.
        """
        index = self._hash(key)
        i = 0

        while self.table[(index + i) % self.size] is not None:
            if self.table[(index + i) % self.size] == key:
                self.table[(index + i) % self.size] = self.deleted
                return f"{key} deleted"
            i += 1 # Due to collision, ele may be at next idx
            if i == self.size:  # If table is full cycle
                break
        
        return f"{key} not found"

    def display(self):
        """
        Prints the current state of the hash table.
        """
        print("\nHash Table:")
        for index, value in enumerate(self.table):
            print(f"Index {index}: {value}")
        print("\n")

# =========================
# 🔹 Example Usage
# =========================
if __name__ == "__main__":
    ht = LinearProbingHashTable(size=7)

    # Insert elements
    print("🔹 Inserting keys: 12, 26, 31, 17, 90")
    ht.insert(12)
    ht.insert(26)
    ht.insert(31)
    ht.insert(17)
    ht.insert(90)
    ht.display()

    # Search for elements
    print("🔍 Searching for keys: 31, 99")
    print(ht.search(31))  # Expected: Found at index
    print(ht.search(99))  # Expected: Not found

    # Delete an element
    print("❌ Deleting key: 26")
    print(ht.delete(26))  # Expected: Deleted
    ht.display()

    # Insert a new element after deletion
    print("🔹 Inserting key: 99 (after deletion)")
    ht.insert(99)
    ht.display()
