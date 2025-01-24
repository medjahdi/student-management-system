"""
Copyright (c) 2025 @medjahdi
"""
import hashlib
from termcolor import colored



HASHED_PASSWORD = "19e05df6b2e5fb94f3ee7eed2c02d340a1128a00231f5f6949641a143ab3b57a"

def login():
    art = """
    +-+-+-+-+-+-+-+-+-+-+-+
    |LOGIN TO YOUR ACCOUNT|
    +-+-+-+-+-+-+-+-+-+-+-+
    """
    print(colored(art, 'cyan'))


    attempts = 3
    
    while attempts > 0:
        password = input("Enter password: ")
        hashed_input = hashlib.sha256(password.encode()).hexdigest()

        if hashed_input == HASHED_PASSWORD:
            print(colored("Login successful! Welcome to the 𓆰 NOVA Management System.", 'green'))
            return True
        else:
            attempts -= 1



            """
Copyright (c) 2025 @medjahdi
"""
            if attempts > 0:
                print(colored(f"Invalid password. {attempts} attempts remaining.", 'red'))
            else:
                print(colored("Too many failed attempts. Access denied.", 'red'))
                return False
