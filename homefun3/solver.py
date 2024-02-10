""" Author: Benjamin Riley Zimmerman, 2024
 This file contains a command line accessible recursive solver.
 Usage: python solver.py <flag> <state>, flag options are -ten and -tic
     Solve -
         Input: state
         Output: { if provided state is strictly winning, | if strictly tying, } if strictly losing, ~ if illegal
"""

# import <your encoding> as encoding
import tic_tac_toe_encoding as encoding
import sys

# invalid == not_primitive

# stores states the have already been solved, O(n) overhead
computed_states = {}
eval_counts = [0, 0, 0, 0, 0, 0]

def Solve(state):
    if state in computed_states:
        return computed_states.get(state)
    eval = encoding.PrimitiveValue(state)
    if eval != '~':
        if eval == '{':
            eval_counts[0] += 1
        if eval == '}':
            eval_counts[1] += 1
        if eval == '|':
            eval_counts[2] += 1
        computed_states[state] = eval
        return eval
    else:
        state_case = '~'
        for move in encoding.GenerateMoves(state):
            result = Solve(encoding.DoMove(state, move))
            if result == '{' and state_case == '~':
                state_case = '}'
            elif result == '|' and state_case != '{':
                state_case = '|'
            elif result == '}':
                state_case = '{'
        if state_case == '{':
            eval_counts[3] += 1
        if state_case == '}':
            eval_counts[4] += 1
        if state_case == '|':
            eval_counts[5] += 1
        computed_states[state] = state_case
        return state_case

def translate_result(result):
    to_str = ""
    if result == '{':
        to_str = "win"
    elif result == '|':
        to_str = "tie"
    elif result == '}':
        to_str = "loss"
    else:
        to_str = "invalid"
    return to_str

def input_to_state(starting_state):
    temp = ""
    for c in starting_state:
        if c == 'x':
            temp += chr(1)
        elif c == 'o':
            temp += chr(2)
        else:
            temp += chr(0)
    return temp


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python solver.py <flag> <state>")
        sys.exit(1)
    if sys.argv[1] == '-tic':
        starting_state = sys.argv[2]
        print(starting_state[:3])
        print(starting_state[3:6] + ': ' + translate_result(Solve(input_to_state(starting_state))))
        print(starting_state[6:])
        print("Losses: " + str(eval_counts[1] + eval_counts[4]) + " (" + str(eval_counts[1]) + " primitives)")
        print("Wins: " + str(eval_counts[0] + eval_counts[3]) + " (" + str(eval_counts[0]) + " primitives)")
        print("Ties: " + str(eval_counts[2] + eval_counts[5]) + " (" + str(eval_counts[2]) + " primitives)")
        print("Total: " + str(eval_counts[0] + eval_counts[1] + eval_counts[2] + eval_counts[3] + eval_counts[4] + eval_counts[5]) + 
                " (" + str(eval_counts[0] + eval_counts[1] + eval_counts[2]) + " primitives)")
    elif sys.argv[1] == '-ten':
        print()
    else:
        print("Usage: python solver.py <flag> <state>")
        sys.exit(1)