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


