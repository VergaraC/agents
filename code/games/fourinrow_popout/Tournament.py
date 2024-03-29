from FourInRow import FourInRow
from RandomPlayer import RandomPlayer
from ManualPlayer import ManualPlayer
from MyPlayer import MyPlayer
from BarthPlayer import BarthPlayer

players = [

    MyPlayer(),
    BarthPlayer(),
    RandomPlayer()
    ]
points = {}
for p in players:
    points[p.name()] = 0
#for vezes in range(0,20):
for i in range(0,len(players)):
    for j in range(i+1, len(players)):
        print(players[i].name() + " vs "+players[j].name())
        winner = FourInRow(players[i], players[j]).game()
        points[winner] += 1 

for i in range(0,len(players)):
    for j in range(i+1, len(players)):
        print(players[j].name() + " vs "+players[i].name())
        winner = FourInRow(players[j], players[i]).game()
        points[winner] += 1

print('Results:')
print('\n')
print(points)