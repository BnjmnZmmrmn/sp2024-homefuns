""" Author: Benjamin Riley Zimmerman, 2024
 This file contains a command line accessible recursive solver.
 Usage: python solver.py <state>
     Solve -
         Input: state
         Output: 0b00 if provided state is strictly winning, 0b01 if strictly tying, 0b10 if strictly losing, 0b11 if illegal
"""

# import <your encoding> as encoding
import ten_encoding as encoding
import sys

# invalid == not_primitive
cases = ["win", "tie", "lose", "invalid"]

# stores states the have already been solved, O(n) overhead
computed_states = {}
cache_hits = 0

def Solve(state):
    if state in computed_states:
        cache_hits += 1
        return computed_states.get(state)
    eval = encoding.PrimitiveValue(state)
    if eval != 0b11:
        computed_states[state] = eval
        return eval
    else:
        state_case = 0b11
        for move in encoding.GenerateMoves(state):
            state_case = min(state_case, (0b10 - Solve(encoding.DoMove(state, move))) % 0b11)
        computed_states[state] = state_case
        return state_case

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python solver.py <state>")
        sys.exit(1)
    starting_state = int(sys.argv[1])
    print(f"{starting_state}: {cases[Solve(starting_state)]}")