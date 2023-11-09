# LL: Partition List ( ** Interview Question)
# Implement the partitionList member function for the LinkedList class, which partitions the list such that all 
# nodes with values less than x come before nodes with values greater than or equal to x.
# Note:  This linked list class does NOT have a tail which will make this method easier to implement.
# The original relative order of the nodes should be preserved.

# Details:
# The function partitionList takes an integer x as a parameter and modifies the current linked list in place
# according to the specified criteria. If the linked list is empty (i.e., head is null), the function should 
# return immediately without making any changes.

# Example 1:
# Input:
# Linked List: 3 -> 8 -> 5 -> 10 -> 2 -> 1 x: 5
# Process:
# Values less than 5: 3, 2, 1
# Values greater than or equal to 5: 8, 5, 10
# Output:
# Linked List: 3 -> 2 -> 1 -> 8 -> 5 -> 10

# Example 2:
# Input:
# Linked List: 1 -> 4 -> 3 -> 2 -> 5 -> 2 x: 3
# Process:
# Values less than 3: 1, 2, 2
# Values greater than or equal to 3: 4, 3, 5
# Output:
# Linked List: 1 -> 2 -> 2 -> 4 -> 3 -> 5

# How to Solve
    # Initalize two dummy nodes to hold values less than and greater than the value "X" passed in
    # Create pointers that will traverse each new list
    # Iterate through the original list, moving nodes to the new lists
    # End the two lists
    # Connect the first list to the beginning of the second, past the dummy node
    # Move the head of the connected list forward one

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def partition_list(self, x):
        if self.head == None: # Check if the list is empty (Nothing to partition)
            return None
        dummy1 = Node(0) # Initialize two dummy nodes
        dummy2 = Node(0)
        prev1 = dummy1 # Initialize a pointer for each list we are creating
        prev2 = dummy2
        current = self.head # Create a current pointer to help us traverse the original list
        while current: # While the current value is not none
            if current.value < x: # If the current node in the original list is less than "X" passed in
                prev1.next = current # Attach it to the end of the list starting at dummy1
                prev1 = prev1.next # Move the "prev1" pointer forward
            else: # If the current node in the original list is not less than "X" passed in
                prev2.next = current # Attach it to the end of the list starting at dummy2
                prev2 = prev2.next # Move the "prev2" pointer forward
            current = current.next # Move the "current" pointer forward
        prev1.next = None # End the two lists - When you reach the end of each list, "prev1" and "prev2" are still 
        prev2.next = None # pointing to the nodes in the original list. Terminate to avoid infitine loops/circular references.
        prev1.next = dummy2.next # Link the first list to the beginning of the second, one node past dummy2 (0)
        self.head = dummy1.next # Update the head to the node after dummy1 (0)
        






#  +=====================================================+
#  |                                                     |
#  |          THE TEST CODE BELOW WILL PRINT             |
#  |              OUTPUT TO "USER LOGS"                  |
#  |                                                     |
#  |  Use the output to test and troubleshoot your code  |
#  |                                                     |
#  +=====================================================+


# Function to convert linked list to Python list
def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

# Function to test partition_list
def test_partition_list():
    test_cases_passed = 0
    
    print("-----------------------")
    
    # Test 1: Normal Case
    print("Test 1: Normal Case")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    ll.append(5)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3, 4, 5]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 2: All Equal Values
    print("Test 2: All Equal Values")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(3)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3, 3, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 3: Single Element
    print("Test 3: Single Element")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 4: Already Sorted
    print("Test 4: Already Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 5: Reverse Sorted
    print("Test 5: Reverse Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(2)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 3, 2]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 6: All Smaller Values
    print("Test 6: All Smaller Values")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(1)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 1, 1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 7: Single Element, Equal to Partition
    print("Test 7: Single Element, Equal to Partition")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Summary
    print(f"{test_cases_passed} out of 7 tests passed.")


# Run the test function
test_partition_list()