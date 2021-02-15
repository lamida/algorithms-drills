# https://leetcode.com/problems/n-queens
class Solution1:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve(q: List[int], r: int, solutions: List[List[int]]):
            if r == len(q):
                solutions.append(q.copy())
            else:
                for j in range(len(q)):
                    legal = True
                    for i in range(r):
                        if q[i] == j or q[i] == j + r - i or q[i] == j - r + i:
                            legal = False
                    if legal:
                        q[r] = j
                        solve(q, r + 1, solutions)
                        
        candidates = []
        q = [0] * n
        solve(q, 0, candidates)
        
        solutions = []
        for candidate in candidates:
            solution = []
            for cell in candidate:
                row = ["."] * n
                row[cell] = "Q"
                solution.append("".join(row))
            solutions.append(solution)
        return solutions

# https://leetcode.com/problems/n-queens-ii
class Solution2:
    def totalNQueens(self, n: int) -> int:
        def solve(q: List[int], r: int, res):
            if r == len(q):
                res["total"] +=1
            else:
                for j in range(len(q)):
                    legal = True
                    for i in range(r):
                        if q[i] == j or q[i] == j + r - i or q[i] == j - r + i:
                            legal = False
                    if legal:
                        q[r] = j
                        solve(q, r + 1, res)
        res = {"total": 0}
        q = [0] * n
        solve(q, 0, res)
        return res["total"]
