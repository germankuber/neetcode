from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        characters = defaultdict(int)
        
        longest_window = 0
        
        left = 0
        
        for right in range(len(s)):
            
            current_character  = s[right]
            
            characters[current_character] += 1
            
            longest_character = max(characters.values())
            
            current_window_size = right - left + 1
            
            while (current_window_size - longest_character) > k:
                
                character_to_remove = s[left]
                characters[character_to_remove] -= 1
                left += 1
                longest_character = max(characters.values())
                current_window_size = right - left + 1
                
            longest_window = max(longest_window,right - left + 1 )
        return longest_window