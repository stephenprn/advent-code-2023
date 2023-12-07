from typing import List


def main(test: bool = False):
    file_name = "input_test.txt" if test else "input.txt"

    res = 1

    with open(file_name, "r") as input_file:
        lines = input_file.readlines()
        times, distances = parse(lines)

        for time, distance in zip(times, distances):
            possible_distances = get_possible_distances(time)
            nbr_winnings = len([dist for dist in possible_distances if dist > distance])
            res *= nbr_winnings

    print(f"Result is: {res}")


def main_two(test: bool = False):
    file_name = "input_test.txt" if test else "input.txt"

    res = 0

    with open(file_name, "r") as input_file:
        lines = input_file.readlines()
        time, distance = parse_two(lines)

        possible_distances = get_possible_distances(time)
        nbr_winnings = len([dist for dist in possible_distances if dist > distance])
        res = nbr_winnings

    print(f"Result is: {res}")


def parse(lines: List[str]):
    times = [int(nbr) for nbr in lines[0].strip().split(":")[1].split()]
    distances = [int(nbr) for nbr in lines[1].strip().split(":")[1].split()]

    return times, distances


def parse_two(lines: List[str]):
    time = int("".join(lines[0].strip().split(":")[1].split()))
    distance = int("".join(lines[1].strip().split(":")[1].split()))

    return time, distance


def get_possible_distances(time: int):
    res = []

    holding_time = 0

    while holding_time <= time:
        moving_time = time - holding_time

        res.append(moving_time * holding_time)

        holding_time += 1

    return res


if __name__ == "__main__":
    main_two()
