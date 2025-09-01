class Deq:

    class Node:
        def __init__(self, data: any, next = None, prev = None):
            self.next = next
            self.prev = prev
            self.data = data

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def count(self):
        return self.__count

    def is_empty(self) -> bool:
        """
        проверка пустоты списка
        :return: True если пустой, иначе False
        """
        return self.__count == 0
    
    def enqueue(self, data: any) -> None:
        """
        добавляет элемент в конец очереди
        :param data: элемент ноды для добавления
        """
        node = Deq.Node(data = data, next = None, prev = None)
        self.__count += 1

        if self.is_empty():
            self.__head = node
            self.__tail = node
            return
        
        node.prev = self.__tail
        self.__tail.next = node
        self.__tail = node

    def enqueue_first(self, data: any) -> None:
        """
        добавляет элемент в начало очереди
        :param data: элемент ноды для добавления
        """
        node = Deq.Node(data = data, next = None, prev = None)
        self.__count += 1

        if self.is_empty():
            self.__head = node
            self.__tail = node
            return
        
        node.next = self.__head
        self.__head.prev = node
        self.__head = node

    def dequeue(self) -> any:
        """
        извлекает первый элемент из очереди и возвращает его
        если очередь пустая, return None
        :return: Node.data
        """

        if self.is_empty():
            return None
        
        self.__count -= 1

        data = self.__head.data
        if self.__count == 0:
            self.__head = None
            self.__tail = None
            return data
        
        
        self.__head = self.__head.prev
        self.__head.next = None

        return data
    
    def dequeue_tail(self) -> any:
        """
        извлекает последний элемет и возвращает егшо
        если очередь пустая, return None
        :return: Node.data
        """

        if self.is_empty():
            return None
        
        data = self.__tail.data
        self.__count -= 1

        if self.__count == 0:
            self.__head = None
            self.__tail = None
            return data
        
        self.__tail = self.__tail.next
        self.__tail.prev = None
        
        return data
    
    def peek(self) -> any:
        """
        возвращает первый элемент без удаления
        если очередь пустая, return None
        :return: Node.data
        """
        if not self.is_empty():
            return self.__head.data
        
        return None
    
    def peek_last(self)-> any:
        """
        возвращает последний элемент без удаления
        если очередь пустая, return None
        :return: Node.data
        """
        if not self.is_empty():
            return self.__tail.data
        
        return None
    
deq = Deq()
deq.enqueue('111')
deq.enqueue_first('222')

deq.peek()
deq.peek_last()

deq.dequeue()
deq.dequeue_tail()