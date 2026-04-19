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

from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinishBFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses # of prereq's for each class
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course) # prereq -> course it unlocks
            in_degree[course] += 1

        courses_taken = 0
        queue = deque()

        # init queue
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            curr_class = queue.popleft()
            courses_taken += 1
            for course in graph[curr_class]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)

        return courses_taken == numCourses






sol = Solution()
print(sol.canFinishBFS(2, [[1,0]])) # true
print(sol.canFinishBFS(2, [[1,0], [0,1]])) # false
print(sol.canFinishBFS(5, [[0,1], [0,2], [1,3], [1,4], [3,4]]))