# Pattern 5: Two Pointers on Sorted Array - Two Sum
def two_sum_sorted(numbers, target):  # LC 167
    """
    Problem: Find two numbers in sorted array that add up to target.
    Return their indices (1-indexed).
    
    Example: [2,7,11,15], target=9 → [1,2] (numbers[0] + numbers[1] = 2 + 7 = 9)
    
    Key insight: Use sorted property with two pointers instead of binary search.
    If sum is too small, increase left. If too large, decrease right.
    """
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            return [left + 1, right + 1]  # 1-indexed