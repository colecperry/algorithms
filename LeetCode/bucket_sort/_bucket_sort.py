"""
=================================================================
BUCKET SORT COMPLETE GUIDE
=================================================================

WHAT IS BUCKET SORT?
--------------------
Bucket sort distributes elements into buckets based on some property (frequency, value range, etc.),
then processes buckets in order. It achieves O(n) time by avoiding comparison-based sorting.

Key Insight:
- Use array index as implicit sorting mechanism
- Index represents frequency, value, or range
- Iterate buckets in order to get sorted result

When to use Bucket Sort:
- Frequency-based problems (top k frequent, sort by frequency)
- Bounded value range (values fit in reasonable array size)
- Need O(n) time instead of O(n log n)

When NOT to use Bucket Sort:
- Unbounded or huge value range
- Need stable sort with complex objects
- Small input where O(n log n) is fine

Common Bucket Sort problem types:
- Top K frequent elements
- Sort by frequency
- Maximum gap problems
- Problems with bounded integer range

BUCKET SORT TEMPLATES
=====================
"""

from typing import List
from collections import Counter

# ================================================================
# FREQUENCY BUCKET TEMPLATE
# ================================================================
def frequency_bucket_template(nums: List[int]) -> List[List[int]]:
    """
    Template for using frequency as bucket index
    
    TC: O(n) - count frequencies, fill buckets, iterate buckets
    SC: O(n) - frequency map + buckets array
    
    WHEN TO USE:
    - "Top K frequent" problems
    - "Sort by frequency" problems
    - Need elements grouped/ordered by how often they appear
    
    KEY INSIGHT:
    - Max possible frequency = len(nums)
    - Use frequency as index: buckets[freq].append(element)
    - Iterate from high to low frequency for "most frequent"
    """
    count = Counter(nums)  # {element: frequency}
    
    # Create buckets: index = frequency, value = list of elements with that frequency
    buckets = [[] for _ in range(len(nums) + 1)]
    
    for num, freq in count.items():
        buckets[freq].append(num)
    
    return buckets

# ================================================================
# VALUE RANGE BUCKET TEMPLATE
# ================================================================
def value_range_bucket_template(nums: List[int], bucket_size: int) -> List[List[int]]:
    """
    Template for distributing values into range-based buckets
    
    TC: O(n) - distribute elements, process buckets
    SC: O(n) - buckets storage
    
    WHEN TO USE:
    - Maximum gap problems
    - Need to group values by range
    - Bounded value range with known min/max
    
    KEY INSIGHT:
    - Bucket index = (value - min_val) // bucket_size
    - Each bucket covers a range of values
    - Useful for gap problems: max gap must be >= ceiling of average gap
    """
    if not nums:
        return []
    
    min_val, max_val = min(nums), max(nums)
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]
    
    for num in nums:
        idx = (num - min_val) // bucket_size
        buckets[idx].append(num)
    
    return buckets

"""
BUCKET SORT COMPLEXITY QUICK REFERENCE
======================================

TIME COMPLEXITY:

- O(n) — Frequency Bucket Sort
  Count frequencies O(n), fill buckets O(n), iterate buckets O(n).

- O(n) — Value Range Bucket Sort
  Distribute O(n), process buckets O(n) if bucket size chosen well.

SPACE COMPLEXITY:

- O(n) — Buckets array + frequency map
  Buckets can hold at most n elements total.

KEY ADVANTAGE:
  Beats O(n log n) comparison-based sorts by using index as implicit order.

================================================================
PATTERN 1: FREQUENCY BUCKET SORT

PATTERN EXPLANATION: Count element frequencies, use frequency as bucket index,
iterate buckets from high to low. Solves "top k frequent" and "sort by frequency"
problems in O(n) time.

TYPICAL STEPS:
1. Count frequencies with hashmap
2. Create buckets array of size n+1
3. Place elements in bucket[frequency]
4. Iterate buckets (high to low for most frequent)
5. Collect results until done

Applications: Top K frequent, sort by frequency, frequency ranking.
================================================================
"""

