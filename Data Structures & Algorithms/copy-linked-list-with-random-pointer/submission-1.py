from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_nodes = {}

        def get_node(node: 'Optional[Node]') -> 'Optional[Node]':
            if node is None:
                return None
            if node not in new_nodes:
                new_nodes[node] = Node(node.val)
            return new_nodes[node]

        curr = head
        while curr:
            copy = get_node(curr)
            copy.next = get_node(curr.next)
            copy.random = get_node(curr.random)
            curr = curr.next

        return get_node(head)