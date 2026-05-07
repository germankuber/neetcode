from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidates = defaultdict(int)
        amount = len(nums) // 3
        for num in nums:
            
            if len(candidates.keys()) == 2:
                if num in candidates:
                    candidates[num] += 1
                else:
                    for num in candidates:
                        candidates[num] -= 1
                    candidates = { k : v for k, v in candidates.items() if v != 0}
            else:
                if num not in candidates:
                    candidates[num] = 0
                candidates[num] += 1
                
        candidates = { k : amount for k,_ in candidates.items()}
        result = []
        for num in nums:
            if num in candidates:
                candidates[num] -= 1
                if candidates[num] == -1:
                    result.append(num)
        return result
            
        