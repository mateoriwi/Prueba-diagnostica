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
    print("3. Consult a student based in them data (ID, Name, etc...) ")
    print("4. Update student information")
    print("5. Delete student information")
    

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
    "student_ID":"ID",
    "student_NAME":"NAME",
    "student_AGE":"AGE",
    "student_CAREER":"CAREER",
    "student_status":"STATUS",
}
    students[student]={}
    print(students)
