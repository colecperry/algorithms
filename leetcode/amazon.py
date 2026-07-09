# The goal is to have the computational power (integer array) in non decreasing order, and you may increase the computational power of each segment by X. Choose the values of X such that after the computational power are in non decreasing order, the sum of the X values is the minimum.

# Ex: n = 5 servers
# [3, 4, 1, 6, 2] ->
#       +3 +3 +3
# [3, 4, 4, 9, 5] ->
#             +4
# [3, 4, 4, 9, 9] -> answer = 5 (3 + 4)

def findMinimumSum(power):
    required_sum = 0
    for i in range(1, len(power)): # Loop through power starting at index 1, ending at len(power)
        if power[i] < power[i-1]: # Check if power[i] < power[i-1]
            difference = power[i-1] - power[i] # Compute required increase
            required_sum = required_sum + difference # Add the sum of the increments
            power[i] = power[i-1] # Update power[i] to match the prev's value
            
    
    return required_sum

print(findMinimumSum([3,3,2,1]))

# Goal is to find the maximum possible reward points by purchasing optimally. Each time you pick an item, the item's picked points go to zero and all remaining reward points decrease by 1

# ex. n = 5
# points = [5,2,2,3,1] -> pick points[2] -> earn 2 points
# points = [4,1,0,2,0] -> pick points[3] -> earn 2 points
# points = [3,0,0,0,0] -> pick points[0] -> earn 3 points
# points = [0,0,0,0,0] -> 7 points earned

# How to Solve (sorting):
    # Sort the array -> prioritizes a greedy strategy where ensuring the highest points are picked first
    # Increase the total by increasing the number by the number minus the index, which represents the cumulative decrease applied to each item, using max(num - i, 0) ensures you don't add a negative value to the total reward

def findMaxPoints(points):
    points.sort(reverse = True) # Sort the points in descending order
    total = 0 # Track total points earned

    for i, num in enumerate(points):
        total += max(num - i, 0)

    return total

print(findMaxPoints([5,2,2,3,1]))
