
class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Expand around the center approach

        def func(s, x):

            i = 0
            while x-i >= 0 and x+i < len(s) and s[x+i] == s[x-i]:
                i += 1
            i -= 1

            j = 0
            while x-j >= 0 and x+j+1 < len(s) and s[x-j] == s[x+j+1]:
                j += 1
            j -= 1
            return s[x-j:x+j+2] if 2*j+2 > 1+2*i else s[x-i:x+i+1]

        l = ""
        for i in range(len(s)):
            l = max(func(s, i), l, key=len)

        return l


print(Solution().longestPalindrome("cbbd"))
