import random
from time import sleep

answer = random.randint(1,5)
print(answer)
numCupboard = 5
correct = False

WrongGuesses = ["The door fell off, sorry.", "A cricket jumped at you and you got scared.", "a"]

print("Welcome to the Agnry Goblin Hunt, a very epic game of adventure and excitement.")
name = input("What is your name? ")

print("Hello", name + ", do you think you can find the goblin hiding in the kitchen cupboards? ")
sleep(1)
print("Yes?")
sleep(1)
print("Great!")
sleep(1)
print("|_| |_| |_| |_| |_|")
sleep(1)

guesses = []

while correct == False:
    guess = int(input("Which cupboard do you think the goblin is in? "))
    guesses.append(guess)
    if guess > numCupboard or guess < 0:
        print("Bad Input.")
    elif guess == answer:
        print("Very neat, you found the goblin!")
        correct = True
    else:
        print(random.choice(WrongGuesses))
