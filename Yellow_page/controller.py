import view
import model
import text

def start():
    while True:
        select = view.menu()
        if select == 1:
            if model.open_file():
                view.print_message(text.load_successful)
            else:
                view.print_message(text.error_load)
        elif select == 2:
            if model.save_file():
                view.print_message(text.save_successful)
            else:
                view.print_message(text.error_save)
        elif select == 3:
            view.show_contacts(model.phone_book, text.empty_book)
        elif select == 4:
            new = view.add_contact()
            model.add_contact(new)
            view.print_message(text.add_successful(new.get('name')))
        elif select == 5:
            word = view.search_word()
            result = model.search(word)
            view.show_contacts(result, text.empty_search(word))
        elif select == 6:
            pass
        elif select == 7:
            pass
        elif select == 8:
            view.print_message()
            break
