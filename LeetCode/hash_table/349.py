# 349. Intersection of Two Arrays

# Topics: Array, Hash Table, Two Pointers, Binary Search, Sorting

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

# Note to self: intersection are elements that are common to each list (don't include duplicates)

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

# How to Solve: (with two hashsets)
    # Store the elements from arr1 in a hashset, and elements from arr2 in another hashset, and then add the numbers in common to both

# How to Solve: (with one hashset)
    # Store elements from arr1 in a set
    # Iterate through second array, if that ele is already in the set, it is common to both arrays, add ele to the output and remove the ele from the set
    # If we get a duplicate, it will not be added because it has been removed from the set after we added the element to the output list

"""
Time and Space Complexity Analysis:

**Set Intersection Approach (`intersection` method)**
- Time Complexity: O(n + m), since converting `nums1` and `nums2` to sets takes O(n) and O(m) respectively, and finding the intersection takes O(min(n, m)).
- Space Complexity: O(n + m), as both `hashset1` and `hashset2` store up to O(n) and O(m) elements.

**Iterative Lookup with Removal (`intersection2` method)**
- Time Complexity: O(n + m), as creating the `seen` set takes O(n) since we iterate over each element, and iterating through `nums2` while checking and removing elements takes O(m) in the worst case.
- Space Complexity: O(n), since `seen` stores only the elements from `nums1`, while `res` stores at most O(min(n, m)) elements.
"""



class Solution(object):
    def intersection(self, nums1, nums2):
        hashset1 = set(nums1)  # Convert nums1 to a set
        hashset2 = set(nums2)  # Convert nums2 to a set
        
        # Find elements unique to both sets (intersection)
        result = hashset1 & hashset2  # Equivalent to hashset1.intersection(hashset2)

        return list(result)  # Convert set to list before returning
    
    def intersection2(self, nums1, nums2):
        seen = set(nums1) # Convert first array to a set

        res = [] # List to store output array
        for n in nums2: # Loop through second array
            if n in seen: # Check if ele in second array is in the set (common to both)
                res.append(n) # Append it to the output array
                seen.remove(n) # Remove that element from the set (to prevent duplicates)
        return res


my_solution = Solution()
arr1, arr2 = [1,2,2,1], [2,2]
arr3, arr4 = [4,9,5], [9,4,9,8,4]
print(my_solution.intersection(arr1, arr2))
print(my_solution.intersection(arr3, arr4))