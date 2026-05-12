from collections import defaultdict
from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter = defaultdict(int)
        left = 0
        max_length = 0
        for right in range(len(s)):
            
            current_char = s[right]
            
            while letter[current_char] != 0:
                
                remove_letter = s[left]
                
                letter[remove_letter] -= 1
                
                left += 1
                
            letter[current_char] += 1
            
            max_length = max(max_length, right - left + 1)
            
        return max_length            
            