class HashMap:
    class Node:
        def __init__(self, key, value, count = 1):
            self.count = count
            self.key = key
            self.value = value
            

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
        self.__count += 1

        if self.__memory[hash] is None:
            self.__memory[hash] = HashMap.Node(key, value)
            return
        else:
            i = 1
            while self.__memory[hash] is not None:
                hash = (hash + i**2) % self.__size
                i += 1
            
            self.__memory[hash] = HashMap.Node(key, value)

    def remove(self, key: any):
        """
        удалить элемент по ключу
        """
        for i in range(self.__size):
            if self.__memory[i] is not None:
                if self.__memory[i].key == key:
                    self.__memory[i] = None
                    self.__count -= 1
                    return 

    def get(self, key) -> any:
        """
        найти значение по ключу
        """
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
