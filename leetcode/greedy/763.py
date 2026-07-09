from typing import List

class StringPartitioning:
    """
    Problem: You are given a string s. Partition s into as many parts as possible so that
    each letter appears in at most one part. Return a list of integers representing the
    size of these parts.
    
    How it works:
    1. Precompute last occurrence index for each character
    2. Track current partition boundary (end)
    3. For each character, GREEDY CHOICE: immediately commit to extending current partition 
       to include its last occurrence (no backtracking, no trying alternatives)
    4. Keep extending until we reach partition boundary, then close it (all chars complete)
    5. Why greedy works: once we see a character, we MUST include all its occurrences in 
       current partition. Extending to furthest occurrence guarantees this while maximizing 
       number of partitions (we close as soon as possible)
    """
    def partitionLabels(self, s: str) -> List[int]:
        """
        Example: "ababcbacadefegdehijhklij"
                -> [9, 7, 8]
        
        - TC: O(n) - two passes (one for last occurrence, one for partitioning)
        - SC: O(1) - hash map stores at most 26 characters
        """
        # Store last occurrence of each character
        # Key insight: Once we reach a char's last occurrence, we'll NEVER see it again
        # This tells us when it's safe to close a partition (all chars in it are complete)
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i  # Overwrites previous value if char seen before
        
        result = []
        partition_start = 0
        partition_end = 0
        
        for i, char in enumerate(s):
            # Greedy choice -> If I see a character, I immediately commit to extending my current partition to include ALL occurrences of that character.
            partition_end = max(partition_end, last_occurrence[char])
            
            # When we reach partition boundary, all chars are complete
            if i == partition_end:
                result.append(partition_end - partition_start + 1)
                partition_start = i + 1
        
        return result

# Example:
# s = "ababcbaca"
#
# last_occurrence = {'a': 8, 'b': 5, 'c': 7}
# partition_start = 0
# partition_end = 0

# i=0, char='a':
#     partition_end = max(0, 8) = 8     -> Must go to index 8 to include all 'a's
#     i (0) != partition_end (8)        -> Can't close partition yet
    
# i=1, char='b':
#     partition_end = max(8, 5) = 8     -> Still need to reach 8 (already extended)
#     i (1) != partition_end (8)
    
# i=2, char='a':
#     partition_end = max(8, 8) = 8     -> Already planning to go to 8
#     i (2) != partition_end (8)
    
# i=3, char='b':
#     partition_end = max(8, 5) = 8
#     i (3) != partition_end (8)
    
# i=4, char='c':
#     partition_end = max(8, 7) = 8     -> Still need to reach 8
#     i (4) != partition_end (8)
    
# i=5, char='b':
#     partition_end = max(8, 5) = 8
#     i (5) != partition_end (8)
    
# i=6, char='a':
#     partition_end = max(8, 8) = 8
#     i (6) != partition_end (8)
    
# i=7, char='c':
#     partition_end = max(8, 7) = 8
#     i (7) != partition_end (8)
    
# i=8, char='a':
#     partition_end = max(8, 8) = 8
#     i (8) == partition_end (8)        -> ✓ Reached the boundary!
#     result.append(9)                   -> Partition size = 8 - 0 + 1 = 9
#     partition_start = 9                -> Next partition starts here

sol = StringPartitioning()
print("Partition sizes:", sol.partitionLabels("ababcbacadefegdehijhklij"))  # [9, 7, 8]
print("Partition sizes:", sol.partitionLabels("eccbbbbdec"))  # [10]