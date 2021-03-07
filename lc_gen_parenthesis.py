#https://leetcode.com/problems/generate-parentheses
from typing import List

class Solution:
    def generateParethensis(self, n: int) -> List[str]:
        ans = []
        def gen(a: List[str] = []):
            if len(a) == 2 * n:
                if valid(a):
                    ans.append("".join(a))
            else:
                a.append("(")
                gen(a)
                a.pop()
                a.append(")")
                gen(a)
                a.pop()
        
        def valid(a: List[str]):
            bal = 0
            for i in a:
                if i == "(": bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        gen()
        return ans

    def generateParethensis2(self, n: int) -> List[str]:
        ans = []
        def backtrack(s = "", left = 0, right = 0):
            if len(s) == 2 * n:
                ans.append(s)
                return

            if left < n:
                backtrack(s + "(", left + 1, right)
            if right < left:
                backtrack(s + ")", left, right + 1)
            
        backtrack()
        return ans

if __name__ == "__main__":
    s = Solution()
    x = s.generateParethensis2(3)
    print(x)