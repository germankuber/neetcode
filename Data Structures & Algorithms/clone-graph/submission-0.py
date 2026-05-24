from typing import Optional, List

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node :
            return None
        visited_node = {}
        def clone_node(node: Optional['Node']) ->'Node':
            if not node:
                return []
            new_node = Node(node.val)
            if node not in visited_node:
                visited_node[node] = new_node
            nodes = []
            
            for neighbor in node.neighbors:
                if neighbor not in visited_node:
                    nodes.append(clone_node(neighbor))
                else:
                    nodes.append(visited_node[neighbor])
            new_node.neighbors = nodes
            return new_node
        
        
        
        return clone_node(node)   