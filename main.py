# Name : Angel Remigio
# SSID : 1848012
# Assignment #: 3
# Submission Date : 10/26/2020
#
# Description of program :
# Single Player Tic Tac Toe against a computer


from random import randint

# void function to print the board state
the_board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


def print_board(board):
    # prints the current board
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(board[row][col], end="")
        print()


print("the board as rows and columns ")


def check_rows(board):
    for row in range(len(board)):
        if board[row][0] == board[row][1] == board[row][2] != "-":
            return True
    return False


def check_cols(board):
    for cols in range(len(board)):
        if board[0][cols] == board[1][cols] == board[2][cols] != "-":
            return True
    return False


def check_diag1(board):
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return True
    return False


def check_diag2(board):
    if board[0][2] == board[1][1] == board[2][0] != "-":
        return True
    return False


def move(board):
    while True:
        ai_x = randint(0, 2)
        ai_y = randint(0, 2)
        if board[ai_x][ai_y] == "-":
            board[ai_x][ai_y] = "0"
            break


# Function to check if there is a winning state on the board
def check_ifwin(board):
    if check_rows(board):
        return True
    if check_cols(board):
        return True
    if check_diag1(board):
        return True
    if check_diag2(board):
        return True
    return False


while True:
    print_board(the_board)
    move(the_board)
    print("use coordinates such as 00,01,02 and etc in order to move")
    user_move = input()
    x = int(user_move[0])
    y = int(user_move[1])
    the_board[x][y] = "X"
    if check_ifwin(the_board):
        print_board(the_board)
        print("We have a winner")
        print("Do you wanna try again? Type yes or no")
        response = input()
        if response == "yes" or response == "Yes" or response == "Y":
            the_board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
        else:
            break
