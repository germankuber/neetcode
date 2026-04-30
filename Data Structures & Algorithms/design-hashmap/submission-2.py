class MyHashMap:

    def __init__(self):
        self.value_key = 1007
        self.values = [[] for _ in range(self.value_key)]

    def put(self, key: int, value: int) -> None:
        values = self.values[key % self.value_key]
        for index,values_to_iterate in enumerate(values):
            if values_to_iterate[0] == key:
                values[index] = (key, value)
                return
        values.append((key,value))

    def get(self, key: int) -> int:

        key_to_insert = key % self.value_key
        values = self.values[key_to_insert]
        for item in values:
            if item[0] == key:
                return item[1]
        return -1
            
        

    def remove(self, key: int) -> None:

        key_to_insert = key % self.value_key
        values = self.values[key_to_insert]
        for index in range(0, len(values)):
            value = values[index]
            if value[0] == key:
                values.pop(index)
                break
