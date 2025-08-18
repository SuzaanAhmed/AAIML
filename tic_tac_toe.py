import random

def check_winner(board, player):
    # Check for row wins
    for row in board: #iterates through each row
        if all(cell == player for cell in row): #checks all cells in each row it iterates
            return True
    # Check for column wins
    for col in range(3): 
        if all(board[row][col] == player for row in range(3)): #checks for collumns
            return True
    # Check for diagonal wins
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' 
               for row in board 
               for cell in row)

def get_available_moves(board):
    return [(i, j) 
            for i in range(3) 
            for j in range(3) 
            if board[i][j] == ' ']

def player_move(board):
    while True:
        try:
            #the input of (x,y) is string, it converts them to integer
            row, col = map(int, input("Enter your move (row and column, e.g., 1 2): ").split())
            if 1 <= row <= 3 and 1 <= col <= 3 and board[row - 1][col - 1] == ' ':
                return row - 1, col - 1
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")

def computer_move(board, player, computer):
    available_moves = get_available_moves(board)
    # Try to win
    for move in available_moves:
        board[move[0]][move[1]] = computer
        if check_winner(board, computer):
            return move
        board[move[0]][move[1]] = ' '  # Undo move
    # Block player from winning
    for move in available_moves:
        board[move[0]][move[1]] = player
        if check_winner(board, player):
            # board[move[0]][move[1]] = computer //do not actually need this AFAIK beacuse we just return the moves
            return move
        board[move[0]][move[1]] = ' '  # Undo move
    # Otherwise, make a random move
    return random.choice(available_moves)

def play_game():
    # Creating a 2D array board with string value ' ' in it.
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    computer = 'O'
    while True:
        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        elif check_winner(board, 'O'):
            print("Computer wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        if player == 'X':
            row, col = player_move(board)
            board[row][col] = 'X'
            player = 'O'
            # computer = 'X'do not need this or the below one, both are pointless
        else:

            row, col = computer_move(board,'X','O')
             #row, col = computer_move(board, computer, player) was this initially, nut that just unnecessarily complicated it so fuck that
            board[row][col] = 'O'
            player = 'X'
            # computer = 'O'

if __name__ == "__main__":
    play_game()
