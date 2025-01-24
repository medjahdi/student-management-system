"""
Copyright (c) 2025 @medjahdi
"""
import mysql.connector
from mysql.connector import Error
from login import login
from setting import (
    load_students, save_students, add_student, delete_student,
    update_student, display_students, search_student ,export_to_csv, logo
)



# ANSI color codes
MAGENTA = '\033[95m'
RESET = '\033[0m'





# start ....
def main():
    if login():
        pass
    else:
        print(f"{MAGENTA}Exiting program.{RESET}")
        return
    logo()
    students = load_students()

    while True:
        print(f"{MAGENTA}\nStudent Management System{RESET}")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. Display All Students")
        print("5. Search Student")
        print("6. Export to CSV")
        print("7. Database info")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")

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
            print(f"{MAGENTA}Database info{RESET}")
            print(f"{MAGENTA}Database: MySQL{RESET}")
            print(f"{MAGENTA}Host: localhost{RESET}")
            print(f"{MAGENTA}Database name: student_management{RESET}")
            print(f"{MAGENTA}Table name: students{RESET}")
            print(f"{MAGENTA}Username: root{RESET}")
            print(f"{MAGENTA}Password: nova{RESET}")
        
        elif choice == '8':
            save_students(students)
            print(f"{MAGENTA}Exiting program. Data saved.{RESET}")
            break
        else:
            print(f"{MAGENTA}Invalid choice. Please select a number between 1 and 6.{RESET}")




if __name__ == "__main__":
    main()
"""
Copyright (c) 2025 @medjahdi
"""
