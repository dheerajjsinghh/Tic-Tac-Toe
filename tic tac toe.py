print("Welcome to the game of Tic Tac Toe")
game = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_game():
    print(f"{game[0]} | {game[1]} | {game[2]}")
    print("--+---+--")
    print(f"{game[3]} | {game[4]} | {game[5]}")
    print("--+---+--")
    print(f"{game[6]} | {game[7]} | {game[8]}")

def check_winner(player):
    win_cond= [
        [game[0], game[1], game[2]],
        [game[3], game[4], game[5]],
        [game[6], game[7], game[8]],
        [game[0], game[3], game[6]],
        [game[1], game[4], game[7]],
        [game[2], game[5], game[8]],
        [game[0], game[4], game[8]],
        [game[2], game[4], game[6]],
    ]
    return [player, player, player] in win_cond

def make_move(player):
    while True:
        try:
            move = int(input(f"Enter block number to put {player}: ")) - 1
            if game[move] not in ["X", "O"]:
                game[move] = player
                break
            else:
                print("Block already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

print_game()
while True:
    print("\n--- First player's turn (X) ---")
    make_move("X")
    print_game()
    if check_winner("X"):
        print("\n--- Player 1 (X) Won ---")
        break

    print("\n--- Second player's turn (O) ---")
    make_move("O")
    print_game()
    if check_winner("O"):
        print("\n--- Player 2 (O) Won ---")
        break
