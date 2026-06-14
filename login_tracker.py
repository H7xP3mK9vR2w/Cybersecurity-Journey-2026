correct_password = "Cyber123"

attempts = 0

while attempts < 3:

    password = input("Enter password: ")

    if password == correct_password:
        print("Access Granted")
        break

    else:
        attempts += 1
        print("Wrong Password")

if attempts == 3:
    print("Account Locked")