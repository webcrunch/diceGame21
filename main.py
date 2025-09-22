import random


def roll_dice():
    """Simulerar ett tärningskast och returnerar ett värde mellan 1 och 6."""
    return random.randint(1, 6)


print(roll_dice())
