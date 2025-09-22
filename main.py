import random


roll_dice = lambda: random.randint(1, 6)
# def roll_dice():
#     return random.randint(1, 6)


def player_turn():
    player_score = 0
    print("\nDin tur att spela.")

    while True:
        choice = input(
            "Vill du rulla tärningen (rulla) eller stanna (stanna)? "
        ).lower()

        if choice == "rulla":
            dice_roll = roll_dice()
            player_score += dice_roll
            print(f"Du slog en {dice_roll}. Din totala poäng är nu {player_score}.")

            if player_score > 21:
                print("Din poäng är över 21! Du förlorar direkt.")
                return player_score

        elif choice == "stanna":
            print(f"Du valde att stanna på {player_score} poäng.")
            return player_score

        else:
            print("Ogiltigt val. Välj 'rulla' eller 'stanna'.")


def dealer_turn():
    dealer_score = 0
    print("\nDealern spelar.")

    while dealer_score < 17:
        dice_roll = roll_dice()
        dealer_score += dice_roll
        print(
            f"Dealern slog en {dice_roll}. Dealerns totala poäng är nu {dealer_score}."
        )

    if dealer_score > 21:
        print("Dealerns poäng är över 21! Dealern förlorar.")

    return dealer_score


def determine_winner(player_score, dealer_score):
    if player_score > 21:
        # Den här regeln hanteras redan i player_turn, men det är bra att dubbelkolla
        print("Du förlorade, eftersom din poäng är över 21.")
    elif dealer_score > 21:
        print("Du vinner! Dealerns poäng är över 21.")
    elif player_score > dealer_score:
        print("Du vinner! Din poäng är närmare 21 än dealerns.")
    elif player_score < dealer_score:
        print("Du förlorar. Dealerns poäng är närmare 21 än din.")
    else:  # player_score == dealer_score
        print("Det blev oavgjort!")


determine_winner(23, 15)
