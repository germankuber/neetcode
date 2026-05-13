from collections import defaultdict
from typing import List

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        included = defaultdict(int)
        
        for char in t:
            included[char] += 1
            
        left = 0
        current_characters = defaultdict(int)
        shortest = None
        for right in range(len(s)):
            current_char = s[right]
            current_characters[current_char] += 1
            
            while self.is_valid(included,current_characters):
                if shortest == None or shortest[0] > (right - left + 1):
                    shortest = (right - left + 1, left, right)
                    
                remove_character = s[left]
                current_characters[remove_character] -= 1
                if current_characters[remove_character] == 0:
                    del current_characters[remove_character]        
                left += 1
                    
        if shortest is None:
            return ""
        return s[shortest[1]: shortest[2] + 1]        
            
    def is_valid(self,  included: dict, current: dict)-> bool:
        
        for key, value in included.items():
            value_to_compare = current.get(key, 0)
            if value > value_to_compare:
                return False
        return True