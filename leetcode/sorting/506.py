# 506. Relative Ranks

# Topics: Array, Sorting, Heap (Priority Queue)

# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.


# Example 1:
# Input: score = [5,4,3,2,1]
# Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
# Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

# Example 2:
# Input: score = [10,3,8,9,4]
# Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
# Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

# How to Solve(sorting)
    # Sort the scores in descending order, create dict for score to medal mapping
    # Iterate through the sorted scores, and map each score to each medal
        # For indexes 3 or greater, map the score to the index + 1
    # Iterate through the original score array (non sorted)
        # For each score in the array, access the prize and append to an output array


def findRelativeRanks(score):
    sorted_score = sorted(score, reverse=True) # Sort arr in descending order

    placement_dict = {} # Dict stores scores to awards
    output_arr = [] # Output arr stores the final awards

    for i, s in enumerate(sorted_score): # Iterate through sorted arr
            if i == 0: # On idx 0
                placement_dict[s] = "Gold Medal" # Assign score to award
            elif i == 1:
                placement_dict[s] = "Silver Medal"
            elif i == 2:
                placement_dict[s] = "Bronze Medal"
            else:
                value = i + 1 # Get value for award
                placement_dict[s] = str(value) # Assign score to award

    for s in score: # Iterate through original array
        output_arr.append(placement_dict[s]) # Append that score's award
    
    return output_arr


# How to solve (heap):
    # Loop through array and create a max heap of scores (negative) and indexes -> will automatically become a max heap with negative nums
    # Create an output array of zero's and placement variable starting at 1
    # Loop through heap:
        # Pop off the root ele, and get the original index of the score
        # Depending on the placement variable, insert the medal in the output array at the original index, and increment the place each iteration


import heapq

def findRelativeRanks2(score):
        N = len(score)

        # Create a heap of pairs (score, index) -> scores in max heap order with placements
        heap = []
        for index, s in enumerate(score):
            heapq.heappush(heap, (-s, index)) # Push negative score for max heap
        
        # Assign ranks to athletes
        rank = [0] * N # Initialize output arr with all zero's
        place = 1 # Start at first place
        while heap: # While there are still ele's in the heap
            original_index = heapq.heappop(heap)[1] # Pop off root, get original index of the score
            if place == 1:
                rank[original_index] = "Gold Medal" # Place medal in rank arr w/ original ordering
            elif place == 2:
                rank[original_index] = "Silver Medal"
            elif place == 3:
                rank[original_index] = "Bronze Medal"
            else:
                rank[original_index] = str(place)
            place +=1 # Increment place after adding medal
            
        return rank


print(findRelativeRanks([5,4,3,2,1]))
print(findRelativeRanks2([10,3,8,9,4]))