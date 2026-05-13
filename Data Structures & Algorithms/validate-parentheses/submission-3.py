from collections import defaultdict
from typing import List

class Solution:
    def isValid(self, text: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        
        for char in text:
            if char not in pairs:
                # es un caracter de apertura → push
                stack.append(char)
            else:
                # es un caracter de cierre → tiene que matchear con el tope
                if not stack or stack.pop() != pairs[char]:
                    return False
        
        return not stack