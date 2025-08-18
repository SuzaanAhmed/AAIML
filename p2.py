import random

class NumGuess:
    def __init__(self):
        self.random_number=random.randint(0,100000000)
        self.prev=0
    def StartGame(self):
        while True:
            suggestion=""
            guess=int(input(f"Guess a Number: "))
            self.prev=guess
            if self.prev>self.random_number:
                suggestion="greater"
            elif self.prev==self.random_number:
                break
            else:
                suggestion="lesser"
            print(f"Your guess is {suggestion} than the actual number.")
        print(f"{self.prev} is the correct guess!!!")

if __name__=="__main__":
    myNum=NumGuess()
    myNum.StartGame()