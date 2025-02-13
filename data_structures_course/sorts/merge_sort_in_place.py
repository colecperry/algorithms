# How it works:  
    # Recurively call merge_sort on the left side (merge_sort(A, low, mid)) until we reach only one node -> we hit the base case and return to the call stack where there are two nodes 
    # We then recursively call merge_sort on the right side(merge_sort(A, mid + 1, high)) where we reach the base case and return to the call stack with two nodes
    # Continue to the next line of code, where we call merge(A, low, mid, high) where we use these args to slice off the left and right subarrays, iterate through both sliced lists and compare the values, whichever is smaller we replace in the original array in the next open spot. Once we finish iterating through one list, we add the rest of the elements in the other one by one.\
    # Return to the previous call stack and 

    # High level
        # merge_sort([3,1,4,2]) -> call merge_sort([3,1]) -> call merge_sort([3]), return -> call merge_sort([1]), return, call merge([3,1]) -> return [1,3,4,2]
        # merge_sort([1,3,4,2]) -> call merge_sort([4,2]) -> call merge_sort([4]), return -> call merge_sort([2]), return, call merge([4,2]) -> return [1,3,2,4]
        # call stack ([1,3,2,4]) -> call merge([1,3,2,4]) -> return [1,2,3,4]

def merge_sort(A, low, high):
    """
    Recursively sorts an array A using Merge Sort.
    
    Parameters:
    A (list): The list to be sorted.
    low (int): The starting index of the array to sort
    high (int): The ending index of the array to sort
    """
    if low < high:
        mid = (low + high) // 2  # Calculate the middle index
        
        merge_sort(A, low, mid)  # Recursively sort the left half
        merge_sort(A, mid + 1, high)  # Recursively sort the right half
        merge(A, low, mid, high)  # Merge the sorted halves

def merge(A, low, mid, high):
    """
    Merges two sorted subarrays of A.
    
    Parameters:
    A (list): The list to be merged.
    low (int): The starting index of the first subarray.
    mid (int): The ending index of the first subarray.
    high (int): The ending index of the second subarray.
    """
    L = A[low:mid+1]  # Get left subarray
    R = A[mid+1:high+1]  # Get right subarray
    
    i = 0  # Pointer for L
    j = 0  # Pointer for R
    k = low  # Pointer for A
    
    while i < len(L) and j < len(R): # While there are still ele's in both lists
        if L[i] < R[j]: # If left node is smaller
            A[k] = L[i] # Replace ele at index k in A with left node (in place sorting)
            i += 1 # Move left pointer forward
        else: # If right node is smaller
            A[k] = R[j] # Replace ele at index k in A with right node
            j += 1 # Move right pointer forward
        k += 1 # Move pointer for list A forward each time we add one
    
    # Copy remaining elements in only L (if any)
    while i < len(L): 
        A[k] = L[i] # Assign left ele to next place in A
        i += 1 # Move pointer forward for left list
        k += 1 # Move pointer forward for original list
    
    # Copy remaining elements in only R (if any)
    while j < len(R):
        A[k] = R[j] # Assign right ele to next place in A
        j += 1 # Move pointer forward for right list
        k += 1 # Move pointer forward for original list

# Example function calls
if __name__ == "__main__":
    arr = [3, 1, 4, 2]
    print("Original array:", arr)
    
    merge_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)

# Initial Call: merge_sort([3,1,4,2], 0, len(A) - 1) = A, low, high
# ┌──────────────────────────────────────┐
# │ Call stack -> merge_sort([3,1,4,2], 0, 3)  
# │ low = 0, high = 3, mid = 1                         
# │ call merge_sort(A, low, mid) -> merge_sort([3,1,4,2], 0, 1)         
# └──────────────────────────────────────┘

# ┌──────────────────────────────────────┐
# │ Call stack -> merge_sort([3,1,4,2]), 0, 1  │
# │ low = 0, high = 1, mid_index = 0     │
# │ call merge_sort([3,1,4,2), 0, 0)    │
# └──────────────────────────────────────┘

