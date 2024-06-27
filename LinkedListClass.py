class Node:
    """Класс узла связанного списка. Содержит данные (data) и ссылку на следующий узел (next_node)"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс использующий узлы(Класс Node), чтобы создать связанный список"""
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        """Метод добавления элемента в начало связанного списка и возвращает
        сообщение о том, что новый узел добавлен в начало списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        return f"Узел с данными {new_node.data} добавлен в начало списка"

    def insert_at_end(self, data):
        """Метод добавления элемента в конец связанного списка и возвращает
        сообщение о том, что новый узел добавлен в конец списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node
        return f"Узел с данными {new_node.data} добавлен в конец списка"

    def remove_node_position(self, rm_position):
        """Метод удаления элемента из переданной позиции в списке"""
        if rm_position == 1:
            removed_node = self.head
            self.head = self.head.next_node
            return f"Удален узел с данными {removed_node.data} позиции {rm_position}"
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < rm_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None or current_node.next_node is None:
            return "Ничего не удалено"
        removed_node = current_node.next_node
        current_node.next_node = current_node.next_node.next_node  # removed_node.next_node
        return f"Удален узел с данными {removed_node.data} позиции {rm_position}"

    def insert_at_position(self, data, node_position):
        """Метод добавления элемента на переданную позицию в списке"""
        new_node = Node(data)
        if node_position == 1:
            self.insert_at_head(data)
            # new_node.next_node = self.head
            # self.head = new_node
            return f"Узел с данными {new_node.data} добавлен на позицию {node_position}"
        """Опционально"""
        current_node = self.head
        # if node_position > self.len_ll():
        #     self.insert_at_end(data)
        #     # while current_node.next_node:
        #     #     current_node = current_node.next_node
        #     # current_node.next_node = new_node
        #     return
        current_node_position = 1
        while current_node is not None and current_node_position < node_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        """Если есть опционально (код выше то следующие 2 строки не нужны)"""
        if current_node is None:
            return None
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        return f"Узел с данными {new_node.data} добавлен на позицию {node_position}"

    def print_ll(self):
        """Метод вывода в консоль связанного списка"""
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node
        return "Данные списка выведены"

    def get(self, data):
        """Метод получения переданного элемента из связанного списка"""
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True, current_node.data
            current_node = current_node.next_node
        return False, None

    def change_data(self, node_data, change_data):
        """Метод для замены выбранного элемента в связанном списке"""
        current_node = self.head
        current_node_position = 1
        while current_node:
            if current_node.data == node_data:
                current_node.data = change_data
                return f"Заменены данные в узле № {current_node_position}"
            current_node = current_node.next_node
            current_node_position += 1
        return "Данные не обнаружены"

    # def change_data(self, node_data, change_data):
    """Это второй способ для примера"""
    #     result, current_node = self.get(node_data)
    #     if result:
    #         current_node.data = change_data
    #         return "Данные изменены!"
    #     return "Данные не обнаружены"
