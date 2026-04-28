from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = {}
        first_element = {}
        for num in nums:
            previous = num - 1
            next = num + 1
            
            if num not in numbers:
                numbers[num] = True
                
        for num in list(numbers.keys()):
            if num - 1 not in numbers:
                first_element[num] = True
        max_total = 0
        for elem in list(first_element.keys()):
            counter = elem
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