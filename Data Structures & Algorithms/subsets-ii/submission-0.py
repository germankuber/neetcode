from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        results = []
        
        nums.sort()
        
        
        def backtracking(index: int, sub_set : List[int]):
            
            if index == len(nums):
                results.append(sub_set[:])
                return
            
            sub_set.append(nums[index])
            backtracking(index + 1, sub_set)
            
            sub_set.pop()
            
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
                
            backtracking(index + 1, sub_set)
        
        backtracking(0, [])
        
        return results