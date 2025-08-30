class Queue:

    class Node:
        def __init__(self, data: any, prev: any = None):
            self.data = data
            self.prev = prev

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def is_empty(self) -> bool:
        """
        Возвращает true, если очередь пуста, иначе false
        :return: true | false
        """
        return self.__count == 0
    
    def enqueue(self, data: any) -> None:
        """
        Добавляет data в конец очереди
        """
        node = Queue.Node(data = data, prev = None)

        if self.is_empty():
            self.__head = node

        self.__count += 1
        self.__tail.prev = node
        self.__tail = node

    def dequeue(self) -> any | None:
        """
        Удаляет и возвращает первый элемент из очереди.
        Если очередь пуста, возвращает None.
        :return: Node.data | None
        """
        if self.is_empty():
            return None
        
        data = self.__head
        self.__head = self.__head.prev
        self.__count -= 1

        if self.__head is None:
            self.__tail = None

        return data.data
    
    def peek(self) -> any | None:
        """
        Возвращает первый элемент из очереди без его удаления.
        Если очередь пуста, возвращает None.
        :return: Node.data | None
        """
        if self.is_empty():
            return None
        
        return self.__head.data
    
    def count(self)-> int:
        """
        Возвращает количество элементов в очереди
        :return: count elems
        """
        return self.__count
    

queue = Queue()
queue.is_empty()
queue.enqueue('11')
queue.peek()
queue.dequeue()