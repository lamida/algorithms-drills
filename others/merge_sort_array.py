# TODO: https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/309/
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while i < len(nums1):
            if j < n:
                if i > m - 1:
                    nums1[i] = nums2[j]
                    i += 1
                    j += 1
                    m += 1
                elif nums1[i] <= nums2[j]:
                    i += 1
                elif nums1[i] > nums2[j]:
                    k = i
                    while k < m:
                        nums1[k + 1] = nums1[k]
                        k += 1
                    nums1[i] = nums2[j]
                    i += 1
                    j += 1

if __name__ == "__main__":
    s = Solution()
    s.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
        
