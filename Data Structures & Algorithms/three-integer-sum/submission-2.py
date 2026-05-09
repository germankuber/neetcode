from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums )
        prev_number = None
        results = []
        for index, negative in enumerate(sorted_nums):
            if sorted_nums[index] > 0:
                break
            if index > 0 and sorted_nums[index] == sorted_nums[index - 1]:
                continue
            left, right = index + 1, len(sorted_nums) - 1
            
            while left < right:
                if negative + (sorted_nums[left] + sorted_nums[right]) > 0:
                    right -= 1
                elif negative + (sorted_nums[left] + sorted_nums[right]) < 0:
                    left += 1
                elif negative + (sorted_nums[left] + sorted_nums[right]) == 0:
                    results.append([negative, sorted_nums[left], sorted_nums[right]])
                    while left < right and sorted_nums[left] == sorted_nums[left + 1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        
        return results
            
            