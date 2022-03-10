from SearchAlgorithms import BuscaProfundidadeIterativa, BuscaProfundidade, BuscaLargura
from Graph import State 
import math

class KnuthProblem(State):

    def __init__(self, number, goal, operation):
        self.number = number
        self.operation = operation
        self.goal = goal
        
    
    def sucessors(self):
        sucessors = []
        self.number = int(self.number)
        if self.operation == "round_down":
            
            if (self.number) > self.goal**2:
                sucessors.append(KnuthProblem(math.sqrt(self.number), self.goal, "sqrt"))
                
            else:
                sucessors.append(KnuthProblem(math.factorial(self.number), self.goal, "factorial"))
            sucessors.append(KnuthProblem(int(self.number), self.goal, "round_down"))
        return sucessors
    
    def is_goal(self):
        return (self.number == self.goal)
    
    def description(self):
        return "Describe the problem"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operation)
    
    def env(self):
        #
        # IMPORTANTE: este não apenas deve retornar uma descrição do environment, mas 
        # deve também retornar um valor que descreva aquele nodo em específico. Pois 
        # esta representação é utilizada para verificar se um nodo deve ou ser adicionado 
        # na lista de abertos.
        #
        # Exemplos de especificações adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)+"#"+str(self.cost)
        # - para o problema das cidades: return self.city+"#"+str(self.cost())
        #
        # Exemplos de especificações NÃO adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)
        # - para o problema das cidades: return self.city
        #
        return self.number+"#"+str(self.cost())


def main():
    print('Busca em profundidade iterativa')
    state = KnuthProblem('')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()