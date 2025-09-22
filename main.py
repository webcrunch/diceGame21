import random


roll_dice = lambda: random.randint(1, 6)
# def roll_dice():
#     return random.randint(1, 6)


def player_turn():
    player_score = 0
    print("\nDin tur att spela.")


print(roll_dice())
