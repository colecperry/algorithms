# 705. Design HashSet

# Topics: Array, Hash Table, Linked List, Design, Hash Function

# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:

# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

# Example 1:

# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]

# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# How to solve: (Chaining)
# Use an array and and for each index store a linked list node
# For collisions use chaining (a linked list)

# Time complexity: If we use a prime number for the length of the array (minimizes collisions) and we implement re-hashing (dynamically re-size the array as it gets full) -> O(1) on the average case

# Space complexity: O(n) -> one index for each key in our array




class MyHashSet:

    def __init__(self):
        self.hash_set = set() # Initialize hash set

    def add(self, key: int) -> None:
        if key in self.hash_set:
            return self.hash_set
        self.hash_set.add(key)
        return self.hash_set


    def remove(self, key: int) -> None:
        if key in self.hash_set:
            self.hash_set.remove(key)
            return self.hash_set
        else:
            return False

    def contains(self, key: int) -> bool:
        for val in self.hash_set:
            if key == val:
                return True
        return False

sol = MyHashSet()
print(sol.add(1))
print(sol.add(2))
print(sol.contains(1))
print(sol.contains(3))
print(sol.add(2))
print(sol.contains(2))
print(sol.remove(2))
print(sol.contains(2))

