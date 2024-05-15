# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using lists and files to work with data
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Leena Chaudhuri,14/05/2024,Created Script
# ------------------------------------------------------------------------------------------ #


# Define the Data Constants
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
"""
FILE_NAME: str = "Enrollments.csv"


# Define the Data Variables
student_first_name: str = " " # Holds the first name of a student entered by the user.
student_last_name: str = " " # Holds the last name of a student entered by the user.
course_name: str = " " # Holds the name of a course entered by the user.
csv_data: str  = ""  # Holds combined string data separated by a comma.
file = None   # Holds a reference to an opened file.
menu_choice: str = " " # Hold the choice made by the user.
student_data: dict[str]= []# one row of student data
students:list[list[str]]=[] # a table of student data
joined_data: str = ""
user: str = ""

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    for row in file.readlines():
        # Transform the data from the file
        row_list = row.split(',')
        print(row_list)
        student_data = {
            "student_name": row_list[0],
            "student_last name": row_list[1],
            "course_name": row_list[2],
        }
        # Load it into our collection (list of lists)
        students.append(student_data)
    file.close()
except FileNotFoundError:
    print("ERROR: Database not found")

# Present and Process the data
while True:
    

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do? ")

    # Input user data
    if menu_choice == "1": # This will not work if it is an integer!

        try:
            student_first_name = input("Enter first name: ")
        except ValueError:
            print("Value Error, please re enter name")

        try:
            student_last_name= input("Enter last name: ")
        except ValueError:
            print("Value Error, please re enter name")

            course_name = input("Please enter the name of the course: ")
            student_data = [student_first_name,student_last_name,course_name]
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            continue


    # Present the current data
    elif menu_choice == "2":

         # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
        print("-"*50)
        continue
        

    # Save the data to a file
    elif menu_choice == "3":
        file = open(FILE_NAME, "w")
        for student in students:
            student_line = f"{student[0]},{student[1]} for {student[2]} \n"
            file.write(csv_data)
        file.close()
        print("The following data was saved to file!")
        for student in students:
            print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
        continue
        
        
    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
1