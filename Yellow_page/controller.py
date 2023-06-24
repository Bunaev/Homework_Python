import view
import model
import text

def start():
    while True:
        select = view.menu()
        if select == 1:
            if model.open_file():
                view.print_message(text.load_successfull)
            else:
                view.print_message(text.error_load)
        elif select == 2:
            if model.save_file():
                view.print_message(text.save_successfull)
            else:
                view.print_message(text.error_save)
        elif select == 3:
            view.show_contacts(model.phone_book, text.empty_book)
            print('\n')
        elif select == 4:
            new = view.add_contact()
            model.add_contact(new)
            view.print_message(text.add_successfull(new.get('name')))
        elif select == 5:
            word = view.search_word()
            result = model.search(word)
            view.show_contacts(result, text.empty_search(word))
        elif select == 6:
            edit = view.search_word()
            result = model.search(edit)
            view.show_contacts(result, text.empty_search(edit))
            view.edit_contact(model.phone_book)
        elif select == 7:
            edit = view.search_word()
            result = model.search(edit)
            view.show_contacts(result, text.empty_search(edit))
            view.delete_contact(model.phone_book)
        elif select == 8:
            view.print_message(text.good_bye)
            break
    
