from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = {}
        first_element = {}
        for num in nums:
            if num not in numbers:
                numbers[num] = True
        max_total = 0      
        for num in list(numbers.keys()):
            if num - 1 not in numbers:
                counter = num
                total = 0
                while True:
                    if counter in numbers:
                        total += 1
                    else:
                        break
                    counter += 1
                if total > max_total:
                    max_total = total
                    
        return max_total