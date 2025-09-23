from Game import Game


def main():
    game = Game()
    while True:
        game.play_round()
        if input("\nVill du spela igen? (ja/nej): ").lower() != "ja":
            print("Tack för att du spelade!")
            break


if __name__ == "__main__":
    main()
