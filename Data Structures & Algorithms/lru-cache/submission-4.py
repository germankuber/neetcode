from typing import List, Optional


class Node:
    def __init__(self, key: int, val: int, next: 'Node' = None, prev: 'Node' = None):
        self.key = key
        self.next = next
        self.prev = prev
        self.val = val


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_use: int = 0
        self.keys: dict[int, Node] = {}
        self.head: Node = None
        self.tail: Node = None

    def move_to_head(self, node: Node):
        if node is self.head:
            return

        if node.prev is not None:
            node.prev.next = node.next

            if node.next is not None:
                node.next.prev = node.prev

            if node.next is None:
                self.tail = node.prev

        node.prev = None

        if self.head is not None:
            self.head.prev = node

        node.next = self.head

        self.head = node

        if self.tail is None:
            self.tail = node

    def clean_tail(self):
        if self.current_use > self.capacity:
            del self.keys[self.tail.key]

            if self.tail.prev is not None:
                self.tail.prev.next = None
                self.tail = self.tail.prev
            else:
                self.head = None
                self.tail = None

            self.current_use -= 1

    def get(self, key: int) -> int:
        if key in self.keys:
            node = self.keys[key]
            self.move_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            node = self.keys[key]
            node.val = value
            self.move_to_head(node)
        else:
            new_node = Node(key, value)
            self.keys[key] = new_node
            self.current_use += 1

            if self.current_use == 1:
                self.tail = new_node
                self.head = new_node
            else:
                self.move_to_head(new_node)
                self.clean_tail()