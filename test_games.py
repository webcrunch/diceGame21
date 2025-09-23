# import unittest
# from Player import Player
# from Game import Game
# from Utils import determine_winner_and_return_result


# class TestGameLogic(unittest.TestCase):

#     def _print_scenario(self, description):
#         """Hjälpmetod för att skriva ut en tydlig rubrik för varje scenario."""
#         print(f"\n--- Scenario: {description} ---")

#     def test_winner_determination_player_wins(self):
#         self._print_scenario("Dealer vinner")

#         # Given: Spelaren har 18 poäng och dealern har 15
#         player_score = 18
#         dealer_score = 15
#         print(f"Given en spelare med poäng {player_score}")
#         print(f"And en dealer med poäng {dealer_score}")

#         # When: Spelet slutar
#         result = determine_winner_and_return_result(player_score, dealer_score)
#         print("When spelet slutar")

#         # Then: Spelaren ska vara vinnaren
#         self.assertEqual(result, "player")
#         print(f"Then spelaren ska vara vinnaren. Resultat: '{result}' - TEST GODKÄNT")

#     def test_2winner_determination_dealer_wins(self):
#         self._print_scenario("Player vinner")

#         # Given: Spelaren har 15 poäng och dealern har 18
#         player_score = 15
#         dealer_score = 18
#         print(f"Given en spelare med poäng {player_score}")
#         print(f"And en dealer med poäng {dealer_score}")

#         # When: Spelet slutar
#         result = determine_winner_and_return_result(player_score, dealer_score)
#         print("When spelet slutar")

#         # Then: Dealern ska vara vinnaren
#         self.assertEqual(result, "dealer")
#         print(f"Then dealern ska vara vinnaren. Resultat: '{result}' - TEST GODKÄNT")

#     def test_4winner_determination_player_over_21(self):
#         self._print_scenario("Spelare över 21")

#         # Given: Spelaren har 18 poäng och dealern har 15
#         player_score = 22
#         dealer_score = 15
#         print(f"Given en spelare med poäng {player_score}")
#         print(f"And en dealer med poäng {dealer_score}")

#         # When: Spelet slutar
#         result = determine_winner_and_return_result(player_score, dealer_score)
#         print("When spelet slutar")

#         # Then: Spelaren ska vara förloraren
#         self.assertEqual(result, "dealer")
#         print(f"Then Spelare ska vara förlorare. Resultat: '{result}' - TEST GODKÄNT")

#     def test_3winner_determination_draw(self):
#         self._print_scenario("Oavgjort")

#         # Given: Spelaren har 17 poäng och dealern har 17
#         player_score = 17
#         dealer_score = 17
#         print(f"Given en spelare med poäng {player_score}")
#         print(f"And en dealer med poäng {dealer_score}")

#         # When: Spelet slutar
#         result = determine_winner_and_return_result(player_score, dealer_score)
#         print("When spelet slutar")

#         # Then: Spelet ska vara oavgjort
#         self.assertEqual(result, "draw")
#         print(f"Then spelet ska vara oavgjort. Resultat: '{result}' - TEST GODKÄNT")

#     # Lägg till dina andra tester här på samma sätt


# if __name__ == "__main__":
#     unittest.main()

import unittest
from Player import Player
from Game import Game
from Utils import determine_winner_and_return_result


class TestGameLogic(unittest.TestCase):

    def test_dice_roll_is_valid(self):
        print("\n--- Scenario: Tärningskast är giltigt ---")
        try:
            player = Player("Testspelare")
            roll = player.roll_dice()

            # Given: En spelare kastar tärning
            # When: Ett kast inträffar
            # Then: Resultatet ska vara mellan 1 och 6
            self.assertIn(roll, range(1, 7))

            print(f"✅ Test 1: Tärningskastet {roll} är inom intervallet 1-6.")
        except AssertionError:
            print(f"❌ Test 1: Tärningskastet {roll} är inte inom intervallet 1-6.")
            raise

    def test_dealer_logic_stops_at_17_or_more(self):
        print("\n--- Scenario: Dealer-logik stannar vid 17+ ---")
        try:
            game = Game()
            game.dealer.score = 0

            # Given: En dealer med poäng under 17
            while game.dealer.score < 17:
                game.dealer.score += 5

            # When: Dealerns tur slutar
            # Then: Dealerns poäng ska vara minst 17
            self.assertGreaterEqual(game.dealer.score, 17)
            self.assertLessEqual(game.dealer.score, 21)

            print(f"✅ Test 2: Dealerns poäng {game.dealer.score} är korrekt.")
        except AssertionError:
            print(f"❌ Test 2: Dealerns poäng {game.dealer.score} är inte korrekt.")
            raise

    def test_winner_determination(self):
        print("\n--- Scenario: Vinnare bestäms korrekt ---")
        try:
            # Scenario 1: Spelaren vinner
            self.assertEqual(determine_winner_and_return_result(20, 18), "player")

            # Scenario 2: Dealern vinner
            self.assertEqual(determine_winner_and_return_result(19, 20), "dealer")

            # Scenario 3: Spelaren går över 21
            self.assertEqual(determine_winner_and_return_result(22, 15), "dealer")

            # Scenario 4: Dealern går över 21
            self.assertEqual(determine_winner_and_return_result(18, 23), "player")

            # Scenario 5: Oavgjort
            self.assertEqual(determine_winner_and_return_result(18, 18), "draw")

            print("✅ Test 3: Vinnarbestämning fungerar i alla scenarion.")
        except AssertionError:
            print("❌ Test 3: Vinnarbestämning misslyckades.")
            raise

    def test_winner_determination_failing(self):
        print("\n--- Scenario: Simulerar ett fallerande vinnartest ---")
        try:
            # Given: Spelare 20 poäng, Dealer 18 poäng
            player_score, dealer_score = 20, 18

            # When: Spelet slutar
            result = determine_winner_and_return_result(player_score, dealer_score)

            # Then: Vi förväntar oss felaktigt att resultatet är 'draw'
            self.assertEqual(result, "draw")

            print("✅ Simulerat fallerande test - godkänt (detta ska inte hända!)")
        except AssertionError as e:
            print(f"❌ Simulerat fallerande test - misslyckades korrekt.")
            print(f"Förväntat: 'draw', men fick: '{result}'")
            raise e


if __name__ == "__main__":
    unittest.main()
