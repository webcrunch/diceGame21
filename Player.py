import random


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def roll_dice(self):
        roll = random.randint(1, 6)
        self.score += roll
        return roll

    def __str__(self):
        return f"{self.name}s poäng: {self.score}"
