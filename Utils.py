def determine_winner(player_score, dealer_score):
    if player_score > 21:
        print("Du förlorade, eftersom din poäng är över 21.")
    elif dealer_score > 21:
        print("Du vinner! Dealerns poäng är över 21.")
    elif player_score > dealer_score:
        print("Du vinner! Din poäng är närmare 21 än dealerns.")
    elif player_score < dealer_score:
        print("Du förlorar. Dealerns poäng är närmare 21 än din.")
    else:
        print("Det blev oavgjort!")


def determine_winner_and_return_result(player_score, dealer_score):
    if player_score > 21:
        determine_winner(player_score, dealer_score)
        return "dealer"
    elif dealer_score > 21:
        determine_winner(player_score, dealer_score)
        return "player"
    elif player_score > dealer_score:
        determine_winner(player_score, dealer_score)
        return "player"
    elif player_score < dealer_score:
        determine_winner(player_score, dealer_score)
        return "dealer"
    else:
        determine_winner(player_score, dealer_score)
        return "draw"
