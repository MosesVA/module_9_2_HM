import unittest
from LinkedListClass import LinkedList


class TestLinkedList(unittest.TestCase):
    my_linked_list = LinkedList()

    def test01_init(self):
        self.assertEqual(self.my_linked_list.head, None)

    def test02_insert_at_head(self):
        self.assertEqual(self.my_linked_list.insert_at_head('test1'), 'Узел с данными test1 добавлен в начало списка')
        self.assertEqual(self.my_linked_list.insert_at_head('test2'), 'Узел с данными test2 добавлен в начало списка')

    def test03_remove_node_position(self):
        self.my_linked_list.insert_at_head('test3')
        self.my_linked_list.insert_at_head('test4')
        self.my_linked_list.insert_at_head('test5')
        self.assertEqual(self.my_linked_list.remove_node_position(3), 'Удален узел с данными test3 позиции 3')
        self.assertEqual(self.my_linked_list.remove_node_position(1), 'Удален узел с данными test5 позиции 1')
        self.my_linked_list.remove_node_position(1)
        self.my_linked_list.remove_node_position(1)
        self.my_linked_list.remove_node_position(1)
        self.assertEqual(self.my_linked_list.remove_node_position(2), 'Ничего не удалено')

    def test04_insert_at_end(self):
        self.assertEqual(self.my_linked_list.insert_at_end('test1'), None)
        self.my_linked_list.insert_at_end('test2')
        self.assertEqual(self.my_linked_list.insert_at_end('test3'), 'Узел с данными test3 добавлен в конец списка')

    def test05_insert_at_position(self):
        self.my_linked_list.remove_node_position(1)
        self.my_linked_list.remove_node_position(2)
        self.assertEqual(self.my_linked_list.insert_at_position('test', 3), None)
        self.assertEqual(self.my_linked_list.insert_at_position('test1', 1), 'Узел с данными '
                                                                             'test1 добавлен на позицию 1')

        self.assertEqual(self.my_linked_list.insert_at_position('test2', 2), 'Узел с данными '
                                                                             'test2 добавлен на позицию 2')

    def test06_print_ll(self):
        self.assertEqual(self.my_linked_list.print_ll(), 'Данные списка выведены')

    def test07_get(self):
        self.assertEqual(self.my_linked_list.get('test1'), (True, 'test1'))
        self.assertEqual(self.my_linked_list.get('test15'), (False, None))

    def test08_change_data(self):
        self.my_linked_list.insert_at_head('test2')
        self.my_linked_list.insert_at_head('test3')
        self.my_linked_list.insert_at_head('test4')
        self.assertEqual(self.my_linked_list.change_data('test3', 'test_change'), 'Заменены данные в узле № 2')
        self.assertEqual(self.my_linked_list.change_data('test15', 'test_change'), 'Данные не обнаружены')
