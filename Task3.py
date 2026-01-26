#A program that asks the user to enter numbers.
Numbers=[]
while True:
    number = input("Enter a number:")

#If the user enter an empty string to quit.
    if number=="":
        print("Quit")
        break
    Numbers.append(float(number))

#The program prints out the smallest and largest number from the numbers it received.
print("Smallest number: ", min(Numbers))
print("Largest number: ", max(Numbers))
