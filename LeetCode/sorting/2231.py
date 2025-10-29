# 2231. Largest Number After Digit Swaps by Parity

# Topics: Sorting, Heap (Priority Queue)

# You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).

# Return the largest possible value of num after any number of swaps.


# Example 1:
# Input: num = 1234
# Output: 3412
# Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
# Swap the digit 2 with the digit 4, this results in the number 3412.
# Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
# Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.

# Example 2:
# Input: num = 65875
# Output: 87655
# Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.
# Swap the first digit 5 with the digit 7, this results in the number 87655.
# Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.

# How to Solve (sorting):
    # Convert string to list of integers
    # Create two arrays of integers, odd and even, sorted by largest to smallest
    # Loop through list of integers from original array, if the number is even, we pop off the largest num from the even arr and append to the result array as a string (We know that index is for even numbers so we can swap and place the largest value there), and same for if the number is odd 
    # Convert the string arr back to an integer


def largestInteger(num):
    arr = [int(i) for i in str(num)]  # Convert number to list of digits
    odd = sorted([i for i in arr if i % 2], reverse=True)   # Create arr with odd numbers in descending order
    even = sorted([i for i in arr if i % 2 == 0], reverse=True)  # Create arr with even numbers in descending order

    res = []
    for i in arr:
        res.append(str(even.pop(0)) if i % 2 == 0 else str(odd.pop(0)))  # Pop the largest available number of the same parity

    return int("".join(res))  # Convert list back to integer


import heapq

def largestInteger2(num):
    arr = [int(i) for i in str(num)]  # Convert number to list of digits
    odd_heap, even_heap = [], []  # Min-heaps for odd and even numbers (stored as negatives for max behavior)

    # Step 1: Separate odd and even numbers into heaps
    for digit in map(int, str(num)):  # Convert each character to an integer
        if digit % 2:  # If odd
            heapq.heappush(odd_heap, -digit)  # Store as negative for max-heap behavior
        else:  # If even
            heapq.heappush(even_heap, -digit)

    # Step 2: Reconstruct the number using the largest available digit of the same parity
    result = []
    for num in arr:
        if num % 2:
            result.append(-heapq.heappop(odd_heap))  # Retrieve largest odd number
        else:
            result.append(-heapq.heappop(even_heap))  # Retrieve largest even number

    return int("".join(map(str, result)))  # Convert list of digits to integer


print(largestInteger2(1234))
print(largestInteger2(65875))
