DIGIT_WORDS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
DIGIT_WORDS_REVERSED = {word[::-1]: num for word, num in DIGIT_WORDS.items()}


DIGIT_WORDS_FIRST_LETTER_MAP = {}
DIGIT_WORDS_FIRST_LETTER_MAP_REVERSED = {}

for word in DIGIT_WORDS.keys():
    first_letter = word[0]

    if not DIGIT_WORDS_FIRST_LETTER_MAP.get(first_letter):
        DIGIT_WORDS_FIRST_LETTER_MAP[first_letter] = []

    DIGIT_WORDS_FIRST_LETTER_MAP[first_letter].append(word)

for word in DIGIT_WORDS_REVERSED.keys():
    first_letter = word[0]

    if not DIGIT_WORDS_FIRST_LETTER_MAP_REVERSED.get(first_letter):
        DIGIT_WORDS_FIRST_LETTER_MAP_REVERSED[first_letter] = []

    DIGIT_WORDS_FIRST_LETTER_MAP_REVERSED[first_letter].append(word)


def main():
    res = 0

    with open("input.txt", "r") as input_file:
        for line in input_file:
            line_num = ""

            line_num += _get_first_num_char(line)
            line_num += _get_last_num_char(line)

            res += int(line_num)

    print(f"Result is: {str(res)}")


def _get_first_num_char(line: str) -> str:
    index_char = 0

    while True:
        current_char = line[index_char]

        if current_char.isdigit():
            return current_char

        for word in DIGIT_WORDS_FIRST_LETTER_MAP.get(current_char, []):
            if line[index_char:].startswith(word):
                return DIGIT_WORDS[word]

        index_char += 1


def _get_last_num_char(line: str) -> str:
    index_char = 0
    line_reversed = line[::-1]

    while True:
        current_char = line_reversed[index_char]

        if current_char.isdigit():
            return current_char

        for word in DIGIT_WORDS_FIRST_LETTER_MAP_REVERSED.get(current_char, []):
            if line_reversed[index_char:].startswith(word):
                return DIGIT_WORDS_REVERSED[word]

        index_char += 1


if __name__ == "__main__":
    main()
