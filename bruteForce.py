import time
login = {"adminLogin": "admin123", "password": "123456"}
      
loginUser = input("Enter your login: ")
passwordUser = input("Enter your password: ")

if loginUser == login["adminLogin"] and passwordUser == login["password"]:
    print("Access granted")
else:
    print("Access denied")
      
# This is a simple brute-force login simulation using a dictionary to store login credentials.

attempts = 3
while attempts > 0:
    loginUser = input("Enter your login: ")
    passwordUser = input("Enter your password: ")

    if loginUser == login["adminLogin"] and passwordUser == login["password"]:
        print("Access granted")
        break
    else:
        attempts -= 1
        print(f"Access denied. You have {attempts} attempts left.")
        time.sleep(2)  # Adding a delay to simulate processing time
if attempts == 0:
    print("Too many failed attempts. Access locked.")