# https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        found = 0
        while i < len(nums):
            c = nums[i]
            if c==val:
                found +=1
                j = i
                while j < len(nums)-1:
                    nums[j] = nums[j+1]
                    j+=1
                nums[-found] = -1 
            else:
                i+=1
        return len(nums) - found

if __name__ == "__main__":
    s = Solution()
    x = s.removeElement([4,4,0,1,0,2], 0)
    print(x)