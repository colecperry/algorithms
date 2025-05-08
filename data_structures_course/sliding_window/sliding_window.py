# Given a list of items with it's angle (degree), and a field of vision, find the most items that can be see at any given time

# Ex. 1    
#           R          
    # arr = 1, 3, 6, 8, 10, 50, 80, 120, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 360   
    #       L
    #                   
    # field_of_vision = 90
    # Output: 12 
    # Explanation: You can fit all degrees 120, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210 inside 90 degrees

# How to solve
    # Use a sliding window approach
    # Create left and right pointers starting at idx 0
    # Create a max count variable to hold the answer and a count variable to hold the current count
    # Loop until the R pointer goes OOB
    # Check if val at R - val at L is less than the field of vision
    # If it is, increase the count, move right pointer over (makes R - L larger), and update max count
    # If R - L is greater than field of vision, decrease the count, and move the left pointer over (makes R - L smaller)

# Follow up: If this problem is circular
    # When r ptr goes OOB, reset it to idx 0, and add 360 to the value so when you subtract r - 1 it gives the correct answer. # Also we need to change the condition of the loop to while l < len(arr) since when l hits the beginning again there are no new values to calculate
    # Another way to do this is to append the array again to the end of the original array that way we don't have to change while loop condition but we do still need to add 360

# Notes about sliding window: It does not work with negative number

def problem(arr, field_of_vision):
    l, r = 0, 0
    max_count = 0
    count = 0
    while r < len(arr):
        if (arr[r] - arr[l]) <= field_of_vision:
            count += 1
            r += 1
            max_count = max(count, max_count)
        else:
            count -= 1
            l += 1

    return max_count

arr = [1, 3, 6, 8, 10, 50, 80, 120, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 360]
field_of_vision = 90

print(problem(arr, field_of_vision))