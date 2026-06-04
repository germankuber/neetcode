from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        
        def dfs(index: int, total: int) -> int:
            
            if index == len(nums):
                return total
            
            
            return dfs(index + 1, total) + dfs(index + 1, total ^ nums[index])
        
        
        return dfs(0,0)