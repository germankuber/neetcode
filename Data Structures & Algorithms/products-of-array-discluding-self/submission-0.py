from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array_right = [1] * len(nums)
        prefix_array_left = [1] * len(nums)
        pointer_left = 0
        first = True
        while pointer_left < len(nums):
            
            pointer_right = len(nums) - pointer_left - 1

            if first:
                first = False
            else:
                number_left_to_process = nums[pointer_left - 1]
                number_right_to_process = nums[pointer_right + 1]
                prefix_array_left[pointer_left] = prefix_array_left[pointer_left - 1] * number_left_to_process
                prefix_array_right[pointer_right]  = prefix_array_right[pointer_right + 1] * number_right_to_process
                
                
            
            
            pointer_left += 1
        result = [1] * len(nums) 
        index = 0
        for index, value in enumerate(prefix_array_left):
            result[index] = value * prefix_array_right[index]
            
        return result