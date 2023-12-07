import math
from typing import Dict, List


def main(test: bool = False):
    file_name = "input_test.txt" if test else "input.txt"

    with open(file_name, "r") as input_file:
        lines = input_file.readlines()

        seeds = [int(seed) for seed in lines[0].split(":")[1].split()]

        # extract map entries

        all_maps_parsed = []
        current_map_lines = []

        for line in lines[2::]:
            line = line.strip()

            if line.endswith("map:"):
                continue

            if line == "":
                all_maps_parsed.append(parse_map(current_map_lines))
                current_map_lines = []
                continue

            current_map_lines.append(line)

        all_maps_parsed.append(parse_map(current_map_lines))

    min_location = None

    for seed in seeds:
        current_value = seed

        for map_parsed in all_maps_parsed:
            current_value = convert_elt(current_value, map_parsed)

        if not min_location or current_value < min_location:
            min_location = current_value

    print(f"Result is: {min_location}")


def main_two(test: bool = False):
    file_name = "input_test.txt" if test else "input.txt"

    with open(file_name, "r") as input_file:
        lines = input_file.readlines()

        seeds_data = [int(seed) for seed in lines[0].split(":")[1].split()]
        seeds_intervals = get_seeds_intervals(seeds_data)

        # extract map entries

        all_maps_parsed = []
        current_map_lines = []

        for line in lines[2::]:
            line = line.strip()

            if line.endswith("map:"):
                continue

            if line == "":
                all_maps_parsed.append(parse_map(current_map_lines))
                current_map_lines = []
                continue

            current_map_lines.append(line)

        all_maps_parsed.append(parse_map(current_map_lines))

    min_location = math.inf

    seeds_intervals = clean_intervals(seeds_intervals)

    for map_parsed in all_maps_parsed:
        for seed_interval in seeds_intervals:
            for seed in list(range(seed_interval[0], seed_interval[1] + 1)):
                current_value = seed

                current_value = convert_elt(current_value, map_parsed)

                if current_value < min_location:
                    min_location = current_value

    print(f"Result is: {min_location}")


def parse_map(lines: List[str]):
    res = {"intervals": [], "factors": []}

    for line in lines:
        destination, source, nbr = [int(n) for n in line.split()]
        res["intervals"].append([source, source + nbr - 1])
        res["factors"].append(destination - source)

    return res


def convert_elt(elt: int, parsed_map: Dict):
    for index, interval in enumerate(parsed_map["intervals"]):
        if elt >= interval[0] and elt <= interval[1]:
            return elt + parsed_map["factors"][index]

    return elt


def get_seeds_intervals(seeds_data: List[int]):
    res = []

    for i in range(0, len(seeds_data), 2):
        start_seed = seeds_data[i]
        res.append([start_seed, start_seed + seeds_data[i + 1] - 1])

    return res


def clean_intervals(intervals: List[List[int]]):
    # Sort the array on the basis of start values of intervals.
    intervals.sort()
    stack = []
    # insert first interval into stack
    stack.append(intervals[0])
    for i in intervals[1:]:
        # Check for overlapping interval,
        # if interval overlap
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)

    return stack


if __name__ == "__main__":
    main_two()
