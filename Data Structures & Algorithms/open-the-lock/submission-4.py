from collections import deque
from typing import List, Optional


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        graph = deque()
        first_node = [0,0,0,0]
        graph.append(first_node)
        dead = set()
        
        for item in deadends:
            if item == "0000":
                return -1
            dead.add(item)
            

        
        visited = set()
        def add_to_graph(current_item:List[int]) -> Optional[int]:
            
            def operate_with_mod(value:int, value_to_operate: int)-> int:
                if value == 0:
                    if value_to_operate == -1:
                        return 9
                elif value == 9:
                    if value_to_operate == 1:
                        return  0
                    
                return value + value_to_operate
                    
            
            
            for index in range(4):
                values_operated = operate_with_mod(current_item[index],1)
                copy = current_item[::]
                copy[index] = values_operated
                
                key = "".join(map(str, copy))
                
                if key not in dead  and key not in visited:
                    if key == target:
                        return key
                    graph.append(copy)
                    visited.add(key)
                    
                values_operated = operate_with_mod(current_item[index],-1)
                copy = current_item[::]
                copy[index] = values_operated
                key = "".join(map(str, copy))
                if key not in dead and key not in visited:
                    if key == target:
                        return key
                    graph.append(copy)
                    visited.add(key)
            return None

            
                
        
        
        counter = 0
        while graph:
            
            counter += 1
            
            for _ in range(len(graph)):
                current_item = graph.popleft()
                result = add_to_graph(current_item)
                if  result is not None:
                    return counter
        
        return -1
                