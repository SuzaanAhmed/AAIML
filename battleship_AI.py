class BTS:
    def __init__(self,size=10):
        self.player_board=[[' ' for _ in range(size)] for _ in range(size)]
        self.AI_board=self.player_board

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

if __name__=="__main__":
    bts=BTS()
    bts.choose_Pos()