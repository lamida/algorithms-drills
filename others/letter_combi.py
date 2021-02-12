# https://leetcode.com/explore/interview/card/facebook/53/recursion-3/267/
from typing import List
class Solution:
    def __init__(self):
        self.d = {
            1: "",
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno", 
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
    def letterCombinations(self, digits: str) -> List[str]:
        print(f"call {digits}")
        if digits == "":
            return []
        
        ll = []
        d = digits[0]
        for l in self.d[int(d)]:
            x = self.letterCombinations(digits[1:])
            print(x)
            ll = ll + [l] + x
        return ll

if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))