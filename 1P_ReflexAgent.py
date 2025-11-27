import os
import time
import random

class PAC:
    def __init__(self, size=12):
        self.size = size
        self.cols = size
        self.rows = size

        self.game = [
            ['%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%'],
            ['%', 'O', '*', '*', '%', '*', '*', '*', '%', '*', '*', '*'],
            ['%', '*', '%', '*', '%', '*', '%', '*', '%', '*', '%', '%'],
            ['%', '*', '%', '*', '*', '*', '%', '*', '*', '*', '*', '%'],
            ['%', '*', '%', '%', '*', '%', '%', '*', '%', '%', '*', '%'],
            ['%', '*', '*', '*', '*', '%', '*', '*', '%', '*', '*', '%'],
            ['%', '*', '%', '%', '*', '%', '*', '*', '%', '*', '%', '%'],
            ['%', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['%', '*', '%', '*', '%', '%', '*', '%', '%', '%', '*', '%'],
            ['%', '*', '%', '*', '*', '*', '*', '*', '*', '*', '*', '%'],
            ['%', '*', '%', '%', '*', '*', '*', '*', '*', '%', '*', '%'],
            ['%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%']
        ]

        self.pac_x = 1
        self.pac_y = 1
        self.game[self.pac_x][self.pac_y] = 'O'
        self.pac_traversal=""
        '''
        pac-x & pac_y, global variables to store the current position of pacman
        gam[][] 2D array to store the game state
        pac_traversal stores the last direction of pacman         
        '''

        self.directions = {
            "right": (0, 1),
            "left": (0, -1),
            "up": (-1, 0),
            "down": (1, 0)
        }
        '''Dictionary to store the possible directions and their respective coordinate changes'''
        
        '''
        self.turn={
            "r":"right",
            "l":"left",
            "u":"up",
            "d":"down"
        }'''
        ''''Dictionary to store the manual turn signal prompts'''

    def display_game(self):
        os.system('cls')
        print("=======================================================")
        # clears terminal
        for i in range(self.cols):
            print("|", end="")
            for j in range(self.rows):
                print(f" {self.game[i][j]} ", end='')
            print("|")
        print("=======================================================")
    '''
    def manual_direction(self):
        inp=input("Enter initial of direction(r: right, l: left, etc)")
        for direction,turn in self.turn.items():
            if direction==inp:
                return turn
    '''
    def get_next_pac_direction(self):
        possible_moves = {}
        for direction, (dx, dy) in self.directions.items():
            #checks immediate next move's validity
            next_x, next_y = self.pac_x + dx, self.pac_y + dy
            if not (0 <= next_x < self.rows and 0 <= next_y < self.cols and self.game[next_x][next_y] != '%'):
                # if self.pac_traversal==direction: self.pac_traversal==""
                continue 
            
            pellet_count = 0
            if direction == "right":
                for y in range(self.pac_y + 1, self.cols):
                    if self.game[self.pac_x][y] == '%':
                        break
                    if self.game[self.pac_x][y] == '*':
                        pellet_count += 1
                        
            elif direction == "left":
                for y in range(self.pac_y - 1, -1, -1):
                    if self.game[self.pac_x][y] == '%':
                        break
                    if self.game[self.pac_x][y] == '*':
                        pellet_count += 1
                        
            elif direction == "up":
                for x in range(self.pac_x - 1, -1, -1):
                    if self.game[x][self.pac_y] == '%':
                        break
                    if self.game[x][self.pac_y] == '*':
                        pellet_count += 1
                        
            elif direction == "down":
                for x in range(self.pac_x + 1, self.rows):
                    if self.game[x][self.pac_y] == '%':
                        break
                    if self.game[x][self.pac_y] == '*':
                        pellet_count += 1
                        
            #counts most pellets in each direction to find optimal turn from the 4 set of pellets
            possible_moves[direction] = pellet_count
        
        max_moves = max(possible_moves.values())
        best_directions = [
            direction for direction, count in possible_moves.items()
            if count == max_moves
        ]
        
        if self.pac_traversal in best_directions:
            return self.pac_traversal
        
        self.pac_traversal = random.choice(best_directions)
        return self.pac_traversal
    
    def move_pacman(self):
    
        next_direction = self.get_next_pac_direction()
        
        if next_direction is None:
            return # Pac-Man is trapped, so he stops moving
        
        self.game[self.pac_x][self.pac_y] = ' '

        for direction, (x,y) in self.directions.items():
            if direction==next_direction:
                self.pac_x+=x
                self.pac_y+=y

        # if next_direction == "right":
        #     self.pac_y += 1
        # elif next_direction == "left":
        #     self.pac_y -= 1
        # elif next_direction == "up":
        #     self.pac_x -= 1
        # elif next_direction == "down":
        #     self.pac_x += 1

        self.game[self.pac_x][self.pac_y] = 'O'

    def run_game(self):
        self.display_game()
        time.sleep(1)
        
        while True:
            self.move_pacman()
            self.display_game()
            time.sleep(.3)
            if not any('*' in row for row in self.game):
                print("YOU WIN! All pellets have been eaten.")
                break

if __name__ == "__main__":
    pac = PAC()
    pac.run_game()
