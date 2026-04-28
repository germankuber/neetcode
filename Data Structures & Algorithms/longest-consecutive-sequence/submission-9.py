from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        max_total = 0      
        for num in numbers:
            if num - 1 not in numbers:
                counter = num
                total = 0
                while counter in numbers:
                    total += 1
                    counter += 1
                if total > max_total:
                    max_total = total
                    
        return max_total
        