# 210. Course Schedule II

# Topics: DFS, BFS, Graph, Topological Sort

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:

# Input: numCourses = 1, prerequisites = []
# Output: [0]

from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Build adj list and in-degree count
        adj_list = defaultdict(list) # adj list : prereq -> list of courses that it unlocks
        in_degree = [0] * numCourses # in-degree for each course (num of prereqs it has)

        for course, prereq in prerequisites:
            adj_list[prereq].append(course) # crs taken -> crs unlocked
            in_degree[course] += 1 # count num of prereqs for each course

        # Initialize an empty queue for BFS search
        queue = deque()
        
        # Loop through all courses to see which ones you can take first
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)

        list_order = [] # output arr

        # Step 3: Process nodes with 0 in-degree (classes with no prereq's)
        while queue:
            current = queue.popleft()
            list_order.append(current)

            # Reduce in-degree for neighbors (did we unlock any new courses)
            for unlocked_course in adj_list[current]:
                in_degree[unlocked_course] -= 1
                if in_degree[unlocked_course] == 0:
                    queue.append(unlocked_course)
        
        # Return empty list if we could not finish all courses, else, return the order of classes taken
        return [] if len(list_order) != numCourses else list_order
    
sol = Solution()
print(sol.findOrder(2, [1,0]))
print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(sol.findOrder(1, []))
