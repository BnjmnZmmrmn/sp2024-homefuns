""" Author: Benjamin Riley Zimmerman, 2024
 This file contains encoding for 10-to-0-by-1-or-2
 Usage:
     DoMove -
         Input: state, move
         Output: state resulting from enacting provided move on provided state
     GenerateMoves:
         Input: state
         Output: set of legal moves for the provided state
     PrimitiveValue:
         Input: state
         Output: 0b00 if provided state is a win, 0b01 if tie, 0b10 if loss, 0b11 if non-primitive
"""


def DoMove(state, move):
    return state - move

def GenerateMoves(state):
    if state <= 0b1010 and state > 0b0001:
        return {0b0001, 0b0010}
    elif state <= 0b1010 and state > 0b0000:
        return {0b0001}
    else:
        return {}

def PrimitiveValue(state):
    if state == 0b0000:
        return 0b10
    return 0b11