#Лаба 3 (реализация 1 версии списка)
class Node:
    """Узел списка

    >>> Node()
    Node(data=None, next=None)

    >>> node3 = Node(3)
    >>> node3
    Node(data=3, next=None)

    >>> node2 = Node(data=2, next=node3)
    >>> node2
    Node(data=2, next=Node(data=3, next=None))

    >>> node1 = Node(None, None)
    >>> node1
    Node(data=None, next=None)

    >>> node1.data = 1
    >>> node1
    Node(data=1, next=None)
    >>> node1.next = node2
    >>> node1
    Node(data=1, next=Node(data=2, next=Node(data=3, next=None)))

    >>> def print_list(node):
    ...   while node:
    ...       print(node)
    ...       node = node.next
    ...
    >>> print_list(node1)
    Node(data=1, next=Node(data=2, next=Node(data=3, next=None)))
    Node(data=2, next=Node(data=3, next=None))
    Node(data=3, next=None)

    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
         return f'{self.__class__.__name__}(data={self.data}, next={self.next})'

    

class SingleLinkedList_v1:
    '''Реализация АТД Односвязный линейный список  (SingleLinkedList_v1)

    >>> SingleLinkedList_v1()
    SingleLinkedList_v1(None)

    >>> list1 = SingleLinkedList_v1()
    >>> list1
    SingleLinkedList_v1(None)

    >>> list1.insert_first_node(2)
    >>> list1
    SingleLinkedList_v1(Node(data=2, next=None))

    >>> list1.insert_first_node(1)
    >>> list1
    SingleLinkedList_v1(Node(data=1, next=Node(data=2, next=None)))

    >>> list1.insert_first_node(0)
    >>> print(list1)
    LinkedList.head -> 0 -> 1 -> 2 -> None

    >>> list1.insert_last_node(3)
    >>> print(list1)
    LinkedList.head -> 0 -> 1 -> 2 -> 3 -> None

    >>> list1.remove_first_node()
    0
    >>> print(list1)
    LinkedList.head -> 1 -> 2 -> 3 -> None

    >>> list1.remove_last_node()
    3
    >>> print(list1)
    LinkedList.head -> 1 -> 2 -> None
    '''

    def __init__(self) -> None:
        '''Возвращает пустой список'''
        self._head = None

    def insert_first_node(self, value:int) -> None:
        '''Добавить элемент в начало списка'''
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node

    def remove_first_node(self) -> int:
        '''Удалить первый элемент списка'''
        temp = self._head.data
        self._head = self._head.next
        return temp

    def insert_last_node(self, value:int) -> None:
        '''Добавить элемент в конец списка'''
        if self._head is None:
            self.insert_first_node(value)
        else:
            current_node = self._head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

    def remove_last_node(self) -> int:
        '''Удалить последний элемент списка'''
        if self._head.next is None:
            return self.remove_first_node()
        else:
            current_node = self._head
            while current_node.next.next is not None:
                current_node = current_node.next
            temp = current_node.next.data
            current_node.next = None
            return temp

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._head})'

    def __str__(self):
        node = self._head
        l = []
        while node:
            l.append(str(node.data))
            node = node.next
        return 'LinkedList.head -> ' + ' -> '.join(l) + ' -> None'

    #Реализация второй версии списка
    
    def get_size(self) -> int:
        count = 0
        current_node = self._head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def find_node(self, value) -> int:
        

    def replace_node(ValueType old_value, ValueType new_value) -> None:
        return 0

    def remove_node(ValueType value) -> ValueType:
        return 0
