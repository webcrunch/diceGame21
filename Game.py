import random
from Player import Player  # Lägg till den här raden för att importera Player-klassen
from Utils import determine_winner  # Importera funktionen här


class Game:
    def __init__(self):
        self.player = Player("Spelare")
        self.dealer = Player("Dealer")

    def play_round(self):
        print("Ny runda startar!")

        # Återställ poängen för en ny runda
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

        determine_winner(self.player.score, self.dealer.score)
