COLOR_MAX_MAP = {"red": 12, "green": 13, "blue": 14}


def main():
    res = 0

    with open("input.txt", "r") as input_file:
        for line in input_file:
            game_with_id_raw, sets_raw = line.split(":")

            if _is_set_possible(sets_raw):
                res += int(game_with_id_raw.split(" ")[1])

    print(f"Result is: {str(res)}")


def main_two():
    res = 0

    with open("input.txt", "r") as input_file:
        for line in input_file:
            sets_raw = line.split(":")[1]

            res += _get_power(sets_raw)

    print(f"Result is: {str(res)}")


def _is_set_possible(sets_raw: str):
    for set_raw in sets_raw.strip().split(";"):
        for nbr_with_color_raw in set_raw.split(","):
            for color, max_nbr in COLOR_MAX_MAP.items():
                if nbr_with_color_raw.endswith(color):
                    if int(nbr_with_color_raw[: -len(color)]) > max_nbr:
                        return False
                    break

    return True


def _get_power(sets_raw: str):
    colors_map = {"red": 0, "green": 0, "blue": 0}

    for set_raw in sets_raw.strip().split(";"):
        for nbr_with_color_raw in set_raw.split(","):
            for color, max_nbr in COLOR_MAX_MAP.items():
                if nbr_with_color_raw.endswith(color):
                    nbr = int(nbr_with_color_raw[: -len(color)])

                    if colors_map.get(color) < nbr:
                        colors_map[color] = nbr
                    break

    return colors_map["blue"] * colors_map["green"] * colors_map["red"]


if __name__ == "__main__":
    # main()
    main_two()
