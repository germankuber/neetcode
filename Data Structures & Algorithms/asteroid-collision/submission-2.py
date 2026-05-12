from collections import defaultdict
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            
            stack.append(asteroid)
            
            while len(stack) >= 2:
                
                top = stack[-2]
                
                if top > 0 and asteroid < 0 :
                    if abs(asteroid) > abs(top):
                        stack.pop()
                        stack.pop()
                        stack.append(asteroid)
                    elif abs(asteroid) == abs(top): 
                        stack.pop() 
                        stack.pop()
                        break
                    elif abs(top) > abs(asteroid):
                        stack.pop()
                        break
                    else:
                        break
                else:
                    break
                
        return stack