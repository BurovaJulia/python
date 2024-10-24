# Лаба 3 (реализация 1 версии списка)
class Node:
    """Узел списка"""

    def print_list(node):
        while node:
            print(node)
            node = node.next



    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.__class__.__name__}(data={self.data}, next={self.next})'


class SingleLinkedList_v1:
    '''Реализация АТД Односвязный линейный список  (SingleLinkedList_v1)'''

    def __init__(self) -> None:
        '''Возвращает пустой список'''
        self._head = None
        self.size = 0
        self._tail = None

    def insert_first_node(self, value: int) -> None:
        '''Добавить элемент в начало списка'''
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node
        if self._tail is None:
            self._tail = new_node
        self.size += 1

    def remove_first_node(self) -> int:
        '''Удалить первый элемент списка'''
        temp = self._head.data
        self._head = self._head.next
        self.size -= 1
        return temp

    def insert_last_node(self, value: int) -> None:
        '''Добавить элемент в конец списка'''
        new_node = Node(value)
        if self._tail is None:
            self._tail = new_node
            self._head = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self.size += 1

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
            self.size -= 1
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

    # Реализация второй версии списка

    def get_size(self) -> int:
        return self.size

    def find_node(self, value) -> int:
        current_node = self._head
        while current_node:
            if current_node.data == value:
                return current_node.data
            current_node = current_node.next

    def replace_node(self, old_value, new_value) -> None:
        current_node = self._head
        while current_node:
            if current_node.data == old_value:
                current_node.data = new_value
                return
            current_node = current_node.next


    def remove_node(self, value) -> None:
        if self._head is None:
            return
        if self._head.data == value:
            self._head = self._head.next
            if self._head is None:
                self._tail = None
            self.size -= 1
            return
        current_node = self._head
        while current_node.next is not None:
            if current_node.data == value:
                current_node.next = current_node.next.next
                if current_node.next is None:
                    self._tail = current_node
                self.size -= 1
                return
            current_node = current_node.next

    def find_previos_node(self, value):
        if self._head is None:
            return
        if self._head.data == value:
            return
        current_node = self._head
        while current_node.next is not None:
            if current_node.next.data == value:
                return current_node.data
            current_node = current_node.next
        return

    def find_next_node(self, value) -> int:
        current_node = self._head
        while current_node.next is not None:
            if current_node.data == value:
                return current_node.next.data
            current_node = current_node.next
        return

    def insert_before_node(self, value) -> None:
        if self._head is None:
            return
        if self._head.data == value:
            new_node = Node(value)
            new_node.next = self._head
            self._head = new_node
            self.size += 1
            return

        current_node = self._head
        while current_node.next is not None:
            if current_node.next.data == value:
                new_node = Node(value)
                new_node.next = current_node.next
                current_node.next = new_node
                self.size += 1
                return
            current_node = current_node.next


    def insert_after_node(self, value) -> None:
        current_node = self._head
        while current_node.next is not None:
            if current_node.data == value:
                new_node = Node(value)
                new_node.next = current_node.next
                current_node.next = new_node
                if current_node == self._tail:
                    self._tail = new_node
                self.size += 1
                return
            current_node = current_node.next

    def replace_previos_node(self, old_value, new_value) -> None:
        if self._head is None:
            return
        if self._head.data == old_value:
            return

        current_node = self._head
        while current_node.next is not None:
            if current_node.next.data == old_value:
                current_node.data = new_value
                return
            current_node = current_node.next

    def replace_next_node(self, old_value, new_value) -> None:
        current_node = self._head
        while current_node is not None:
            if current_node.data == old_value:
                current_node.next.data = new_value
                return
            current_node = current_node.next

    def remove_previos_node(self, value) -> None:
        if self._head is None:
            return
        if self._head.data == value:
            return
        current_node = self._head
        while current_node.next is not None:
            if current_node.next.data == value:
                if current_node == self._head:
                    self._head = current_node.next
                else:
                    current_node.next = current_node.next.next
                if current_node.next is None:
                    self._tail = current_node
                self.size -= 1
                return
            current_node = current_node.next

    def remove_next_node(self, value) -> int:
        current_node = self._head
        while current_node.next is not None:
            if current_node.data == value:
                current_node.next = current_node.next.next
                self.size -= 1
                return
            current_node = current_node.next

    def reverse_list(self):
        prev = None
        current_node = self._head
        while current_node:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
        self._head = prev
        if self.size > 0:
            self._tail = current_node

    def bubble_sort_list(self):
        if self._head is None or self._head.next is None:
            return
        sorted = False
        while not sorted:
            sorted = True
            current_node = self._head
            while current_node.next is not None:
                if current_node.data > current_node.next.data:
                    sorted = False
                    current_node.data, current_node.next.data = current_node.next.data, current_node.data
                current_node = current_node.next

    def list_of_unique(self, value):
        if self._head is None:
            self.insert_last_node(value)
            self.size += 1
            return

        current_node = self._head
        while current_node.next is not None:
            if current_node.data == value:
                return
            current_node = current_node.next
        self.insert_last_node(value)
        self.size += 1
