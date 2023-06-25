import json

# class Contact:
#     def __init__(self, name: str, phone: str, comment: str):
#         self.name = name
#         self.phone = phone
#         self.comment = comment

#     def get(self, index: int or None = None):
#         if index:
#             return self.contact.get(index)
#         return self.contact

#     def __repr__(self) -> str:
#         return f'{self.name} {self.phone} {self.comment}'
    
#     def update(self, new):
#         self.name = new.name if new.name else self.name
#         self.phone = new.phone if new.phone else self.phone
#         self.comment = new.comment if new.comment else self.comment

#     def to_dict(self):
#         return {'name': self.name, 'phone': self.phone, 'comment': self.comment}

class PhoneBook:

    def __init__(self, path: str = 'Yellow_page\phone.json'):
        self.contact: dict = {}
        self.path = path

    def get(self, index: int or None = None):
        if index:
            return self.contact.get(index)
        return self.contact

    def open_file(self):
        try:
            with open(self.path, 'r', encoding='UTF=8') as file:
                self.contact = json.load(file)
                self.not_changet = self.contact.copy()
            return True
        except:
            return False
    
    def search(self, word: str):
        result = {}
        for index, contact in self.contact.items():
            if word.lower() in ' '.join(contact.values()).lower():
                result[index] = contact
        return result


    def save_file(self):
        try:
            with open(self.path, 'w', encoding='UTF=8') as file:
                json.dump(self.contact, file, ensure_ascii=False, indent=4)
            return True
        except:
            return False

    def add_contact(self, new):
        contact = {self.check_id(): new}
        self.contact.update(contact)

    def check_id(self):
        if self.contact:
            return max(list(map(int, self.contact))) + 1
        return 1
    
    def chek_on_exit(self):
        if self.contact == self.not_changet:
            return False
        return True


