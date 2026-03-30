programs = ('Foreign Trade Operations','Management Administrative','Logistics Operations Management', 
'Tourism and Hotel Management','Electrical Systems Management', 'Occupational Health and Safety Management'
'Operation of Industrial Processes', 'Computer Systems Maintenance')

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
        try:
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
        
        except ValueError:
            print("Error: You only have to enter numbers. ")
            continue

        NAME = input("What is the student name?")
        
        try: 
            AGE = input("How old the student is?")
            
            if not AGE: 
                print("Error: Could not read anything")
                continue

            if not AGE.isdigit():
                print("Error: Only numbers")

        except ValueError:
            print("Error: You only have to enter numbers. ")
        
        try:
            CAREER = input(f"What is the student career from next? {programs} ")
            if not CAREER.isalpha():
                print("Invalid input")
                continue

        except ValueError:
            print("Error: Invalid input")

        try: 
            STATUS = input("The student is currently active? Type: True or False")

            if not STATUS == "True":
                print("Error: Type 'True' or 'False'")
                continue

            elif not STATUS == "False":      
                print("Error: Type 'True' or 'False'")
                continue

        except ValueError:
            print("Error: Invalid input")   
     



