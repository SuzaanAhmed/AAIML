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
        else: # 'v'
            if x + ship_size > self.size:
                return False
        for i in range(ship_size):
                if board[x][y+i] != ' ':
                    return False
        return True
        


    def choose_Pos(self):
        while True:
            for ship,shipCount in self.ships.items():
                # for i in range(shipCount):
                self.print_playerBoard()
                x,y=map(int,input(f"Enter positon for {ship}, {shipCount} boxes long: ").split())
                for i in range(shipCount):
                    if 0<=x<self.size and 0<=y<self.size and self.player_board[x][y]==' ':
                        self.player_board[x][i]='*'
                # else:
                #     print("Invalid move. Try again.")
                #     i-=1
                #     continue                    

            reset=(input("Do you want to reset the board?(y/n): "))
            if reset=="n":
                break

            self.player_board=[[' ' for _ in range(self.size)] for _ in range(self.size)]

if __name__=="__main__":
    bts=BTS()
    bts.choose_Pos()