# 207. Course Schedule

# Topics: Depth-First Search, Breadth-First Search, Graph, Topological Sort

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

# How to Solve:
    # If we regard each course as a node and draw an edge from b to a, we get a directed graph. If there is a cycle, we will not be able to complete all the courses. Otherwise, we can perform a topological sort on the graph to determine the order in which all classes can be finished.
    # A topological sort or topological ordering of a directed graph is a linear ordering of its vertices such that for every directed edge u -> v from vertex u to vertex v, u comes before v in the ordering.
    # In a directed acyclic graph, we can use Kahn's algorithm to get the topological ordering.

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass

sol = Solution()
print(sol.canFinish(2, [[1,0]])) # true
print(sol.canFinish(2, [[1,0], [0,1]])) # false