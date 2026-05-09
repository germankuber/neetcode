from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        
        index = 0
        
        while index < length:
            
            current_num = nums[index]
            if current_num < 0:
                index += 1
            elif current_num <= length and current_num - 1 != index:
                to_change = nums[current_num - 1]
                
                nums[current_num - 1] = current_num
                
                nums[index] =  to_change
                
                if current_num == to_change:
                    index += 1
            else:
                index += 1
                
        found = len(nums) + 1
        for index, num in enumerate(nums):
            if num != index + 1:
                found = index + 1
                break
                
        return found