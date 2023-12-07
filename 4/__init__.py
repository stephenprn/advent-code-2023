def main(test: bool = False):
    res = 0

    file_name = "input_test.txt" if test else "input.txt"

    with open(file_name, "r") as input_file:
        lines = input_file.readlines()

        for line in lines:
            line = line.strip()

            winning_numbers, draw_numbers = get_numbers(line)
            winners_numbers = set(winning_numbers) & set(draw_numbers)

            res += 2 ** len(winners_numbers)

    print(f"Result is: {str(res)}")


def main_two(test: bool = False):
    res = 0

    file_name = "input_test.txt" if test else "input.txt"
    queue = []

    with open(file_name, "r") as input_file:
        lines = input_file.readlines()

        for line in lines:
            line = line.strip()

            winning_numbers, draw_numbers = get_numbers(line)
            winners_len = len(set(winning_numbers) & set(draw_numbers))

            additionnal_cards = 0
            if queue:
                additionnal_cards = queue.pop(0)

            for i in range(winners_len):
                if not i < len(queue):
                    queue.append(0)

                queue[i] += additionnal_cards + 1

            res += additionnal_cards + 1

    print(f"Result is: {str(res)}")


def get_numbers(line: str):
    _, all_numbers_raw = line.split(":")
    winning_numbers_raw, draw_numbers_raw = all_numbers_raw.split("|")
    winning_numbers = [int(nbr) for nbr in winning_numbers_raw.strip().split()]
    draw_numbers = [int(nbr) for nbr in draw_numbers_raw.strip().split()]

    return winning_numbers, draw_numbers


if __name__ == "__main__":
    main_two()
