"""
1888. Minimum Number of Flips to Make the Binary String Alternating

Difficulty:Medium
You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
"""

class Solution:
    def minFlips(self, s: str) -> int:

        if len(s) == 0:
            return 0

        s = [int(x) for x in s]

        def func(s, flag):

            if len(s) % 2 == 0:
                count = 0
                for i in range(len(s)):
                    if flag != s[i]:
                        count += 1
                    flag = not flag

                return count

            else:
                dom = 1 if sum(s) > len(s)/2 else 0
                count = 0
                for i in range(len(s)):
                    if flag != s[i]:
                        if s[i] == dom:
                            flag = not flag
                            dom = None
                        else:
                            count += 1
                    flag = not flag

                return count

        return min(func(s, 0), func(s, 1))



print(Solution().minFlips("111000"))

print(Solution().minFlips("010"))

print(Solution().minFlips("1110"))

print(Solution().minFlips("01001001101"))

print(Solution().minFlips("001000000010"))

print(Solution().minFlips("10001100101000000"))



