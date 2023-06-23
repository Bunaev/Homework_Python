import json

phone_book = {}
path = 'Yellow_page\phone.json'

def open_file():
    global phone_book
    try:
        with open(path, 'r', encoding='UTF=8') as file:
            phone_book = json.load(file)
        return True
    except:
        return False
    
def search(word: str):
    result = {}
    for index, contact in phone_book.items():
        if word.lower() in ' '.join(contact.values()).lower():
            result[index] = contact
    return result


def save_file():
    try:
        with open(path, 'w', encoding='UTF=8') as file:
            json.dump(phone_book, file, ensure_ascii=False)
        return True
    except:
        return False

def add_contact(new):
    contact = {check_id(): new}
    phone_book.update(contact)

def check_id():
    if phone_book:
        return max(list(map(int, phone_book))) + 1
    return 1


