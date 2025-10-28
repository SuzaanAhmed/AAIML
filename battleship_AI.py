import random
import time
class BTS:
    def __init__(self,size=10):
        self.size=size

        self.ships={
            "Biggest Ship":5,
            "Sub-Big Ship":4,
            "Mid Ship":3,
            "Sub mid ship":2,
            "Tiny Ship":1
        }

        # self.MainShip=5
        # self.SubShip=3
        # self.TinyShip=1

        # self.MainShipTest=False
        # self.SubShipTest=False
        # self.TinyShipTest=False
        self.total_ship_cells = sum(self.ships.values())

        """Below is what either side sees their board as"""
        self.player_board = self.create_board()
        self.ai_board = self.create_board()

        """Below is what either side sees the others board as"""
        self.player_guess_board = self.create_board()
        self.ai_guess_board = self.create_board()

    def create_board(self):
        return [[' ' for _ in range(self.size)] for _ in range(self.size)]


    def print_boards(self):
        """Decided to print out both boards"""
        print("\n" + "="*53)
        print("     PLAYER'S GUESSES (AI Board)         YOUR BOARD (AI's Guesses)")
        header = "   " + " ".join([f"{i}" for i in range(self.size)])
        print(header + "        " + header)
        print("  " + "-"*(self.size*2+1) + "        " + "  " + "-"*(self.size*2+1))
        
        for i in range(self.size):
            row_guess = " | ".join(self.player_guess_board[i])
            row_own = " | ".join(self.player_board[i])
            print(f"{i:1} | {row_guess} |      {i:1} | {row_own} |")
        
        print("  " + "-"*(self.size*2+1) + "        " + "  " + "-"*(self.size*2+1))
        print("Legend: 'S' = Your Ship, 'H' = Hit, 'M' = Miss, 'X' = Sunk Ship Part")

    def is_valid_placement(self, board, ship_size, x, y, orientation):
        """Checks if a ship can be placed at the given location."""
        if orientation == 'h':
            if y + ship_size > self.size:
                return False
            for i in range(ship_size):
                if board[x][y+i] != ' ':
                    return False
        else: # 'v'
            if x + ship_size > self.size:
                return False
            for i in range(ship_size):
                if board[x+i][y] != ' ':
                    return False
        return True

    def place_ship_on_board(self, board, ship_size, x, y, orientation, ship_char='S'):
        """Actually places ship as wanted by the person or a clanker"""
        if orientation == 'h':
            for i in range(ship_size):
                board[x][y+i] = ship_char
        else: # 'v'
            for i in range(ship_size):
                board[x+i][y] = ship_char

    def choose_Pos(self):
        """Allows the player to interactively place their ships."""
        print("\n--- Place Your Ships ---")
        for ship_name, ship_length in self.ships.items():
            while True:
                self.print_boards()
                print(f"Placing {ship_name} (length {ship_length})")
                
                try:
                    pos = input(f"Enter start coordinate (row,col) (e.g., 3,4): ")
                    x, y = map(int, pos.split(','))
                    
                    orientation = input("Enter orientation (h for horizontal, v for vertical): ").lower()
                    if orientation not in ['h', 'v']:
                        raise ValueError("Invalid orientation.")
                    
                    if self.is_valid_placement(self.player_board, ship_length, x, y, orientation):
                        self.place_ship_on_board(self.player_board, ship_length, x, y, orientation)
                        break
                    else:
                        print("Invalid placement. Ship is out of bounds or overlaps another ship. Try again.")
                
                except ValueError as e:
                    print(f"Invalid input ({e}). Please use the format 'row,col' and 'h' or 'v'.")
                except IndexError:
                     print("Invalid coordinates. Please enter numbers between 0 and 9.")
 
    def place_ships_ai(self):
        """Clanker places ships"""
        print("\nClanker placing ships")
        time.sleep(5)
        for _, ship_length in self.ships.items():
            while True:
                orientation = random.choice(['h', 'v'])
                x = random.randint(0, self.size - 1)
                y = random.randint(0, self.size - 1)
                
                if self.is_valid_placement(self.ai_board, ship_length, x, y, orientation):
                    self.place_ship_on_board(self.ai_board, ship_length, x, y, orientation)
                    break # Move to the next ship

    def get_player_guess(self):
            """Validity of guess"""
            while True:
                try:
                    pos = input("Enter your guess (row,col): ")
                    x, y = map(int, pos.split(','))
                    
                    if not (0 <= x < self.size and 0 <= y < self.size):
                        print("Coordinates out of bounds. Try again.")
                    elif self.player_guess_board[x][y] != ' ':
                        print("You've already guessed that spot. Try again.")
                    else:
                        return x, y
                except ValueError:
                    print("Invalid input. Please use the format 'row,col'.")

    def process_player_guess(self, x, y):
        """Checks whether its correct guess i.e. 'Hit' or 'Miss'"""
        target = self.ai_board[x][y]
        
        if target == 'S':
            print(">>> HIT!")
            self.player_guess_board[x][y] = 'H'
            self.ai_board[x][y] = 'H' # Mark on AI's board as hit
        else:
            print(">>> MISS!")
            self.player_guess_board[x][y] = 'M'

    def check_game_over(self):
        """whether either of their ships have been destroyed"""
        player_hits = sum(row.count('H') for row in self.player_guess_board)
        if player_hits == self.total_ship_cells:
            print("\n" + "="*30)
            print("Hooray! YOU WIN! All AI ships sunk!")
            print("="*30)
            return True
            
        ai_hits = sum(row.count('H') for row in self.player_board)
        if ai_hits == self.total_ship_cells:
            print("\n" + "="*30)
            print("Oh no! The AI sunk all your ships! AI WINS!")
            print("="*30)
            return True
            
        return False

    def play_game(self):
        print("Battleship gameplay")
        self.choose_Pos()
        self.place_ships_ai()

        while True:
            self.print_boards()
            
            # --- Player's Turn ---
            print("\n--- Your Turn ---")
            px, py = self.get_player_guess()
            self.process_player_guess(px, py)
            if self.check_game_over():
                break
        

if __name__=="__main__":
    bts=BTS()
    bts.play_game()