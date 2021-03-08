# https://leetcode.com/problems/course-schedule/
# Still TODO
from typing import List, Dict, Set
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node: int, white_set: Set[int], grey_set: Set[int], black_set: Set[int], g: Dict[int, List[int]]):
            white_set.remove(node)
            grey_set.add(node)

            for n in g[node]:
                if n in black_set:
                    continue
                if n in grey_set: 
                    return True
                if dfs(n, white_set, grey_set, black_set, g):
                    return True
            grey_set.remove(node)
            black_set.add(node)
            return False

        def detect_cycle(g: Dict[int, List[int]]) -> bool:
            white_set = set()
            grey_set = set()
            black_set = set()

            for i in range(numCourses):
                white_set.add(i)
            s = white_set.copy()
            for n in s:
                if dfs(n, white_set, grey_set, black_set, g):
                    return True
            return False

        def topo_util(node: int, visited: List[bool], stack: List[int], g: Dict[int, List[int]]):
            visited[node] = True
            for n in g[node]:
                topo_util(n, visited, stack, g)
            stack.append(node)
            
        visited = [False for _ in range(numCourses)]
        stack = []
        g = defaultdict(list)

        for (course, prereq) in prerequisites:
            g[prereq].append(course)

        if detect_cycle(g):
            return False
            
        for n in visited:
            if not visited[n]:
                topo_util(n, visited, stack, g)
                
        return len(stack) == numCourses

if __name__ == "__main__":
    s = Solution()
    res = s.canFinish(2, prerequisites=[[1, 0]])
    print(res)
    res = s.canFinish(2, prerequisites=[[1, 0], [0, 1]])
    print(res)