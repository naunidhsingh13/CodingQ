
class Solution:

    def sol(self, nums, k):

        s = 0
        arr = []

        for n in nums:
            s += n
            arr.append(s)

        i = 0
        memo = {}
        max_len = 0
        while i < len(arr):

            if arr[i] == k:
                max_len = max(max_len, i+1)
            elif arr[i]-k in memo:
                max_len = max(max_len, i - memo[arr[i]-k])

            if arr[i] not in memo:
                memo[arr[i]] = i
            i += 1

        return max_len


print(Solution().sol([61, 1, -1, 5, -2, 3], 3))
print(Solution().sol([-2, -1, 2, 1], 1))
