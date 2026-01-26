#A game where the computer draws a random integer between 1 and 10.
import random
number=random.randint(1,10)
guess=0

#The user tries to guess the number until they guess the right number.
while guess != number:
    guess= int(input("Guess the random number: "))

#After each guess the program prints out a text: Too high, Too low or Correct.
    if guess<number:
        print("To low")
    elif guess>number:
        print("To high")
    else:
        print("Correct")
