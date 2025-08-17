import os
import time
import random

class PAC:

    def __init__(self, size=13):    
        self.size = size
        self.cols = size
        self.rows = size
        # self.game=[['*' for _ in range(size)]for _ in range(size)] Gird movement testing
        self.game = [
            ['%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%'],
            ['%', 'O', '*', '*', '%', '*', '*', '*', '%', '*', '*', '*', '*'],
            ['%', '%', '%', '*', '%', '*', '%', '*', '%', '*', '%', '%', '*'],
            ['%', '*', '%', '*', '*', '*', '%', '*', '*', '*', '*', '%', '*'],
            ['%', '*', '%', '%', '%', '%', '%', '*', '%', '%', '*', '%', '*'],
            ['%', '*', '*', '*', '*', '%', '*', '*', '%', '*', '*', '%', '*'],
            ['%', '%', '%', '%', '*', '%', '%', '%', '%', '*', '%', '%', '*'],
            ['%', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['%', '*', '%', '*', '%', '%', '%', '%', '%', '%', '%', '%', '*'],
            ['%', '*', '%', '*', '*', '*', '*', '*', '*', '*', '*', '%', '*'],
            ['%', '*', '%', '%', '%', '%', '%', '%', '%', '%', '*', '%', '*'],
            ['%', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '%', '*'],
            ['%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%']
        ]

        self.pac_x = 1
        self.pac_y = 1
        self.directions = {
            "right": (0, 1),
            "left": (0, -1),
            "up": (-1, 0),
            "down": (1, 0)
        }
        self.traversal = "right"
        
        self.game[self.pac_x][self.pac_y] = 'O'

        self.cache="none"

    def get_next_PAC_direction(self):
        possible_moves = {}
        '''
        directions = {
            "right": (0, 1),
            "left": (0, -1),
            "up": (-1, 0),
            "down": (1, 0)
        }
        '''
        for direction, (dx, dy) in self.directions.items():
            next_x, next_y = self.pac_x + dx, self.pac_y + dy
            if not (0 <= next_x < self.rows and 0 <= next_y < self.cols and self.game[next_x][next_y] != '%'):
                continue 
            """
            Every 'step_count' starts with the next step under the presumption it isn't a wall.
            The above's to test that first step.
            """
      
            steps_count = 0
            if direction == "right":
                for y in range(self.pac_y + 1, self.cols):
                    if self.game[self.pac_x][y] == '%':
                        break
                    if self.game[self.pac_x][y] == '*':
                        steps_count += 1
            elif direction == "left":
                for y in range(self.pac_y - 1, -1, -1):
                    if self.game[self.pac_x][y] == '%':
                        break
                    if self.game[self.pac_x][y] == '*':
                        steps_count += 1
            elif direction == "up":
                for x in range(self.pac_x - 1, -1, -1):
                    if self.game[x][self.pac_y] == '%':
                        break
                    if self.game[x][self.pac_y] == '*':
                        steps_count += 1
            elif direction == "down":
                for x in range(self.pac_x + 1, self.rows):
                    if self.game[x][self.pac_y] == '%':
                        break
                    if self.game[x][self.pac_y] == '*':
                        steps_count += 1
            
            '''took steps in every direction till hitting a wall
                wrapped in list
                may the best man win'''
            possible_moves[direction] = steps_count
        max_moves = max(possible_moves.values())
        best_directions = [
            direction for direction, count in possible_moves.items()
            if count == max_moves
        ]
        # next_x, next_y = self.pac_x + dx, self.pac_y + dy
        # if not (0 <= next_x < self.rows and 0 <= next_y < self.cols and self.game[next_x][next_y] != '%'):
        #     self.cache="none" 
        # if random.choice(best_directions)=="right": self.cache="left" 

        return random.choice(best_directions)

    def display_game(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        # Clears terminal
        for i in range(self.cols):
            print("|", end="")
            for j in range(self.rows):
                print(f" {self.game[i][j]} ", end='')
            print("|")
        print("")

    def move_pacman(self):
        self.traversal = self.get_next_PAC_direction()
        # print(self.traversal)
        next_x, next_y = self.pac_x, self.pac_y

        if self.traversal == "right":
            next_y += 1
        elif self.traversal == "left":
            next_y -= 1
        elif self.traversal == "up":
            next_x -= 1
        elif self.traversal == "down":
            next_x += 1

        self.game[self.pac_x][self.pac_y] = ' '
        self.pac_x, self.pac_y = next_x, next_y
        self.game[self.pac_x][self.pac_y] = 'O'
            
    def run_game(self):
        playing=True
        while playing:
            self.display_game()
            self.move_pacman()
            time.sleep(.4)
            playing=False
            for i in range(self.size):
                for j in range(self.size):
                    if self.game[i][j]=='*':
                        playing=True
            if not playing:
                print("GAME ENDED!!!")

            #adjust time for faster or slower observations

if __name__ == "__main__":
    pac = PAC()
    pac.run_game()