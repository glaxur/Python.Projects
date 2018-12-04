import random

computers_number = random.randint(1,100)
prompt = "what is your guess? "
while True:
    players_guess = int(input(prompt))

    if computers_number == int(players_guess):
        print("correct!")
        break
    elif computers_number > int(players_guess):
        print("Too low")
    else:
        print("Too high")
    
    
    




