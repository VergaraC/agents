from SearchAlgorithms import BuscaLargura
from SearchAlgorithms import BuscaProfundidade
from SearchAlgorithms import BuscaProfundidadeIterativa
from SearchAlgorithms import BuscaCustoUniforme
from SearchAlgorithms import BuscaGananciosa
from SearchAlgorithms import AEstrela
from Graph import State

#
# Initial state: 1
# Operations: +1 and +2
# Final state: any number bigger than 0
#

class U2(State):

    def __init__(self, bono, edge, adam, larry, cross1, cross2, time):
        self.bono = bono
        self.edge = edge
        self.adam = adam
        self.larry = larry
        self.cross1 = cross1
        self.cross2 = cross2
        self.time = time
        
        ## Todos comecam False e precisam ir para True
    def env(self):
         return ";"+str(self.number)
    
    def sucessors(self):
        sucessors = []
        if (self.bono == False and self.edge == False and self.adam == False and self.larry == False ):

            sucessors.append(U2(self.number +2, "2", self.Goal))
            sucessors.append(U2(self.number +1, "1", self.Goal))
        return sucessors
        
    
    def is_goal(self):
        return (self.number ==self.Goal)
    
    def description(self):
        return "Problema simples com operadores de soma 1 e soma 2. Estados representados apenas por um numero"
    
    def cost(self):
        return 1

    def h(self):
        return 0
    
    def print(self):
        return str(self.operator)

from datetime import datetime

def main():
    
    #
    # Executando busca em largura
    #
    print('Busca em largura')
    state = U2(1, '', 10)
    algorithm = BuscaLargura()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')


if __name__ == '__main__':
    main()
