from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list) # Course: [prereq]
        # in_degree[i] = num of prereqs
        in_degree = [0] * numCourses 

        # Create adj list and in degree array
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1

        courses_taken = 0

        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            courses_taken += 1

            for neighbor in adj_list[course]:
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return courses_taken == numCourses
    
sol = Solution()
print(sol.canFinish(2, [[1,0]])) # true
print(sol.canFinish(2, [[1,0], [0,1]])) # false
print(sol.canFinish(5, [[0,1], [0,2], [1,3], [1,4], [3,4]]))