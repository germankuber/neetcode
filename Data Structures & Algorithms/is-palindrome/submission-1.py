class Solution:
    def isPalindrome(self, text: str) -> bool:
        left, right = 0, len(text) - 1
        
        while left <= right:
            char_left  = text[left]
            char_right = text[right]
            if not self.is_valid_char(char_left):
                left += 1
                continue
            if not self.is_valid_char(char_right):
                right -= 1
                continue
            if char_left.upper() == char_right.upper():
                left  += 1 
                right -= 1
            else:
                return False
        
        return True
            
        
    def is_valid_char(self, char: str)-> bool:
        char_value = ord(char)
        
        if char_value >= 97 and char_value <= 122:
            return True
        elif char_value >= 65 and char_value <= 90:
            return True
        elif char_value >= 48 and char_value <= 57:
            return True
        
        return False
            
        