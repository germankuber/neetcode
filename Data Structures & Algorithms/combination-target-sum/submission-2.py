from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        solutions = []
        
        iterations = []
        
        def process(index: int,  total:int):
            
            if total == target:
                solutions.append(iterations[:])
                return
                
            if total > target or index >= len(nums):
                return
            
            
            current_number = nums[index]
            
            iterations.append(current_number)
            process(index, total + current_number)
            
            iterations.pop()
            
            process(index + 1, total)
                
        process(0, 0)  

        return solutions