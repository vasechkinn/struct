class HashMap:
    def __init__(self):
        self.__count = 0
        self.__size = 100
        self.__memory = [None] * self.__size


    def add(self, key, value) -> None:
        """
        добавление элемента value по ключу key
        :param value: elem
        :param key: ключ
        """
        hash = self.__hash(key)

        if self.__memory[hash] is None:
            self.__memory[hash] = value
            return
        else:
            counter = 1
            while self.__memory[hash]: pass
            
            

    def get(self, key) -> any:
        hash = self.__hash(key)
        value = self.__memory[hash]

        if value is None:  raise ValueError(f"Value not exists by key: {key}")

        return value

    def exist_by_key(self, key):
        hash = self.__hash(key)
        value = self.__memory[hash]
        return not (value is None)

    def __hash(self, key) -> int:
        return hash(key) % self.__size


map = HashMap()

for i in range(0, 600, 1):
    print(f"Add:: key[{str(i)}]; value={i}")
    map.add(str(i), i)

print(HashMap.counter)


collection = {
    "пн": "mn",
    "вт": "tu"
}

collection["ср"] = "wn"
collection["вт"] = "tu2"
