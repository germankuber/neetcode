class Node:
    def __init__(self, current: str = "", is_final: bool = False):
        self.data = {}
        self.is_final = is_final
        self.current = current

    def add_word(self, word: str) -> None:
        node = self
        for letter in word:
            if letter not in node.data:
                node.data[letter] = Node(letter, False)
            node = node.data[letter]
        node.is_final = True


class WordDictionary:
    def __init__(self):
        self.root = Node("", False)

    def addWord(self, word: str) -> None:
        self.root.add_word(word)

    def search(self, word: str) -> bool:
        return self._search(self.root, word, 0)

    def _search(self, node: Node, word: str, index: int) -> bool:
        if index == len(word):
            return node.is_final

        letter = word[index]

        if letter == ".":
            for child in node.data.values():
                if self._search(child, word, index + 1):
                    return True
            return False

        if letter not in node.data:
            return False
        return self._search(node.data[letter], word, index + 1)