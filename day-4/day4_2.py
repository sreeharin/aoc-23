def main() -> None:
    cards: list[int] = []
    i = 0
    with open("input.txt", "r") as file:
        for line in file.readlines():
            card, numbers = line.split(":")
            winning, in_hand = numbers.split("|")
            matches = 0
            for num in in_hand.split():
                if num in winning.split():
                    matches += 1
            card_no = int(card.split()[-1])
            cards += winning_cards(card_no, matches)
            i += 1
            for num_times in range(0, cards.count(card_no)):
                cards += winning_cards(card_no, matches)
            cards += [card_no]

    print(len(cards))


def winning_cards(card_no: int, matches: int) -> list[int]:
    return [card_no + x for x in range(1, matches + 1)]


if __name__ == "__main__":
    main()
