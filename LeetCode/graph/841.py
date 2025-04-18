# 841. Keys and Rooms

# Topics: DFS, BFS, Graph

# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

# When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

# Example 1:
# Input: rooms = [[1],[2],[3],[]]
# Output: true
# Explanation: 
# We visit room 0 and pick up key 1.
# We then visit room 1 and pick up key 2.
# We then visit room 2 and pick up key 3.
# We then visit room 3.
# Since we were able to visit every room, we return true.

# Example 2:
# Input: rooms = [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.


# How to solve: (BFS)
    # - We treat each room as a node in a graph.
    # - Each room may contain keys to other rooms, which are the edges.
    # - We start with room 0 and perform a Breadth-First Search (BFS)
    #   to explore all reachable rooms.
    # - We use a queue to control the BFS traversal order (FIFO).
    # - We also use a 'visited' list to track which rooms we've already entered, so we don’t revisit the same room and cause infinite loops.

# BFS Steps:
    # 1. Create a queue and initialize it with room index 0.
    # 2. Create a 'visited' list of size n (number of rooms), all set to False.
    # 3. Mark room 0 as visited since it's our starting point.
    # 4. While the queue is not empty:
    #     a. Pop the current room from the front of the queue.
    #     b. Loop through each key in the current room.
    #     c. If the key leads to a room that hasn't been visited:
    #         - Mark that room as visited.
    #         - Add it to the queue to visit later.
    # 5. After the BFS loop ends, check if all rooms were marked as visited.

# Time Complexity: O(n + k)
    # - n = number of rooms
    # - k = total number of keys across all rooms
    # - Each room is enqueued at most once, and each key is processed once.

# Space Complexity: O(n)
    # - O(n) space for the visited list.
    # - O(n) space for the BFS queue in the worst case (if all rooms are connected).


from typing import List
from collections import deque

class Solution: # BFS
    def canVisitAllRoomsBFS(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms) # Track rooms visited
        visited[0] = True  # We always start in room 0

        queue = deque([0]) # Start BFS from room index 0

        while queue:
            current_room = queue.popleft() # Take the next room to explore

            # Look at every key in the current room
            for key in rooms[current_room]:
                if not visited[key]: # If key isn't visited
                    visited[key] = True # Mark the room as visited
                    queue.append(key) # Add the room index to the queue for later exploration

        # If we've visited all rooms, return True
        return all(visited)

# How to solve using Iterative DFS:
    # - Think of each room as a node in a graph.
    # - Each room contains keys that act as directed edges to other nodes (rooms).
    # - The goal is to visit all rooms starting from room 0.
    # - We'll use a stack to simulate Depth-First Search (DFS) traversal.
    # - We also maintain a 'visited' list to mark rooms we've already explored.

# DFS Steps:
    # 1. Initialize a 'visited' list of size n (number of rooms), all set to False.
    # 2. Mark room 0 as visited, since we always start there.
    # 3. Initialize a stack with room 0.
    # 4. While the stack is not empty:
    #     a. Pop a room off the top of the stack (DFS explores depth-first).
    #     b. Loop through all keys in the current room.
    #     c. For each key, if the corresponding room hasn't been visited:
    #         - Mark it as visited.
    #         - Push it onto the stack to explore next.
    # 5. After the traversal ends, return True only if all rooms were visited.

# Time Complexity: O(n + k)
    # - n = number of rooms (each node visited once)
    # - k = total number of keys across all rooms (each edge followed once)

# Space Complexity: O(n)
    # - O(n) space for the visited list
    # - O(n) space for the stack in the worst case (fully connected graph)
    
    def canVisitAllRoomsIterative(self, rooms: List[List[int]]) -> bool: # DFS Iterative
        visited = [False] * len(rooms) # Track if each idx was visited
        visited[0] = True # First room always visited

        stack = [0] # Initialize Iterative DFS stack
        while stack:
            curr_room = stack.pop() # Take next room to explore

            for key in rooms[curr_room]: # Loop over keys in that room
                if not visited[key]:
                    visited[key] = True
                    stack.append(key)
        
        return all(visited)


sol = Solution()
print(sol.canVisitAllRooms([[1],[2],[3],[]]))
print(sol.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))