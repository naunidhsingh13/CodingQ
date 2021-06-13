import math
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int):

        f, s = firstPlayer, secondPlayer


        def new_arr(arr, f, s, cond):

            n_arr = []
            i, j = 0, len(arr)-1
            while i <= j:
                if arr[i] in {f,s}:
                    n_arr.append(arr[i])
                elif arr[j] in {f,s}:
                    n_arr.append(arr[j])
                else:
                    n_arr.append(arr[i] if cond(arr[i], arr[j]) else arr[j])
                i += 1
                j -= 1

            return n_arr


        def door(f, s, arr, count):

            if arr.index(f) == len(arr)-1-arr.index(s):
                return count

            elif f <= math.ceil(len(arr)/2) and s <= math.ceil(len(arr)/2):

                return door(f, s, new_arr(arr, f, s, lambda x,y: x>y), count+1)


            elif f >= math.ceil(len(arr)/2) and s >= math.ceil(len(arr)/2):

                return door(f, s, new_arr(arr, f, s, lambda x,y: x<y), count+1)

            else:

                l = 0
                while arr[l] != f:
                    l += 1
                r = 0
                while arr[-r-1] != s:
                    r += 1

                if l < r:
                    return door(f, s, new_arr(arr, f, s, lambda x,y: x>y), count+1)
                elif r > l:
                    return door(f, s, new_arr(arr, f, s, lambda x,y: x<y), count+1)

                else:
                    return count


        def paas(f, s, arr, count):

            if arr.index(f) == len(arr)-1-arr.index(s):
                return count

            elif f <= math.ceil(len(arr)/2) and s <= math.ceil(len(arr)/2):

                return paas(f, s, new_arr(arr, f, s, lambda x, y: x<y), count+1)


            elif f >= math.ceil(len(arr)/2) and s >= math.ceil(len(arr)/2):

                return paas(f, s, new_arr(arr, f, s, lambda x,y: x>y), count+1)

            else:

                l = 0
                while arr[l] != f:
                    l += 1
                r = 0
                while arr[-r-1] != s:
                    r += 1

                if (l + r)%2 == 1:
                    return count + 1
                else:
                    return count + 2

        return paas(f, s, [i for i in range(1, n+1)], 1), door(f, s, [i for i in range(1, n+1)], 1)


print(Solution().earliestAndLatest(11, 2, 4))  # 3,4

print(Solution().earliestAndLatest(4, 1, 3))  # 2,2
print(Solution().earliestAndLatest(5, 1, 3))  # 2,3
