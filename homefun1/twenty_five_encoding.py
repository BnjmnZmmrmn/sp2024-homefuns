""" Author: Benjamin Riley Zimmerman, 2024
 This file contains encoding for 25-to-0-by-1-or-3-or-4
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
    if state <= 0b11001 and state > 0b00011:
        return {0b00001, 0b00011, 0b00100}
    elif state <= 0b11001 and state > 0b00010:
        return {0b00001, 0b00011}
    elif state <= 0b11001 and state > 0b00000:
        return {0b00001}
    else:
        return {}

def PrimitiveValue(state):
    if state == 0b0000:
        return 0b10
    return 0b11