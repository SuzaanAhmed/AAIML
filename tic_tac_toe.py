import random
import time

class TicTacToe:
    def __init__(self):
        """
        Initializes the game state.
        All game variables are managed here.
        """
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.human_player = 'X'
        self.computer_player = 'O'
        self.current_player ='' #initializes as per user choice in initialise()

    def print_board(self):
        #basic looping for board printing
        print('-------------')
        for row in self.board:
            print('|', end='')
            for cell in row:
                print(f" {cell} ", end='|')
            print('\n-------------')
        print()

    def get_available_moves(self):
        """Returns a list of empty cells (row, col).
            ex: [(1,2),(2,2),(3,3)]"""
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']

    def is_board_full(self):
        return len(self.get_available_moves()) == 0

    def check_winner(self, player):
        """Checks if the specified player has won the game.
            horizontal, vertical, and diagonal checks"""
        for r in range(3):
            if all(self.board[r][c] == player for c in range(3)):
                return True
        
        for c in range(3):
            if all(self.board[r][c] == player for r in range(3)):
                return True
            
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True
        
        return False

    def switch_player(self):
        #Switches current player state
        self.current_player = self.computer_player if self.current_player == self.human_player else self.human_player

    def player_move(self):
        #Fetches player move
        while True:
            try:
                row, col = map(int, input("Enter your move (row col), e.g., 1 2: ").split())
                if 1 <= row <= 3 and 1 <= col <= 3 and self.board[row - 1][col - 1] == ' ':
                    return row - 1, col - 1
                else:
                    print("Invalid move. That spot is taken or out of bounds. Try again.")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")

    def computer_move(self):
        """ 1. Check for victory.
            2. Check for inhibition of human's victory.
            3. Random."""
        time.sleep(1)
        available_moves = self.get_available_moves()

        for row, col in available_moves:
            self.board[row][col] = self.computer_player
            if self.check_winner(self.computer_player):
                self.board[row][col] = ' '  
                return row, col
            self.board[row][col] = ' '  

        for row, col in available_moves:
            self.board[row][col] = self.human_player
            if self.check_winner(self.human_player):
                self.board[row][col] = ' ' 
                return row, col
            self.board[row][col] = ' ' 

        return random.choice(available_moves)
    
    def initialise(self):
        #Initializes all game variables
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        start_prompt=input("Do you want to start first? (y/n): ").lower()
        if start_prompt == 'n':
            self.current_player = self.computer_player
        else:
            self.current_player = self.human_player
        self.print_board()

    def play_game(self):
        #Game starts
        self.initialise()
        print("Welcome to Tic-Tac-Toe!")
        
        while True:#Game stays within this loop till game over
            self.print_board()
            
            #Swtiches turns based on "current_player"
            if self.current_player == self.human_player:
                row, col = self.player_move()
            else:
                print("Computer is thinking...")
                row, col = self.computer_move()
                print(f"Computer chose: ({row + 1}, {col + 1})")

            #move update
            self.board[row][col] = self.current_player

            #WinCheck
            if self.check_winner(self.current_player):
                self.print_board()
                winner = "You" if self.current_player == self.human_player else "The Computer"
                print(f"Congratulations! {winner} win(s)!")
                break
            
            #TieCheck
            if self.is_board_full():
                self.print_board()
                print("It's a tie!")
                break

            #Switch call
            self.switch_player()

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()