# ┌──────────────────────────────────────┐
# │ Call stack -> merge_sort([3,1,4,2), 0, 0)│
# │ Base case: low < high is false, return back to 
# |  call stack merge_sort([3,1,4,2], 0, 1)
# └──────────────────────────────────────┘

# ┌──────────────────────────────────────┐
# │ Call stack -> merge_sort([3,1,4,2], 0, 1)     │       
# │ call merge_sort(A, mid + 1, high) -> ([3,1,4,2], 1, 1) │
# └──────────────────────────────────────┘

# ┌──────────────────────────────────────┐
# │ Call stack -> merge_sort([3,1,4,2], 1, 1)       │
# │ Base case: low < high is false, return back to 
# │ call stack merge_sort([3,1,4,2], 0, 1)
# └──────────────────────────────────────┘

# ┌──────────────────────────────────────┐
# │ Call stack -> merge_sort([3,1,4,2], 0, 1)       │           
# │ Call merge(A, low, mid, high) -> ([3,1,4,2], 0, 0, 1)
# └──────────────────────────────────────┘

# ┌──────────────────────────────────────┐
# │ Call stack -> merge([3,1,4,2], 0, 0, 1) │
# | Left: [3], Right: [1]
# │ A becomes [1,3,4,2]                         │
# │ Back to call stack merge_sort([1,3,4,2]), 0, 3  │
# └──────────────────────────────────────┘

# ┌──────────────────────────────────────┐
# │ merge_sort([1,3,4,2]), 0, 3      │
# │ low = 0, high = 3, mid = 1           │
# │ Calls merge_sort(A, mid + 1, high) -> merge_sort([1,3,4,2], 2, 3)   │
# | 
# └──────────────────────────────────────┘

# ┌──────────────────────────────────────┐
# │ Call stack -> merge_sort([1,3,4,2], 2, 3)       │
# │ low = 2, high = 3, mid = 2
# | Calls merge_sort(A, low, mid) -> merge_sort([1,3,4,2], 2, 2)
# └──────────────────────────────────────┘

# ┌──────────────────────────────────────┐
# │ Call stack -> merge_sort([1,3,4,2], 2, 2)     │
# │ base case is false, return to call stack merge_sort([1,3,4,2], 2, 3)                      │
# │ call merge_sort(A, mid + 1, high) ->  merge_sort([1,3,4,2], 3, 3)     │
# └──────────────────────────────────────┘

# ┌──────────────────────────────────────┐
# │ Call stack -> merge_sort([1,3,4,2], 3, 3)       │
# │ base case is false, return to call stack merge_sort([1,3,4,2], 2, 3) │
# └──────────────────────────────────────┘

# ┌──────────────────────────────────────┐
# │ Call stack ->  merge_sort([1,3,4,2], 2, 3)        │             │
# │ Call merge(A, low, mid, high) -> merge([1,3,4,2], 2, 2, 3) │
# └──────────────────────────────────────┘

# ┌──────────────────────────────────────┐
# │ Call stack -> merge(A, low, mid, high) -> merge([1,3,4,2], 2, 2, 3)  │
# | Left: [4], Right: [2]
# │ A becomes [1,3,2,4]     
# | Back to call stack merge_sort([1,3,4,2], 0, 3) 
# | Call merge(A, low, mid, high) -> merge([1,3,4,2], 1, 3)   │
# └──────────────────────────────────────┘

# ┌──────────────────────────────────────┐
# │ Call stack -> merge([1,3,4,2], 1, 3)   │
# | Left becomes [1,3], right becomes [2,4]
# │ A becomes [1,2,3,4] 
# └──────────────────────────────────────┘

# Back to the original function call: merge_sort([3,1,4,2])
# Final Result: [1,2,3,4] -> A changed in place