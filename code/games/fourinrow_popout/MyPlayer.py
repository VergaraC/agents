from Player import Player
import numpy as np
from random import randint


class MyPlayer(Player): 


    def name(self):
        return "Victor Vergara"
    
    def max_value(self, board, action, alpha, beta, player_code, p):
        if (p==0):
            return self.eval(player_code, board), action
        sucessores = self.sucessores(player_code, board)
        for s in sucessores:
            mv, ac = self.min_value(s['board'], s['action'], alpha, beta, player_code, p-1)
            if (mv > alpha):
                alpha = mv
                action = ac
            if (alpha >= beta):
                return alpha, action
        return alpha, action
    
    def min_value(self, board, action, alpha, beta, player_code, p):
        if (p==0):
            return self.eval(player_code, board), action
        sucessores = self.sucessores(player_code, board)
        for s in sucessores:
            mv, ac = self.max_value(s['board'], s['action'], alpha, beta, player_code, p-1)
            if (mv < beta):
                beta = mv
                action = ac
            if (beta <= alpha):
                return beta, action 
        return beta, action

    def isThereAnyEmergency(self, board, player_code):
        opponent = self.opponent(player_code)
        op_points_line = self.count_row_line(opponent, board)
        op_points_col = self.count_row_column(opponent, board)
        op_points_dig = self.count_row_diag(opponent, board)
        op_points_dig2 = self.count_row_diag(opponent, board[::-1])
        if (op_points_col['3'] > 0 or op_points_line['3'] > 0 or op_points_dig['3'] > 0 or op_points_dig2['3']> 0):
            return True
        return False

    def myEmergency(self,player,board):
        threat = None
        for i in range(6):
            counter = 0
            for j in range(6):
                if ((board[i, j] == player) and (board[i, j+1] == player)):
                    counter = counter + 1
                else:
                    counter = 0
                if counter >= 2:
                    if i == 5: 
                        if j <= 3:
                            if board[i,j+2] == 0:
                                threat = j+2
                                return True, threat
                        if j >= 1:
                            if board[i,j-1] == 0:
                                threat = j-1
                                return True, threat
                    else:
                        if j <= 3:
                            if (board[i,j+2] == 0) and (board[i+1,j+2] != 0):
                                threat = j+2
                                return True, threat
                        if j >= 1:
                            if board[i,j-1] == 0 and (board[i+1,j-1] != 0):
                                threat = j-1
                                return True, threat
                if (counter >= 1):
                    if i == 5:  
                        if j <= 3:
                            if (board[i, j+3] == player) and (board[i,j+2] == 0):
                                threat = j+2
                                return True, threat 
                        if j >= 2:                            
                            if (board[i,j-2] == player) and (board[i,j-1] == 0):
                                threat = j-1
                                return True, threat
                    else:
                        if j <= 3:
                            if (board[i, j+3] == player) and (board[i,j+2] == 0) and (board[i+1,j+2] != 0):
                                threat = j+2
                                return True, threat 
                        if j >= 2:                            
                            if (board[i,j-2] == player) and (board[i,j-1] == 0) and (board[i+1,j-1] != 0):
                                threat = j-1
                                return True, threat
            for i in reversed(range(7)): 
                counter = 0
            for j in range(5):
                if(board[j][i] == player) and (board[j+1][i] == player):
                    counter+=1
                else:
                    counter = 0
                if counter >= 2:
                    if j >= 2:
                        if board[j-2][i] == 0:
                            return True, i
        return False, threat


    def move(self, player_code, board):
        _, action = self.max_value(board, None, -999999, 999999, player_code, 6)
        #
        # Poderiamos fazer soh o 
        #
        #print(int(self.opponent(player_code)))
        playerEmergency = self.myEmergency(player_code,board)
        if playerEmergency[0]:
            print("my Emergency")
            return None,playerEmergency[1]
        if player_code == 1:
            opP =2
        else:
            opP =1
        #opEmergency = self.isThereAnyEmergency(opP,board)
        #if opEmergency[0]:
            #return None,opEmergency[1]
        if (self.isThereAnyEmergency(board, player_code)):
            # simulando ser o adversario para identificar qual a jogada de vitoria
            sucessores = self.sucessores(self.opponent(player_code), board)
            for s in sucessores:
                v = self.eval(self.opponent(player_code), s['board'])
                if (v > 70000):
                    print("Barth")
                    return None, s['action']
        print("not")
        return None,action
            

        # sucessores = self.sucessores(player_code, board)
        # max_eval = 0
        # action = randint(3, 5)
        # for s in sucessores:
        #     v = self.eval(player_code, s['board'])
        #     print(str(s['action'])+' '+str(v))
        #     if (v > max_eval):
        #         max_eval = v
        #         action = s['action']
        # return action

    def sucessores(self, player_code, board):
        suc = []
        for i in range(0,7):
            b = self.movement(player_code, board, i)
            if(b is not None):
                suc.append({'board':b, 'action':i})
        return suc

    def opponent(self, player):
        if player==1:
            return 2
        return 1

    def domain_center(self, player, board):
        h = np.matrix([
            [0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 1., 1., 1., 0., 0.],
            [0., 0., 1., 1., 1., 0., 0.],
            [0., 1., 1., 1., 1., 1., 0.],
            [0., 1., 1., 1., 1., 1., 0.],
            [0., 1., 1., 1., 1., 1., 0.]])
        
        return np.sum(np.logical_and(board==player, h))
    
    def eval(self, player, board): 
        my_points_line = self.count_row_line(player, board)
        my_points_col = self.count_row_column(player, board)
        my_points_dig = self.count_row_diag(player, board)
        my_points_dig2 = self.count_row_diag(player, board[::-1])
        my_qtd_2 = my_points_line['2'] + my_points_col['2'] + my_points_dig['2'] + my_points_dig2['2']
        my_qtd_3 = my_points_line['3'] + my_points_col['3'] + my_points_dig['3'] + my_points_dig2['3']
        my_qtd_4 = my_points_line['4'] + my_points_col['4'] + my_points_dig['4'] + my_points_dig2['4']
        #gaps = my_points_line["gap"]
        #print('my 2', str(my_qtd_2))
        #print('my 3', str(my_qtd_3))
        #print('my 4', str(my_qtd_4))
        sum_my_points = 100000*my_qtd_4 + 1000*my_qtd_3 + 2*my_qtd_2 #+ 100000*gaps

        opponent = self.opponent(player)
        op_points_line = self.count_row_line(opponent, board)
        op_points_col = self.count_row_column(opponent, board)
        op_points_dig = self.count_row_diag(opponent, board)
        op_points_dig2 = self.count_row_diag(opponent, board[::-1])
        op_qtd_2 = op_points_line['2'] + op_points_col['2'] + op_points_dig['2'] + op_points_dig2['2']
        op_qtd_3 = op_points_line['3'] + op_points_col['3'] + op_points_dig['3'] + op_points_dig2['3']
        op_qtd_4 = op_points_line['4'] + op_points_col['4'] + op_points_dig['4'] + op_points_dig2['4']
        #op_gaps = op_points_line["gap"]
        #print('op 2', str(op_qtd_2))
        #print('op 3', str(op_qtd_3))
        #print('op 4', str(op_qtd_4))
        sum_op_points = 100000*op_qtd_4 + 1000*op_qtd_3 + 2*op_qtd_2 #+100000*op_gaps
        
        return sum_my_points - sum_op_points + self.domain_center(player, board)

    def count_row_line(self, player, board):
        retorno = {'2': 0, '3': 0, '4': 0, 'gap': 0}
        for i in range(6):
            counter = 0
            for j in range(6):
                if ((board[i, j] == player) and (board[i, j] == board[i, j + 1])):
                    counter = counter + 1
                else:
                    counter = 0
                if (counter == 1):
                    retorno['2'] = retorno['2'] + 1
                if (counter == 2):
                    retorno['3'] = retorno['3'] + 1
                if (counter == 3):
                    retorno['4'] = retorno['4'] + 1
                '''if (counter >= 1):
                    if i == 5:  # Primeira linha
                        if j <= 3:
                            if (board[i, j+3] == player) and (board[i,j+2] == 0):
                                retorno["gap"] = retorno["gap"]+1
                        if j >= 2:
                            if (board[i,j-2] == player) and (board[i,j-1] == 0):
                                retorno["gap"] = retorno["gap"]+1      
                    else:
                        if j <= 3:
                            if (board[i, j+3] == player) and (board[i,j+2] == 0) and (board[i+1,j+2] != 0):
                                retorno["gap"]  = retorno["gap"]+1
                        if j >= 2:
                            if (board[i,j-2] == player) and (board[i,j-1] == 0) and (board[i+1,j-1] != 0):
                                retorno["gap"] = retorno["gap"]+1'''
        
                                  
        return retorno
    
    def count_row_column(self, player, board):
        retorno = {'2': 0, '3': 0, '4': 0}
        for i in range(7):
            counter = 0
            for j in range(5):
                if ((board[j, i] == player) and (board[j,i] == board[j+1,i])):
                    counter = counter + 1
                else:
                    counter = 0
                if (counter == 1):
                    retorno['2'] = retorno['2'] + 1
                if (counter == 2):
                    retorno['3'] = retorno['3'] + 1
                if (counter == 3):
                    retorno['4'] = retorno['4'] + 1
        return retorno
    
    def count_row_diag(self, player, board):
        retorno = {'2': 0, '3': 0, '4': 0}
        for k in range(-2,4):
            counter = 0
            x = np.diag(board, k=k)
            for i in range(0,len(x)-1):
                if ((x[i] == player) and (x[i] == x[i+1])):
                    counter = counter + 1
                else:
                    counter = 0
                if (counter == 1):
                    retorno['2'] = retorno['2'] + 1
                if (counter == 2):
                    retorno['3'] = retorno['3'] + 1
                if (counter == 3):
                    retorno['4'] = retorno['4'] + 1
        return retorno

    
    def movement(self, player, board, column):
        result_board = np.matrix(board)
        for i in range(5,-2,-1):
            if (board[i,column] == 0):
                break
        if(i<0):
            return None
        result_board[i, column] = player
        return result_board

