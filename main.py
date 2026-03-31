from functions import *

load_students()
main_menu()

option = input("Choose what option you need by its number\n")
if option == "1":
    registering_student()
elif option == "2":
    show_students()
elif option == "3":
    find_student()
elif option == "4":
    update_student()
elif option == "5":
    delete_student()
elif option == "0":
    exit_program()
