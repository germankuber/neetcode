from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        results = []
        
        subset = []
        
        def dfs(index: int):
            if index >= len(nums):
                results.append(subset[:])
                return
            
            
            current_number = nums[index]
            
            subset.append(current_number)
            dfs(index + 1)
            
            subset.pop()
            
            dfs(index + 1)
            
        dfs(0)
        return results
        