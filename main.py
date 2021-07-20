import numpy as np
from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

def build_NFA():
    nfa = NFA(
        states={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'},
        input_symbols={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'},
        transitions={
            '0': {'0': {'7', '0'}, '1': {'7', '1'}, '2': {'7', '2'}, '3': {'7', '3'}, '4': {'7', '4'}, '5': {'7', '5'}, '6': {'7', '6'}, '7': {'7', '0'}, '8': {'7', '1'}, '9': {'7', '2'}},
            '1': {'0': {'8', '3'}, '1': {'8', '4'}, '2': {'8', '5'}, '3': {'8', '6'}, '4': {'8', '0'}, '5': {'8', '1'}, '6': {'8', '2'}, '7': {'8', '3'}, '8': {'8', '4'}, '9': {'8', '5'}},
            '2': {'0': {'9', '6'}, '1': {'9', '0'}, '2': {'9', '1'}, '3': {'9', '2'}, '4': {'9', '3'}, '5': {'9', '4'}, '6': {'9', '5'}, '7': {'9', '6'}, '8': {'9', '0'}, '9': {'9', '1'}},
            '3': {'0': {'10', '2'}, '1': {'10', '3'}, '2': {'10', '4'}, '3': {'10', '5'}, '4': {'10', '6'}, '5': {'10', '0'}, '6': {'10', '1'}, '7': {'10', '2'}, '8': {'10', '3'}, '9': {'10', '4'}},
            '4': {'0': {'11', '5'}, '1': {'11', '6'}, '2': {'11', '0'}, '3': {'11', '1'}, '4': {'11', '2'}, '5': {'11', '3'}, '6': {'11', '4'}, '7': {'11', '5'}, '8': {'11', '6'}, '9': {'11', '0'}},
            '5': {'0': {'12', '1'}, '1': {'12', '2'}, '2': {'12', '3'}, '3': {'12', '4'}, '4': {'12', '5'}, '5': {'12', '6'}, '6': {'12', '0'}, '7': {'12', '1'}, '8': {'12', '2'}, '9': {'12', '3'}},
            '6': {'0': {'13', '4'}, '1': {'13', '5'}, '2': {'13', '6'}, '3': {'13', '0'}, '4': {'13', '1'}, '5': {'13', '2'}, '6': {'13', '3'}, '7': {'13', '4'}, '8': {'13', '5'}, '9': {'13', '6'}},
            '7': {'0': {'7'}, '1': {'8'}, '2': {'9'}, '3': {'10'}, '4': {'11'}, '5': {'12'}, '6': {'13'}, '7': {'7'}, '8': {'8'}, '9': {'9'}},
            '8': {'0': {'10'}, '1': {'11'}, '2': {'12'}, '3': {'13'}, '4': {'7'}, '5': {'8'}, '6': {'9'}, '7': {'10'}, '8': {'11'}, '9': {'12'}},
            '9': {'0': {'13'}, '1': {'7'}, '2': {'8'}, '3': {'9'}, '4': {'10'}, '5': {'11'}, '6': {'12'}, '7': {'13'}, '8': {'7'}, '9': {'8'}},
            '10': {'0': {'9'}, '1': {'10'}, '2': {'11'}, '3': {'12'}, '4': {'13'}, '5': {'7'}, '6': {'8'}, '7': {'9'}, '8': {'10'}, '9': {'11'}},
            '11': {'0': {'12'}, '1': {'13'}, '2': {'7'}, '3': {'8'}, '4': {'9'}, '5': {'10'}, '6': {'11'}, '7': {'12'}, '8': {'13'}, '9': {'7'}},
            '12': {'0': {'8'}, '1': {'9'}, '2': {'10'}, '3': {'11'}, '4': {'12'}, '5': {'13'}, '6': {'7'}, '7': {'8'}, '8': {'9'}, '9': {'10'}},
            '13': {'0': {'11'}, '1': {'12'}, '2': {'13'}, '3': {'7'}, '4': {'8'}, '5': {'9'}, '6': {'10'}, '7': {'11'}, '8': {'12'}, '9': {'13'}},
            '14': {'0': {'16'}, '1': {'1', '15'}, '2': {'2', '15'}, '3': {'3', '15'}, '4': {'4', '15'}, '5': {'5', '15'}, '6': {'6', '15'}, '7': {'0', '15'}, '8': {'1', '15'}, '9': {'2', '15'}},
            '15': {'0': {'7'}, '1': {'8'}, '2': {'9'}, '3': {'10'}, '4': {'11'}, '5': {'12'}, '6': {'13'}, '7': {'7'}, '8': {'8'}, '9': {'9'}},
            '16': {'0': {'16'}, '1': {'16'}, '2': {'16'}, '3': {'16'}, '4': {'16'}, '5': {'16'}, '6': {'16'}, '7': {'16'}, '8': {'16'}, '9': {'16'}}
        },
        initial_state='14',
        final_states={'0', '7'}
    )

    return nfa

def count(_states, transitions, k, finalS):
    cur = []
    states = []
    numberOfStates = len(_states)

    next = [0 for i in range(0, numberOfStates)]

    for i in _states:
        states.append(i) #fills the state array with all the keys needed to access the dictioary

    for l in range(0,len(states)):
        if states[l] in finalS:
            cur.append(1)
        else:
            cur.append(0)

    for x in range(0, k):
        for i in range(0, numberOfStates):
            row = getStates(states[i],transitions)
            place = []
            for pos, st in row.items():
                for s in range(0,len(states)):
                    if st == states[s]:
                        place.append(s)
            next[i] = cur[place[0]] + cur[place[1]] + cur[place[2]] + cur[place[3]] + cur[place[4]] + cur[place[5]] + cur[place[6]] + cur[place[7]] + cur[place[8]] + cur[place[9]]

        for j in range(0, numberOfStates):
            cur[j] = next [j]

        for h in range(0, numberOfStates):
            next[h] = 0

    return cur[847]

def getStates(idx, transitions):
    #uses the key to find the approriate row of values
    for key, row in transitions.items():
        if idx == key:
           return row;

def main():
    k = input(
        "please provide a value k or type exit to terminate: ")  # Get value n that will be the length of the strings

    while (k != "exit"):  # repeatedly do this untill user decides to exit

        nfa = build_NFA()  # builds the NFA that has been hard coded
        dfa = DFA.from_nfa(nfa)  # returns an equivalent DFA from hard coded NFA

        transitions = dict(sorted(dfa.transitions.items()))
        states = sorted(dfa.states)
        dfa_final_states = sorted(dfa.final_states)

        table = [[0] * 10 for i in range(0, len(dfa.states))]

        row = 0

        for value1 in dfa.transitions.values():
            for key2, value2 in value1.items():
                if value2 in dfa.final_states:
                    table[row][int(key2)] = 1
                else:
                    table[row][int(key2)] = 0
            row += 1

        k = int(k)
        weak_div = count(states, transitions, k, dfa_final_states)  # count the strings based on the DFA

        print("Total strings of length: " + str(k) + " that are weakly divisible by 7 are: " + str(weak_div))
        k = input("please provide a value k or type exit to terminate: ")

    print("exiting...")
    exit(0)

main()
