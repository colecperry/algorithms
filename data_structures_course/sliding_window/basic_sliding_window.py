"""
Sliding Window Tutorial

This file shows two classic sliding window patterns:
1. Fixed-length sliding window
2. Variable-length sliding window

Both are essential for efficient algorithms on arrays and strings!
"""

def fixed_length_sliding_window(nums, k):
    """
    Find the maximum sum of any subarray of fixed length k.
    Sliding window size stays constant.
    """
    if not nums or k == 0 or k > len(nums):
        return 0

    window_sum = sum(nums[:k])  # Sum of first window
    max_sum = window_sum

    for end in range(k, len(nums)):
        # Slide the window right by removing the element going out
        # and adding the new element coming in
        window_sum += nums[end] - nums[end - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

def variable_length_sliding_window(s, target):
    """
    Find the length of the smallest substring with sum >= target.
    Window size expands and contracts based on the current sum.
    """
    left = 0
    window_sum = 0
    min_length = float('inf')

    for right in range(len(s)):
        window_sum += s[right]  # Expand window to the right

        # Contract window from the left as long as we meet the condition
        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum -= s[left]
            left += 1

    return min_length if min_length != float('inf') else 0

if __name__ == "__main__":
    # Example for fixed-length window
    nums = [2, 1, 5, 1, 3, 2]
    k = 3
    print(f"Max sum of fixed window size {k}:", fixed_length_sliding_window(nums, k))
    # Expected output: 9 (subarray [5,1,3])

    # Example for variable-length window
    nums2 = [2, 3, 1, 2, 4, 3]
    target = 7
    print(f"Min length subarray sum >= {target}:", variable_length_sliding_window(nums2, target))
    # Expected output: 2 (subarray [4,3])
