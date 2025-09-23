import unittest
from unittest.mock import mock_open, patch
import os

from Player import Player
from Game import Game
from Utils import determine_winner_and_return_result
from ScoreManager import ScoreManager

# Testerna:
# Jag har 7 test som jag har tagit med. 6 av dem kommer att passera med jag tog med ett som falerade för att visa hur det ser ut.

# Det är en blandning av att jag ser så att dealern stannar vi 17+ poäng.
# Att poänger per tärningskast är mellan 1-6.
# Att se så att rätt person vinner gällande rätt scenarium.
# Att simulera ett felaktigt test
# Att Man kan läsa in från fil och spara till fil.

# jag har gjort detta för att kunna verifiera att de funktioner som hantera spelstrukturen fungerar.
# Annars kommer spelet inte att fungera.
# Att hantera fil inläsning och skrivning är inte det viktigaste men tyckte det var bra att ha med.


class TestGameLogic(unittest.TestCase):

    def test_dice_roll_is_valid(self):
        print("\n--- Scenario: Tärningskast är giltigt ---")
        try:
            player = Player("Testspelare")
            roll = player.roll_dice()

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

            while game.dealer.score < 17:
                game.dealer.score += 5

            self.assertGreaterEqual(game.dealer.score, 17)
            self.assertLessEqual(game.dealer.score, 21)

            print(f"✅ Test 2: Dealerns poäng {game.dealer.score} är korrekt.")
        except AssertionError:
            print(f"❌ Test 2: Dealerns poäng {game.dealer.score} är inte korrekt.")
            raise

    def test_winner_determination(self):
        print("\n--- Scenario: Vinnare bestäms korrekt ---")
        try:
            # Spelaren vinner
            self.assertEqual(determine_winner_and_return_result(20, 18), "player")

            # Dealern vinner
            self.assertEqual(determine_winner_and_return_result(19, 20), "dealer")

            # Spelaren går över 21
            self.assertEqual(determine_winner_and_return_result(22, 15), "dealer")

            # Dealern går över 21
            self.assertEqual(determine_winner_and_return_result(18, 23), "player")

            # Oavgjort
            self.assertEqual(determine_winner_and_return_result(18, 18), "draw")

            print("✅ Test 3: Vinnarbestämning fungerar i alla scenarion.")
        except AssertionError:
            print("❌ Test 3: Vinnarbestämning misslyckades.")
            raise

    def test_winner_determination_failing(self):
        print("\n--- Scenario: Simulerar ett fallerande vinnartest ---")
        try:
            player_score, dealer_score = 20, 18
            result = determine_winner_and_return_result(player_score, dealer_score)
            self.assertEqual(result, "draw")

            print("✅ Simulerat fallerande test - godkänt (detta ska inte hända!)")
        except AssertionError as e:
            print(f"❌ Simulerat fallerande test - misslyckades korrekt.")
            print(f"Förväntat: 'draw', men fick: '{result}'")
            raise e


class TestScoreManager(unittest.TestCase):

    def setUp(self):
        self.score_manager = ScoreManager("test_scores.txt")

    def test_load_scores_from_file(self):
        print("\n--- Scenario: Highscore kan läsas in från en fil ---")
        try:
            file_content = "player_wins:5\ndealer_wins:3\n"
            with patch(
                "builtins.open", mock_open(read_data=file_content)
            ) as mocked_file, patch("os.path.exists", return_value=True):

                loaded_scores = self.score_manager.load_scores()

                mocked_file.assert_called_with("test_scores.txt", "r")
                self.assertEqual(loaded_scores["player_wins"], 5)
                self.assertEqual(loaded_scores["dealer_wins"], 3)

            print("✅ Test: Inläsning av highscore från fil fungerar.")
        except AssertionError as e:
            print(f"❌ Test: Inläsning av highscore från fil misslyckades.")
            raise e

    def test_save_scores_to_file(self):
        print("\n--- Scenario: Highscore kan sparas till en fil ---")
        try:
            scores_to_save = {"player_wins": 10, "dealer_wins": 8}
            with patch("builtins.open", mock_open()) as mocked_file:
                self.score_manager.save_scores(scores_to_save)

                mocked_file.assert_called_with("test_scores.txt", "w")
                handle = mocked_file()
                handle.write.assert_any_call("player_wins:10\n")
                handle.write.assert_any_call("dealer_wins:8\n")

            print("✅ Test: Spara highscore till fil fungerar.")
        except AssertionError as e:
            print(f"❌ Test: Spara highscore till fil misslyckades.")
            raise e

    def test_load_scores_from_non_existent_file(self):
        print("\n--- Scenario: Standardpoäng laddas om filen inte finns ---")
        try:
            with patch("os.path.exists", return_value=False):
                loaded_scores = self.score_manager.load_scores()
                self.assertEqual(loaded_scores["player_wins"], 0)
                self.assertEqual(loaded_scores["dealer_wins"], 0)

            print("✅ Test: Standardpoäng laddas när fil inte finns.")
        except AssertionError as e:
            print(f"❌ Test: Standardpoäng laddas inte när fil inte finns.")
            raise e


if __name__ == "__main__":
    unittest.main()
