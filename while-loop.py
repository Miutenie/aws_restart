# a while loop makes a section of code repeat until a certain condition is met
# by convention, import statements are place at the top of the script.
import random
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
#enter a statement which will generate a random number between 1 and 10 using randint()
number = random.randint(1,10)
isGuessRight = False

#create a while loop
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else: 
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))
