from collections import defaultdict
from typing import List
class Solution:
    # Using disjoinset
    class DisjoinSet:
        def __init__(self, n: int):
            self.s = [-1] * n

        def union(self, i: int, j: int):
            root_i = self.find(i)
            root_j = self.find(j)
            if root_i != root_j:
                self.s[root_i] = root_j

        def find(self, i: int) -> int:
            return i if self.s[i] < 0 else self.find(self.s[i])

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dj = Solution.DisjoinSet(n)
        for v1, v2 in edges:
            dj.union(v1, v2)
        
        count = 0
        for i in dj.s:
            if i == -1:
                count += 1
        return count

    def countComponents_dfs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        visited = [False for _ in range(n)]

        def dfs(i: int):
            visited[i] = True
            for v in graph[i]:
                if not visited[v]:
                    dfs(v)

        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)

        return count

if __name__ == "__main__":
    s = Solution()
    # print(s.countComponents_dfs(5, [[0,1],[1,2],[3,4]]))
    res = s.countComponents(5, [[0,1],[1,2],[3,4]])
    print(res)
