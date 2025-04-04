"""
📌 Hash Table Implementation using Open Addressing (Linear Probing) - each table entry contains either an element, or a null -> we store a single list

🔹 Features:
    - `insert(key)`: Inserts a key using linear probing -> we successively probe the hash table until we find an empty slot in which to put the key
        - Best case time complexity: O(1) -> if there is no collision, we place the key directly into it's hashed index
        - Average case time complexity: O(1) -> a well distributed hash function ensures few collisions, leading to few probes before finding an empty slot
        - Worst case: O(n) -> if many elements collide into the same cluster, we may have to probe the entire table before finding an empty slot
        - Brute force: O(n) -> scan the entire list for duplicates before inserting
    - `search(key)`: Searches for a key in the hash table -> probe the same sequence of slots that the insertion algorithm examined
        - Best case time complexity: O(1) -> if no collision happened, the key is found at it's hashed index immediately
        - Average case time complexity: O(1) -> with a low load factor, a few probes might be needed to locate the key
        - Worst case time complexity: O(n) -> if keys are clustered, we might need to probe n-1 slots before finding the key or confirming it's missing
        - Brute force: O(n) -> scan through the entire list to find the key
    - `delete(key)`: Deletes a key (marks it as "DELETED")
        - Best case time complexity: O(1) -> if the key is at it's expected index, it's marked "DELETED" instantly
        - Average case time complexity: O(1) -> with a well distributed hash function, deletion required few probes
        - Worst case time complexity: O(n) -> if clustering is bad, we may have to scan through many slots to find the key
        - Brute force: O(n) -> scan through the entire list to find and remove the key O(n)

🔹 Linear Probing:
    - If a collision occurs, probe the next available slot.
    - If the table is full, insertion fails.
    - Deleted keys are marked as `"DELETED"` to preserve search sequence
    - If we earlier had a collision and marked the key as None instead of "Deleted", we would hit none in our search sequence before we found our ele

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

        # Linear probing: Find next available slot -> look in table at index i
        while self.table[(index + i) % self.size] not in (None, self.deleted): # See if ele in list is None or "deleted"
            i += 1 # Move to next open slot
            if i == self.size:  # If table is full
                print(f"Error: Hash table is full. Cannot insert {key}.")
                return
        
        self.table[(index + i) % self.size] = key  # Insert key at that index or next open spot

    def search(self, key):
        """
        Searches for a key using linear probing.
        Returns the index if found, else None.
        """
        index = self._hash(key) # Find original hashed index for that key
        i = 0

        # Linear probing: Search for the key
        while self.table[(index + i) % self.size] is not None: # Continue until loop hits none (if collision happened, key would be inserted before None)
            if self.table[(index + i) % self.size] == key: # See if ele at that index == key passed in
                return f"Found {key} at index {(index + i) % self.size}"
            i += 1 # Move to next index (collision must have happened)
            if i == self.size:  # If table is full cycle
                break
        
        return f"{key} not found"

    def delete(self, key):
        """
        Deletes a key using linear probing.
        Instead of removing it, marks the slot as "DELETED" to maintain search sequence.
        """
        index = self._hash(key) # Find original hashed index for that key
        i = 0

        while self.table[(index + i) % self.size] is not None: # Loop until you hit None
            if self.table[(index + i) % self.size] == key: # If you find the key
                self.table[(index + i) % self.size] = self.deleted # Mark element as 'DELETED'
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
    ht = LinearProbingHashTable(size=5)

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
    print(ht.search(12))
    print(ht.search(26))
    print(ht.search(17))
    print(ht.search(90))

    # Delete an element
    print("❌ Deleting key: 26")
    print(ht.delete(26))  # Expected: Deleted
    ht.display()

    # Insert a new element after deletion
    print("🔹 Inserting key: 99 (after deletion)")
    ht.insert(99)
    ht.display()
