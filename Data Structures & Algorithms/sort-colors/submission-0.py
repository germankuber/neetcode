class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            
            number = nums[mid]
            
            match number:
                case 1:
                    mid += 1
                case 0:
                    nums[low], nums[mid] = nums[mid], nums[low]
                    mid += 1
                    low += 1
                case 2:
                    nums[high], nums[mid] = nums[mid], nums[high]
                    high -= 1
        
        return nums
        