from typing import List
class Solution:
    def __init__(self):
        self.cache = {}

    # https://leetcode.com/problems/pascals-triangle
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = [None] * (i + 1)
            row[0], row[-1] = 1, 1
            for j in range(1, len(row) - 1):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]    
            triangle.append(row)
        return triangle

    # https://leetcode.com/problems/pascals-triangle-ii
    def getRow(self, rowIndex: int) -> List[int]:
        def getRC(row: int, col: int) -> int:
            key = str(row) + str(col)
            if row == 0 or col == 0 or row == col:
                return 1
            if self.cache.get(key) is None:
                self.cache[key] = getRC(row-1, col-1) + getRC(row-1, col)
            return self.cache[key]

        r = []
        for c in range(rowIndex+1):
            r.append(getRC(rowIndex, c))
        return r
            

if __name__ == "__main__":
    s = Solution()
    print(s.generate(0))
    print(s.generate(1))
    print(s.generate(2))
    print(s.generate(3))