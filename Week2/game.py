# Keeley Imlah
# CSE-210 Winter 2022
# Tic Tac Toe game in Python

def main():
    player = next_player("")
    values = create_board()
    while not (check_for_win(values) or check_for_tie(values)):
        game_board(values)
        make_a_move(player, values)
        player = next_player(player)
    game_board(values)
    print("Great game! Thanks for playing!")

def create_board():
    values = []
    for square in range(9):
        values.append(square + 1)
    return values


# function to print game when called
def game_board(values):
    # row 1 boxes
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print("\t_____|_____|_____")
    # row 2 boxes
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print("\t_____|_____|_____")
    # row 3 boxes
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

def check_for_win(values):
    return (values[0] == values[1] == values[2] or
            values[3] == values[4] == values[5] or
            values[6] == values[7] == values[8] or
            values[0] == values[3] == values[6] or
            values[1] == values[4] == values[7] or
            values[2] == values[5] == values[8] or
            values[0] == values[4] == values[8] or
            values[2] == values[4] == values[6])

# check to see if game is a tie
def check_for_tie(values):
    for square in range(9):
        if values[square] != "X" and values[square] != "O":
            return False
    return True 

def make_a_move(player, values):
    # square is the spot chosen by player for that turn
    square = int(input(f"{player}'s turn to choose a square (numbers 1-9): "))
    # square chosen by current player is the input value -1 (used to mark correct square)
    values[square -1] = player

def next_player(current):
    if current == "" or current =="O":
        return "X"
    elif current == "X":
        return "O"

if __name__ == "__main__":
    main()