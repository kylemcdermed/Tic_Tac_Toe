from IPython.display import clear_output
import random

def choose_first():
    number = random.randint(0,1)
    return number

def space_check(board, position):
    if board[position-1] not in ['X','O']:
        return True
    else:
        return False

def full_board_check(board):
    for i in range(len(board)):
        if board[i] not in ['X','O']:
            return False
    return True

def replay():
    play_again = input("Do you want to play again: ")
    while play_again not in ['Y', 'y', 'N', 'n']:
        play_again = input("Do you want to play again: ")
    if play_again in ['Y', 'y']:
        return True
    return False

def display_board(board):
    for i in range(len(board)):
        print(" "+board[i]+" ", end="|" if i % 3 != 2 else '')
        if i % 3 == 2 and i != len(board)-1:
            print("\n---+---+---")               
    print()

def player_input():
    player1_marker = ''
    while player1_marker not in ['X', 'O']:
        player1_marker = input("Please pick a marker 'X' or 'O': ")
    if player1_marker == 'X':
        player2_marker = 'O'
    else:
        player2_marker = 'X'
    return player1_marker, player2_marker

def place_marker(board, marker, position):
    board[position - 1] = marker

def win_check(board, mark):
    if board[0] == mark and board[1] == mark and board[2] == mark: return True
    if board[3] == mark and board[4] == mark and board[5] == mark: return True
    if board[6] == mark and board[7] == mark and board[8] == mark: return True

    if board[0] == mark and board[3] == mark and board[6] == mark: return True
    if board[1] == mark and board[4] == mark and board[7] == mark: return True
    if board[2] == mark and board[5] == mark and board[8] == mark: return True

    if board[0] == mark and board[4] == mark and board[8] == mark: return True
    if board[2] == mark and board[4] == mark and board[6] == mark: return True

    return False

def player_choice(board):
    next_position = 0
    while next_position not in range(1,10):
        next_position = int(input("What is your next position: "))
    free_space = space_check(board, next_position)
    if not free_space:
        print("Position unavailable.")
        return player_choice(board)
    return next_position


clear_output()
print('\n')
print('Welcome to Tic Tac Toe!')

while True:
    board = [' '] * 9
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print("Player 1 will go first." if turn == 0 else "Player 2 will go first.")

    play_game = input("Are you ready to play? (Y/N): ").lower()
    game_on = play_game == 'y'

    while game_on:
        if turn == 0:
            # Player 1's turn
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)
            
            if win_check(board, player1_marker):
                display_board(board)
                print("Player 1 wins!")
                game_on = False
            elif full_board_check(board):
                display_board(board)
                print("The game is a draw!")
                game_on = False
            else:
                turn = 1  # Switch to Player 2
        else:
            # Player 2's turn
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)
            
            if win_check(board, player2_marker):
                display_board(board)
                print("Player 2 wins!")
                game_on = False
            elif full_board_check(board):
                display_board(board)
                print("The game is a draw!")
                game_on = False
            else:
                turn = 0  # Switch to Player 1

    if not replay():
        break
