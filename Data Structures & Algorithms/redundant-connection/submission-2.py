class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        num_nodes = len(edges)
        parent = [i for i in range(num_nodes + 1)]
        size = [1] * (num_nodes + 1)

        def find_root(node):
            if node != parent[node]:
                parent[node] = find_root(parent[node])
            return parent[node]

        def union(node_a, node_b):
            root_a, root_b = find_root(node_a), find_root(node_b)
            if root_a == root_b:
                return False
            if size[root_a] > size[root_b]:
                parent[root_b] = root_a
                size[root_a] += size[root_b]
            else:
                parent[root_a] = root_b
                size[root_b] += size[root_a]
            return True

        # Recorro las aristas en orden. La primera que NO se puede unir
        # (porque sus dos nodos ya están en el mismo componente) es la redundante:
        # cierra un ciclo.
        for node_a, node_b in edges:
            if not union(node_a, node_b):
                return [node_a, node_b]