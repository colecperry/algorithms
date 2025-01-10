# Always have a prime number of addresses b/c a prime number increases the randomness for how the key value pairs will be distributed in the hash table -> decreases collisions

# Big 0 of __hash: 0(1) -> constant time
    # Fixed number of operations: The number of operations is dependant on the length of the key string, and does not depend on the number of elements in the hash table

class HashTable:
    def __init__(self, size = 7): # Size 7 is default if we don't pass in a value
        self.data_map = [None] * size # Create list with 7 items all containing "None"

    def __hash(self, key): # Create our hash method -> Where we pass our key to find the address we will store our key value pair
        my_hash = 0 # Initialize hash to zero
        for letter in key: # Loop through letters in the key passed to the hash method
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
            # ord(letter) get ASCII value for each letter in key
            # Multiply by any prime number
            # Remainder will be 0->6 which is our address space
        return my_hash # Return number (address to store key value pair) in hash table
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

my_hash_table = HashTable()
my_hash_table.print_table()

