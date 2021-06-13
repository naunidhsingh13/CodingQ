from collections import defaultdict, deque

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        mp1 = defaultdict(lambda : 0)
        mp2 = defaultdict(lambda : 0)
        for ch in s1:
            mp1[ch] += 1
        for ch in s2:
            mp2[ch] += 1

        mp = defaultdict(lambda : 0)
        for key in mp1:
            if key in mp2:
                mp[key] = min(mp1[key], mp2[key])

        s1, s2 = deque(list(s1)), deque(list(s2))
        sm = 0

        while s1 and s2:
            print(sm)

            if s1[0] not in mp:
                sm+= ord(s1.popleft())
                continue

            if s2[0] not in mp:
                sm += ord(s2.popleft())
                continue


            if s1[0] != s2[0]:
                if s1[0] < s2[0]:
                    sm += ord(s1.popleft())

                else:
                    sm += ord(s2.popleft())

            else:

                mp[s1[0]] -= 1
                if mp[s1[0]] == 0:
                    del[mp[s1[0]]]
                s1.popleft()
                s2.popleft()

        while s1:
            sm+= ord(s1.popleft())
        while s2:
            sm += ord(s2.popleft())

        return sm


print(Solution().minimumDeleteSum('delete', 'leet'))
