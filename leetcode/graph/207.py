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

# Kahn's Algorithm (BFS Topological Sort) - High-Level Steps:
# 1. Build graph + calculate in-degrees
# - Create adjacency list: prereq → [dependent courses]
# - Count in-degrees for each node
# 2. Initialize queue with in-degree 0 nodes
# - These have no prerequisites, ready to process
# 3. Process queue (BFS):
# - Remove node from queue
# - For each neighbor: decrease in-degree by 1
# - If neighbor's in-degree becomes 0 → add to queue
# 4. Check if all nodes processed
# - If yes → valid order ✓
# - If no → cycle exists ✗

from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinishBFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        TC: O(V + E)
            - Build graph and in-degree: O(E) - iterate through all prereqs (prereq list has E enteries -> each entry = one edge)
            - Initialize queue: O(V) - check all courses for in-degree == 0
            - Process queue: O(V) - each course dequeued at most once worst case (all courses taken)
            - Update neighbors: O(E) - each edge traversed once via graph[course] worst case (all courses taken)
            - Total: O(E) + O(V) + O(V) + O(E) = O(V + E)

        SC: O(V + E)
            - Graph (adjacency list): O(V + E) - stores all verticies and edges
            - In-degree array: O(V) - one entry per course
            - Queue: O(V) worst case - all courses with no prereqs at start
        """
        # Step 1: Build graph and in-degree count
        adj_list = defaultdict(list)  # adj list : prereq -> list of courses it unlocks
        in_degree = [0] * numCourses  # in-degree for each course (num of prereqs it has)

        for course, prereq in prerequisites: # Build in degree array and adj list
            adj_list[prereq].append(course) 
            in_degree[course] += 1 

        # Initialize an empty queue for BFS search
        queue = deque()

        # Init BFS with courses w/ no prereq's
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        completed_courses = 0 # track total number of completed courses

        # Step 3: Process nodes with 0 in-degree (classes with no prereq's)
        while queue:
            current = queue.popleft() 
            completed_courses += 1

            # Reduce in-degree for neighbors (unlocked any new courses?)
            for unlocked_course in adj_list[current]:
                in_degree[unlocked_course] -= 1 # took the course, reduce it's neighbor's prereq count for it
                if in_degree[unlocked_course] == 0: # if course has 0 in deg, it has no prereq's
                    queue.append(unlocked_course) # take the class

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