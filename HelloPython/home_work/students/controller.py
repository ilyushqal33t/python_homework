import menu, mod, view
def start():
    main_dict = {}
    subjects = ['Матеша','Ин.яз','Физика']
    while True:
        choice = menu.print_menu()
        if choice == 1:
            mod.input_student(main_dict,subjects)
        elif choice == 2:
            mod.input_subjetc(subjects, main_dict)
        elif choice == 3:
            mod.input_marks(main_dict)
        elif choice == 4:
            view.print_students(main_dict)
        elif choice == 5:
            view.print_marks_student(main_dict)
        elif choice == 6:
            return
        else:
            continue