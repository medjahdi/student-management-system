import mysql.connector
from mysql.connector import Error
import csv
import os
from termcolor import colored
from datetime import datetime







# DB CONFIG
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'nova',
    'database': 'student_management'
}

# Student info
class Student:
    def __init__(self, id, name, surname, dob, address, nationality, faculty, department, specialization, year):
        self.id = id
        self.name = name.upper()
        self.surname = surname.upper()
        self.dob = dob
        self.address = address.upper()
        self.nationality = nationality.upper()
        self.faculty = faculty.upper()
        self.department = department.upper()
        self.specialization = specialization.upper()
        self.year = year

# Connect to MySQL Db
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='nova',
            database='student_management',
            auth_plugin='mysql_native_password'
        )
        return conn
    except Error as e:
        print(colored(f"Error connecting to MySQL: {e}", 'red'))
        return None


# my logo
def logo():
    txt="""
    ███╗   ██╗ ██████╗ ██╗   ██╗ █████╗     ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
    ████╗  ██║██╔═══██╗██║   ██║██╔══██╗    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
    ██╔██╗ ██║██║   ██║██║   ██║███████║    ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
    ██║╚██╗██║██║   ██║╚██╗ ██╔╝██╔══██║    ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
    ██║ ╚████║╚██████╔╝ ╚████╔╝ ██║  ██║    ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
    ╚═╝  ╚═══╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                                                                         
    """
    txt1="This is a simple Student Management System that allows you to manage student information...."
    txt2="      Developed by @medjahdi      |      Reach me out on : https://medjahdi.github.io       "
    print(colored(txt, 'cyan'))
    print(colored(txt1, 'green'))
    print(colored(txt2, 'green'))


# clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Load students from the database
def load_students():
    students = []
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        for row in rows:
            student = Student(*row)
            students.append(student)
        cursor.close()
        conn.close()
    return students

# Save students to the database
def save_students(students):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        # Clear existing data
        cursor.execute("DELETE FROM students")
        # Insert new data
        for student in students:
            cursor.execute('''
                INSERT INTO students (id, name, surname, dob, address, nationality, faculty, department, specialization, year)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (
                student.id, student.name, student.surname, str(student.dob), student.address,
                student.nationality, student.faculty, student.department, student.specialization, student.year
            ))
        conn.commit()
        cursor.close()
        conn.close()

# Validate date format
def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Add a new student
def add_student(students):
    print(colored("\nAdd Student", 'green'))
    id = input("Enter Student ID: ")
    name = input("Enter Name: ").upper()
    surname = input("Enter Surname: ").upper()
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")
    while not validate_date(dob):
        print(colored("Invalid date format. Please enter the date in YYYY-MM-DD format.", 'red'))
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")
    address = input("Enter Address: ").upper()
    nationality = input("Enter Nationality: ").upper()
    faculty = input("Enter Faculty: ").upper()
    department = input("Enter Department: ").upper()
    specialization = input("Enter Specialization: ").upper()
    year = input("Enter Year: ")

    student = Student(id, name, surname, dob, address, nationality, faculty, department, specialization, year)
    students.append(student)
    print(colored("Student added successfully.", 'green'))

# Delete a student by ID
def delete_student(students):
    print(colored("\n Delete Student", 'red'))
    id = input("Enter Student ID to delete: ")
    for student in students:
        if student.id == id:
            students.remove(student)
            print(colored("Student deleted successfully.", 'red'))
            return
    print(colored("Student not found.", 'red'))

# Update student info by ID
def update_student(students):
    print(colored("\nUpdate Student", 'blue'))
    id = input("Enter Student ID to update: ")
    for student in students:
        if student.id == id:
            print("Enter new details ( or press Enter to keep current value ): ")
            student.name = input(f"Name [ {student.name} ]: ").upper() or student.name
            student.surname = input(f"Surname [ {student.surname} ]: ").upper() or student.surname
            dob = input(f"Date of Birth [ {student.dob} ]: ") or student.dob
            while not validate_date(dob):
                print(colored("Invalid date format. Please enter the date in YYYY-MM-DD format.", 'red'))
                dob = input(f"Date of Birth [ {student.dob} ]: ") or student.dob
            student.dob = dob
            student.address = input(f"Address [ {student.address} ]: ").upper() or student.address
            student.nationality = input(f"Nationality [ {student.nationality} ]: ").upper() or student.nationality
            student.faculty = input(f"Faculty [ {student.faculty} ]: ").upper() or student.faculty
            student.department = input(f"Department [ {student.department} ]: ").upper() or student.department
            student.specialization = input(f"Specialization [ {student.specialization} ]: ").upper() or student.specialization
            student.year = input(f"Year [{student.year}]: ") or student.year
            print(colored("Student updated successfully.", 'blue'))
            return
    print(colored("Student not found.", 'blue'))

# print all students
def display_students(students):
    print(colored("\nAll Students"+ "-"*115, 'cyan'))
    if not students:
        print("No students to display.")
        return
    print("{:<5} {:<10} {:<10} {:<12} {:<20} {:<12} {:<10} {:<12} {:<15} {:<5}".format(
        "ID", "Name", "Surname", "DOB", "Address", "Nationality", "Faculty", "Department", "Specialization", "Year"))
    print(colored("*"*127, 'cyan'))
    for student in students:
        print("{:<5} {:<10} {:<10} {:<12} {:<20} {:<12} {:<10} {:<12} {:<15} {:<5}".format(
            student.id, student.name, student.surname, str(student.dob), student.address,
            student.nationality, student.faculty, student.department, student.specialization, student.year))
        print(colored("-"*127, 'cyan'))

# search for a student by ID or Name ...
def search_student(students):
    print(colored("\nSearch Student", 'yellow'))
    search_term = input("Enter Student ID or Name to search: ")
    results = []
    for student in students:
        if student.id == search_term or student.name.lower() == search_term.lower() or student.surname.lower() == search_term.lower():
            results.append(student)
    if results:
        print("{:<5} {:<10} {:<10} {:<12} {:<20} {:<12} {:<10} {:<12} {:<15} {:<5}".format(
            "ID", "Name", "Surname", "DOB", "Address", "Nationality", "Faculty", "Department", "Specialization", "Year"))
        print(colored("*"*127, 'cyan'))
        for student in results:
            print("{:<5} {:<10} {:<10} {:<12} {:<20} {:<12} {:<10} {:<12} {:<15} {:<5}".format(
                student.id, student.name, student.surname, str(student.dob), student.address,
                student.nationality, student.faculty, student.department, student.specialization, student.year))
            print(colored("-"*127, 'cyan'))
    else:
        print(colored("No matching students found.", 'yellow'))

# Export to CSV
def export_to_csv(students, filename='students.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Name', 'Surname', 'DOB', 'Address', 'Nationality', 'Faculty', 'Department', 'Specialization', 'Year'])
        for student in students:
            writer.writerow([
                student.id, student.name, student.surname, student.dob, student.address,
                student.nationality, student.faculty, student.department, student.specialization, student.year
            ])
    print(colored(f"Data exported to {filename}", 'green'))


