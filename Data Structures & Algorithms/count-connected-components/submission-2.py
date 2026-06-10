from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(dict)

        for node_1, node_2 in edges:
            graph[node_1][node_2] = True
            graph[node_2][node_1] = True  
            
            
        visited = set()
        
        
        def dfs(current:int ):
            visited.add(current)
            for neighbor in graph.get(current, {}):
                if neighbor not in visited:
                    dfs(neighbor)
                    
        
        
        count = 0
        for item in range(n):
            if item not in visited:
                count += 1
                dfs(item)
                
        return count