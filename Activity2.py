#This program will ask the user for their age and password and will verify if they are old enough and if the password is correct.
age = int(input("What is your age: "))

if age >= 18:
    print("Age verified")
else:
    print("Access denied")
    exit()

password = str(input("Enter a password: "))

if password == "password123":
    print("Password verified")
else:
    print("Access denied")


