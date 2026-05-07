from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        prefix = defaultdict(int)
        
        prefix[0] = 1
        result = 0
        
        for index in range(len(nums)):
            
            current_value = nums[index]
            
            total += current_value
            
            difference = prefix[total - k]
                        
            prefix[total] += 1
            if difference > 0:
                result += difference
        
        return result            

            
        
        

