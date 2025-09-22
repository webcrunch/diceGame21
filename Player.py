from Dice import Dice


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.dice = Dice()  # Spelaren har nu tillgång till en tärning

    def roll_dice(self):
        roll = self.dice.roll()
        self.score += roll
        return roll

    def __str__(self):
        return f"{self.name}s poäng: {self.score}"
