import unittest
from Player import Player
from Game import Game
from Utils import determine_winner_and_return_result


class TestGameLogic(unittest.TestCase):

    def _print_scenario(self, description):
        """Hjälpmetod för att skriva ut en tydlig rubrik för varje scenario."""
        print(f"\n--- Scenario: {description} ---")

    def test_winner_determination_player_wins(self):
        self._print_scenario("Spelare vinner")

        # Given: Spelaren har 18 poäng och dealern har 15
        player_score = 18
        dealer_score = 15
        print(f"Given en spelare med poäng {player_score}")
        print(f"And en dealer med poäng {dealer_score}")

        # When: Spelet slutar
        result = determine_winner_and_return_result(player_score, dealer_score)
        print("When spelet slutar")

        # Then: Spelaren ska vara vinnaren
        self.assertEqual(result, "player")
        print(f"Then spelaren ska vara vinnaren. Resultat: '{result}' - TEST GODKÄNT")

    def test_winner_determination_player_wins(self):
        self._print_scenario("Spelare över 21")

        # Given: Spelaren har 18 poäng och dealern har 15
        player_score = 22
        dealer_score = 15
        print(f"Given en spelare med poäng {player_score}")
        print(f"And en dealer med poäng {dealer_score}")

        # When: Spelet slutar
        result = determine_winner_and_return_result(player_score, dealer_score)
        print("When spelet slutar")

        # Then: Spelaren ska vara förloraren
        self.assertEqual(result, "dealer")
        print(f"Then spelaren ska vara förlorare. Resultat: '{result}' - TEST GODKÄNT")

    def test_winner_determination_dealer_wins(self):
        self._print_scenario("Dealer vinner")

        # Given: Spelaren har 15 poäng och dealern har 18
        player_score = 15
        dealer_score = 18
        print(f"Given en spelare med poäng {player_score}")
        print(f"And en dealer med poäng {dealer_score}")

        # When: Spelet slutar
        result = determine_winner_and_return_result(player_score, dealer_score)
        print("When spelet slutar")

        # Then: Dealern ska vara vinnaren
        self.assertEqual(result, "dealer")
        print(f"Then dealern ska vara vinnaren. Resultat: '{result}' - TEST GODKÄNT")

    def test_winner_determination_draw(self):
        self._print_scenario("Oavgjort")

        # Given: Spelaren har 17 poäng och dealern har 17
        player_score = 17
        dealer_score = 17
        print(f"Given en spelare med poäng {player_score}")
        print(f"And en dealer med poäng {dealer_score}")

        # When: Spelet slutar
        result = determine_winner_and_return_result(player_score, dealer_score)
        print("When spelet slutar")

        # Then: Spelet ska vara oavgjort
        self.assertEqual(result, "draw")
        print(f"Then spelet ska vara oavgjort. Resultat: '{result}' - TEST GODKÄNT")

    # Lägg till dina andra tester här på samma sätt


if __name__ == "__main__":
    unittest.main()
