from collections import defaultdict
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1. Chequeo de aristas (atajo del teorema)
        if len(edges) != n - 1:
            return False

        # 2. Lista de adyacencia (no dirigida → ambos sentidos)
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # 3. DFS desde el nodo 0 con visited set
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for vecino in adj[node]:
                dfs(vecino)

        dfs(0)

        # 4. ¿Visité todos los nodos?
        return len(visited) == n