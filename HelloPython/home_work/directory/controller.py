import menu
import view_get
import view_out
import sorting

def start():
    while True:
        choice = menu.print_menu()
        if choice == 1:
            view_get.input_contact()
            sorting.sort()
        elif choice == 2:
            view_out.print_directory()
        elif choice == 3:
            return
        else:
            continue