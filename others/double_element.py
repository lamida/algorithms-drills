# https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/
from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        i = 0
        while i < len(arr):
            j = 0
            while j < len(arr):
                if i != j and (arr[i] == 2 * arr[j] or arr[j] == 2*arr[i]):
                    return True
                j+=1
            i+=1
        return False

if __name__ == "__main__":
    s = Solution()
    x = s.checkIfExist([-20,8,-6,-14,0,-19,14,4])
    print(x)