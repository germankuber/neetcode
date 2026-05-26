from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {}
        
        for node_1, node_2 in edges:
            
            if node_1 not in graph:
                graph[node_1] = {}
            
            if node_2 not in graph:
                graph[node_2] = {}
                
            graph[node_1][node_2] = True
            graph[node_2][node_1] = True
                

        visited = set()
        def dfs(current:int, parent: int) -> bool:
            
            visited.add(current)
            
            for neighbor in graph.get(current, {}).keys():
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                if not dfs(neighbor, current):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        
        return len(visited) == n
                
            