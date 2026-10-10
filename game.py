import random



while True:
    things = ["Rock", "Paper", "Scissors"]
    bot = random.choice(things)
    player = input("Enter what you choose in Rock, Paper, Scissors: ")

    print(f"Bot chose: {bot}")
    print(f"Player chose: {player}")
    if player == "exit":
        print("Okay quit the game")
        break
    if bot == player:
        print("It's a tie")
    elif bot == "Paper" and player == "Scissors" or bot == "Scissors" and player == "Rock" or bot == "Rock" and player == "Paper":
        print("Player is wins")
    elif bot == "Scissors" and player == "Paper" or bot == "Rock" and player == "Scissors" or bot == "Paper" and player == "Rock":
        print("Bot wins")
    else:
        print("Please choose valid options")

