import text

def menu() -> int:
    print(text.main_menu[0])
    for i in range(1, len(text.main_menu)):
        print(f'\t{i}. {text.main_menu[i]}')
    while True:
        select = input(text.select_menu)
        if select.isdigit() and 0 < int(select) < int(len(text.main_menu)):
            return int(select)
        print(text.imput_error)

def add_contact():
    new = {}
    for key, value in text.new_contact.items():
        new[key] = input(value)
    return new

def show_contacts(book, message):
    if book:
        max_name = []
        max_phone = []
        max_comment = []
        for contact in book.values():
            max_name.append(len(contact.get('name')))
            max_phone.append(len(contact.get('phone')))
            max_comment.append(len(contact.get('comment')))
        size_name = max(max_name)
        size_phone = max(max_phone)
        size_comment = max(max_comment)
        print('\n' + '=' * (size_name+size_comment+size_phone+7))
        for index, contact in book.items():
            print(f'{index:>3}. {contact.get("name"):<{size_name}} {contact.get("phone"):<{size_phone}} {contact.get("comment"):<{size_comment}}')
            print('=' * (size_name+size_comment+size_phone+7))
    else:
        print_message(message)

def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')

def search_word() -> str:
    return input(text.search_word)

def edit_key():
    while True:
        change = input(text.change_massege)
        if change.isdigit() and 0 < int(change) < 4:
            return int(change)
        print(text.change_index_error)

def sure():
    while True:
        a_y_s = input(text.sure_massege).lower()
        if a_y_s == 'y':
            return 1
        elif a_y_s == 'n':
            return 0
        else:
            print(text.sure_error)
            continue

def edit_contact(book: dict):
    index = input(text.edit_index)
    find_key = edit_key()
    new_value = input(text.edit_new)
    if find_key == 1:
        book[index]['name'] = new_value
    elif find_key == 2:
        book[index]['phone'] = new_value
    elif find_key == 3:
        book[index]['comment'] = new_value
    print_message(text.edit_successfull)

def delete_contact(book: dict):
    index = input(text.delete_massege)
    confir = sure()
    if confir == 1:
        temp = book.pop(index)
        print_message(text.delete_successfull(temp['name']))
