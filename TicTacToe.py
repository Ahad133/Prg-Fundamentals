import time

# Define the Board
board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

# Print the Board
def print_board():
    print("      |      |     ")
    print("   "+board[1]+"  |  "+board[2]+"   |  "+board[3]+"   ")
    print("      |      |      ")
    print("------|------|------")
    print("      |      |      ")
    print("   "+board[4]+"  |  "+board[5]+"   |  "+board[6]+"   ")
    print("      |      |      ")
    print("------|------|------")
    print("      |      |      ")
    print("   "+board[7]+"  |  "+board[8]+"   |  "+board[9]+"   ")
    print("      |      |      ")

while True:

    print_board()
    # Taking player X input
    choice = int(input("Please choose an empty space for X : "))

    # Check if the space is empty
    if (board[choice] == " "):
        board[choice] = "X"
    else:
        print("Space is not empty")
        time.sleep(1)

        # Check if X wins
    if (board[1] == 'X' and board[2] == 'X' and board[3] == 'X') or \
        (board[4] == 'X' and board[5] == 'X' and board[6] == 'X') or \
        (board[7] == 'X' and board[8] == 'X' and board[9] == 'X') or \
        (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or \
        (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or \
        (board[3] == 'X' and board[6] == 'X' and board[9] == 'X') or \
        (board[1] == 'X' and board[5] == 'X' and board[9] == 'X') or \
        (board[3] == 'X' and board[5] == 'X' and board[7] == 'X'):

        print_board()
        print("Congratulations! \nX WINS!")
        break

    # Check for Tie
    isFull = True
    if " " in board:
        isFull = False
    # If the board is full
    if isFull == True:
        print_board()
        print("TIE!")
        break

    print_board()
    # Taking player O input
    choice = int(input("Please choose an empty space for O : "))

    # Check if the space is empty
    if (board[choice] == " "):
        board[choice] = "O"
    else:
        print("Space is not empty")
        time.sleep(1)

    # Check if O wins
    if (board[1] == 'O' and board[2] == 'O' and board[3] == 'O') or \
        (board[4] == 'O' and board[5] == 'O' and board[6] == 'O') or \
        (board[7] == 'O' and board[8] == 'O' and board[9] == 'O') or \
        (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or \
        (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or \
        (board[3] == 'O' and board[6] == 'O' and board[9] == 'O') or \
        (board[1] == 'O' and board[5] == 'O' and board[9] == 'O') or \
        (board[3] == 'O' and board[5] == 'O' and board[7] == 'O'):

        print_board()
        print("Congratulations! \nO WINS!")
        break

    # Check for Tie
    isFull = True
    if " " in board:
        isFull = False
    # If the board is full
    if isFull == True:
        print_board()
        print("TIE!")
        break