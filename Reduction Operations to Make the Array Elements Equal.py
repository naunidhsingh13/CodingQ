"""
1887. Reduction Operations to Make the Array Elements Equal

Difficulty:Medium
Given an integer array nums, your goal is to make all elements in nums equal.
To complete one operation, follow these steps:

Find the largest value in nums. Let its index be i (0-indexed) and its value be largest.
If there are multiple elements with the largest value, pick the smallest i.
Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
Reduce nums[i] to nextLargest.
Return the number of operations to make all elements in nums equal.
"""

import heapq
from collections import defaultdict

class Solution:
    def reductionOperations(self, nums: list[int]) -> int:

        mp = defaultdict(lambda: 0)
        for x in nums:
            mp[x] += 1

        heap = [[-key, mp[key]] for key in mp]

        heapq.heapify(heap)

        count = 0

        while len(heap) > 1:

            node = heapq.heappop(heap)

            if node[0] != heap[0][0]:
                count += node[1]

            temp = heapq.heappop(heap)
            temp[1] += node[1]
            heapq.heappush(heap, temp)

        return count

print(Solution().reductionOperations([5,1,3]))

print(Solution().reductionOperations([1,1,1]))

print(Solution().reductionOperations([1,1,2,2,3]))