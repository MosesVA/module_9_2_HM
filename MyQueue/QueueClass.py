class Node:
    """Класс узла связанного списка. Содержит данные (data) и ссылку на следующий узел (next_node)"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс использующий узлы(Класс Node), чтобы создать очередь"""

    def __init__(self, queue_size, head=None, tail=None):
        self.queue_size = queue_size
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        """Метод добавления элемента в конец очереди"""
        if self.size_queue() < self.queue_size:
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                self.tail.next_node = new_node
            self.tail = new_node
        else:
            print('Очередь полная')
            return False

    def dequeue(self):
        """Метод удаления первого элемента из очереди"""
        if self.head is None:
            print('Нет элемента для удаления')
            return None
        else:
            dequeue_item = self.head
            self.head = self.head.next_node
        return dequeue_item.data

    def is_empty(self):
        """Метод возвращает True, если очередь пуста, иначе возвращает False"""
        if self.head:
            print('Очередь не пуста')
            return False
        else:
            print('Очередь пуста')
            return True

    def size_queue(self):
        """Метод для подсчета кол-ва элементов в стеке"""
        counter = 0
        stack_item = self.head
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter

    def is_full(self):
        """Метод возвращает True, если стек заполнен, иначе возвращает False"""
        if self.queue_size == self.size_queue():
            print('Очередь полная')
            return True
        else:
            print('Очередь полная')
            return False

    def show(self):
        """Метод для вывода в консоль всех элементов очереди"""
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node

    def clear_queue(self):
        """Метод очищает полностью стек"""
        while self.head:
            self.dequeue()
        return 'Удалены все элементы очереди'
