#A program that converts inches to centimeters.
while True:
    inches= float(input("Enter the number of inches (Only positive numbers): "))

    #If the user inputs a negative value, then the program ends.
    if inches<0:
        print("Program ended")
        break
    print(f"{inches} inches is {inches*2.54} centimeters")