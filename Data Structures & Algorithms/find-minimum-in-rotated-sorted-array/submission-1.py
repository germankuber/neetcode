
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        while low < high:
            
            mid = (low + high) // 2
            
            max_number = nums[high]
            
            mid_number = nums[mid]
            
            if mid_number >  max_number:
                low = mid + 1
            else:
                high = mid
                
        return nums[low]