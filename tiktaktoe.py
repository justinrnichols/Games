import random
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(' ___ ___ ___')
    print('| ' + board[9] + ' | ' + board[8] + ' | ' + board[7] + ' |')
    print(' ___ ___ ___')
    print('| ' + board[6] + ' | ' + board[5] + ' | ' + board[4] + ' |')
    print(' ___ ___ ___')
    print('| ' + board[3] + ' | ' + board[2] + ' | ' + board[1] + ' |')
    print(' ___ ___ ___')

def player_input():
    answer = False
    while not answer:
        player1 = input("Please pick a marker 'X' or 'O': ").upper()
        if player1 == 'X' or player1 == 'O':
            answer = True
            if player1 == 'X':
                player2 = "O"
            else:
                player2 = "X"
        else:
            print("Wrong input.")
    return (player1,player2)

def choose_first():
    if random.randint(0, 1) == 0:
        return "Player 1"
    else:
        return "Player 2"

def place_marker(board, marker, position):
    board[position] = marker

def player_choice(board, player):
    while True:
        try:
            position = int(input(f"{player}, please pick a number 1-9: "))
            if position not in range(1,10):
                print("Number is not in range.")
            elif not space_check(board, position):
                print("Position is already taken.")
            else:
                return position
        except ValueError:
            print("Wrong input.")

def space_check(board, position):
    if board[position] != 'X' and board[position] != 'O':
        return True
    return False

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def win_check(board, mark):
    return (
    (board[9] == mark and board[8] == mark and board[7] == mark) or
    (board[6] == mark and board[5] == mark and board[4] == mark) or
    (board[3] == mark and board[2] == mark and board[1] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark)
    )

def replay():
    while True:
        answer = input("Do you want to play again (Y/N)? ")
        if answer.lower().startswith('y'):
            return True
        elif answer.lower().startswith('n'):
            return False
        else:
            print("Wrong input.")


def ready():
    while True:
        answer = input("Are both players ready (Y/N)? ")
        if answer.lower().startswith('y'):
            return True
        elif answer.lower().startswith('n'):
            return False
        else:
            print("Wrong input.")

def game():
    print("Welcome to Tic Tac Toe!")
    while True:
        players = ["Player 1", "Player 2"]
        board = ['#','1','2','3','4','5','6','7','8','9']
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + " will go first.")
        while True:
            if ready():
                game_on = True
                break
            else:
                game_on = False
                if not replay():
                    return
        while game_on:
            if turn == players[0]:
                display_board(board)
                position = player_choice(board, players[0])
                place_marker(board, player1_marker, position)
                if win_check(board, player1_marker):
                    display_board(board)
                    print("Congratulations! You have won the game!")
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print("The game is a draw!")
                        break
                    else:
                        turn = players[1]
            else:
                display_board(board)
                position = player_choice(board, players[1])
                place_marker(board, player2_marker, position)
                if win_check(board, player2_marker):
                    display_board(board)
                    print("Player 2 has won!")
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print("The game is a draw!")
                        break
                    else:
                        turn = players[0]
        if not replay():
            print("Thanks for playing!")
            break

game()