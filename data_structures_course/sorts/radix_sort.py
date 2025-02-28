# Radix sort distributes elements of an array to sort into bins (buckets)), based on each digit’s (letter’s ) value.
# It then repeatedly sorts elements in the bins using some stable sort, from the least significant position to the the most significant.
# In iteration 1 we sort the array in place based on the last digit, then using that array sort the array in place using second digit, so on and so forth

# EX:

"""
Visualization of Radix Sort (Least Significant Digit First):

Step 1: Sort by least significant digit (rightmost column)
--------------------------------------------------------
Original Array:    After Step 1 (sorted by LSD):
1  7  5            7  5  2
4  7  3            4  7  3
2  4  7     ->     8  4  3
3  4  6            1  2  5
9  6  8            3  4  6
7  5  2            2  4  7
8  4  3            9  6  8

Step 2: Sort by middle digit
--------------------------------------------------------
After Step 1:      After Step 2 (sorted by 2nd digit):
7  5  2            1  2  5
4  7  3            8  4  3
8  4  3     ->     3  4  6
1  2  5            2  4  7
3  4  6            7  5  2
2  4  7            9  6  8
9  6  8            4  7  3

Step 3: Sort by most significant digit (leftmost column)
--------------------------------------------------------
After Step 2:      Final Sorted Array:
1  2  5            1  2  5
8  4  3            2  4  7
3  4  6     ->     3  4  6
2  4  7            4  7  3
7  5  2            7  5  2
9  6  8            8  4  3
4  7  3            9  6  8

Each step sorts the numbers based on one digit at a time,
starting from the least significant digit to the most significant.
"""

"""
📌 Time and Space Complexity of Radix Sort

🔹 Time Complexity:
    - Counting Sort (per digit) → O(n + k), where k is the range of digits (0-9 → k = 10).
    - Radix Sort runs Counting Sort for each digit (d digits in the max number).
   - Total Time Complexity: O(d * (n + k))
   - Since k = 10 (constant), it simplifies to **O(d * n)**.
   - d ≈ log_{10}(max_val), so the final complexity is **O(n * log(max_val))**.

🔹 Space Complexity:
    - Counting Sort uses:
        - `count` array → O(k) = O(10) = O(1) (constant space)
        - `sorted_arr` (output array) → O(n)
    - Radix Sort calls Counting Sort `d` times but reuses space.
    - Overall Space Complexity: **O(n + k) = O(n + 10) = O(n)**.
"""


def counting_sort(arr, exp):
    if len(arr) == 0:
        return arr

    # Find the range of the input digits (0-9 for radix sort)
    min_val = 0  # Always 0 since we're dealing with single digits (0-9)
    max_val = 9  # Maximum digit is 9
    range_of_elements = max_val - min_val + 1  # Should be 10

    sorted_arr = [0] * len(arr)  # Create output array of correct length

    # Step 0: Create a count array to store # of times each digit appears
    count = [0] * range_of_elements

    # Loop through input array, extract digit at 'exp' place, and increment count
    for num in arr:
        digit = (num // exp) % 10  # Extract the digit at 'exp' place
        count[digit - min_val] += 1  # Align min_val at index 0 (redundant here, since min_val is 0)

    # Create a cumulative count array: modify count[i] to store number of elements ≤ that index
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Iterate through arr backwards and place elements in their correct sorted positions
    for num in reversed(arr):
        digit = (num // exp) % 10  # Extract the digit at 'exp' place
        position = count[digit - min_val] - 1  # Find the correct sorted position
        sorted_arr[position] = num  # Place element in sorted array
        count[digit - min_val] -= 1  # Decrement the count for handling duplicates

    # Copy back to original array
    for i in range(len(arr)):
        arr[i] = sorted_arr[i]


def radix_sort(arr):
    """
    Main function to sort an array using Radix Sort.
    """

    # Find the maximum number to determine the number of digits
    max_val = max(arr)

    # Perform counting sort for each digit, starting from the least significant digit
    exp = 1  # Initial place value (1s, 10s, 100s, ...)
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10  # Move to the next digit place



# Test the function with the given input
arr = [175, 473, 247, 346, 968, 752, 843]  # Input array from the image
radix_sort(arr)
print(arr)  # Expected output: [125, 247, 346, 473, 752, 843, 968]

