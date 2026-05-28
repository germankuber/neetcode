class Node:
    def __init__(self, current: str = "", is_final: bool = False):
        self.data = {}
        self.is_final = is_final
        self.current = current

    def add_word(self, word: str) -> None:
        if not word:
            self.is_final = True
            return
        letter = word[0]
        if letter not in self.data:
            self.data[letter] = Node(letter, False)
        self.data[letter].add_word(word[1:])

    def find(self, word: str):
        """Devuelve el nodo del último char, o None si el camino no existe."""
        node = self
        for letter in word:
            if letter not in node.data:
                return None
            node = node.data[letter]
        return node


class PrefixTree:
    def __init__(self):
        self.root = Node("", False)

    def insert(self, word: str) -> None:
        self.root.add_word(word)

    def search(self, word: str) -> bool:
        node = self.root.find(word)
        return node is not None and node.is_final

    def startsWith(self, prefix: str) -> bool:
        return self.root.find(prefix) is not None