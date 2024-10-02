# TIC TAC TOE GAME

def print_board(board):
    """Print the Tic-Tac-Toe board."""
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))

def check_win(board, player):
    """Check if the current player has won."""
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def check_tie(board):
    """Check if the game is a tie."""
    return all(space in ['X', 'O'] for space in board)

def get_move():
    """Get the player's move."""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                raise ValueError
            return move
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def tic_tac_toe():
    """Play the Tic-Tac-Toe game."""
    board = [' ' for _ in range(9)]
    players = ['X', 'O']
    turn = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player = players[turn % 2]
        print(f"Player {player}'s turn")
        
        move = get_move()
        if board[move] != ' ':
            print("The space is already taken. Try again.")
            continue

        board[move] = player
        print_board(board)

        if check_win(board, player):
            print(f"Player {player} wins!")
            break
        if check_tie(board):
            print("The game is a tie!")
            break

        turn += 1

# Start the game
tic_tac_toe()
