from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        def execute_permute(index: int)-> List[List[int]]:
            if index >= len(nums):
                return [[]]
            
            current_number = nums[index]
            
            results =  execute_permute(index + 1)
            
            local_result = []
            for result in results:
                for position_to_insert in range(0, len(result) + 1):
                    new_permutation = result[:]
                    new_permutation.insert(position_to_insert, current_number)
                    local_result.append(new_permutation)
                    
            return local_result
                
        return execute_permute(0)    