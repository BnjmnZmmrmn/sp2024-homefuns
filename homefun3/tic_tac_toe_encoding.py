""" Author: Benjamin Riley Zimmerman, 2024
 This file contains encoding for tic_tac_toe
 Usage:
     DoMove -
         Input: state, move
         Output: state resulting from enacting provided move on provided state
     GenerateMoves:
         Input: state
         Output: set of legal moves for the provided state
     PrimitiveValue:
         Input: state
         Output: { if provided state is strictly winning, | if strictly tying, } if strictly losing, ~ if non-primitive
"""

def DoMove(state, move):
    state = list(state)
    state[move[0]] = move[1]
    temp = ""
    for c in state:
        temp += c
    return temp

def GenerateMoves(state):
    moves = []
    num_x = 0
    num_o = 0
    for i in range(0, 9):
        if state[i] == chr(0):
            moves += [i]
        elif state[i] == chr(1):
            num_x += 1
        elif state[i] == chr(2):
            num_o += 1
    next_move = chr(1)
    if num_x > num_o:
        next_move = chr(2)
    return [(i, next_move) for i in moves]

def PrimitiveValue(state):
    top_hor = state[0] + state[1] + state[2]
    mid_hor = state[3] + state[4] + state[5]
    low_hor = state[6] + state[7] + state[8]
    lef_ver = state[0] + state[3] + state[6]
    mid_ver = state[1] + state[4] + state[7]
    rig_ver = state[2] + state[5] + state[8]
    diag_on = state[0] + state[4] + state[8]
    diag_tw = state[2] + state[4] + state[6]
    for three in [top_hor, mid_hor, low_hor, lef_ver, mid_ver, rig_ver, diag_on, diag_tw]:
        if three[0] == three[1] == three[2] and three[0] != chr(0):
            return '}'
    if chr(0) in state:
        return '~'
    else:
        return '|'