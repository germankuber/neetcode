from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            value = nums[mid]
            if value > target:
                right = mid - 1
            elif value < target:
                left = mid + 1
            else:
                return mid
        return left
             