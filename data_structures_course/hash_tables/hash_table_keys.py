# Keys method takes all of the keys out of the hash table and creates and returns a list of keys

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
        if self.data_map[index] == None: # Initialize an empty list at that address
            self.data_map[index] = [] # Only if empty list hasn't already been created
        self.data_map[index].append([key, value]) # Append a list containing key & val

    def get_item(self, key):
        index = self.__hash(key) # Find the index for the key by using the hash fn
        if self.data_map[index] is not None: # look for item if key-val pairs at that address
            for i in range(len(self.data_map[index])): # Loop thru list inside index in hashmap
                if self.data_map[index][i][0] == key: # Check if there is a match at the index in the list inside the index in the hashmap, 0 is the first element b/c we are looking for key
                    return self.data_map[index][i][1] # Return the value at that index inside the list inside the index of the hashmap
        return None # Return none if there was no match
    
    def keys(self):
        all_keys = [] # Create a list to store the list of keys
        for i in range(len(self.data_map)): # Loop through hashmap indexes
            if self.data_map[i] is not None: # If there is a list inside the hashmap index
                for j in range(len(self.data_map[i])): # Create a second for loop to loop through the list inside the hashmap index
                    all_keys.append(self.data_map[i][j][0]) # Append the key, i is the index of the hashmap, j is the index of the list inside the hashmap index, 0 is the first element
        return all_keys

    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

print(my_hash_table.keys()) # Prints: ['bolts', 'washers', 'lumber']