import view
import model
import text

def start():
    pb = model.PhoneBook()
    while True:
        select = view.menu()
        if select == 1:
            if pb.open_file():
                view.print_message(text.load_successfull)
            else:
                view.print_message(text.error_load)
        elif select == 2:
            if pb.save_file():
                view.print_message(text.save_successfull)
            else:
                view.print_message(text.error_save)
        elif select == 3:
            view.show_contacts(pb.get(), text.empty_book)
            print('\n')
        elif select == 4:
            new = view.add_contact()
            pb.add_contact(new)
            view.print_message(text.add_successfull(new.get('name')))
        elif select == 5:
            word = view.search_word()
            result = pb.search(word)
            view.show_contacts(result, text.empty_search(word))
        elif select == 6:
            edit = view.search_word()
            result = pb.search(edit)
            view.show_contacts(result, text.empty_search(edit))
            view.edit_contact(pb.phone_book)
        elif select == 7:
            edit = view.search_word()
            result = pb.search(edit)
            view.show_contacts(result, text.empty_search(edit))
            view.delete_contact(pb.phone_book)
        elif select == 8:
            if pb.chek_on_exit():
                answer = view.view_input(text.change_confirm).lower()
                if answer != 'n':
                    pb.save_file()
            view.print_message(text.good_bye)
            break
    
