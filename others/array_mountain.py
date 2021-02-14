# https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/

from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i = 1
        j = 0
        stage = "start" # up then down
        while i < len(arr):
            j = i- 1
            c = arr[i]
            b = arr[j]
            
            if b == c:
                return False
            
            if c > b and (stage == "start" or stage == "up"):
                stage = "up"
                i+=1
                continue
            elif c < b and (stage == "up" or stage=="down"):
                stage = "down"
                i+=1
                continue
            else:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    x = s.validMountainArray([0,3,2,1])
    print(x)