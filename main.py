from automata.fa.dfa import DFA
from automata.fa.nfa import NFA


class converted_DFA:

    # Class constructor
    def __init__(self):
        # Creates NFS and converts it to DFA
        self.dfa = DFA.from_nfa(self.build_NFA())
        self.transitions = dict(sorted(self.dfa.transitions.items()))
        self.states = sorted(self.dfa.states)
        self.dfa_final_states = sorted(self.dfa.final_states)

        table = [[0] * 10 for i in range(0, len(self.dfa.states))]

        row = 0

        for value1 in self.dfa.transitions.values():
            for key2, value2 in value1.items():
                if value2 in self.dfa.final_states:
                    table[row][int(key2)] = 1
                else:
                    table[row][int(key2)] = 0
            row += 1

    # Builds NFA and all of its transitions
    def build_NFA(self):
        nfa = NFA(
            states={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'},
            input_symbols={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'},
            transitions={
                '0': {'0': {'7', '0'}, '1': {'7', '1'}, '2': {'7', '2'}, '3': {'7', '3'}, '4': {'7', '4'},
                      '5': {'7', '5'}, '6': {'7', '6'}, '7': {'7', '0'}, '8': {'7', '1'}, '9': {'7', '2'}},
                '1': {'0': {'8', '3'}, '1': {'8', '4'}, '2': {'8', '5'}, '3': {'8', '6'}, '4': {'8', '0'},
                      '5': {'8', '1'}, '6': {'8', '2'}, '7': {'8', '3'}, '8': {'8', '4'}, '9': {'8', '5'}},
                '2': {'0': {'9', '6'}, '1': {'9', '0'}, '2': {'9', '1'}, '3': {'9', '2'}, '4': {'9', '3'},
                      '5': {'9', '4'}, '6': {'9', '5'}, '7': {'9', '6'}, '8': {'9', '0'}, '9': {'9', '1'}},
                '3': {'0': {'10', '2'}, '1': {'10', '3'}, '2': {'10', '4'}, '3': {'10', '5'}, '4': {'10', '6'},
                      '5': {'10', '0'}, '6': {'10', '1'}, '7': {'10', '2'}, '8': {'10', '3'}, '9': {'10', '4'}},
                '4': {'0': {'11', '5'}, '1': {'11', '6'}, '2': {'11', '0'}, '3': {'11', '1'}, '4': {'11', '2'},
                      '5': {'11', '3'}, '6': {'11', '4'}, '7': {'11', '5'}, '8': {'11', '6'}, '9': {'11', '0'}},
                '5': {'0': {'12', '1'}, '1': {'12', '2'}, '2': {'12', '3'}, '3': {'12', '4'}, '4': {'12', '5'},
                      '5': {'12', '6'}, '6': {'12', '0'}, '7': {'12', '1'}, '8': {'12', '2'}, '9': {'12', '3'}},
                '6': {'0': {'13', '4'}, '1': {'13', '5'}, '2': {'13', '6'}, '3': {'13', '0'}, '4': {'13', '1'},
                      '5': {'13', '2'}, '6': {'13', '3'}, '7': {'13', '4'}, '8': {'13', '5'}, '9': {'13', '6'}},
                '7': {'0': {'7'}, '1': {'8'}, '2': {'9'}, '3': {'10'}, '4': {'11'}, '5': {'12'}, '6': {'13'},
                      '7': {'7'}, '8': {'8'}, '9': {'9'}},
                '8': {'0': {'10'}, '1': {'11'}, '2': {'12'}, '3': {'13'}, '4': {'7'}, '5': {'8'}, '6': {'9'},
                      '7': {'10'}, '8': {'11'}, '9': {'12'}},
                '9': {'0': {'13'}, '1': {'7'}, '2': {'8'}, '3': {'9'}, '4': {'10'}, '5': {'11'}, '6': {'12'},
                      '7': {'13'}, '8': {'7'}, '9': {'8'}},
                '10': {'0': {'9'}, '1': {'10'}, '2': {'11'}, '3': {'12'}, '4': {'13'}, '5': {'7'}, '6': {'8'},
                       '7': {'9'}, '8': {'10'}, '9': {'11'}},
                '11': {'0': {'12'}, '1': {'13'}, '2': {'7'}, '3': {'8'}, '4': {'9'}, '5': {'10'}, '6': {'11'},
                       '7': {'12'}, '8': {'13'}, '9': {'7'}},
                '12': {'0': {'8'}, '1': {'9'}, '2': {'10'}, '3': {'11'}, '4': {'12'}, '5': {'13'}, '6': {'7'},
                       '7': {'8'}, '8': {'9'}, '9': {'10'}},
                '13': {'0': {'11'}, '1': {'12'}, '2': {'13'}, '3': {'7'}, '4': {'8'}, '5': {'9'}, '6': {'10'},
                       '7': {'11'}, '8': {'12'}, '9': {'13'}},
                '14': {'0': {'16'}, '1': {'1', '15'}, '2': {'2', '15'}, '3': {'3', '15'}, '4': {'4', '15'},
                       '5': {'5', '15'}, '6': {'6', '15'}, '7': {'0', '15'}, '8': {'1', '15'}, '9': {'2', '15'}},
                '15': {'0': {'7'}, '1': {'8'}, '2': {'9'}, '3': {'10'}, '4': {'11'}, '5': {'12'}, '6': {'13'},
                       '7': {'7'}, '8': {'8'}, '9': {'9'}},
                '16': {'0': {'16'}, '1': {'16'}, '2': {'16'}, '3': {'16'}, '4': {'16'}, '5': {'16'}, '6': {'16'},
                       '7': {'16'}, '8': {'16'}, '9': {'16'}}
            },
            initial_state='14',
            final_states={'0', '7'}
        )

        return nfa

    # Counts the number of integers that are weakly divisible by 7
    def count(self, _states, transitions, k, finalS):
        cur = []
        states = []
        numberOfStates = len(_states)

        next = [0 for i in range(0, numberOfStates)]

        for i in _states:
            # Fills the state array with all the keys needed to access the dictionary
            states.append(i)

        for l in range(0, len(states)):
            if states[l] in finalS:
                cur.append(1)
            else:
                cur.append(0)

        for x in range(0, k):
            for i in range(0, numberOfStates):
                row = self.getStates(states[i], transitions)
                place = []
                for pos, st in row.items():
                    for s in range(0, len(states)):
                        if st == states[s]:
                            place.append(s)
                next[i] = cur[place[0]] + cur[place[1]] + cur[place[2]] + cur[place[3]] + cur[place[4]] + cur[
                    place[5]] + cur[place[6]] + cur[place[7]] + cur[place[8]] + cur[place[9]]

            for j in range(0, numberOfStates):
                cur[j] = next[j]

            for h in range(0, numberOfStates):
                next[h] = 0

        return cur[847]

    # Uses the key to find the appropriate row of values
    def getStates(self, idx, transitions):
        for key, row in transitions.items():
            if idx == key:
                return row;


def main():
    # Builds instance of DFA
    d = converted_DFA()
    m = 0

    # Creating an options menu for user
    while m != 1 or m != 2 or m != 3:
        n = input(
            "Enter: \n"
            "1: Check single input\n"
            "2: Check file\n"
            "3: Exit\n")
        if n.isdigit():
            m = int(n)
        else:
            # Resets 'm' value in case of anything other than integers being given as input
            m = 0
            print("\n")

        # User chose single check
        if m == 1:
            k = 'empty'

            # Get the max size of the integers to be checked
            while k != "exit":
                k = input(
                    "Please provide a max size of integers to check or type 'exit' to return to previous menu: \n")

                # Checks to see if input is within the appropriate range
                if k.isdigit():
                    l = int(k)
                    if l < 21:
                        break
                    else:
                        print("At this time we are not checking integers that have more than 20 digits. Please "
                              "try again.\n")

                # Changes input to lower case so that if "exit" was typed it will be recognisable by the check
                else:
                    k = k.lower()
                    print("\n")

            # If appropriate range was entered continues with program
            if k.isdigit():
                k = int(k)
                # Counts the numbers weakly divisible by 7 based on the DFA
                weak_div = d.count(d.states, d.transitions, k, d.dfa_final_states)

                print("Total numbers of length: " + str(k) + " that are weakly divisible by 7 are: " + str(
                    weak_div) + "\n")
                k = input("Please provide a value k or type exit to return to previous menu: \n")

        # User wants to check all values in txt file
        elif m == 2:
            path = input(
                "Enter file location: \n")

            try:
                with open(path, "r") as num_file:
                    # Print the success message
                    print("File has opened for reading.\n")
                    numbers = num_file.read().split()
            # Raise error if the file is opened before
            except IOError:
                print("File has opened already.")

            # steps through all items in list. Checks to see if items are ints, if so typecasts to int
            for i in range(len(numbers)):
                if numbers[i].isdigit():
                    numbers[i] = int(numbers[i])
                else:
                    numbers[i] = 0

            # Checks to see if numbers are in range, if so, continues
            for number in numbers:
                if number <= 0:
                    print("Your list contained a value of 0, a negative number or a non-integer\n")
                elif number > 20:
                    print("Your file contains a number larger than 20. At this time we are not checking integers that"
                          " have more than 20 digits\n")
                else:
                    k = number
                    # Count the numbers weakly divisible by 7 based on the DFA
                    weak_div = d.count(d.states, d.transitions, k, d.dfa_final_states)

                    print("Total numbers of length " + str(k) + " that are weakly divisible by 7 are: " + str(
                        weak_div) + "\n")
                    num_file.close()
        elif m == 3:
            print("Exiting...")
            exit(0)


main()
