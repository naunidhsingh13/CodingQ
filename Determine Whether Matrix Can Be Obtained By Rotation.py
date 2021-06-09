"""
1886. Determine Whether Matrix Can Be Obtained By Rotation
Difficulty:Easy
Given two n x n binary matrices mat and target, return true if it is possible to make
mat equal to target by rotating mat in 90-degree increments, or false otherwise.
"""

class Solution:
    def findRotation(self, mat, target) -> bool:

        n = len(mat)
        no_match = False
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[j][n-i-1]:
                    no_match = True
                    break

        if not no_match:
            return True

        no_match = False
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[n-i-1][n-j-1]:
                    no_match = True
                    break

        if not no_match:
            return True

        no_match = False
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[n-j-1][i]:
                    no_match = True
                    break

        if not no_match:
            return True

        no_match = False
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[i][j]:
                    no_match = True
                    break

        if not no_match:
            return True

        return False


print(Solution().findRotation([[0,1],[1,0]], [[1,0],[0,1]]))
print(Solution().findRotation([[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]]))
