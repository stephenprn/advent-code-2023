from collections import OrderedDict
from typing import List

CARD_VALUES_HEX_VALUES_MAP = OrderedDict([
    ('A', 'd'),
    ('K', 'c'),
    ('Q', 'b'),
    ('J', 'a'),
    ('T', '9'),
    ('9', '8'),
    ('8', '7'),
    ('7', '6'),
    ('6', '5'),
    ('5', '4'),
    ('4', '3'),
    ('3', '2'),
    ('2', '1')

])
CARDS_ORDERED = [
    card for card in reversed(CARD_VALUES_HEX_VALUES_MAP.keys())
]


def main(test: bool = False):
    file_name = "input_test.txt" if test else "input.txt"

    with open(file_name, "r") as input_file:
        lines = input_file.readlines()

        bids_scores = []

        for line in lines:
            hand, bid = parse_line(line)
            score = compute_score(hand)
            bids_scores.append(
                (bid, score)
            )

    res = 0
    for index, bid_score in enumerate(sorted(bids_scores, key=lambda bid_score: int(bid_score[1], 16))):
        res += (index + 1) * bid_score[0]

    print(f"Result is: {res}")


def parse_line(line: str):
    hand, bid = line.split()

    return hand, int(bid)


def compute_score(hand: str):
    # count cards
    cards_count = {
        card: 0 for card in CARD_VALUES_HEX_VALUES_MAP.keys()
    }

    for card in hand:
        cards_count[card] += 1

    cards_counts = [
        (card, count) for card, count in cards_count.items()
    ]
    cards_counts = sorted(cards_counts, key=lambda card_count: (
        card_count[1], CARDS_ORDERED.index(card_count[0])), reverse=True)

    highest_occurences = cards_counts[0][1]
    highest_occurences_card = cards_counts[0][0]

    if highest_occurences == 5:
        return f'{CARD_VALUES_HEX_VALUES_MAP[highest_occurences_card]}00000000000'

    if highest_occurences == 4:
        remaing_card_value = cards_counts[1][0]
        return f'0{CARD_VALUES_HEX_VALUES_MAP[highest_occurences_card]}000000000{CARD_VALUES_HEX_VALUES_MAP[remaing_card_value]}'

    if highest_occurences == 3:
        # full house
        if cards_counts[1][1] == 2:
            pair_card_value = cards_counts[1][0]
            return f'00{CARD_VALUES_HEX_VALUES_MAP[highest_occurences_card]}000{CARD_VALUES_HEX_VALUES_MAP[pair_card_value]}00000'

        # three of kind
        return f'00{CARD_VALUES_HEX_VALUES_MAP[highest_occurences_card]}0000000{CARD_VALUES_HEX_VALUES_MAP[cards_counts[1][0]]}{CARD_VALUES_HEX_VALUES_MAP[cards_counts[2][0]]}'

    if highest_occurences == 2:
        # two pairs
        if cards_counts[1][1] == 2:
            other_pair_value = cards_counts[1][0]
            remainig_card_value = cards_counts[2][0]
            return f'000{CARD_VALUES_HEX_VALUES_MAP[highest_occurences_card]}{CARD_VALUES_HEX_VALUES_MAP[other_pair_value]}000000{CARD_VALUES_HEX_VALUES_MAP[remainig_card_value]}'

        # one pairs
        return f'000{CARD_VALUES_HEX_VALUES_MAP[highest_occurences_card]}00000{CARD_VALUES_HEX_VALUES_MAP[cards_counts[1][0]]}{CARD_VALUES_HEX_VALUES_MAP[cards_counts[2][0]]}{CARD_VALUES_HEX_VALUES_MAP[cards_counts[3][0]]}'

    return f'0000000{CARD_VALUES_HEX_VALUES_MAP[cards_counts[0][0]]}{CARD_VALUES_HEX_VALUES_MAP[cards_counts[1][0]]}{CARD_VALUES_HEX_VALUES_MAP[cards_counts[2][0]]}{CARD_VALUES_HEX_VALUES_MAP[cards_counts[3][0]]}{CARD_VALUES_HEX_VALUES_MAP[cards_counts[4][0]]}'


def main_two(test: bool = False):
    file_name = "input_test.txt" if test else "input.txt"

    res = 0

    with open(file_name, "r") as input_file:
        lines = input_file.readlines()

    print(f"Result is: {res}")


if __name__ == "__main__":
    main(True)
