class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:

        sums = [[0, 0]]
        sm = [0, 0]
        for i in range(len(nums)-1, -1, -1):
            sm[i%2] += nums[i]
            sums.append(sm[:])

        sums = sums[::-1]

        sm = [0, 0]

        count = 0

        for i in range(len(nums)):

            if sm[0] + sums[i+1][1] == sm[1] + sums[i+1][0]:
                count += 1
            sm[i%2] += nums[i]

        return count