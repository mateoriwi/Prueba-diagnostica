from functions import *
student_data = []

student = {
    "student_ID":"ID",
    "student_NAME":"NAME",
    "student_AGE":"AGE",
    "student_CAREER":"CAREER",
    "student_status":"STATUS",
}

main_menu()

option = input("Choose what option you need by its number\n")
if option == "1":
    registering_student()
