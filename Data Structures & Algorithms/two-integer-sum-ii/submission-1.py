from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    
        for index, number in enumerate(numbers):
            
            for index_2, number_2 in enumerate(numbers[index:]):
                
                if number + number_2 == target:
                    return [index + 1, index_2 + index + 1]
                
                