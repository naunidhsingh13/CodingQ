
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
                max_len = max(max_len, i)
            elif k-arr[i] in memo:
                max_len = max(max_len, i - memo[k-arr[i]])

            if arr[i] not in memo:
                memo[arr[i]] = i

        return max_len