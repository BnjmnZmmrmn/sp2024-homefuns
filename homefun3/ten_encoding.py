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
         Output: { if provided state is strictly winning, | if strictly tying, } if strictly losing, ~ if non-primitive
"""


def DoMove(state, move):
    return chr(ord(state) - move)

def GenerateMoves(state):
    if state <= chr(10) and state > chr(1):
        return [1, 2]
    elif state <= chr(10) and state > chr(0):
        return [1]
    else:
        return []

def PrimitiveValue(state):
    if state == chr(0):
        return '}'
    return '~'