import random


def guessing_game():
    ranno = random.randint(0, 50)
    i = 0
    name = input("\nWhat's your name?: ")
    print(f"\nWelcome to this game {name}")
    while True:
        response = int(input(f"What no has been chosen? ({i + 1}/3 chance): "))
        i += 1
        if i >= 3:
            print("Sorry, your 3 attempts are over. Better luck next time\n")
            break
        elif response == ranno:
            print("just right")
            break
        elif response > ranno:
            print("Too high")
        elif response < ranno:
            print("Too low")


guessing_game()
