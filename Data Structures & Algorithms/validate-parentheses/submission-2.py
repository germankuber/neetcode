from collections import defaultdict
from typing import List

class Solution:
    def isValid(self, text: str) -> bool:
        stack = []
        
        for char in text:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                last_value = stack[-1]
                match char:
                    case ")":
                        if last_value == "(":
                            stack.pop()
                        else:
                            return False
                    case "]":
                        if last_value == "[":
                            stack.pop()
                        else:
                            return False
                    case "}":
                        if last_value == "{":
                            stack.pop()
                        else:
                            return False
        return len(stack) == 0