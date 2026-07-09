from typing import List

class HeapGreedy:
    """
    Problem: You are climbing buildings. To go from building i to i+1:
    - If heights[i+1] <= heights[i]: free (going down or same)
    - If heights[i+1] > heights[i]: need bricks OR a ladder for the climb
    
    Bricks: Use (heights[i+1] - heights[i]) bricks for the climb
    Ladders: Skip any climb (unlimited height), but you have limited ladders
    
    Return the furthest building index you can reach.
    
    Example 1:
    Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
    Output: 4
    Explanation: Starting at 0, you can reach 4:
    - 0→1: down (free)
    - 1→2: climb 5, use ladder
    - 2→3: down (free)  
    - 3→4: climb 3, use bricks (5-3=2 left)
    - 4→5: climb 5, need 5 bricks but only have 2 ❌
    
    How it works:
    1. Greedy strategy: Save ladders for BIGGEST climbs (but we don't know future!)
    2. Solution: Use ladders OPTIMISTICALLY, track in min heap
    3. When out of ladders, swap SMALLEST ladder-climb for bricks (heap gives us this)
    4. This ensures ladders end up on the biggest climbs
    5. Greedy works: retrospectively optimizing ensures optimal resource allocation
    """
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int: # LC 1642
        # Min heap tracks climbs where we've used ladders
        # Stores the HEIGHT of each climb, smallest on top
        ladder_climbs = []
        
        for i in range(len(heights) - 1):
            climb_height = heights[i + 1] - heights[i]
            
            # No resources needed for going down or staying level
            if climb_height <= 0:
                continue
            
            # Use a ladder for this climb (optimistic choice)
            heapq.heappush(ladder_climbs, climb_height)
            
            # If we've used more ladders than available
            if len(ladder_climbs) > ladders:
                # Swap the smallest ladder-climb for bricks instead (min heap)
                # This keeps ladders on the biggest climbs
                smallest_climb = heapq.heappop(ladder_climbs)
                bricks -= smallest_climb
                
                # Can't proceed without enough bricks
                if bricks < 0:
                    return i
        
        # Successfully reached the last building
        return len(heights) - 1

# Example walkthrough:
# heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
#
# i=0: 4→2, climb=-2, going down (skip)
# i=1: 2→7, climb=5, use ladder → heap=[5], ladders_used=1
# i=2: 7→6, climb=-1, going down (skip)
# i=3: 6→9, climb=3, use ladder → heap=[3,5], ladders_used=2
#      But we only have 1 ladder! Swap smallest:
#      Pop 3 from heap, use bricks instead → bricks=5-3=2, heap=[5]
# i=4: 9→14, climb=5, use ladder → heap=[5,5], ladders_used=2
#      But we only have 1 ladder! Swap smallest:
#      Pop 5 from heap, use bricks instead → bricks=2-5=-3 ❌
#      Not enough bricks! Return i=4
#
# Output: 4 (can reach building at index 4)
#
# Why greedy works:
# By always swapping smallest ladder-climb for bricks, we ensure ladders
# end up on the BIGGEST climbs. Since ladders can handle any height but
# bricks are limited, this minimizes brick usage and maximizes reach.

sol = HeapGreedy()
print("Furthest building:", sol.furthestBuilding([4,2,7,6,9,14,12], 5, 1))  # 4
print("Furthest building:", sol.furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2))  # 7
print("Furthest building:", sol.furthestBuilding([14,3,19,3], 17, 0))  # 3