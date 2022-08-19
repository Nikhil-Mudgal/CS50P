import random # import random library 
# from random import choice # this makes choice belong to the scope of the generate.py function!

coin = random.choice(["heads", "tails"]) # composes a list mentioned inside the argument

random_int = random.randint(1,10)

cards = ["jack","queen","king"]

random.shuffle(cards)

for card in cards:
    print(card)