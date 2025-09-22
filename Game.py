# Game.py

import os.path
from Player import Player
from Utils import determine_winner_and_return_result


class Game:
    def __init__(self):
        self.player = Player("Spelare")
        self.dealer = Player("Dealer")
        self.scores = {"player_wins": 0, "dealer_wins": 0}
        self.load_scores()

    def load_scores(self):
        if os.path.exists("scores.txt"):
            with open("scores.txt", "r") as file:
                for line in file:
                    try:
                        key, value = line.strip().split(":")
                        self.scores[key] = int(value)
                    except (ValueError, IndexError):
                        # Ignorera felaktiga rader för att undvika krascher
                        continue
        print("Nuvarande ställning:")
        print(f"Spelare: {self.scores['player_wins']} vinster")
        print(f"Dealer: {self.scores['dealer_wins']} vinster")

    def save_scores(self):
        with open("scores.txt", "w") as file:
            for key, value in self.scores.items():
                file.write(f"{key}:{value}\n")

    def play_round(self):
        print("\nNy runda startar!")

        self.player.score = 0
        self.dealer.score = 0

        # Spelarens tur
        while True:
            choice = input(
                "Vill du rulla tärningen (rulla) eller stanna (stanna)? "
            ).lower()
            if choice == "rulla":
                roll = self.player.roll_dice()
                print(f"Du slog en {roll}. Din totala poäng är nu {self.player.score}.")
                if self.player.score > 21:
                    print("Din poäng är över 21! Du förlorar direkt.")
                    break
            elif choice == "stanna":
                print(f"Du valde att stanna på {self.player.score} poäng.")
                break
            else:
                print("Ogiltigt val. Välj 'rulla' eller 'stanna'.")

        # Dealerns tur
        print("\nDealern spelar.")
        while self.dealer.score < 17:
            roll = self.dealer.roll_dice()
            print(
                f"Dealern slog en {roll}. Dealerns totala poäng är nu {self.dealer.score}."
            )

        # Avgör vinnaren
        print(f"\nSPELET ÄR SLUT:")
        print(self.player)
        print(self.dealer)

        # Här bestäms vinnaren för att uppdatera poängen
        winner = determine_winner_and_return_result(
            self.player.score, self.dealer.score
        )

        # print(winner) - Denna rad kan du ta bort då den bara var för att testa

        if winner == "player":
            self.scores["player_wins"] += 1
        elif winner == "dealer":
            self.scores["dealer_wins"] += 1

        print("\nUppdaterad ställning:")
        print(f"Spelare: {self.scores['player_wins']} vinster")
        print(f"Dealer: {self.scores['dealer_wins']} vinster")

        self.save_scores()
