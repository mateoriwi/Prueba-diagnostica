import json

def load_students():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []

def save_students():
    with open("students.json", "w") as archivo:
        json.dump(students, archivo, indent=4)

programs = ('Foreign_Trade_Operations','Management_Administrative','Logistics_Operations_Management', 
'Tourism_and_Hotel_Management','Electrical_Systems_Management', 'Occupational_Health_and_Safety_Management',
'Operation_of_Industrial_Processes', 'Computer_Systems_Maintenance')

students = []

def main_menu():

    print("Welcome to the official page of Insitución Universitaria de Barranquilla!")
    print("You have entered has Admin")
    print("Here are some options for Admins, choose what you need")
    print("1. Register a new student")
    print("2. Consult a student information")
    print("3. Consult a student based in them data (ID, Name, etc...)")
    print("4. Update student information")
    print("5. Delete student information")
    print("0. Exit")

def registering_student():
    
    while True:
            ID = input("What is the ID of the student?\n")
        
            if not ID:
                print("Error: Could not read anything")
                continue

            if not ID.isdigit():
                print("Error: Only numbers")
                continue

            if len(ID) not in range (4,8):

                print("Error: We only process between 4 and 7 characters")
                continue
            break
    

    while True:
        NAME = input("What is the student name?\n")

        if not NAME.isalpha():
            print("Invalid input")
            continue
        break

    while True:
            AGE = input("How old the student is?\n")
            
            if not AGE: 
                print("Error: Could not read anything")
                continue

            if not AGE.isdigit():
                print("Error: Only numbers")
                continue
            break
    
    while True:
        CAREER = input(f"What is the student career from next? {programs}\n")
        
        if CAREER in programs:
            break 

    while True:
        STATUS = input("The student is currently active? Type: True or False\n").strip().lower()

        if STATUS in ["true", "false"]:
            STATUS = True if STATUS == "true" else False
            break


    student = {
    "student_ID":ID,
    "student_NAME":NAME,
    "student_AGE":AGE,
    "student_CAREER":CAREER,
    "student_STATUS":STATUS,
}
    students.append(student)
    save_students()

def show_students():
    if not students:
        print("There are no stundets")
        return
    
    for student in students:
        print(student)

def find_student():
    search = input(" Enter ID or Name of the student")

    found = False 

    for student in students:
        if student["student_ID"] == search or student["student_NAME"].lower() == search.lower():
            print(student)
            found = True
            
    if not found:
            print("Student not found")

def update_student():
    ID = input("Enter student ID: ")
    for student in students:
        if student["student_ID"] == ID:

            student["student_NAME"] = input("New name: ")
            student["student_AGE"] = int(input("New age: "))
            student["student_CAREER"] = input(f"New career {programs}: ")
            status = input("New student status (True/false): ").lower()
            student["student_status"] = True if status == "true" else False

            save_students()
            print("student_updated")
            return
    print("Student not found")

def delete_student():
    ID = input("Enter student ID: ")
    
    for student in students:
        if student ["student_ID"] == ID:
            students.remove(student)
            save_students()
            print("Student deleted")
            return
    print("Student not found")

def exit_program():
    exit
