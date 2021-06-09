from collections import deque
import math
class Solution:
    def shortestSubarray(self, nums, k: int) -> int:

        i = 0
        j = 0
        s = 0
        l = math.inf
        while j < len(nums):

            s += nums[j]

            if s <= 0:
                s = 0
                i = j+1

            while s >= k:
                l = min(l, j-i+1)
                s -= nums[i]
                i +=1

            j += 1

        return l if l < math.inf else -1


print(Solution().shortestSubarray([84,-37,32,40,95], 167))