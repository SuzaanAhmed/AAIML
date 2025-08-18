import os
import time
import random

class PAC:

    def __init__(self, size=13):
        self.size = size
        self.cols = size
        self.rows = size
        
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
        self.game[self.pac_x][self.pac_y] = 'O'
        self.pac_traversal="right"
        
        # self.ghost_x = 10
        # self.ghost_y = 10
        # self.game[self.ghost_x][self.ghost_y] = 'X'
        # self.ghost_traversal = "up"
        
        # self.ghost_before_after_spot = '*'
        
        self.directions = {
            "right": (0, 1),
            "left": (0, -1),
            "up": (-1, 0),
            "down": (1, 0)
        }

        self.turn={
            "r":"right",
            "l":"left",
            "u":"up",
            "d":"down"
        }

        self.opposite_directions = {
            "right": "left",
            "left": "right",
            "up": "down",
            "down": "up"
        }

    def display_game(self):

        os.system('cls' if os.name == 'nt' else 'clear')
        # terminal clearance
        for i in range(self.cols):
            print("|", end="")
            for j in range(self.rows):
                print(f" {self.game[i][j]} ", end='')
            print("|")
        print("")
    '''
    def escape_ghosts(self, ghost_direction):
        
        possible_moves = {}
        
        for direction, (dx, dy) in self.directions.items():
            next_x, next_y = self.pac_x + dx, self.pac_y + dy
            
            #wall,ghost or bounds
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
    '''
    '''
    def get_next_ghost_direction(self):
        
        dx, dy = self.directions[self.ghost_traversal]
        next_x, next_y = self.ghost_x + dx, self.ghost_y + dy
        
        if not (0 <= next_x < self.rows and 0 <= next_y < self.cols and self.game[next_x][next_y] != '%'):
            
            valid_directions = []
            for direction, (dx_alt, dy_alt) in self.directions.items():
                next_x_alt, next_y_alt = self.ghost_x + dx_alt, self.ghost_y + dy_alt
                if 0 <= next_x_alt < self.rows and 0 <= next_y_alt < self.cols and self.game[next_x_alt][next_y_alt] != '%':
                    valid_directions.append(direction)
            
            if valid_directions:
                return random.choice(valid_directions)
            else:
                return None # Ghost  trapped
        
        return self.ghost_traversal
    '''

    def manual_direction(self):
        inp=input("Enter initial of direction(r: right, l: left, etc)")
        for direction,turn in self.turn.items():
            if direction==inp:
                return turn

    def get_next_pac_direction(self):
        #3 box ghost detection
        '''
        for step in range(1, 4):
            next_x, next_y = self.pac_x, self.pac_y + step
            if 0 <= next_x < self.rows and 0 <= next_y < self.cols:
                if self.game[next_x][next_y] == 'X':
                    return self.escape_ghosts("right")

            next_x, next_y = self.pac_x, self.pac_y - step
            if 0 <= next_x < self.rows and 0 <= next_y < self.cols:
                if self.game[next_x][next_y] == 'X':
                    return self.escape_ghosts("left")

            next_x, next_y = self.pac_x - step, self.pac_y
            if 0 <= next_x < self.rows and 0 <= next_y < self.cols:
                if self.game[next_x][next_y] == 'X':
                    return self.escape_ghosts("up")

            next_x, next_y = self.pac_x + step, self.pac_y
            if 0 <= next_x < self.rows and 0 <= next_y < self.cols:
                if self.game[next_x][next_y] == 'X':
                    return self.escape_ghosts("down")
        '''
        # If no ghost is in range, find the path with the most pellets
        possible_moves = {}
        for direction, (dx, dy) in self.directions.items():
            next_x, next_y = self.pac_x + dx, self.pac_y + dy
            if not (0 <= next_x < self.rows and 0 <= next_y < self.cols and self.game[next_x][next_y] != '%'):
                if self.pac_traversal==direction: self.pac_traversal==""
                continue 
            
            steps_count = 0
            if direction == "right":
                for y in range(self.pac_y + 1, self.cols):
                    if self.game[self.pac_x][y] == '%':
                        break
                    if self.game[self.pac_x][y] == '*':
                        steps_count += 10
                    # if self.game[self.pac_x][y] == ' ':
                        # steps_count += 1
            elif direction == "left":
                for y in range(self.pac_y - 1, -1, -1):
                    if self.game[self.pac_x][y] == '%':
                        break
                    if self.game[self.pac_x][y] == '*':
                        steps_count += 10
                    # if self.game[self.pac_x][y] == ' ':
                        # steps_count += 1
            elif direction == "up":
                for x in range(self.pac_x - 1, -1, -1):
                    if self.game[x][self.pac_y] == '%':
                        break
                    if self.game[x][self.pac_y] == '*':
                        steps_count += 10
                    # if self.game[x][self.pac_y] == ' ':
                        # steps_count += 1
            elif direction == "down":
                for x in range(self.pac_x + 1, self.rows):
                    if self.game[x][self.pac_y] == '%':
                        break
                    if self.game[x][self.pac_y] == '*':
                        steps_count += 10
                    # if self.game[x][self.pac_y] == ' ':
                        # steps_count += 1
            
            possible_moves[direction] = steps_count
            
        if not possible_moves:
            return None # Pac-Man is trapped
        
        max_moves = max(possible_moves.values())
        best_directions = [
            direction for direction, count in possible_moves.items()
            if count == max_moves
        ]
        
        if all(value == max_moves for value in possible_moves.values()):
            return pac.manual_direction()

        return random.choice(best_directions)
    
    def move_pacman(self):
    
        next_direction = self.get_next_pac_direction()
        
        if next_direction is None:
            return # Pac-Man is trapped, so he stops moving
        
        self.game[self.pac_x][self.pac_y] = ' '
        if next_direction == "right":
            self.pac_y += 1
        elif next_direction == "left":
            self.pac_y -= 1
        elif next_direction == "up":
            self.pac_x -= 1
        elif next_direction == "down":
            self.pac_x += 1
        
        # Game over state
        # if self.pac_x == self.ghost_x and self.pac_y == self.ghost_y:
        #     print("GAME OVER! A ghost caught you.")
        #     exit()
            
        self.game[self.pac_x][self.pac_y] = 'O'
    '''
    def move_ghostm(self):
        
        self.ghost_traversal = self.get_next_ghost_direction()

        if self.ghost_traversal is None:
            return 

        next_x, next_y = self.ghost_x, self.ghost_y
        
        if self.ghost_traversal == "right":
            next_y += 1
        elif self.ghost_traversal == "left":
            next_y -= 1
        elif self.ghost_traversal == "up":
            next_x -= 1
        elif self.ghost_traversal == "down":
            next_x += 1

        # Check for collision with Pac-Man
        if next_x == self.pac_x and next_y == self.pac_y:
            print("GAME OVER! A ghost caught you.")
            exit()

        self.game[self.ghost_x][self.ghost_y] = self.ghost_before_after_spot
        
        self.ghost_x, self.ghost_y = next_x, next_y
        self.ghost_before_after_spot = self.game[self.ghost_x][self.ghost_y]
        self.game[self.ghost_x][self.ghost_y] = 'X'
    '''
    def run_game(self):
        self.display_game()
        time.sleep(1)
        
        while True:
            self.move_pacman()
            # self.move_ghostm()
            self.display_game()
            time.sleep(.2)
            if not any('*' in row for row in self.game):
                print("YOU WIN! All pellets have been eaten.")
                break

if __name__ == "__main__":
    pac = PAC()
    pac.run_game()
