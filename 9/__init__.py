from collections import OrderedDict
from typing import List

def main(test: bool = False):
    file_name = "input_test.txt" if test else "input.txt"

    res = 0

    with open(file_name, "r") as input_file:
        lines = input_file.readlines()
        sequences = parse(lines)

        for sequence in sequences:
            current_seq = sequence

            while True:
                next_seq = []
                res += current_seq[-1]

                current_nbr = current_seq[0]

                for nbr in current_seq[1:]:
                    next_seq.append(nbr - current_nbr)
                    current_nbr = nbr

                if all(nbr == 0 for nbr in next_seq):
                    break
                
                current_seq = next_seq

    print(f"Result is: {res}")

def parse(lines):
    res = []

    for line in lines:
        line = line.strip()
        res.append([int(nbr) for nbr in line.split()])

    return res

def main_two(test: bool = False):
    file_name = "input_test.txt" if test else "input.txt"
    res = 0

    with open(file_name, "r") as input_file:
        lines = input_file.readlines()
        sequences = parse(lines)

        for sequence in sequences:
            current_seq = sequence
            first_nbrs = []

            while True:
                next_seq = []

                current_nbr = current_seq[0]

                for nbr in current_seq[1:]:
                    next_seq.append(nbr - current_nbr)
                    current_nbr = nbr

                first_nbrs.append(current_seq[0])
                if all(nbr == 0 for nbr in next_seq):
                    break
                
                current_seq = next_seq

            previous_nbr = 0

            for nbr in first_nbrs[::-1]:
                start_nbr = nbr - previous_nbr
                previous_nbr = start_nbr
                
            res += start_nbr

    print(f"Result is: {res}")


if __name__ == "__main__":
    main_two()
