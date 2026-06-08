from typing import Counter, List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        permutations = []
        
        counters = Counter(nums)

        def backtracking() -> bool:
            if len(permutations) == len(nums):
                result.append(permutations[::])
                return
            
            
            for count in counters:
                if counters[count] <= 0:
                    continue
                
                counters[count] -= 1
                
                permutations.append(count)
                
                backtracking()
                
                
                counters[count] += 1 
                
                permutations.pop()
            
        backtracking()
        
        return result
        