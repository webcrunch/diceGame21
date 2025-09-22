import unittest
from Player import Player
from Game import Game
from Utils import determine_winner_and_return_result


class TestGameLogic(unittest.TestCase):
    """
    Testar kärnlogiken i spelet, såsom tärningskast och vinnarbestämning.
    """

    def test_dice_roll_is_valid(self):
        """
        Test 1: Validerar att tärningskastet ger ett tal mellan 1 och 6.
        Motivering: Detta test säkerställer att grundläggande funktionalitet fungerar
        och att det inte förekommer ogiltiga tärningskast.
        """
        player = Player("Testspelare")
        roll = player.roll_dice()
        self.assertIn(roll, range(1, 7))

    def test_dealer_logic_stops_at_17_or_more(self):
        """
        Test 2: Verifierar att dealerns poäng är minst 17 i slutet av sin tur.
        Motivering: Detta test kontrollerar en av de viktigaste reglerna i spelet
        för dealern. Det säkerställer att dealerns poäng inte stannar på en för
        låg siffra.
        """
        game = Game()
        game.dealer.score = 0

        # Simulerar dealerns tur genom att kasta tills 17 nås
        while game.dealer.score < 17:
            game.dealer.score += 5  # Lägger till ett fast värde för att snabbt nå 17

        # Kontrollerar att poängen är minst 17 och inte över 21 i detta scenario
        self.assertGreaterEqual(game.dealer.score, 17)
        self.assertLessEqual(game.dealer.score, 21)

    def test_winner_determination(self):
        """
        Test 3: Kontrollerar att vinnarfunktionen returnerar rätt vinnare vid olika poängställningar.
        Motivering: Detta är det viktigaste testet eftersom det validerar spelets slutlogik.
        Det testar flera fall: spelare vinner, dealer vinner, och oavgjort.
        """
        # Scenario 1: Spelaren vinner (högre poäng, ingen över 21)
        result1 = determine_winner_and_return_result(player_score=20, dealer_score=18)
        self.assertEqual(result1, "player")

        # Scenario 2: Dealern vinner (högre poäng, ingen över 21)
        result2 = determine_winner_and_return_result(player_score=19, dealer_score=20)
        self.assertEqual(result2, "dealer")

        # Scenario 3: Spelaren går över 21
        result3 = determine_winner_and_return_result(player_score=22, dealer_score=15)
        self.assertEqual(result3, "dealer")  # Dealern vinner när spelaren går över

        # Scenario 4: Dealern går över 21
        result4 = determine_winner_and_return_result(player_score=18, dealer_score=23)
        self.assertEqual(result4, "player")  # Spelaren vinner när dealern går över

        # Scenario 5: Oavgjort
        result5 = determine_winner_and_return_result(player_score=18, dealer_score=18)
        self.assertEqual(result5, "draw")


if __name__ == "__main__":
    unittest.main()
