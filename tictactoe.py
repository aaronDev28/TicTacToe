import math
from copy import deepcopy
import numpy as np

def threeRow(row):
    return True if row.count(
        row[0]) == 3 else False

def getCols(board):
    columns = []

    for i in range(3):
        columns.append([row[i] for row in board])
    return columns

def get_diag_cells(board):
    return [[board[0][0], board[1][1], board[2][2]],  
            [board[0][2], board[1][1], board[2][0]]]  


X = "X"
O = "O"
EMPTY = None

def init_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def max_alphaBetaPruning(board, alpha, beta):
    if terminal(board):  
        return util(board), None
    vall = float("-inf")  
    best = None  
    for act in acts(board):  
        min_val = min_alphaBetaPruning(res(board, act), alpha, beta)[
            0]  
        if min_val > vall:  
            best = act  
            vall = min_val  
        alpha = max(alpha, vall)  
        if beta <= alpha: 
            break
    return vall, best  


def min_alphaBetaPruning(board, alpha, beta):
    if terminal(board):  
        return util(board), None
    vall = float("inf")  
    best = None  
    for act in acts(board):  
        max_val = max_alphaBetaPruning(res(board, act), alpha, beta)[
            0]  
        if max_val < vall:  
            best = act  
            vall = max_val  
        beta = min(beta, vall)  
        if beta <= alpha: 
            break
    return vall, best 


def mini_max_algorithm(board):
    if terminal(board):  
        return None
    if plyr(board) == X:  
        return max_alphaBetaPruning(board, float("-inf"), float("inf"))[
            1]  
    elif plyr(board) == O:  
        return min_alphaBetaPruning(board, float("-inf"), float("inf"))[
            1]  
    else:
        raise Exception(
            "Error in Calculating Optimal Move") 
def terminal(board):
    xx = winr(board)  
    if xx is not None:  
        return True
    if all(all(j != EMPTY for j in i) for i in board):  
        return True
    return False


def util(board):
    xx = winr(board)  
    if xx == X:  
        return 1
    elif xx == O:  
        return -1
    else:  
        return 0
    
def plyr(board):
    count_x = 0  
    count_o = 0  
    for i in board:  
        for j in i:  
            if j == "X":  
                count_x += 1
            if j == "O":  
                count_o += 1
    return O if count_x > count_o else X  


def acts(board):
    act = set()  
    for i, row in enumerate(board):  
        for j, val in enumerate(row):  
            if val == EMPTY: 
                act.add((i, j))
    return act 


def res(board, act):
    i, j = act  
    if board[i][j] != EMPTY:  
        raise Exception("Invalid Move")
    next_move = plyr(board)  
    deep_board = deepcopy(board)  
    deep_board[i][j] = next_move  
    return deep_board 


def winr(board):
    rows = board + get_diag_cells(board) + getCols(board)  
    for row in rows: 
        current_plyr = row[0]  
        if current_plyr is not None and threeRow(row):  
            return current_plyr  
    return None 




