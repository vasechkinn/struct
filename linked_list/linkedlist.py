# ---------- LinkedList (Связный список) ----------
# Это динамическая структура данных, состоящая из узлов (Node), где каждый узел хранит значение и ссылку на следующий элемент.
# Доступ к элементам осуществляется по связям, а не по индексам, как в массиве.
#
# ---- Fields (Атрибуты)
# head — ссылка на первый элемент списка (т.е. на первую Node)
# tail — ссылка на последний элемент списка (для оптимизации... подумайте, что при этом оптимизируется)
# count (иногда size) — фактическое количество элементов

# ---- Interface (Операции)
# add(elem) -- добавить элемент в конец списка
# add_first(elem) -- добавить элемент в начало списка
# insert(position, elem) -- вставить элемент по позиции

# remove(elem) -- удалить элемент (первое вхождение)
# remove_first() -- удалить первый элемент
# remove_last() -- удалить последний элемент

# find(elem) -- найти позицию элемента (первое вхождение)
# is_empty() -- проверить, пуст ли список
# clear() -- очистить список

# count -- свойство, возвращает количество элементов

class Node:

    def __init__(self, data, next):
        self.data = data
        self.next = next


# Полная реализация структуры данных "Односвязный список" идет как дом. работа
class LinkedList:

    def __init__(self):
        self.__head = None
        self.__count = 0


    def add(self, item):
        node = Node(data=item, next=None)
        self.__count +=1

        if self.__head is None:
            self.__head = node
            
            return

        iterator = self.__head
        while iterator.next is not None:
            iterator = iterator.next

        iterator.next = node
        
        

    def add_first(self, item):
        node = Node(data = item, next = self.__head)
        self.__head = node
        self.__count +=1


    def insert(self, position: int, item: any):
        """
        вставить элемент по позиции, нумерация с 1
        :param position: позиция для добавления
        :param item: нада
        """
        if position < 1 or position > self.__count + 1:  raise ValueError('нумерация начинается с 1')
        node = Node(data=item, next=None)

        if self.is_empty():
            return None
        
        if self.__count +1 == position:
            self.add(item)
            return
        
        self.__count += 1
        
        if position == 1:
            self.add_first(item)
            return
        
        iterator = self.__head
        counter = 0

        while counter != position - 1:
            iterator = iterator.next
            counter += 1

        node.next = iterator.next
        iterator.next = node


    def remove(self, elem: any):
        """
        удалить элемент (первое вхождение)
        :param elem: Node.data
        """
        if self.is_empty():
            return None
        
        if self.__count == 1 and self.__head.data == elem:
            self.__head = None
            self.__count = 0
            return
        
        if self.__head.data == elem:
            self.remove_first()
            return

        iterator = self.__head

        while iterator is not None:
            if  iterator.next is not None and iterator.next.data == elem:
                iterator.next = iterator.next.next
                self.__count -= 1
                break

            iterator= iterator.next

        return None


    def remove_first(self):
        """
        удалить первый элемент
        """
        if not self.is_empty():
            self.__head = self.__head.next
            self.__count -= 1
        
        else:
            return None
        

    def remove_last(self):
        """
        удалить последний элемент
        """
        if self.is_empty():
            return None
        
        if self.__head.next is None:
            self.__head = None
            self.__count -=1
            return

        iterator = self.__head
        while iterator.next.next is not None:
            iterator = iterator.next

        iterator.next = None
        self.__count -= 1

    def find(self, elem: any)-> None | Node:
        """
        найти позицию элемента (первое вхождение)
        :param elem: элемент для поиска
        """
        if self.is_empty():
            return None
        
        if self.__head.next == None:
            if self.__head.data == elem:
                return self.__head
            
        iterator = self.__head
        while iterator.next is not None:
            if iterator.data == elem:
                return iterator
            iterator = iterator.next

        return None

    def is_empty(self)-> bool:
        """
        проверяет пустоту списка
        :return: true | false
        """
        return self.__count == 0

    def clear(self):
        """
        очищает список
        """
        self.__head = None
        self.__count = 0

    def count(self):
        return self.__count