from Game import Game


def main():
    game = Game()
    while True:
        game.play_round()
        play_again = input("\nVill du spela igen? (ja/nej): ").lower()
        if play_again != "ja":
            print("Tack för att du spelade!")
            break


if __name__ == "__main__":
    main()
