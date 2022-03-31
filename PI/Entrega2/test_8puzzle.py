from datetime import datetime
from SearchAlgorithms import AEstrela
from _8puzzle import puzzle

goal= [[1,2,3],[8,0,4],[7,6,5]]

def test_1():
  board = [[8,1,3],[0,7,2],[6,5,4]]
  state = puzzle(" ", board, 1, 0, goal)
  beginning = datetime.now()
  print(beginning)
  algorithm = AEstrela()
  result = algorithm.search(state)
  ending = datetime.now()
  
  print("Tempo de resolucao:", ending-beginning)
  assert result.state.env() == str(goal)
  
def test_2():
  board = [[7,8,6],[2,3,5],[1,4,0]] 
  state = puzzle(" ", board, 2, 2, goal)
  beginning = datetime.now()
  algorithm = AEstrela()
  result = algorithm.search(state)
  ending = datetime.now()
  print("Tempo de resolucao:", ending-beginning)
  assert result.state.env() == str(goal)
  
def test_3():
  board = [[7,8,6],[2,3,5],[0,1,4]] 
  state = puzzle(" ", board, 2, 0, goal)
  beginning = datetime.now()
  algorithm = AEstrela()
  result = algorithm.search(state)
  ending = datetime.now()
  print("Tempo de resolucao::", ending-beginning)
  assert result.state.env() == str(goal)
  
def test_4():
  board = [[8,3,6],[7,5,4],[2,1,0]] 
  state = puzzle(" ", board, 2, 2, goal)
  beginning = datetime.now()
  algorithm = AEstrela()
  result = algorithm.search(state)
  ending = datetime.now()
  print("Tempo de resolucao::", ending-beginning)
  assert result.state.env() == str(goal)
  
def test_5():
  board = [[3,4,8],[1,2,5],[7,0,6]] 
  state = puzzle(" ", board, 2, 1, goal)
  print("Teste impossível")
  assert state.isSolvable() == False