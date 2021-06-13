class Solution:
    def maxSumAfterPartitioning(self, arr, k: int) -> int:

        dp = dict()     # 0 to k-1
        dp[0] = [0, []]

        for a in arr:
            new_dp = dict()

            # 0 condition
            s0 = 0
            for key in dp:
                s, ls = dp[key]
                if key < k:
                    s0 = max(s0, s + ( (len(ls)+1)*max(max(ls), a) if key>0 else a))

            new_dp[0] = [s0, []]

            for key in dp:
                if key < k:
                    s, ls = dp[key]
                    new_dp[key+1] = [s, ls+[a]]

            dp = new_dp

        mx_sum = 0
        for key in dp:
            s, ls = dp[key]
            mx_sum = max(mx_sum, s + (len(ls)*max(ls) if key>0 else 0))

        return mx_sum


print(Solution().maxSumAfterPartitioning([1,15,7,9,2,5,10], 3))