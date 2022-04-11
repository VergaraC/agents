from SearchAlgorithms import AEstrela
from Graph import State
import numpy as np
import time
import gym

class TaxiDriver(State):

    def __init__(self, taxi, pasPosition, barreiras, passIn, op, goal):
        self.taxi = TaxiDriver\
            .checkTupla(taxi)              # taxi pos  
        self.pasPosition = TaxiDriver\
            .checkTupla(pasPosition)       # pas pos            
        self.barreiras = TaxiDriver\
            .arrumaMapa(barreiras)      # barreiras pos
        self.passIn = passIn               # passIn vira True quando passageiro embarca, 
        self.operator = op                 # esqueda, direita, cima, baixo, pega 
        self.goal = goal                   # goal pos
        
    def env(self):
        return str(self.operator)+str(self.taxi)+str(self.passIn)

    def sucessors(self):
        sucessors = []

        #esquerda
        if (self.taxi and [self.taxi[0],self.taxi[1]-1]) not in self.barreiras:
            sucessors.append(TaxiDriver([self.taxi[0],self.taxi[1]-1], self.pasPosition, self.barreiras, self.passIn, "esquerda", self.goal))
        #direita
        if (self.taxi and [self.taxi[0],self.taxi[1]+1]) not in self.barreiras:
            sucessors.append(TaxiDriver([self.taxi[0],self.taxi[1]+1], self.pasPosition, self.barreiras, self.passIn, "direita", self.goal))
        #cima
        if (self.taxi and [self.taxi[0]-1,self.taxi[1]]) not in self.barreiras:
            sucessors.append(TaxiDriver([self.taxi[0]-1,self.taxi[1]], self.pasPosition, self.barreiras, self.passIn, "cima", self.goal))
        #baixo
        if (self.taxi and [self.taxi[0]+1,self.taxi[1]]) not in self.barreiras:
            sucessors.append(TaxiDriver([self.taxi[0]+1,self.taxi[1]], self.pasPosition, self.barreiras, self.passIn, "baixo", self.goal))
        
        #pega passageiro
        if (not self.passIn) and (self.taxi == self.pasPosition):
            sucessors.append(TaxiDriver(self.taxi, self.pasPosition, self.barreiras, True, "pegou", self.goal))
        return sucessors
    
    def is_goal(self):
        return (self.taxi == self.goal) and self.passIn

    def description(self):
        return "Taxi needs to find a path to its passenger and delier him to his destinations "
    
    def cost(self):
        return 1 

    def h(self):

        if self.passIn:
            x = abs(self.taxi[1] - self.goal[1])
            y = abs(self.taxi[0] - self.goal[0])
            
        else:
            x = abs(self.taxi[1] - self.pasPosition[1])
            y = abs(self.taxi[0] - self.pasPosition[0])
            
        return x + y

    def checkTupla(tupla):
        for i in tupla:
            if i == 0:
                raise ValueError("Tupla com problema")
        return tupla
        
    def arrumaMapa(map):
        if type(map) != list:
            proibidos = ["|","-","+"]
            listaCoords = []
            M = np.zeros((map.shape[0],map.shape[1]))
            M = M.astype(str)
            for i in range(map.shape[0]):
                for j in range(map.shape[1]):
                    M[i,j] = map[i,j].decode('UTF-8')
                    if M[i,j] in proibidos:
                        listaCoords.append([i,j])
            return listaCoords
        return map
        

    def print(self):
        return str(self.operator)


def main():
    print('Busca A*')
    env = gym.make("Taxi-v3").env
    M = np.zeros((env.desc.shape[0],env.desc.shape[1]))
    M = M.astype(str)
    points = ["R", "G", "B", "Y"]
    letters = []
    for i in range(env.desc.shape[0]):
        for j in range(env.desc.shape[1]):
            M[i,j] = env.desc[i,j].decode('UTF-8')
            if M[i,j] in points:
                letters.append([i,j])
    start = [1,6]
    M[start[0],start[1]] = '0'
    print(M)
    map = env.desc
    state = TaxiDriver(start,letters[0],map,False,'',letters[2])
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print('Achou!')
        print(result.show_path()+" ; drop off")
        print(f"Em {tf-ts}")
    else:
        print('Nao achou solucao')


if __name__ == '__main__':
    main()