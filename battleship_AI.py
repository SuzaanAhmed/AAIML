class BTS:
    def __init__(self,size=14):
        self.player_board=[[' ' for _ in range(size)] for _ in range(size)]
        self.AI_board=self.player_board

        self.size=size

        self.MainShip=5
        self.SubShip=3
        self.TinyShip=1

        self.MainShipTest=False
        self.SubShipTest=False
        self.TinyShipTest=False

    def choose_Pos(self):
        while True:
            if self.MainShipTest and self.SubShipTest and self.TinyShipTest:
                choice=print("Are you satisfied? Do you want to leave?")
                if choice=='y':
                    break
                
            shipName=input("Enter ship to place: MS:5,SS:3,TS:1 or R for reset: ") 
            
            if shipName=='MS':
                cache=[]
                for i in range(self.MainShip):
                    x,y=input(int("Enter positon of ships, 5 boxes long: ")).split()
                    cache.append(x,y)
                    if 0<=x<self.size and 0<=y<self.size and self.player_board[x][y]==' ':
                        self.player_board[x][y]='*'
                    else:
                        print("Invalid move. Try again.")
                        i-=1
                        continue
            
            elif shipName=='SS':
                cache=[]
                for i in range(self.SubShip):
                    x,y=input(int("Enter positon of ships, 3 boxes long: ")).split()
                    cache.append(x,y)
                    if 0<=x<self.size and 0<=y<self.size and self.player_board[x][y]==' ':
                        self.player_board[x][y]='*'
                    else:
                        print("Invalid move. Try again.")
                        i-=1
                        continue
            
            elif shipName=='TS':
                cache=[]
                for i in range(self.TinyShip):
                    x,y=input(int("Enter positon of ships, 1 box long: ")).split()
                    cache.append(x,y)
                    if 0<=x<self.size and 0<=y<self.size and self.player_board[x][y]==' ':
                        self.player_board[x][y]='*'
                    else:
                        print("Invalid move. Try again.")
                        i-=1
                        continue
            
            elif shipName=='reset':
                self.player_board=[[' ' for _ in range(self.size)] for _ in range(self.size)]


    def print_playerBoard(self):
        print('-------------')
        for row in self.player_board:
            print('|', end='')
            for cell in row:
                print(f" {cell} ", end='|')
            print('\n-------------')
        print()
            
    