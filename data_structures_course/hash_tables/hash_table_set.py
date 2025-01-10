# Set method is going to use the hash method on the key to create the address & also will create a key value pair in a list which goes into the address space

# Big 0 of set_item:
    # 0(1) -> constant time
    # The hashing method is 0(1) 
    # Accessing an element in an array is 0(1)
    # Appending to a list if 0(1)


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
    
    def set_item(self, key, value):
        index = self.__hash(key) # Compute the address "index" to store key value pair
        if self.data_map[index] == None: # If empty list hasn't already been created
            self.data_map[index] = [] # Initialize an empty list at that address
        self.data_map[index].append([key, value]) # Append a list containing key & val
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

my_hash_table.print_table()