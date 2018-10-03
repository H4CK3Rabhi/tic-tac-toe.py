from os import system, name
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
def playGame():
    newGame= Game()
    clear()
    i=1
    while True:
        move=0
        if i%2==0:
            p=2
        else:
            p=1
        newGame.printBoard()
        move=int(input())
        #else:
         #   moves = nn.feedforward(newGame.getcurrentstate())
         #   move=moves.index(max(moves))+1
        if newGame.moveValidity(move)==False:
            print("Move Invalid......")
            continue
        newGame.makemove(move,p)
        if newGame.checkwinner()==1:
            print("Player1 Won...")
            print("New Game?Y/N ::",end=" ")
            isw=input()
            if isw=='Y':
                playGame(nn)
            else:
                break
        elif newGame.checkwinner()==2:
            newGame.printBoard()
            print("Player2 Won...")
            print("New Game?Y/N ::",end=" ")
            isw=input()
            if isw=='Y':
                playGame()
            else:
                break
        i+=1
        clear()
class Game:

    def __init__(self):
        self.positions=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

    def printBoard(self) :
        print( '\n ---------')
        print( '|' ,self.positions[0] , '|' , self.positions[1] , '|' , self.positions[2] , '|')
        print( ' ---------')
        print( '|', self.positions[3] , '|' , self.positions[4] , '|' , self.positions[5] , '|')
        print( ' ---------')
        print( '|' , self.positions[6] ,'|' , self.positions[7] , '|' + self.positions[8] , ' |')
        print( ' ---------\n')

    def getcurrentstate(self):
        state=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for i in range(9):
            u=self.positions[i]
            if u=='x':
                state[i]=1
        for i in range(9):
            u=self.positions[i]
            if u=='o':
                state[i+9]=1
        return state
    
    

    def makemove(self,move,p):
        if p==1:
            self.positions[move-1]='x'
        else:
            self.positions[move-1]='o'
            
    def moveValidity(self,move):
        if self.positions[move-1]=='x' or self.positions[move-1]=='o':
            return False
        return True
    
    def checkwinner(self):
        for i in range(3):
            if self.positions[i]=='x' and self.positions[i+3]=='x' and self.positions[i+6]=='x':
                return 1
            elif self.positions[i]=='o' and self.positions[i+3]=='o' and self.positions[i+6]=='o':
                return 2
        if self.positions[0]=='x' and self.positions[4]=='x' and self.positions[8]=='x':
            return 1
        elif self.positions[2]=='x' and self.positions[4]=='x' and self.positions[6]=='x':
            return 1
        if self.positions[0]=='o' and self.positions[4]=='o' and self.positions[8]=='o':
            return 2
        elif self.positions[2]=='o' and self.positions[4]=='o' and self.positions[6]=='o':
            return 2
        for i in [0,3,6]:
               if self.positions[i]=='x' and self.positions[i+1]=='x' and self.positions[i+2]=='x':
                return 1
               elif self.positions[i]=='o' and self.positions[i+1]=='o' and self.positions[i+2]=='o':
                return 2
        return 0
    
if __name__ == "__main__":
    playGame()
    
    

        
