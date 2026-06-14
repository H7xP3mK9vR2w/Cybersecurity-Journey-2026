import random
import string

def password_generator():

    length = int(input("Password Length: "))

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:")
    print(password)

def password_checker():

    password = input("Enter Password: ")

    if len(password) < 8:
        print("Weak Password")

    elif len(password) < 12:
        print("Moderate Password")

    else:
        print("Strong Password")

while True:

    print("\n=== Security Toolkit ===")
    print("1. Password Generator")
    print("2. Password Checker")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        password_generator()

    elif choice == "2":
        password_checker()

    elif choice == "3":
        print("Goodbye")
        break

    else:
        print("Invalid Choice")