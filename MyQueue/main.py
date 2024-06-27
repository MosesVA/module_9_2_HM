from QueueClass import Queue

print('Привет, Человек!')
user_num_of_queue = int(input('Какова будет длина очереди?: '))
user_queue = Queue(user_num_of_queue)

while True:
    print()
    user_choice = int(input("""Выберите действие:
1. Добавить элемент в очередь.
2. Удалить элемент из очереди.
3. Проверить пустая ли очередь.
4. Проверить заполнена ли очередь.
5. Показать все элементы очереди
6. Очистить очередь.
7. Выход из программы.
    
Ваш выбор: """))

    if user_choice == 1:
        user_enqueue_el = input('Какой элемент вы хотите добавить?: ')
        if user_queue.enqueue(user_enqueue_el) is not False:
            print(f'Элемент "{user_enqueue_el}" добавлен в конец очереди.')
        else:
            print(f'Нельзя добавить больше {user_num_of_queue} элементов')
    elif user_choice == 2:
        print(f'Удален первый элемент в очереди "{user_queue.dequeue()}".')
    elif user_choice == 3:
        user_queue.is_empty()
    elif user_choice == 4:
        user_queue.is_full()
    elif user_choice == 5:
        user_queue.show()
    elif user_choice == 6:
        print(user_queue.clear_queue())
    elif user_choice == 7:
        break
    else:
        print('Введен некорректный запрос.')
        print('Попробуйте еще раз!')
