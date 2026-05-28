from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        num_nodes: int = len(edges)

        # Al inicio, cada nodo es su propio padre (cada uno es raíz de su grupo)
        parent: List[int] = [i for i in range(num_nodes + 1)]




        def find_root(node : int) -> int:
            
            direct_parent = parent[node]
            
            if direct_parent == node:
                return node
            
            root = find_root(direct_parent)
            
            parent[node] = root
            
            return root
        
        
        def union(node_a : int, node_b : int) -> bool:
            
            root_a = find_root(node_a)
            
            root_b = find_root(node_b)
            
            if root_a == root_b:
                return False
            
            parent[root_a] = root_b
            
            return True
        
        
        for node_a, node_b  in edges:
            if not union(node_a, node_b):
                return [node_a, node_b]
            
   
