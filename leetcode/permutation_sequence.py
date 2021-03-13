from heapq import heappush, heappop
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        h = []
        l = [(i + 1) for i in range(n)]
        def backtrack(l: List[int], idx: int = 0):
            if idx == n:
                heappush(h, "".join([str(i) for i in l]))
            else:
                for i in range(idx, n):
                    l[i], l[idx] = l[idx], l[i]
                    backtrack(l, idx + 1)
                    l[i], l[idx] = l[idx], l[i]
        backtrack(l)
        res = None
        for i in range(k):
            res = heappop(h)
        return res