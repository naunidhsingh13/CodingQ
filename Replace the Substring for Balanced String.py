"""
1234. Replace the Substring for Balanced String
    Medium

You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.

A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.

Return 0 if the string is already balanced.

"""

import math
from collections import defaultdict
class Solution:
    def balancedString(self, s: str) -> int:

        n = len(s)//4

        mp = defaultdict(lambda : 0)

        for ch in s:
            mp[ch] -= 1

        for ch in "QWER":
            mp[ch] = min(mp[ch]+n, 0)
            if mp[ch] == 0:
                del mp[ch]

        if len(mp) == 0:
            return 0
        i = 0
        j = 0
        count = -sum([mp[ch] for ch in mp])
        l = math.inf
        while j < len(s):

            if mp[s[j]] < 0:
                count -= 1

            mp[s[j]] += 1
            while count == 0:
                l = min(l, j - i + 1)
                mp[s[i]] -= 1
                if mp[s[i]] < 0:
                    count += 1
                i += 1
            j += 1

        return l



print(Solution().balancedString("QEQQWQQQ"))