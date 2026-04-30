class MyHashSet:

    def __init__(self):
        self.size = 1007
        self.values = [[] for self.size in range(0, self.size)]

    def add(self, key: int) -> None:
        key_to_insert = key % self.size
        if key not in self.values[key_to_insert]:
            self.values[key_to_insert].append(key)

    def remove(self, key: int) -> None:
        key_to_insert = key % self.size
        if key in self.values[key_to_insert]:
            self.values[key_to_insert].remove(key)

    def contains(self, key: int) -> bool:
        key_to_insert = key % self.size
        return key in self.values[key_to_insert]