# https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        for i in range(len(mat)):
            s += mat[i][i] + mat[i][-i - 1]
        center = len(mat)//2
        sub = 0 if len(mat) % 2 == 0 else mat[center][center]
        return s - sub