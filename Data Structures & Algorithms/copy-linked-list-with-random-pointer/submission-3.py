from typing import List, Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_nodes = {}
        
        head_to_iterate = head
        def get_node(node: 'Optional[Node]') -> 'Optional[Node]':
            if node is None:
                return None
            if node in new_nodes:
                return new_nodes[node]
            new_node = Node(node.val)
            new_nodes[node] = new_node
            
            return new_node
        while head_to_iterate:
            next_node = head_to_iterate.next
            random    = head_to_iterate.random
            
            new_node_next_node = get_node(next_node)
            
            new_node_random_node = get_node(random)
            
            current_node = get_node(head_to_iterate)
            
            if current_node.next is None:
                current_node.next = new_node_next_node
            if current_node.random is None:
                current_node.random = new_node_random_node
            
            head_to_iterate = head_to_iterate.next
        
        return get_node(head)
