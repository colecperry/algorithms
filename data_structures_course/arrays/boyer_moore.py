class Solution:
    def majorityElement(self, nums):
        """
        Finds the majority element (element appearing more than n/2 times)
        using the Boyer-Moore Voting Algorithm.
        
        :param nums: List[int] - input array
        :return: int - the majority element
        """
        # Step 1: Initialize variables
        candidate = None  # Variable to store the potential majority element
        count = 0  # Counter to track the balance of the current candidate
        
        # Step 2: Find the candidate
        for num in nums:
            if count == 0:
                # If count is 0, select the current number as the new candidate
                candidate = num
                print(f"New candidate selected: {candidate}")
            # Update the count: increment if num matches candidate, decrement otherwise
            count += 1 if num == candidate else -1
            print(f"Processing {num}: candidate={candidate}, count={count}")
        
        # Step 3: Verify the candidate (optional if majority element is guaranteed)
        # Count the occurrences of the candidate to ensure it is the majority element
        occurrence = nums.count(candidate)
        if occurrence > len(nums) // 2:
            print(f"Candidate {candidate} is the majority element with {occurrence} occurrences.")
            return candidate
        else:
            print(f"No majority element found (should not happen in guaranteed input).")
            return None

# Example usage
nums = [3, 3, 4, 2, 3, 3, 3]
solution = Solution()
majority_element = solution.majorityElement(nums)

# Output the result
print(f"The majority element is: {majority_element}")