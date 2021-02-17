# https://leetcode.com/problems/maximum-subarray
# This is cannonical divide and conquer problems.
# See also Cormen et all, chapter 4.

from typing import List
PREFIX = "| "
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def cross(nums: List[int], low: int, mid: int, high: int, depth: int = 0) -> (int, int, int):
            print(f"{PREFIX * depth}cross(low = {low}, mid = {mid}, high = {high})")
            left_sum = None
            max_left = None
            sum = 0
            for i in range(mid, low - 1, -1):
                sum += nums[i]
                if left_sum is None or sum > left_sum:
                    left_sum = sum
                    max_left = i
                    
            right_sum = None
            max_right = None
            sum = 0
            for i in range(mid+1, high + 1):
                sum += nums[i]
                if right_sum is None or sum > right_sum:
                    right_sum = sum
                    max_right = i
                    
            return (max_left, max_right, left_sum + right_sum)
        
        def mx(nums: List[int], low: int, high: int, depth: int = 0) -> (int, int, int):
            print(f"{PREFIX * depth}mx(low = {low}, high = {high})")
            if low == high:
                return (low, high, nums[low])
            else:
                mid = (low + high)//2
                left_low, left_high, left_sum = mx(nums, low, mid, depth + 1)
                right_low, right_high, right_sum = mx(nums, mid+1, high, depth + 1)
                cross_low, cross_high, cross_sum = cross(nums, low, mid, high, depth + 1)
                # TODO: why using > instead >= in these comparison gives wrong result?
                if left_sum >= right_sum and left_sum >= cross_sum:
                    return (left_low, left_high, left_sum)
                elif right_sum >= left_sum and right_sum >= cross_sum:
                    return (right_low, right_high, right_sum)
                else:
                    return (cross_low, cross_high, cross_sum)
        return mx(nums, 0, len(nums) - 1)[2]
        
if __name__ == "__main__":
    a = [-2,1,-3,4,-1,2,1,-5,4]
    a_expected = 6

    s = Solution()
    assert s.maxSubArray(a) == a_expected

    a = [-1,-1,-2,-2]
    a_expected = -1
    assert s.maxSubArray(a) == a_expected