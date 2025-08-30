class Stack:
    class Node:
        def __init__(self, data: any, prev: any = None):
            self.data = data
            self.prev = prev

    def __init__(self):
        self.__top = None
        self.__count = 0

    def is_empty(self)-> bool:
        """
        Возвращает true, если стек пуст, иначе false
        :return: true | false
        """
        return self.__count == 0

    def push(self, data: any) -> None:
        """
        Добавляет новую node на вершину стека.
        :return: none
        """
        node = Stack.Node(data = data, prev = self.__top)

        self.__count += 1
        self.__top = node

    def pop(self) -> any | None:
        """
        Удаляет и возвращает Node.Data с вершины стека. 
        Если стек пуст, возвращает None.
        """
        if self.is_empty():        
            return None
        
        node = self.__top
        self.__top = self.__top.prev
        self.__count -= 1
        return node.data
    
    def peek(self) -> any | None:
        """
        Возвращает Node.Data с вершины стека без её удаления.
        Если стек пуст, возвращает None
        :return: Node.data | None
        """
        if self.is_empty():        
            return None
        
        return self.__top.data
    
    def count(self) -> int:
        """
        Возвращает количество элементов в стеке.
        :return: count
        """
        return self.__count
    
stack = Stack()
stack.is_empty()
stack.push("11")
stack.peek()
stack.pop()
stack.count()