from SearchAlgorithms import AEstrela
from Graph import State
import time
import copy
from os import error



boardEasy = [[8,1,3],[0,7,2],[6,5,4]]
goal = [[1,2,3], [8,0,4], [7,6,5]]
class puzzle(State):

    def __init__(self, op, board, x, y, goal):
        self.operator = op
        self.board = board
        self.x = x
        self.y = y
        self.goal = goal

    def env(self):
        return str(self.board)
    
    def sucessors(self):
        sucessores = []
        print(self.x, self.y)
        for items in range(3):
            print(self.board[items])
        if 3 -1 > self.y:
            tempR = copy.deepcopy(self.board)
            ## right
            tempR[self.x][self.y] = tempR[self.x][self.y+1] 
            tempR[self.x][self.y+1] = 0
            sucessores.append(puzzle("right",tempR, self.x, self.y+1, self.goal))
           
            print("Board:  ", tempR)
        if self.y > 0:
            tempL = copy.deepcopy(self.board)
            ## left
            tempL[self.x][self.y] = tempL[self.x][self.y-1] 
            tempL[self.x][self.y-1] = 0
            sucessores.append(puzzle("left",tempL, self.x, self.y-1, self.goal))
           
            print("Board:  ", tempL)
        if self.x > 0:
            tempU = copy.deepcopy(self.board)
            ## up
            tempU[self.x][self.y] = tempU[self.x-1][self.y] 
            tempU[self.x-1][self.y] = 0
            sucessores.append(puzzle("up",tempU, self.x-1, self.y, self.goal))
           
            print("Board:  ", tempU)
        if 3 -1 > self.x:
            tempD = copy.deepcopy(self.board)
            ## down
            tempD[self.x][self.y] = tempD[self.x+1][self.y] 
            tempD[self.x+1][self.y] = 0
            sucessores.append(puzzle("down",tempD, self.x+1, self.y, self.goal))
           
            print("Board:  ", tempD)
        
        #print(sucessores)
        return sucessores
                      
    def is_goal(self):
        if self.board ==self.goal:
            print("BOARD FINAL")
            print(self.board)
            return True
        return False
    
    def description(self):
        return "8 Puzzle solver"
    
    def cost(self):
        return 1

    def print(self):
        pass
    
    def h(self):
        #manhattan distance
        d = 0
        for x in range(0, 3):
            for y in range(0, 3):
                xGoal = 10
                yGoal = 10
                if self.board[self.x][self.y] == 0:
                    xGoal = 1
                    yGoal = 1
                elif self.board[self.x][self.y] == 1:
                    xGoal = 0
                    yGoal = 0
                elif self.board[self.x][self.y] == 2:
                    xGoal = 0
                    yGoal = 1
                elif self.board[self.x][self.y] == 3:
                    xGoal = 0
                    yGoal = 2
                elif self.board[self.x][self.y] == 4:
                    xGoal = 1
                    yGoal = 2
                elif self.board[self.x][self.y] == 5:
                    xGoal = 2
                    yGoal = 2
                elif self.board[self.x][self.y] == 6:
                    xGoal = 2
                    yGoal = 1
                elif self.board[self.x][self.y] == 7:
                    xGoal = 2
                    yGoal = 0
                elif self.board[self.x][self.y] == 8:
                    xGoal = 1
                    yGoal = 0
                else:
                    raise error
                d += abs(xGoal -x) + abs(yGoal - y)
        print("h:  ", d)
        return d
                
def main():
    print('Busca A*')
    print("InitialBoard:  ", boardEasy)
    state = puzzle("", boardEasy, 1, 0, goal)
   # state.randomBoard()
    algorithm = AEstrela()
    print("Initial state with h = "+str(state.h()))
    start = time.time()
    result = algorithm.search(state)
    end = time.time()
    if result != None:
        print('Achou!')
        print(result.show_path())
        print('Final state with h = '+str(result.h()))
        print('Duration in seconds = '+str(end-start))
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()