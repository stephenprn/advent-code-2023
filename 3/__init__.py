def main():
    res = 0

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        nbr_lines = len(lines)

        for line_index, line in enumerate(lines):
            line = line.strip()
            index = 0

            while True:
                if len(line) == index:
                    break

                char = line[index]

                if not char.isdigit():
                    index += 1
                    continue

                is_adjacent = False

                num = ""

                for num_char in line[index:]:
                    if not num_char.isdigit():
                        break

                    num += num_char

                # check symbols same line
                if index != 0 and line[index - 1] != ".":
                    is_adjacent = True

                index_right = index + len(num)
                if (
                    not is_adjacent
                    and index_right != len(line)
                    and line[index_right] != "."
                ):
                    is_adjacent = True

                index_left_adjacent_line = max(0, index - 1)
                index_right_adjacent_line = min(index + len(num) + 1, len(line) - 1)

                # check symbols line top
                if not is_adjacent and line_index != 0:
                    string_top = lines[line_index - 1][
                        index_left_adjacent_line:index_right_adjacent_line
                    ]
                    is_adjacent = _string_contains_symbol(string_top)

                # check symbols line bottom
                index_bottom = line_index + 1
                if not is_adjacent and index_bottom != nbr_lines:
                    string_bottom = lines[index_bottom][
                        index_left_adjacent_line:index_right_adjacent_line
                    ]
                    is_adjacent = _string_contains_symbol(string_bottom)
                if is_adjacent:
                    res += int(num)

                index += len(num)

    print(f"Result is: {str(res)}")


def _string_contains_symbol(string: str) -> bool:
    for char in string:
        if char != "." and not char.isdigit():
            return True

    return False


def main_two():
    res = 0

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        nbr_lines = len(lines)

        for line_index, line in enumerate(lines):
            line = line.strip()
            index = 0

            while True:
                if len(line) == index:
                    break

                char = line[index]

                if char != "*":
                    index += 1
                    continue

                adjacents = []

                # adjacent left
                adjacent_left = _get_number_left_direction(line, index - 1)

                if adjacent_left:
                    adjacents.append(adjacent_left)

                # adjacent right
                adjacent_right = _get_number_right_direction(line, index + 1)

                if adjacent_right:
                    adjacents.append(adjacent_right)

                # top and bottom lines

                # adjacents top

                if line_index != 0:
                    adjacents += _get_numbers_adjacent_lines(
                        lines[line_index - 1], index
                    )

                # adjacents bottom
                index_bottom = line_index + 1
                if index_bottom != nbr_lines:
                    adjacents += _get_numbers_adjacent_lines(lines[index_bottom], index)

                if len(adjacents) == 2:
                    res += adjacents[0] * adjacents[1]

                index += 1

    print(f"Result is: {str(res)}")


def _get_numbers_adjacent_lines(line, index):
    index_left = max(0, index - 1)
    index_right = min(index + 1, len(line) - 1)
    adjacents = []

    # we have to get the first digit on the left
    if line[index_left:index_right].isdigit() or line[index_left].isdigit():
        index_start = index_left

        while index_start > 0:
            if not line[index_start - 1].isdigit():
                break

            index_start -= 1

        adjacents.append(_get_number_right_direction(line, index_start))

        if line[index_left:index_right].isdigit():
            return adjacents

    if (
        line[index].isdigit()
        and not line[index_right].isdigit()
        and not line[index_left].isdigit()
    ):
        adjacents.append(int(line[index]))
        return adjacents

    if line[index_right].isdigit():
        if line[index].isdigit():
            adjacents.append(_get_number_right_direction(line, index))
        else:
            adjacents.append(_get_number_right_direction(line, index_right))

    return adjacents


def _get_number_left_direction(line, index):
    adjacent_left_reversed = ""

    while index >= 0 and line[index].isdigit():
        adjacent_left_reversed += line[index]
        index -= 1

    return int(adjacent_left_reversed[::-1]) if adjacent_left_reversed else None


def _get_number_right_direction(line, index):
    adjacent_right = ""

    while index < len(line) and line[index].isdigit():
        adjacent_right += line[index]
        index += 1

    return int(adjacent_right) if adjacent_right else None


if __name__ == "__main__":
    # main()
    main_two()
