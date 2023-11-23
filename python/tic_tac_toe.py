import os
import random
import platform

def clear():
    """
    clear() clears the output screen of any previous outputs and results
    
    :param : No parameters are passed in
    :return: nothing being returned
    """
    # Check mac/os systems for the appropriate clear command
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    
    
def user_assign():
    """
    user_assign assigns user names. Also, randomly assign their order in the game. First (X) or Second (O)
    
    :param : No parameters are passed in
    :return: returns a list with two player names and their positions
    """
    p1 = input("Enter Player 1 Name: ")
    p2 = input("Enter Player 2 Name: ")
    p = [p1, p2]
    random.shuffle(p)
    clear()
    return p


def display_user_info():
    """
    Displays assigned players and their positions. Along with the assigned mark
    
    :param : No parameters are passed in
    :return: nothing is being returned
    """
    print(f"Player 1: {player1} (X)\nPlayer 2: {player2} (O)\n")
    

def display_position_system():
    """
    Displays index positions in the game board. These index values are used to input their game plays
    
    :param : No parameters are passed in
    :return: nothing is being returned
    """
    print(f"See the positional indexes for the Tic-Tac-Toe Board:")
    print(" 1 | 2 | 3 ")
    print("~~~~~~~~~~~")
    print(" 4 | 5 | 6 ")
    print("~~~~~~~~~~~")
    print(" 7 | 8 | 9 ")
    print(f"\n")
    

def display_board(lst):
    """
    Displays current game board status. Filled ones will have X or Os. Empty one will have #
    
    :param : list that contains the game board as is
    :return: nothing is being returned
    """
    print(f"Current Board (# Represents empty slots): ")
    print(f" {lst[0]} | {lst[1]} | {lst[2]} ")
    print("~~~~~~~~~~~")
    print(f" {lst[3]} | {lst[4]} | {lst[5]} ")
    print("~~~~~~~~~~~")
    print(f" {lst[6]} | {lst[7]} | {lst[8]} ")
    print("\n")
    

def check_proceed():
    """
    Checks if the players would like another round of the game
    
    :param : no parameters
    :return: nothing is being returned
    """
    acceptable_vals = ['y', 'n']
    inp ='i'
    
    # Get user input and validate
    while not inp.lower() in acceptable_vals:
        inp = input("Would you like to keep playing? (Y/N): ")
        
        if not inp.lower() in acceptable_vals:
            clear()
            display_user_info()
            display_position_system()
            display_board(ttt_board)
            print("Incorrect Input. Please select Y or N")
        
    # Return True/False based on accepted user input
    if inp.lower() == acceptable_vals[0]:
        return True
    else:
        return False
        

def user_play(board_slot_list):
    """
    Manages the game play each time a game starts. Continues untill all the positions on the board are filled.
    Breaks if any player wins the game
    
    :param : list that contains the initial game board
    :return: nothing is being returned
    """
    counter = 1
    check = False
    
    # Game Play loop till. 10 Tries / One of the player wins
    while counter < 10 and not check:
        
        # Get input and validate the move entry
        if counter%2 == 0:
            user_input_val = user_play_validate(board_slot_list, player2, 'O')
        else:
            user_input_val = user_play_validate(board_slot_list, player1, 'X')
            
        # Insert the validated move into the board and checks if any player has won
        if counter%2 == 0:
            board_slot_list[int(user_input_val)-1] = 'O'
            check = check_win(board_slot_list, 'O')
        else:
            board_slot_list[int(user_input_val)-1] = 'X'
            check = check_win(board_slot_list, 'X')
        
        counter += 1
    
        clear()
        display_user_info()
        display_position_system()
        display_board(board_slot_list)
        
    # Print who won the game/ if match was tied
    if check and (counter-1)%2 == 0:
        clear()
        display_user_info()
        display_board(board_slot_list)
        print(f"Congratulations {player2}! You win!!")
    elif check and (counter-1)%2 != 0:
        clear()
        display_user_info()
        display_board(board_slot_list)
        print(f"Congratulations {player1}! You win!!")  
    else:
        clear()
        display_user_info()
        display_board(board_slot_list)
        print(f"Tie game!! Good try {player1} & {player2}!")


def user_play_validate(board_updated_list, player, mark):
    """
    Validated player inputs to make a move on the game board. 
    Checks if the inputs are within 0-9. Also, checks if an existing play is being tried to be overwritten
    
    :param : list that contains the game board with all the moves that players have played
    :return: a valid play input - integer
    """
    acceptable_range = range(0, 10)
    play = 'h'
    
    # check input is within the acceptable range
    while not play in list(map(str, acceptable_range)):
        play = input(f"Enter the index position for your play {player} ({mark}): ")
        
        # check if input is to an existing filled slot
        if play.isdigit() and play in list(map(str, acceptable_range)):
            while board_updated_list[int(play)-1] != '#':
                play = input("Your selection is already filled. Enter a different position: ")
            
        if not play in list(map(str, acceptable_range)):
            clear()
            display_user_info()
            display_position_system()
            display_board(board_updated_list)
            print("Invalid input. Input values 0-9")
    
    return int(play)
        
        
def check_win(board, mark):
    """
    Check if a player has won after each player move
    
    :param : list that contains the game board with all the moves that players have played, mark of the player
    :return: win/no win - boolean
    """
    return (
    (board[0] == mark and board[1] == mark and board[2] == mark) or # across the top
    (board[3] == mark and board[4] == mark and board[5] == mark) or # across the middle
    (board[6] == mark and board[7] == mark and board[8] == mark) or # across the bottom
    (board[0] == mark and board[3] == mark and board[6] == mark) or # down the middle
    (board[1] == mark and board[4] == mark and board[7] == mark) or # down the middle
    (board[2] == mark and board[5] == mark and board[8] == mark) or # down the right side
    (board[0] == mark and board[4] == mark and board[8] == mark) or # diagonal
    (board[2] == mark and board[4] == mark and board[6] == mark)) # diagonal
    
        
            


# Players Assignment
players = user_assign()
player1 = players[0]
player2 = players[1]

# Initialize variable to start the game
proceed = True


# Actual Game Play Initiation
while proceed:
    
    # Initialize/Reset Board
    ttt_board = ['#', '#', '#', '#', '#', '#', '#', '#', '#']
    
    #Display Players
    display_user_info()
    
    # Display Positions & Board
    display_position_system()
    display_board(ttt_board)
    
    # User Plays
    user_play(ttt_board)
    
    # Check if players would like to play again
    proceed = check_proceed()
    
    # Clear Screen
    clear()