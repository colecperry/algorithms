# Two-Pointer Technique
# This file demonstrates the two-pointer technique, common patterns, and examples for solving problems.

class TwoPointerExamples:
    
    def two_sum_sorted(self, nums, target):
        """
        Problem: Find two numbers in a sorted array that add up to a given target.
        Technique: Two pointers starting at opposite ends of the array.
        """
        left, right = 0, len(nums) - 1 # Start pointer at beginning and ending indexes
        while left < right: # Loop until they meet
            current_sum = nums[left] + nums[right] # Add up the two nums in the array
            if current_sum == target: # If the sum equals the target
                return [left, right] # Return the two indexes in a list
            elif current_sum < target: # If the sum is less than the target
                left += 1 # Increase the left pointer (b/c we know the array is sorted)
            else:
                right -= 1 # If the sum is greater than the target, move the right pointer over to left
        return []  # Return empty if no solution exists

    def remove_duplicates(self, nums):
        """
        Problem: Remove duplicates from a sorted array in-place and return the length of the modified array.
        Technique: Two pointers moving in the same direction.
        """
        if not nums:
            return 0

        write_pointer = 1  # Points to the place where the next unique element should go
        for read_pointer in range(1, len(nums)): # Loop through nums starting at index 1
            if nums[read_pointer] != nums[read_pointer - 1]: # If current num does not equal last num
                nums[write_pointer] = nums[read_pointer]
                write_pointer += 1

        return write_pointer  # Length of the array with unique elements

    def valid_palindrome(self, s):
        """
        Problem: Check if a given string is a palindrome, ignoring non-alphanumeric characters.
        Technique: Two pointers moving inward from both ends of the string.
        """
        left, right = 0, len(s) - 1 # Set left and right pointers
        while left < right: # Loop until numbers meet
            while left < right and not s[left].isalnum(): # Move left ptr until it is alphanumeric
                left += 1
            while left < right and not s[right].isalnum(): # Move right ptr until it is alphanumeric
                right -= 1
            if s[left].lower() != s[right].lower(): # If chars are not equal
                return False
            left += 1 # Else move pts
            right -= 1
        return True # Return true if all ===

    def trap_rain_water(self, height):
        """
        Problem: Given an array representing elevations, find how much water can be trapped after raining.
        Technique: Two pointers moving inward, calculating water trapped at each step.
        """
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        trapped_water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    trapped_water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    trapped_water += right_max - height[right]
                right -= 1

        return trapped_water

# Main function to demonstrate examples
def main():
    examples = TwoPointerExamples()

    # Example 1: Two Sum in Sorted Array
    nums = [2, 7, 11, 15]
    target = 9
    print("Two Sum:", examples.two_sum_sorted(nums, target))  # Output: [0, 1]

    # Example 2: Remove Duplicates
    nums = [1, 1, 2, 3, 3, 4]
    length = examples.remove_duplicates(nums)
    print("Remove Duplicates:", nums[:length], ", Length:", length)  # Output: [1, 2, 3, 4], Length: 4

    # Example 3: Valid Palindrome
    s = "A man, a plan, a canal: Panama"
    print("Valid Palindrome:", examples.valid_palindrome(s))  # Output: True

    # Example 4: Trapping Rain Water
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print("Trapping Rain Water:", examples.trap_rain_water(height))  # Output: 6

if __name__ == "__main__":
    main()
