"""
📌 Hash Table Implementation in Python (Using Separate Chaining) -> we store lists for each index inside a list

Preventing Collisions 
- Chaining: placing all the elements that hash into the same hash value to the same linked list
- Load factor = (number of items in a hash table / total number of slots)


🔹 This implementation provides:
    - `put(key, value)`: Insert or update a key-value pair.
        - Best case time complexity: O(1) where the hash function distributes keys evenly across buckets
        - Worst case time complexity: O(n) where all keys hash to the same bucket resulting in high collisions, insertion results in searching through the entire bucket to check if that key already exists (preventing duplicate keys or overwriting values fot the same key) before adding the key value pair
        - Average case time complexity: O(1) where we have a hash function resulting in even distribution and few collisions
        - Brute force (without hashing) would require us to check for duplicate keys, or if we don't care about duplicates, we can insert at the end of the list
    - `get(key)`: Retrieve a value based on the key.
        - Best case time complexity: O(1) the key hashes directly to an empty bucket or single entry bucket, finding it immediately
        - Worst case time complexity: O(n) if all the elements hash to the same bucket meaning we scan through all n elements
        - Average case time complexity: O(1) in a well balanced hash table keys are evenly distributed across buckets
        - Brute force (without hashing): O(n) to find a key we must iterate through every element in the list, and if the key is near the end, this results in an O(n) time complexity
    - `_hash(key)`: Generates a hash for a given key using python's built in hash function that returns the same integer for the same key passed in in the same program run
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
        Uses Python's built-in `hash()` function (returns the same integer for the same key passed in in the same program run) and modulo operation to ensure the hash falls within the range [0, size-1].
        """
        return hash(key) % self.size

    def put(self, key, value):
        """
        Insert a key-value pair into the hash table.
        If the key already exists, update its value.
        """
        hashed_key = self._hash(key)  # Compute hash index
        bucket = self.table[hashed_key]  # Locate the correct bucket based on the hashed key

        # Loop through each (key, value) tuple in the bucket
        for index, (existing_key, _) in enumerate(bucket):
            if existing_key == key: # Check if key already exists
                bucket[index] = (key, value)  # Update value
                return

        # If key does not exist, add it to the bucket
        bucket.append((key, value)) # Append key and value to bucket

    def get(self, key):
        """
        Retrieve a value by its key.
        Returns None if the key does not exist.
        """
        hashed_key = self._hash(key)  # Compute hash index for the passed in key
        bucket = self.table[hashed_key]  # Locate the correct bucket

        # Loop through each (key,val) tuple in the bucket
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

    test_keys = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

    hash_table = HashTable(size=5)  # Small size to increase collision probability

    for key in test_keys:
        print(f"Key: {key} -> Bucket: {hash_table._hash(key)}")


    # Insert values
    hash_table.put("cherry", 1)
    hash_table.put("date", 2)
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
