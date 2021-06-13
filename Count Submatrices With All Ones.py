import math
class Solution:
    def numSubmat(self, mat) -> int:

        m, n = len(mat), len(mat[0])
        dp = [[None]*n for _  in range(m)]


        def func(mat, dp, i, j):
            dp[i][j] = [1, 0]

            # fill left count
            for l in range(j-1, -1, -1):
                if mat[i][l] == 1:
                    dp[i][j][0] += 1
                else:
                    break

            # get total count
            min_j = math.inf
            for k in range(i, -1, -1):
                if mat[k][j] == 1:
                    min_j = min(min_j, dp[k][j][0])
                    dp[i][j][1] += min_j
                else:
                    break

        s = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    func(mat, dp, i, j)
                    s += dp[i][j][1]

        return s


print(Solution().numSubmat([[1,0,1],
                            [1,1,0],
                            [1,1,0]]))
