"""
992. Subarrays with K Different Integers
Hard

Given an array nums of positive integers, call a (contiguous, not necessarily distinct) subarray of nums good if the number of different integers in that subarray is exactly k.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of nums.
"""

from collections import defaultdict

class Solution:

    def subarraysWithKDistinct(self, nums, k) -> int:

        def func(nums, k):

            i = 0
            j = 0

            count = 0

            mp = defaultdict(lambda : 0)

            while j < len(nums):

                mp[nums[j]] += 1
                while len(mp) > k:
                    mp[nums[i]] -= 1
                    if mp[nums[i]] == 0:
                        del mp[nums[i]]
                    i += 1
                count += j-i+1
                j += 1

            return count

        return func(nums, k) - func(nums, k-1)


print(Solution().subarraysWithKDistinct([1,2,1,2,3], 2))
# [1,2,1,3,4]
# 3))