# 1539. Kth Missing Positive Number

# Topics: Array, Binary Search

# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

# Return the kth positive integer that is missing from this array.

# Example 1:

# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
# Example 2:

# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

# Could you solve this problem in less than O(n) complexity?

# How to Solve: O(n):
    # Start with two variables: one to keep track of number of missing #'s from the arr, and one to use to use check for each positive number
    # Convert the arr to a set for O(1) lookup time vs O(n)
    # Create a while loop -> while the number of missing numbers is less than k (the kth positive integer missing from the array)
        # Increment the num each loop
        # Check if the num is in the set -> only increment the number of missing #'s if the number is not in the set
    # Once our while loop condition fails, we will be on the missing num

# How to Solve: O(log N) -> Binary Search - Big Picture
    # Sorted input array should ring a bell -> Use binary search
    # We need a way to check how many positive numbers are missing before any given array element -> 
        # Compare input array [2,3,4,7,11] to an array with no missing integers [1,2,3,4,5]
        # That means at index i (using 0-indexing), the number should be exactly i + 1
        # The number you actually see at that index is increased by the count of the missing numbers that should have come before it -> if at index 2 you expect 3 but instead see 5, that means there are two missing numbers
            # Missing count up to arr[i] = arr[i] - (i + 1)
                # For index 0, expected number if nothing were missing = i + 1 = 0 + 1 = 1
                    # Actual number at index 0 = 2
                    # Missing count: 2 - (0 + 1) = 1
                # For index 1, expected number if nothing were missing = i + 1 = 1 + 1 = 2
                    # Actual number at index 1 = 3
                    # Missing count: 3 - (1 + 1) = 1


# How to Solve: O(log N) -> Binary Search - Code
    # Create l and r pointers -> initialize to idx 0 and idx len - 1
    # Create binary search while loop
        # Calculate middle index 
        # Calculate the number of missing numbers before the middle index
        # Compare the number of missing numbers at index middle to K:
            # If we have too few missing numbers at index middle, search right
            # If we have too many missing numbers at index middle, search left
        # Return left + k-> Left tells us how many real numbers we have considered before finding the kth missing number, so if we adjust left by k, we shift left by the number of real numbers plus the number of missing numbers, ending in the correct position
            # When we move left = pivot + 1, we are confirming that all elements before the pivot are not enough to reach k missing numbers. Eliminating numbers from the right side of the array that are too large does not count because we have to count from the left to find the result.


# O(n)
def findKthPositive(arr, k):
    missing = 0 # Number of missing numbers
    num = 0 # We start with num = 0
    arr_set = set(arr) # Convert arr to set for O(1) lookup checks
    while missing < k: # While number of missing numbers is less than k
        num += 1 # Increment the number we are looking for no matter what
        if num not in arr_set: # Check if that num is in the set
            missing += 1 # If not, increment the number of missing elements
    return num

def findKthPositive2(arr, k):
    left, right = 0, len(arr) - 1
    while left <= right:
        pivot = (left + right) // 2 # find middle index to guess target val
        missing_nums = arr[pivot] - pivot - 1 # Calc number of missing nums before pivot
        if missing_nums < k: # If we have too few missing numbers
            left = pivot + 1 # Search right -> move left pointer to pivot + 1
        else: # Search left -> move right pointer to pivot - 1
            right = pivot - 1

    # At the end of the loop, left represents how many numbers from a perfect sequence (1,2,3...) we have passed while counting up to the kth missing number
    return left + k



print(findKthPositive2([2,3,4,7,11], 5))
print(findKthPositive([1,2,3,4], 2))
