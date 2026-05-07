from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n_value = len(nums) // 3
        values = {}
        result = []
        for n in nums:
            if n not in values:
                values[n] = 0
            if values[n] is None:
                continue
            values[n] += 1
            
            if values[n] > n_value:
                result.append(n)
                values[n] = None
                
        return result
        