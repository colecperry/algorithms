# boyer_moore_majority_vote.py

def majority_element(nums):
    """
    Finds the majority element in a list using the Boyer–Moore Majority Vote Algorithm.
    A majority element is one that appears more than n/2 times in the list.
    
    Parameters:
    nums (List[int]) : A list of integers

    Returns:
    int : The majority element if one exists, otherwise None
    """

    # Step 1: Find a candidate for majority
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Step 2 (optional): Verify the candidate is actually a majority
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    else:
        return None


# Example usage:
if __name__ == "__main__":
    # Example 1: Majority element exists
    nums1 = [2, 2, 1, 1, 1, 2, 2]
    print("Input:", nums1)
    print("Majority element:", majority_element(nums1))  # Output: 2

    # Example 2: No majority element
    nums2 = [1, 2, 3, 4]
    print("\nInput:", nums2)
    print("Majority element:", majority_element(nums2))  # Output: None

    # Example 3: All same elements
    nums3 = [5, 5, 5, 5]
    print("\nInput:", nums3)
    print("Majority element:", majority_element(nums3))  # Output: 5
