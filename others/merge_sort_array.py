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
            while j < len(nums2) and i < len(nums1):
                a = nums1[i]
                b = nums2[j]
                if i <= m:
                    if a < b:
                        i+=1
                    else:
                        nums1.insert(i, b)
                        nums1.pop()
                        i+=1
                        j+=1
                else: 
                    nums1[i] = nums2[j]
                    i+=1
                    j+=1

