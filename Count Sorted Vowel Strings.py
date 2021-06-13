class Solution:
    def countVowelStrings(self, n: int) -> int:

        dp = [1, 1, 1, 1, 1]

        for i in range(n-1):
            dp_sum = sum(dp)
            temp_dp = []

            for el in dp:
                temp_dp.append(dp_sum)
                dp_sum -= el

            dp = temp_dp

        return sum(dp)