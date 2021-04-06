from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for col in range(n)] for row in range(n)]
        results = []

        def valid(row: int, col: int) -> bool:
            for r in range(row):
                for c in range(n):
                    if board[r][c] == "Q" and (r + c == row + col or row + c == col + r or col == c):
                        return False
            return True

        def dfs(row: int = 0):
            if row == n:
                results.append(["".join(row) for row in board])
            else:
                for col in range(n):
                    if valid(row, col):
                        board[row][col] = "Q"
                        dfs(row + 1)
                        board[row][col] = "."

        dfs()
        return results

if __name__ == "__main__":
    s = Solution();
    res = s.solveNQueens(4)
    print(res)