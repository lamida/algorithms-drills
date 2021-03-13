# https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start: int = 0, current: List[int] = []):
            if len(current) == k:
                output.append(current[:])
            else:
                for i in range(start, len(nums)):
                    current.append(nums[i])
                    backtrack(i + 1, current)
                    current.pop()
        
        output = []
        for k in range(len(nums) + 1):
            backtrack()    
        return output

        # Another approach
        def subsets(self, nums: List[int]) -> List[List[int]]:
            result = []
            def backtrack(candidates: List[int], depth: int = 0):
                if depth == len(nums):
                    result.append(candidates[:])
                else:
                    backtrack(candidates + [nums[depth]], depth + 1)
                    backtrack(candidates, depth + 1)
            backtrack([])
            return result