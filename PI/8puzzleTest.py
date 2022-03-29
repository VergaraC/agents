from datetime import datetime
from SearchAlgorithms import AEstrela
from _8puzzle import puzzle

goal= str([[1,2,3],[8,0,4],[7,6,5]])

def test1():
  board = [[8,1,3],[0,7,2],[6,5,4]]
  state = puzzle("", board, 1, 0, goal)
  beginning = datetime.now()
  algorithm = AEstrela()
  result = algorithm.search(state)
  ending = datetime.now()
  print(f"Tempo de resolucao:", ending-beginning)
  assert result.state.env() == goal
  
def test2():
  board = [[7,8,6],[2,3,5],[1,4,0]] 
  state = puzzle("", board, 2, 2, goal)
  beginning = datetime.now()
  algorithm = AEstrela()
  result = algorithm.search(state)
  ending = datetime.now()
  print(f"Tempo de resolucao:", ending-beginning)
  assert result.state.env() == goal
  
def test3():
  board = [[7,8,6],[2,3,5],[0,1,4]] 
  state = puzzle("", board, 2, 0, goal)
  beginning = datetime.now()
  algorithm = AEstrela()
  result = algorithm.search(state)
  ending = datetime.now()
  print(f"Tempo de resolucao::", ending-beginning)
  assert result.state.env() == goal
  
def test4():
  board = [[8,3,6],[7,5,4],[2,1,0]] 
  state = puzzle("", board, 2, 2, goal)
  beginning = datetime.now()
  algorithm = AEstrela()
  result = algorithm.search(state)
  ending = datetime.now()
  print(f"Tempo de resolucao::", ending-beginning)
  assert result.state.env() == goal
  
def test5():
  board = [[3,4,8],[1,2,5],[7,0,6]] 
  state = puzzle("", board, 2, 1, goal)
  beginning = datetime.now()
  algorithm = AEstrela()
  result = algorithm.search(state)
  ending = datetime.now()
  print(f"Tempo de resolucao: {ending-beginning}")
  assert result.state.env() == goal