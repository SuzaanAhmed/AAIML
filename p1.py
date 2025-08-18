class AASCII_GridSearch:

    def __init__(self, size=13):
        self.size = size
        self.cols = size
        self.rows = size
        
        self.grid = [
            ['@', 'z', '^', '[', '#', '+', '1', '>', '~', 'V', '(', ',', '?'],
            ['Q', '&', '}', 'R', 'g', '*', 'Z', 'F', ':', '7', 'j', '=', '!'],
            ['$', '>', '.', '5', 'T', 'B', 'u', '|', 'W', 'o', '[', '0', '/'],
            ['+', 'y', 'K', '`', ';', 'X', '2', 'A', 'c', 'L', 'd', '}', 'T'],
            ['(', 'S', '#', '>', 'J', 'I', ')', '9', '[', ':', 'n', '4', 'E'],
            ['R', '>', 'e', 'm', 'Y', '(', '-', 'k', '}', 'q', 'C', ')', 'a'],
            ['"', '{', ']', '[', 'D', '!', '=', '#', ':', 'x', '<', '3', 'b'],
            ['^', 'n', 'h', 'v', 'r', '!', 'N', 'M', '_', 'w', 'f', '8', ';'],
            ['`', 'K', ']', 'f', '#', '0', '6', '@', '?', '+', '/', '[', 'y'],
            ['9', '%', '~', '4', '>', 'z', 'l', 'b', '.', 'H', 'g', '#', '5'],
            ['|', 'A', '2', '[', '{', '1', 'U', ']', 'P', ')', 'X', '3', 'J'],
            ['(', '!', '7', 'c', 'd', '=', 'x', ':', '!', '"', 'Y', '6', '$'],
            ['[', '[', '{', '&', ']', '%', '#', '3', '@', '*', '9', '(', ']']
        ]
        
        self.StartHolder=(0,0)
        self.TaskHolder=[]

    def checkStart(self,character,x,y):
        if character=="S":
            self.StartHolder=(x+1,y+1)

    def checkTasks(self,character,x,y):
        if character=="T":
            self.TaskHolder.append((x+1,y+1))


    def run_search(self):
        for x in range(self.cols):
            print('|',end='')
            for y in range(self.rows):
                print(f" {self.grid[x][y]} ",end='')
                myMain.checkStart(self.grid[x][y],x,y)
                myMain.checkTasks(self.grid[x][y],x,y)
            print('|')
        print(f"The Start State 'S' is in cell [{self.StartHolder}]")
        print(f"The Task States 'T' exists in cell [{self.TaskHolder}]")
            

if __name__=="__main__":
    myMain=AASCII_GridSearch()
    myMain.run_search()
    
        
