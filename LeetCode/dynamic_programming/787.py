# 787. Cheapest Flights Within K Stops

# Topics: Dynamic Programming
# Depth-First Search
# Breadth-First Search
# Graph
# Heap (Priority Queue)
# Shortest Path

# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [from i, to i, price i] indicates that there is a flight from city from i to city to i with cost price i.

# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

# Example 1
# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# Output: 700
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop (k = 1) from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph is shown above.
# The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

# How to solve
# Use Bellman Ford algorithm instead of Djkstra's b/c of condition of max k-stops
# Main idea of Bellman Ford: start at source and do a breadth first search -> From node A, which nodes can we travel to? Now from those nodes, which nodes can we travel to? While doing the BFS, simultaneously keep track of the minimum total path

# Code explained: 
# def findCheapestPrice(self, n, flights, src, dst, k) -> function findCheapestPrice takes in n = number of cities, flights = an array of flights[i] = [from i, to i, price i], src is an integer that represents from i, dst is an integer that represents to i, and k = number of max stops as an integer. Return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
# prices = [float("inf")] * n -> Create an array prices to store the minimum prices to reach each city from the source city. Initialize each city with "inf" because we don't know the costs to reach them initially
# prices[src] = 0 -> Set the price to reach the source city to 0. Suppose n = 4, and src = 0, prices = [0, inf, inf, inf]
# for i in range(k+1) -> Iterate over k+1 "stops" or edges because k stops means visiting k+1 edges (if k = 0, that means we have 0 stops, so we can iterate once. If  k = 1, that means we have 1 stop, so we iterate twice)
# tmpPrices = prices.copy() -> Create an copy of array prices tmpPrices. In the Bellman Ford algoritm, edge relaxations must use the prices of the previous iteration. Without tmpPrices, you might use partially updated values in the same iteration. This ensures we only update the prices for each city once per iteration of the outer loop
# for s, d, p in flights -> Iterate over the flights list where each flight is represented as a tuple which unpacks [s, d, p] to for use inside the loop: s = source city, d = destination city, and p = price of the flight. 
# if prices[s] == float("inf"):
# continue -> If the source city (s) is currently unreachable(prices[s] == inf), skip processing this flight. For example, in the first iteration, prices = [0, inf, inf, inf], only flights from city 0 will be processed. These cities are unreachable because the number of stops is limiting how far we can go
# if prices[s] + p < tmpPrices[d]:
# tmpPrices[d] = prices[s] + p -> Check if the cost to reach d (dest) through s is cheaper than the current recorded cost. If so, update the cost in tmpPrices[d]
# prices = tmpPrices -> After processing all flights in the current iteration, update the prices array with the new costs stored in tmpPrices
# return -1 if prices[dst] == float("inf") else prices[dst] -> If the dst city is unreachable return -2, else return the cheapest price to reach the destination

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float("inf")] * n # Create a price array which represents the min price to reach each city from the source city
        prices[src] = 0 # Set price to reach source city to zero

        for i in range(k+1): # Iterate k + 1 times since k=0 means we iterate once
            tmpPrices = prices.copy() # Create a temporary array so we only update the prices for each city once per outer loop
            for s, d, p in flights: #Iterate over each flight & allow for tuple unpacking
                if prices[s] == float("inf"): #
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
            
        return -1 if prices[dst] == float("inf") else prices[dst]
    
my_solution = Solution()
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
print(my_solution.findCheapestPrice(n, flights, src, dst, k))

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
print(my_solution.findCheapestPrice(n, flights, src, dst, k))

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0
print(my_solution.findCheapestPrice(n, flights, src, dst, k))

# Code walk through for: 
# n = 4
# flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
# src = 0
# dst = 3
# k = 1

# Initialization:
# prices = [0, inf, inf, inf]

# Iteration 1:
# Process flights:
# [0,1,100]: Update tmpPrices[1] = 100.
# Other flights skipped (source city unreachable).
# After processing: prices = [0, 100, inf, inf]

# Iteration 2: 
# Process flights: 
# [1,2,100]: Update tmpPrices[2] = 200.
# [1,3,600]: Update tmpPrices[3] = 700.
# After processing: prices = [0, 100, 200, 700]

# Result
# dst = 3, so return prices[3] = 700