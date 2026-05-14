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
        # 🐛 BUG 1: si el nodo ya es la head, no hay nada que hacer.
        # Sin este early-return, más abajo terminás haciendo
        # self.head.prev = node y node.next = self.head sobre el MISMO nodo,
        # creando un ciclo (node.next == node).
        if node is self.head:
            return

        if node.prev is not None:
            node.prev.next = node.next

            # 🐛 BUG 2: cuando el nodo está en el MEDIO, te olvidás de
            # reconectar el prev del sucesor. Queda apuntando a un nodo
            # que ya no está en su posición -> lista corrupta.
            if node.next is not None:
                node.next.prev = node.prev   # ✅ FIX

            if node.next is None:
                self.tail = node.prev

        node.prev = None

        # 🐛 BUG 3: si self.head es None (lista vacía, caso de inserción
        # de un nodo nuevo cuando aún no había head), esto explota con
        # AttributeError. En tu put() lo evitás con el if current_use == 1,
        # pero conceptualmente move_to_head NO debería usarse para insertar
        # un nodo nuevo. Aun así, lo cubrimos por las dudas.
        if self.head is not None:
            self.head.prev = node

        node.next = self.head

        self.head = node

        # 🐛 BUG 4: si la lista estaba vacía, también hay que setear la tail.
        if self.tail is None:
            self.tail = node   # ✅ FIX

    def clean_tail(self):
        if self.current_use > self.capacity:
            del self.keys[self.tail.key]

            # 🐛 BUG 5: si después de evictar quedaría 0 nodos (capacity = 0
            # o casos extremos), self.tail.prev es None y self.tail.prev.next
            # explota. Hay que manejar el caso.
            if self.tail.prev is not None:
                self.tail.prev.next = None
                self.tail = self.tail.prev
            else:
                # único nodo, la lista queda vacía
                self.head = None
                self.tail = None

            self.current_use -= 1

    def get(self, key: int) -> int:
        if key in self.keys:
            node = self.keys[key]
            self.move_to_head(node)
            self.print()
            return node.val
        self.print()
        return -1

    def print(self):
        head = self.head
        text = ""
        while head:
            text += "-> " + str(head.key)
            head = head.next
        print(text)

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
                # 🐛 BUG 6 (conceptual): estás usando move_to_head para
                # INSERTAR un nodo que todavía no está en la lista.
                # Funciona "de casualidad" porque node.prev es None y
                # entra al camino correcto, pero es frágil. Lo dejo así
                # porque con los fixes de arriba ya no rompe, pero idealmente
                # tendrías una función _add_front separada.
                self.move_to_head(new_node)
                self.clean_tail()
        self.print()