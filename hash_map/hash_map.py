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

        if self.__memory[hash] is None:
            self.__memory[hash] = HashMap.Node(key, value)
            
        else:
            i = 1
            while self.__memory[hash] is not None:
                hash = (hash + i**2) % self.__size
                i += 1
                if self.__size <= i:
                    self.__realoc()
                    
            self.__memory[hash] = HashMap.Node(key, value, i)
        
        self.__count += 1

    def __realoc(self):
        old_memory = self.__memory
        self.__size *= 2
        self.__memory = [None] * self.__size

        for i in range(len(old_memory)):
            self.__memory.append(old_memory[i])

    def remove(self, key: any):
        """
        удалить элемент по ключу
        """
        hash = self.__hash(key)
        if self.__memory[hash].count == 1:
            self.__memory[hash] = None
            self.__count -= 1

        else:
            count =self.__memory[hash].count
            for i in range(count - 1):
                hash = (hash + i**2) % self.__size
                i += 1

            if key == self.__memory[hash].key:
                self.__memory[hash] = None
                self.__count -= 1
            return None

    def get(self, key) -> any:
        """
        найти значение по ключу
        """
        hash = self.__hash(key)
        if self.__memory[hash].count == 1:
            return self.__memory[hash].value
            
        else:
            count =self.__memory[hash].count
            for i in range(count - 1):
                hash = (hash + i**2) % self.__size
                i += 1

            if key == self.__memory[hash].key:
                return self.__memory[hash].value
                
        return None

    def __hash(self, key) -> int:
        return hash(key) % self.__size
