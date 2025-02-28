"""
📌 Hash Table Implementation in Python (Using Separate Chaining)

Preventing Collisions 
- Chaining: placing all the elements that hash into the same hash value to the same linked list


🔹 This implementation provides:
    - `put(key, value)`: Insert or update a key-value pair.
    - `get(key)`: Retrieve a value based on the key.
    - `_hash(key)`: Generates a hash for a given key.
    - Uses **separate chaining** to handle collisions.

🔹 Time Complexity:
    - **Best Case:** O(1) (No collisions, direct access)
    - **Worst Case:** O(n) (All elements in one bucket due to hash collisions)
    - **Average Case:** O(1) for well-distributed keys
"""

class HashTable:
    def __init__(self, size=10):
        """
        Initialize the hash table with a fixed number of buckets (default: 10).
        Each bucket is a list to handle collisions via separate chaining.
        """
        self.size = size
        self.table = [[] for _ in range(size)]  # Create a list of empty lists (buckets)

    def _hash(self, key):
        """
        Generate a hash for a given key.
        Uses Python's built-in `hash()` function and modulo operation
        to ensure the hash falls within the range [0, size-1].
        """
        return hash(key) % self.size

    def put(self, key, value):
        """
        Insert a key-value pair into the hash table.
        If the key already exists, update its value.
        """
        hashed_key = self._hash(key)  # Compute hash index
        bucket = self.table[hashed_key]  # Locate the correct bucket

        # Check if key already exists, and update its value if found
        for index, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[index] = (key, value)  # Update value
                return

        # If key does not exist, add it to the bucket
        bucket.append((key, value))

    def get(self, key):
        """
        Retrieve a value by its key.
        Returns None if the key does not exist.
        """
        hashed_key = self._hash(key)  # Compute hash index
        bucket = self.table[hashed_key]  # Locate the correct bucket

        # Search for the key in the bucket
        for existing_key, value in bucket:
            if existing_key == key:
                return value  # Return the associated value

        return None  # Return None if key is not found

# =========================
# 🔹 Example Usage
# =========================
if __name__ == "__main__":
    # Create a hash table
    hash_table = HashTable(size=5)  # Small size to force collisions

    # Insert values
    hash_table.put("name", "Alice")
    hash_table.put("age", 25)
    hash_table.put("city", "New York")

    # Retrieve values
    print("Name:", hash_table.get("name"))  # Output: Alice
    print("Age:", hash_table.get("age"))    # Output: 25
    print("City:", hash_table.get("city"))  # Output: New York

    # Update existing key
    hash_table.put("age", 26)
    print("Updated Age:", hash_table.get("age"))  # Output: 26

    # Retrieve a non-existent key
    print("Country:", hash_table.get("country"))  # Output: None
