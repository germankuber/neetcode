from typing import Optional, List

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Mapa: nodo original -> su copia. Sirve para dos cosas:
        # 1) cortar la recursión en ciclos
        # 2) reusar la MISMA copia cuando un nodo es vecino de varios
        visited_node = {}

        def clone_node(node: Optional['Node']) -> Optional['Node']:
            # GUARD: si ya empecé a clonar este nodo, devuelvo su copia y corto.
            # Esto es lo que evita el loop infinito en grafos con ciclos.
            if node in visited_node:
                return visited_node[node]

            # Creo la copia y la registro ANTES de recursar a los vecinos.
            # El orden importa: si la registrara después, un ciclo me mandaría
            # de vuelta a este nodo antes de que esté en el mapa -> recursión infinita.
            new_node = Node(node.val)
            visited_node[node] = new_node

            # Ahora sí recorro los vecinos. La recursión se encarga sola del corte:
            # si el vecino ya está clonado, clone_node devuelve la copia del mapa.
            for neighbor in node.neighbors:
                new_node.neighbors.append(clone_node(neighbor))

            return new_node

        # Caso borde: grafo vacío -> None (NO lista vacía)
        return clone_node(node) if node else None