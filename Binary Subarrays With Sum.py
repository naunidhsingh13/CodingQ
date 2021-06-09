"""930. Binary Subarrays With Sum
Medium

Share
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array."""

class Solution:
    def numSubarraysWithSum(self, nums, goal: int) -> int:

        s = 1
        arr = []
        for n in nums:
            if n == 0:
                s += 1
            else:
                arr.append(s)
                s = 1
        arr.append(s)

        if goal == 0:

            return sum([x*(x-1)//2 for x in arr])


        count = 0
        for i in range(len(arr)-goal):

            count += arr[i]*arr[i+goal]

        return count


