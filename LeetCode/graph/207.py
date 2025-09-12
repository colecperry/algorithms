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

    # How to Solve: BFS with Kahn's Algorithm
        # Kahn's Algorithm - helps detect cycles in a directed graph, and gives an order in which you can complete all tasks
        # How does it apply to this problem? 
            # Each course is a node
            # Each prereq pair [a,b] is a directed edge b -> a (prereq -> class)
            # If the graph has no cycles, you can finish all courses, if not, you can't

        # Step by Step: Kahn's Algorithm (BFS for Topological Sort)
            # 1. Build an adjacency list: adj_list[b] = a
                # - every prereq pair [a, b] means to take course a, you must take course b first
                # - in Kahn's algorithm, we need to flip the direction -> for each course we just finished, what other courses does it unlock?
            # 2. Build an in-degree array: in_degree[a] = a list of the number prereq's a course has to see when it can be taken (when it reaches 0)
            # 3. Start with courses that can be taken right away (in_degree = 0), and add them to a queue
            # 4. Start BFS:
                # - Take a course out of the queue
                # - Count that you've taken that course
                # - For each course that depends on it
                    # - Subtract 1 from it's in-degree
                    # - If it's in-degree becomes 0 -> it's ready to take, add to the queue
            # 5. Final Check -> check that total number of courses taken == total number of courses -> return True, if not, return False. This works because if there's a cycle, some courses in_degrees will never reach 0

    # ===============================
    # ⏱️ TIME COMPLEXITY
    # ===============================

    # Let n be the number of courses (nodes), and p be the number of prerequisites (edges)

    # - Building the adjacency list takes O(p)
    # - Building the in-degree array also takes O(p)
    # - We process each course at most once → O(n)
    # - For each course, we look at its neighbors (edges) → total O(p)

    # ✅ Total time complexity: O(n + p)

    # ===============================
    # 📦 SPACE COMPLEXITY
    # ===============================

    # - Adjacency list: O(p) space to store the edges
    # - In-degree array: O(n)
    # - Queue for BFS: O(n) in the worst case
    # - Optional: a visited set or result list could take O(n)

    # ✅ Total space complexity: O(n + p)

from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinishBFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build graph and in-degree count
        adj_list = defaultdict(list)  # adj list : prereq -> list of courses that it unlocks
        in_degree = [0] * numCourses  # in-degree for each course (num of prereqs it has)

        for course, prereq in prerequisites:
            adj_list[prereq].append(course) # prereq -> courses it unlocks
            in_degree[course] += 1 # count # of prereqs for each course

        # Initialize an empty queue for BFS search
        queue = deque()

        # Loop through all courses
        for i in range(numCourses):
            # If a course has no prerequisites, add it to the queue
            if in_degree[i] == 0:
                queue.append(i)

        completed_courses = 0 # track total number of completed courses

        # Step 3: Process nodes with 0 in-degree (classes with no prereq's)
        while queue:
            current = queue.popleft() 
            completed_courses += 1

            # Reduce in-degree for neighbors (unlocked any new courses?)
            for unlocked_course in adj_list[current]:
                in_degree[unlocked_course] -= 1 # update # of prereq's for each course after we took current prereq
                if in_degree[unlocked_course] == 0: # All prereqs satisfied
                    queue.append(unlocked_course) # Course is now ready to take

        # Step 4: If we processed all courses, there's no cycle
        return completed_courses == numCourses
    

    def canFinishDFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)} # Map every course to an empty list (adj dict)
        for course, prereq in prerequisites: # Fill adj list (course -> list of prereq's)
            preMap[course].append(prereq) 
        
        visited = set() # all courses along current DFS path

        def dfs(crs):
            if crs in visited: # detected a loop -> cannot finish all courses
                return False
            if not preMap[crs]: # course has no prerequisites -> can be completed
                return True
            
            visited.add(crs) # If we don't hit any base cases, we visit this course
            for prereq in preMap[crs]: # Loop through all this courses prereq's
                if not dfs(prereq): # If we return False from dfs()
                    return False # Return False in the main function
            visited.remove(crs) # ?
            preMap[crs] = [] # ?
            return True
        
        for crs in range(numCourses): # Loop through every course
            if not dfs(crs): # If any of the courses return False -> we cannot complete all prerequisites -> return False
                return False
        return True # 


sol = Solution()
print(sol.canFinishBFS(2, [[1,0]])) # true
print(sol.canFinishBFS(2, [[1,0], [0,1]])) # false
print(sol.canFinishBFS(5, [[0,1], [0,2], [1,3], [1,4], [3,4]]))