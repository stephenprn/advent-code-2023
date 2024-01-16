from collections import OrderedDict
from typing import List
import sys
sys.setrecursionlimit(100000)

PIPES_EXPLORE_MAP = {
    '|': [[1, 0], [-1, 0]],
    '-': [[0, 1], [0, -1]],
    'L': [[-1, 0], [0, 1]],
    'J': [[-1, 0], [0, -1]],
    'W': [[1, 0], [0, -1]],
    'F': [[1, 0], [0, 1]],
    'S': [[1, 0], [-1, 0], [0, 1], [0, -1]]
}


class Main:
    def main(self, test: bool = False):
        file_name = "input_test.txt" if test else "input.txt"

        res = 0

        with open(file_name, "r") as input_file:
            lines = input_file.readlines()
            self.lines = [line.strip().replace('7', 'W') for line in lines]

            self.lines_with_dist = []
            for line in self.lines:
                self.lines_with_dist.append([None for char in self.lines[0]])

            self.index_line_max = len(self.lines) - 1
            self.index_char_max = len(self.lines[0]) - 1

            for index_line, line in enumerate(lines):
                for index_char, char in enumerate(line):
                    if char == 'S':
                        start_pos = [index_line, index_char]
                        break
            
            self.explore([start_pos[0] + 1, start_pos[1]], 1, start_pos)
            self.explore([start_pos[0] - 1, start_pos[1]], 1, start_pos)
            self.explore([start_pos[0], start_pos[1] + 1], 1, start_pos)
            self.explore([start_pos[0], start_pos[1] - 1], 1, start_pos)
                    
        self.print_map()
        self.print_max_dist()

    def explore(self, pos: [int, int], dist: int, previous_pos: [int, int] = None):
        index_line, index_char = pos

        char = self.lines[index_line][index_char]

        if previous_pos and char in ['.', 'S']:
            return

        dist_existing = self.lines_with_dist[index_line][index_char]
        if dist_existing and dist_existing < dist:
            return

        self.lines_with_dist[index_line][index_char] = dist

        for explore_indexes in PIPES_EXPLORE_MAP[char]:
            index_line_to_explore = index_line + explore_indexes[0]
            index_char_to_explore = index_char + explore_indexes[1]

            if index_line_to_explore < 0 or index_char_to_explore < 0 or index_line_to_explore > self.index_line_max or index_char_to_explore > self.index_char_max:
                continue

            new_pos = [index_line_to_explore, index_char_to_explore]

            if previous_pos and [index_line_to_explore, index_char_to_explore] == previous_pos:
                continue

            self.explore(new_pos, dist+1, pos)

    def print_max_dist(self):
        res = 0

        for dists in self.lines_with_dist:
            dists_ = [dist for dist in dists if dist]

            if not dists_:
                continue

            max_dist = max(dists_)

            if max_dist > res:
                res = max_dist

        print(f"{res=}")

    def print_map(self):
        print(f"=========DIST=========")
        for line in self.lines_with_dist:
            print(' '.join([str(dist or 0) for dist in line]))
        print(f"=====END=DIST=END=====")

        print(f"=========LINE=========")
        for line in self.lines:
            print(' '.join(line))
        print(f"=====END=LINE=END=====")

if __name__ == "__main__":
    Main().main()
