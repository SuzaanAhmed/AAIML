class BTS:
    def __init__(self,size=10):
        self.player_board=[[' ' for _ in range(size)] for _ in range(size)]
        self.AI_board=self.player_board

        self.size=size

        self.ships={
            "Main Ship":5,
            "Sub Ship":3,
            "Tiny Ship":1
        }

        # self.MainShip=5
        # self.SubShip=3
        # self.TinyShip=1

        # self.MainShipTest=False
        # self.SubShipTest=False
        # self.TinyShipTest=False


    def print_playerBoard(self):
        print('\n-----------------------------------------')
        for row in self.player_board:
            print('|', end='')
            for cell in row:
                print(f" {cell} ", end='|')
            print('\n-----------------------------------------')
        print()


    def choose_Pos(self):
        while True:
            for ship,shipCount in self.ships.items():
                # for i in range(shipCount):
                self.print_playerBoard()
                x,y=map(int,input(f"Enter positon for {ship}, {shipCount} boxes long: ").split())
                for i in range(shipCount):
                    if 0<=x<self.size and 0<=y<self.size and self.player_board[x][y]==' ':
                        self.player_board[x][y]='*'
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