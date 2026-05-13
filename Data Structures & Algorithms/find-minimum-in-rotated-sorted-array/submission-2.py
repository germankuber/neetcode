from collections import defaultdict
from typing import List, Optional

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        
        right = len(nums) - 1
        
        while left < right:
            
            mid =  (left + right) // 2
            
            highest_number = nums[right]
            
            mid_number =  nums[mid]
            
            if mid_number > highest_number:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]