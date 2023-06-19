phone_book = {}
path: str = 'Phone.txt'

def open_file():
    phone_book.clear()
    file = open(path, 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    for contact in data:
        nc = contact.strip().split(':')
        phone_book[int(nc[0])] = {'name' : nc[1], 'phone' : nc[2], 'comment' : nc[3]}
    print('\nТелефонная книга успешно загружена!')

def show_contacts(book):
    for i,cnt in book.items():
        print(f'{i:>3} - {cnt.get("name"):<20}{cnt.get("phone"):<20}{cnt.get("comment"):<20}')

def add_contact():
    uid = max(list(phone_book.keys())) + 1
    name = input('Введите имя контакта: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий к контакту: ')
    phone_book[uid] = {'name':name, 'phone':phone, 'comment':comment}
    print(f'\nКонтакт {name} успешно добавлен в книгу!')
    print('=' * 100 + '\n')

def save_file():
    data = []
    for i, contact in phone_book.items():
        new = ':'.join([str(i), contact.get('name'), contact.get('phone'), contact.get('comment')])
        data.append(new)
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF=8') as file:
        file.write(data)
    print('Телефонная книга успешно сохранена')
    print('=' * 100 + '\n')

def find_contact():
    result = {}
    word = input('Введите параметр поиска: ')
    for i, contact in phone_book.items():
        if word.lower() in ' '.join(list(contact.values())).lower():
            result[i] = contact
    if len(result) == 0:
        print('\n' + '=' * 100)
        print('По заданным параметрам контактов не найдено!')
    print('\n' + '=' * 100)
    return result 

def remove():
    result = find_contact()
    show_contacts(result)
    index = int(input('Введите ID контакта, который необходимо удалить: '))
    del_cnt = phone_book.pop(index)
    print(f'\nКонтакт {del_cnt.get("name")} успешно удален!')
    print('=' * 100 + '\n')

def edit_contact():
    result = find_contact()
    show_contacts(result)
    index = int(input('Введите ID контакта, который необходимо изменить: '))
    find_key = int(input('''Что именно Вы хотите изменить? 
    Введите "1" для измения имени;
    Введите "2" для изменения телефона;
    Введите "3" для изменения комментария: '''))
    while find_key < 1 or find_key > 3:
        find_key = int(input('Ошибка ввода! Введите значение от 1 до 3: '))
    new_value = input('Введите новое значение: ')
    if find_key == 1:
        phone_book[index]['name'] = new_value
    elif find_key == 2:
        phone_book[index]['phone'] = new_value
    elif find_key == 3:
        phone_book[index]['comment'] = new_value
    print('Контакт успешно изменен')
    print('=' * 100 + '\n')

def menu() -> int:
    main_menu = '''Главное меню: 
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход'''
    print(main_menu)
    while True:
        select = input('Выберете пункт меню: ')
        if select.isdigit() and 0 < int(select) < 9:
            return int(select)
        print('Ошибка ввода. Введите число от 1 до 8!')

open_file()
while True:
    select = menu()
    if select == 1:
        open_file()
    elif select == 2:
        save_file()
    elif select == 3:
        print('\n' + '=' * 100)
        show_contacts(phone_book)
        print('=' * 100 + '\n')
    elif select == 4:
        add_contact()
    elif select == 5:
        result = find_contact()
        show_contacts(result)
        print('=' * 100 + '\n')
    elif select == 6:
        edit_contact()
    elif select == 7:
        remove()
    elif select == 8:
        print('До свидания! До новых встреч')
        break