""" guessing game using a function """




import random

computers_number = random.randint(1,100)
PROMPT = "What is your guess?"
def do_guess_round():
    """Choose a random number,ask user for a guess
    check whether the guess is true and repeat whether the user is correct"""
    computers_number = random.randint(1,100)
    while True:
        players_guess = int(input(PROMPT))

        if computers_number == int(players_guess):
            print("correct!")
            break
        elif computers_number > int(players_guess):
            print("Too low")
        else:
            print("Too high")
while True:
    print("Starting a new round")
    print("The computer's number should be "+str(computers_number))
    print("Let the guessing begin!!!")
    do_guess_round()
    print(" ")
    
