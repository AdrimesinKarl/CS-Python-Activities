print("Welcome to the login system")
username = str(input("Enter your username: "))

if username == "admin":
    print("Username verified")
else:
    print("Wrong username, try again!")
    exit()

age = int(input("Enter your age: "))

if age >= 18:
    print("Age verified")
else:
    print("Access denied")
    exit()

password = str(input("Enter your password: "))

if password == "admin123":
    print("Password verified")
else:
    print("Access denied")
    exit()

print("List with elements")
list = ["Mercury", "Mars", "Jupiter", "Uranus"]
list.insert(0,"Moon")
list[3] = "Venus"
for item in list:
    print(item)