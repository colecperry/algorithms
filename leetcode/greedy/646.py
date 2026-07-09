class IntervalSelection:
    """
    You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti. A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

    Return the length longest chain which can be formed. You do not need to use up all the given intervals. You can select pairs in any order.

    Example 1:
    Input: pairs = [[1,2],[2,3],[3,4]]
    Output: 2
    Explanation: The longest chain is [1,2] -> [3,4].

    Example 2:
    Input: pairs = [[1,2],[7,8],[4,5]]
    Output: 3
    Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
    
    How it works:
    1. Sort pairs by end time (greedy choice: earliest ending first)
    2. Always select pair that finishes earliest
    3. For each pair, if it doesn't overlap with last selected, take it
    4. Count total pairs selected
    5. Greedy works: earliest ending leaves most room for future selections
    """
    def findLongestChain(self, pairs: List[List[int]]) -> int: # LC 646
        """
        - TC: O(n log n) - sorting intervals by end time
        - SC: O(1) or O(log n) - depending on sorting implementation
        """
        if not pairs:
            return 0
        
        # Sort by end time (greedy: finish earliest activities first)
        pairs.sort(key=lambda x: x[1])
        
        count = 1  # Always select first pair after sorting
        last_end = pairs[0][1] # get end of first interval
        
        for i in range(1, len(pairs)):
            start, end = pairs[i]
            
            # If current pair doesn't overlap with last selected pair
            # (pair follows: previous end < current start)
            if start > last_end:
                count += 1
                last_end = end # update end of prev interval
        
        return count

sol = IntervalSelection()
print("Longest chain:", sol.findLongestChain([[1,2],[2,3],[3,4]]))  # 2
print("Longest chain:", sol.findLongestChain([[1,2],[7,8],[4,5]]))  # 3