from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        buffer = nums[-k:] + nums[:-k]
        print("buffer: ", buffer, "k: ", k)
        for i in range(len(nums)):
            nums[i] = buffer[i]

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4,5,6]
    k = 1
    s.rotate(nums, k)
    print(nums)