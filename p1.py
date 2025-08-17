import os
import time
import random
from multiprocessing import Process
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
            ['%', '*', '%', '%', '%', '%', '%', '%', '%', '%', 'X', '%', '*'],
            ['%', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '%', '*'],
            ['%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%']
        ]

        self.pac_x = 1
        self.pac_y = 1
        self.pac_traversal = "right"
        self.game[self.pac_x][self.pac_y] = 'O'
        
        #=======================================================
        #=======================================================

        self.directions = {
            "right": (0, 1),
            "left": (0, -1),
            "up": (-1, 0),
            "down": (1, 0)
        }
        self.opposite_directions = {
            "right": "left",
            "left": "right",
            "up": "down",
            "down": "up"
        }
        self.ghost_directions = {
            "right": (0, 1),
            "right": (0, 2),
            "right": (0, 3),
            "left": (0, -1),
            "left": (0, -2),
            "left": (0, -3),
            "up": (-1, 0),
            "up": (-2, 0),
            "up": (-3, 0),
            "down": (1, 0),
            "down": (2, 0),
            "down": (3, 0)
        }        
        #=======================================================
        #=======================================================
        #Kept initialisations for ghosts seperated
        self.ghost_x = 10
        self.ghost_y = 10
        self.game[self.ghost_x][self.ghost_y] = 'X'
        self.ghost_traversal = "right"
        self.ghost_before_after_spot=' '
        #=======================================================
        #=======================================================
        
        self.cache="none"

    def escape_ghosts(self, ghost_direction):

        possible_moves = {}
        
        for direction, (dx, dy) in self.directions.items():
            next_x, next_y = self.pac_x + dx, self.pac_y + dy
            
            # Skip this direction if the path is a wall or if it's the direction the ghost is coming from
            if not (0 <= next_x < self.cols and 0 <= next_y < self.cols and self.game[next_x][next_y] != '%'):
                continue
            if direction == ghost_direction:
                continue

            steps_count = 0
            if direction == "right":
                for y in range(self.pac_y + 1, self.cols):
                    if self.game[self.pac_x][y] == '%':
                        break
                    if self.game[self.pac_x][y] in [' ', '*']:
                        steps_count += 1
            elif direction == "left":
                for y in range(self.pac_y - 1, -1, -1):
                    if self.game[self.pac_x][y] == '%':
                        break
                    if self.game[self.pac_x][y] in [' ', '*']:
                        steps_count += 1
            elif direction == "up":
                for x in range(self.pac_x - 1, -1, -1):
                    if self.game[x][self.pac_y] == '%':
                        break
                    if self.game[x][self.pac_y] in [' ', '*']:
                        steps_count += 1
            elif direction == "down":
                for x in range(self.pac_x + 1, self.rows):
                    if self.game[x][self.pac_y] == '%':
                        break
                    if self.game[x][self.pac_y] in [' ', '*']:
                        steps_count += 1
            
            possible_moves[direction] = steps_count
            
        if not possible_moves:
            # If all valid moves are towards the ghost, pick a random one
            valid_directions = [d for d in self.directions if d != ghost_direction]
            return random.choice(valid_directions) if valid_directions else None
            
        max_moves = max(possible_moves.values())
        best_directions = [
            direction for direction, count in possible_moves.items()
            if count == max_moves
        ]
        return random.choice(best_directions)

    def get_next_ghost_direction(self):
        possible_moves = {}
        step_count=0
        '''
        directions = {
            "right": (0, 1),
            "left": (0, -1),
            "up": (-1, 0),
            "down": (1, 0)
        }
        '''
        for y in range(self.ghost_y + 1, self.cols):
                if self.game[self.ghost_x][y] == '%':
                    break
                if self.game[self.ghost_x][y] == 'O':
                    return "right"
                step_count+=1
        possible_moves["right"]=step_count
        step_count=0

        # elif direction == "left":
        for y in range(self.ghost_y - 1, -1, -1):
            if self.game[self.ghost_x][y] == '%':
                break
            if self.game[self.ghost_x][y] == 'O':
                return "left"
            step_count+=1
        possible_moves["left"]=step_count
        step_count=0

        # elif direction == "up":
        for x in range(self.ghost_x - 1, -1, -1):
            if self.game[x][self.ghost_y] == '%':
                break
            if self.game[x][self.ghost_y] == 'O':
                return "up"
            step_count+=1
        possible_moves["right"]=step_count
        step_count=0

        # elif direction == "down":
        for x in range(self.ghost_x + 1, self.rows):
            if self.game[x][self.ghost_y] == '%':
                break
            if self.game[x][self.ghost_y] == 'O':
                return "down"
            step_count+=1
        possible_moves["right"]=step_count
        step_count=0
            
        # for direction, (dx, dy) in self.directions.items():
        #     next_x, next_y = self.ghost_x + dx, self.ghost_y + dy
        #     if not (0 <= next_x < self.rows and 0 <= next_y < self.cols and self.game[next_x][next_y] != '%'):
        #         if self.ghost_traversal==direction:
        #             max_moves = max(possible_moves.values())
        #             best_directions = [
        #                 direction for direction, count in possible_moves.items()
        #                 if count == max_moves
        #             ]
        #             return random.choice(best_directions)
            
        dx, dy = self.directions[self.ghost_traversal]
        next_x, next_y = self.ghost_x + dx, self.ghost_y + dy
        
        # Check for wall collision
        if not (0 <= next_x < self.rows and 0 <= next_y < self.cols and self.game[next_x][next_y] != '%'):
            # Wall detected, find all valid, non-wall directions
            valid_directions = []
            for direction, (dx_alt, dy_alt) in self.directions.items():
                next_x_alt, next_y_alt = self.ghost_x + dx_alt, self.ghost_y + dy_alt
                if 0 <= next_x_alt < self.rows and 0 <= next_y_alt < self.cols and self.game[next_x_alt][next_y_alt] != '%':
                    valid_directions.append(direction)
            
            if valid_directions:
                # Choose a new, random direction from the valid ones
                return random.choice(valid_directions)
            else:
                return None # Ghost is trapped   
        return self.ghost_traversal

    def get_next_PAC_direction(self):
        for direction, (dx, dy) in self.ghost_directions.items():
            next_x, next_y = self.pac_x + dx, self.pac_y + dy
            if 0 <= next_x < self.rows and 0 <= next_y < self.cols and self.game[next_x][next_y] == 'X':
                # Ghost found, escape
                return self.escape_ghosts(self.opposite_directions[direction])

        
        possible_moves = {}
        for direction, (dx, dy) in self.directions.items():
            next_x, next_y = self.pac_x + dx, self.pac_y + dy
            if not (0 <= next_x < self.rows and 0 <= next_y < self.cols and self.game[next_x][next_y] != '%'):
                continue 
            
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
            
            possible_moves[direction] = steps_count
            
        if not possible_moves:
            return None # Pac-Man is trapped
        
        max_moves = max(possible_moves.values())
        best_directions = [
            direction for direction, count in possible_moves.items()
            if count == max_moves
        ]
        
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
    
    def move_ghostm(self):
        self.ghost_traversal = self.get_next_ghost_direction()
        print(self.ghost_traversal)
        next_x, next_y = self.ghost_x, self.ghost_y
        
        if self.ghost_traversal == "right":
            next_y += 1
        elif self.ghost_traversal == "left":
            next_y -= 1
        elif self.ghost_traversal == "up":
            next_x -= 1
        elif self.ghost_traversal == "down":
            next_x += 1
        if self.ghost_before_after_spot=='O': self.ghost_before_after_spot=' '
        self.game[self.ghost_x][self.ghost_y] = self.ghost_before_after_spot
        self.ghost_x, self.ghost_y = next_x, next_y
        self.ghost_before_after_spot=self.game[self.ghost_x][self.ghost_y]
        self.game[self.ghost_x][self.ghost_y] = 'X'

    def move_pacman(self):
        self.pac_traversal = self.get_next_PAC_direction()
        # print(self.pac_traversal)
        next_x, next_y = self.pac_x, self.pac_y

        if self.pac_traversal == "right":
            next_y += 1
        elif self.pac_traversal == "left":
            next_y -= 1
        elif self.pac_traversal == "up":
            next_x -= 1
        elif self.pac_traversal == "down":
            next_x += 1

        self.game[self.pac_x][self.pac_y] = ' '
        self.pac_x, self.pac_y = next_x, next_y
        self.game[self.pac_x][self.pac_y] = 'O'
            
    def run_game(self):
        playing=True
        while playing:
            self.display_game()
            p1=Process(target=self.move_pacman())
            p1.start()
            p2=Process(target=self.move_ghostm())
            p2.start()
            time.sleep(.5)
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