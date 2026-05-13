from collections import defaultdict
from typing import List, Optional

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        
        def validate(nums: List[int]) -> Optional[int]:
            if len(nums) == 0:
                return None
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return min(nums[0], nums[1])
            
            to_split = len(nums) // 2
            
            left  = nums[:to_split]
            right = nums[to_split:] 
            
            left_min  = validate(left)
            
            right_min = validate(right)
            
            min_value =  get_min(left_min, right_min)
            
            return min_value
            
            
        
        def get_min(right: Optional[int], left: Optional[int])-> int:
            if left is not None and right is not None:
                return min(left, right)
            elif left is None:
                return right
            elif right is None:
                return left
            return None
        
        min_value = validate(nums)
        
        return min_value
                
            
        