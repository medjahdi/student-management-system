import mysql.connector
from mysql.connector import Error
from termcolor import colored
from login import login
from setting import (
    load_students, save_students, add_student, delete_student,
    update_student, display_students, search_student ,export_to_csv, logo
)

# start ....
def main():
    if login():
        pass
    else:
        print(colored("Exiting program.", 'magenta'))
        return
    logo()
    students = load_students()

    while True:
        print(colored("\nStudent Management System", 'magenta'))
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. Display All Students")
        print("5. Search Student")
        print("6. Export to CSV")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_student(students)
            save_students(students)
        elif choice == '2':
            delete_student(students)
            save_students(students)
        elif choice == '3':
            update_student(students)
            save_students(students)
        elif choice == '4':
            display_students(students)
        elif choice == '5':
            search_student(students)
        elif choice == '6':
            export_to_csv(students)
        elif choice == '7':
            save_students(students)
            print(colored("Exiting program. Data saved.", 'magenta'))
            break
        else:
            print(colored("Invalid choice. Please select a number between 1 and 6.", 'magenta'))


if __name__ == "__main__":
    main()