class FrequencyBucketPattern:
    """
    Problem: Given an integer array nums and an integer k, return the k most frequent elements.
    
    How it works:
    1. Count frequency of each element
    2. Use frequency as bucket index
    3. Iterate from highest frequency down
    4. Collect k elements
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  # LC 347
        """
        TC: O(n) - count + bucket fill + iterate
        SC: O(n) - frequency map + buckets hold "n" elements
        """
        count = Counter(nums) # count freq's
        buckets = [[] for _ in range(len(nums) + 1)] # buckets[i] represents freq "i"
        
        for num, freq in count.items():
            buckets[freq].append(num) # put nums in freq buckets
        
        result = []
        for i in range(len(buckets) - 1, 0, -1):  # High to low frequency
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result

# Example:
# nums = [1,1,1,2,2,3], k = 2
#
# Step 1: Count frequencies
# count = {1: 3, 2: 2, 3: 1}
#
# Step 2: Fill buckets (index = frequency)
# buckets[1] = [3]      ← 3 appears 1 time
# buckets[2] = [2]      ← 2 appears 2 times
# buckets[3] = [1]      ← 1 appears 3 times
# buckets = [[0],[3],[2],[1]]
#
# Step 3: Iterate high to low
# i=3: add 1, result = [1]
# i=2: add 2, result = [1, 2], len == k, return
#
# Output: [1, 2]

sol1 = FrequencyBucketPattern()
print("Top 2 frequent:", sol1.topKFrequent([1,1,1,2,2,3], 2))  # [1, 2]

"""
================================================================
PATTERN 2: VALUE RANGE BUCKET SORT (GAP PROBLEMS)

PATTERN EXPLANATION: Distribute values into buckets covering value ranges.
Useful for gap problems where you need to find maximum difference between
consecutive elements in sorted order without fully sorting.

TYPICAL STEPS:
1. Find min and max values
2. Calculate bucket size based on problem constraints
3. Distribute elements into buckets
4. Process buckets to find answer (e.g., max gap between bucket boundaries)

Applications: Maximum gap, range-based grouping.
================================================================
"""

class MaxGapPattern:
    """
    Problem: Find max difference between successive elements in sorted form.
    Must run in O(n) time.
    
    Input: [3, 6, 9, 1] → sorted: [1, 3, 6, 9]
    Output: 3 (gap between 3→6 or 6→9)
    """
    def maximumGap(self, nums: List[int]) -> int:  # LC 164
        """
        - TC: O(n)
        - SC: O(n)
        """
        if len(nums) < 2: # Edge case -> if arr contains less than 2 ele
            return 0
        
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0
        
        n = len(nums)
        
        # Bucket size chosen so max gap MUST span across buckets
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        # Each bucket only stores [min, max] — we don't need all values
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]
        
        # Place each number in its bucket
        for num in nums:
            i = (num - min_val) // bucket_size
            buckets[i][0] = min(buckets[i][0], num)
            buckets[i][1] = max(buckets[i][1], num)
        
        # Max gap = largest jump from one bucket's max to next bucket's min
        max_gap = 0
        prev_max = min_val
        
        for bucket_min, bucket_max in buckets:
            if bucket_min == float('inf'):  # Skip empty buckets
                continue
            max_gap = max(max_gap, bucket_min - prev_max)
            prev_max = bucket_max
        
        return max_gap

# Example: nums = [3, 6, 9, 1]
#
# min=1, max=9, bucket_size=2
#
# Buckets by range:
#   [0] range [1-2]: has 1
#   [1] range [3-4]: has 3
#   [2] range [5-6]: has 6
#   [3] range [7-8]: empty
#   [4] range [9-10]: has 9
#
# Gaps between bucket boundaries:
#   1 → 3 = 2
#   3 → 6 = 3  ← max
#   6 → 9 = 3
#
# Output: 3

sol3 = MaxGapPattern()
print("Maximum gap:", sol3.maximumGap([3, 6, 9, 1]))  # 3
