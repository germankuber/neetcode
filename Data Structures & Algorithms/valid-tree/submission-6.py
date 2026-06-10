class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adjacency : dict[int, list[int]]= defaultdict(list)
        for node_a, node_b in edges:
            adjacency[node_a].append(node_b)
            adjacency[node_b].append(node_a)

        visited = set()

        def dfs(node : int):
            visited.add(node)
            for neighbor in adjacency[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(0)
        return len(visited) == n