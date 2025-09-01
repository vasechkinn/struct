class Node:
    def __init__(self, data: any, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def count(self):
        return self.__count

    def is_empty(self):
        """
        проверка пустоты списка
        :return: True если пустой, иначе False
        """
        return self.__count == 0

    def add(self, data: any) -> None:
        """
        добавить элемент в конец списка
        :param data: элемент для добавления
        :return: none
        """
        node = Node(data = data, next = None, prev= self.__tail)

        if self.is_empty():
            self.__head = node
        else:
            self.__tail.next = node
        
        self.__count += 1
        self.__tail = node

    def add_first(self, data: any) -> None:
        """
        добавить элемент в начало списка
        :param data: элемент для добавления
        :return: none
        """
        node = Node(data = data, next = self.__head, prev =None)

        if self.is_empty():
            self.__tail = node
        else:
            self.__head.prev = node

        self.__count += 1
        self.__head = node

    def insert(self, position: int, data: any) -> None :
        """
        вставить элемент по позиции
        :param position: позиция элемента, начиная с 1
        :param data: элемент для добавления
        :return: none
        """
        if position < 1 or position > self.__count + 1:  raise ValueError('нумерация начинается с 1')

        if position == 1:
            self.add_first(data)
            return
        
        if position == self.__count + 1:
            self.add(data)
            return

        mid = (self.__count + 1) // 2

        if position > mid:
            count = self.__count - position + 1
            counter = 0
            iterator = self.__tail

            while counter != count:
                iterator = iterator.prev
                counter += 1

        else:
            counter = 1
            iterator = self.__head

            while counter != position - 1:
                iterator = iterator.next
                counter += 1
            
        node = Node(data = data, next = iterator.next, prev= iterator)

        if iterator.next is not None:
            iterator.next.prev = node

        iterator.next = node
            
        self.__count += 1

    def remove(self, elem: any) -> None :
        """
        удалить элемент (первое вхождение)
        """
        if self.is_empty():
            return None
        
        if self.__head.data == elem:
            self.__count -= 1
        
            if self.__head.next is None:
                self.__head = None
                self.__tail = None
            else:
                self.__head = self.__head.next
                self.__head.prev = None
            
            return
        
        iterator = self.__head
        while iterator is not None:

            if iterator.data == elem:
                self.__count -= 1

                if iterator.next is not None:
                    iterator.prev.next = iterator.next
                    iterator.next.prev = iterator.prev

                else:
                    self.__tail = iterator.prev
                    self.__tail.next = None

                break
            iterator = iterator.next
    
    def remove_first(self) -> None :
        """
        удалить первый элемент
        :return: None
        """
        if self.is_empty():
            return None

        if self.__count == 1:
            self.__head = None
            self.__tail = None
            self.__count -= 1
            return

        self.__head = self.__head.next
        self.__head.prev = None
        self.__count -= 1

    def remove_last(self) -> None:
        """
        удалить последний элемент
        :return: none
        """
        if self.is_empty():
            return None

        if self.__count == 1:
            self.__head = None
            self.__tail = None
            self.__count -= 1
            return
        
        self.__tail = self.__tail.prev
        self.__tail.next = None
        self.__count -= 1

    def find(self, elem: any) -> Node | None:
        """
        найти позицию элемента (первое вхождение)
        :return: NOde | None
        """
        if self.is_empty():
            return None
        
        iterator = self.__head
        while iterator is not None:
            if iterator.data == elem:
                return iterator
            iterator = iterator.next

        return None
    
    def clear(self) -> None:
        """
        очистка списка
        """
        self.__head = None
        self.__tail = None
        self.__count = 0