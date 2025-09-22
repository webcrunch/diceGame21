from Player import Player
from ScoreManager import ScoreManager
from Utils import determine_winner_and_return_result


class Game:
    def __init__(self):
        self.score_manager = ScoreManager()
        self.scores = self.score_manager.load_scores()
        self.player = Player("Spelare")
        self.dealer = Player("Dealer")

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

        # Bestämmer vinnaren för att uppdatera poängen
        winner = determine_winner_and_return_result(
            self.player.score, self.dealer.score
        )

        if winner == "player":
            self.scores["player_wins"] += 1
        elif winner == "dealer":
            self.scores["dealer_wins"] += 1

        print("\nUppdaterad ställning:")
        print(f"Spelare: {self.scores['player_wins']} vinster")
        print(f"Dealer: {self.scores['dealer_wins']} vinster")

        # Spara poängen med ScoreManager-instansen
        self.score_manager.save_scores(self.scores)
