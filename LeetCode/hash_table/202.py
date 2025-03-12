# 202. Happy Number

# Topics - Hash Table, Math, Two Pointers

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# Example 2:
# Input: n = 2
# Output: false

# How to Solve: (with hashset)
    # Big Picture:
        # We have two options -> either we keep squaring each digit and adding together until we get 1, or we get stuck in an infinite loop. The infinite loop would occur if we get to a number (sum of squared digits) that we have already encountered.
        # Example: 37 -> 30 -> 9 -> 81 -> 65 -> 61 -> 37
    # Code:
        # Create a hashset to track every number we have previously visitied -> If we get to that number again, we know to return False
        # Keep looping as long as the sum of digits isn't in the hashset already
            # Add new number to hashset
            # Compute the num of squares with a helper function
            # Check if sum is one, if so return True
            # End loop and return False if we find n in the hashset
        # Helper function to compute sum of squares
            # Loop until floor division // 10 == 0 (we know that anything less than 10 will be only one digit left)
            # Take n and mod by 10 to get the second digit
            # Take n and divide it by 10 to get the first digit

"""
Time Complexity: O(log n)
- Each step computes the sum of squares of digits by extracting and squaring each digit.
- The number of digits in n is approximately log_10(n), so computing the sum of squares takes O(log n) time.
- The process repeats for at most O(log n) steps before reaching 1 or entering a cycle, giving an overall complexity of O(log n).

Space Complexity: O(log n)
- A HashSet stores previously seen numbers to detect cycles.
- The sum of squared digits quickly reduces n, limiting the number of unique values stored.
- Since the sequence of numbers before repeating is at most O(log n) in practice, the space complexity remains O(log n).

"""

# How to Solve (without hashset) - Tortise and Hare/ Floyd's Cycle detection algorithm
    # Create nested function to compute sum of squares 
    # Create slow and fast pointers -> slow pointer is current n, fast pointer is the sum of numbers of n (call helper function to compute sum of squares on n & store in variable)
    # Create while loop -> continues as long as fast does not calculate 1 or slow == fast (we found a loop)
        # Call helper fn and assign to slow (next sum of squares)
        # Call helper fn on fast's next element (double nested call) to move two steps forward
    # If fast calculates 1 we return true, if slow == fast we return false

'''
**Floyd’s Cycle Detection (Tortoise and Hare)**
   Time Complexity: O(log n)
   - Similar to the original approach, each step computes the sum of squares in O(log n).
   - The cycle detection loop runs at most O(log n) times.
   - So, the overall complexity remains O(log n).

   Space Complexity: O(1)
   - No extra data structures are used (only two integer variables `slow` and `fast`).
   - This reduces space complexity to constant O(1).
'''

class Solution(object):
    # Solution using hashset
    def isHappy(self, n):
        visit = set() # Hashset holds previously visited elements

        while n not in visit: # Keep looping until we find a cycle
            visit.add(n) # Add element to the set
            n = self.sumOfSquares(n)
            if n == 1: # Return True if sum of squares == 1
                return True
        
        return False # Return False if we exit loop (found a cycle)
    
    def sumOfSquares(self, n):
        output = 0 # Sum of squares output
        while n: # While n is not 0 
            digit = n % 10 # Get second digit
            digit = digit ** 2 # Square it
            output += digit # Add sum of current digit to output
            n = n // 10 # Floor division to get next digit

        return output
    
    def isHappy2(self, n):
        # Solution without hashset
        def sumOfSquares(n):
            total = 0
            while n:
                digit = n % 10
                total += digit ** 2
                n //= 10
            return total
        # Skips nested function and comes right to here
        slow, fast = n, sumOfSquares(n) 
        while fast != 1 and slow != fast:
            slow = sumOfSquares(slow)  # Move one step
            fast = sumOfSquares(sumOfSquares(fast))  # Move two steps
        
        return fast == 1  # If we reach 1, it's a happy number



my_solution = Solution()
print(my_solution.isHappy2(19))
print(my_solution.isHappy(2))