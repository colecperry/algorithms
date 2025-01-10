# Sliding window is not typically categorized as a "searching" technique, it is an iterative technique where a "window" of a fixed or variable size slides over a data structure (like an array or a string) to analyze subarrays, substrings, or specific conditions. Instead of recalculating values for every new window, it reuses computations to optimize the solution to O(n) time complexity. Sliding windows are most commonly used when searching for optimal subarrays, substrings, or finding a specific pattern or condition within a range of elements.

def find_max_sum_subarray(arr, k):
    """
    Find the maximum sum of any contiguous subarray of size k.

    Parameters:
        arr (list): The list of integers.
        k (int): The size of the window.

    Returns:
        int: The maximum sum of a subarray of size k.
    """
    window_sum = 0
    max_sum = float('-inf')
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # Add the next element to the window

        # Slide the window when we hit size k
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)  # Update max sum
            window_sum -= arr[window_start]  # Remove the element going out of the window
            window_start += 1  # Slide the window forward

    return max_sum


def find_longest_unique_substring(s):
    """
    Find the length of the longest substring without repeating characters.

    Parameters:
        s (str): The input string.

    Returns:
        int: The length of the longest substring without repeating characters.
    """
    char_index = {}
    window_start = 0
    max_length = 0

    for window_end in range(len(s)):
        current_char = s[window_end]

        # If the character is already in the map, move the start
        if current_char in char_index:
            window_start = max(window_start, char_index[current_char] + 1)

        char_index[current_char] = window_end  # Update the latest index of the character
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def find_smallest_subarray_sum(arr, target):
    """
    Find the length of the smallest subarray with a sum greater than or equal to target.

    Parameters:
        arr (list): The list of integers.
        target (int): The target sum.

    Returns:
        int: The length of the smallest subarray. If no such subarray, return 0.
    """
    window_sum = 0
    min_length = float('inf')
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        # Shrink the window as much as possible while the window sum >= target
        while window_sum >= target:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    return min_length if min_length != float('inf') else 0


def main():
    """Main function demonstrating sliding window examples."""
    # Example 1: Maximum sum of subarray of size k
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    print("Maximum sum of subarray of size k:", find_max_sum_subarray(arr, k))

    # Example 2: Longest substring without repeating characters
    s = "abcabcbb"
    print("Length of longest unique substring:", find_longest_unique_substring(s))

    # Example 3: Smallest subarray with sum >= target
    arr = [2, 1, 5, 2, 3, 2]
    target = 7
    print("Smallest subarray length with sum >= target:", find_smallest_subarray_sum(arr, target))


if __name__ == "__main__":
    main()
