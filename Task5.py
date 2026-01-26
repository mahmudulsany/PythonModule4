#A program that asks the user for a username and password.
attempt=0

while attempt<5:
    username= input("Enter your username: ")
    password= input("Enter your password: ")

#If both are correct, the program print out welcome.
    if username=="python" and password=="rules":
        print("Welcome")
        break

#If either or both are incorrect, the program ask the user to enter the username and password again.
    else:
        attempt = attempt + 1
        if attempt<5:
            print("Please try again.")

#After five failed attempts the program prints out Access denied.
if attempt==5:
    print("Access denied")



