from collections import defaultdict
from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        first = defaultdict(int)
        for c in s1:
            first[c] += 1
            
        left  = 0
        right = len(s1)
        
        def validate(first_dict : dict, sub_str :str) -> bool:
            for c in sub_str:
                if c in first_dict:
                    first_dict[c] -= 1
                else:
                    return False
            return max(first_dict.values()) == 0 
        
        while right <= len(s2):
            if validate(first.copy(), s2[left:right]):
                return True
            else:
                left  += 1
                right += 1
            
            
                
        return max(first.values()) == 0
            
            