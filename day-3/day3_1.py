from collections import namedtuple

Number = namedtuple("Number", ["number", "start", "end"])


def main():
    numbers = []
    part_numbers = []

    with open("input.txt", "r") as file:
        input_data = file.readlines()

    for line in input_data:
        numbers.append(find_numbers(line))

    for line_idx, line in enumerate(input_data):
        for symbol_idx, char in enumerate(line.strip()):
            if not char.isdigit() and char != ".":
                # Search adjacent numbers
                pos = [-1, 0, 1]
                for x in pos:
                    res = find_adjacent(numbers[line_idx + x], symbol_idx)
                    if res:
                        for res_number in res:
                            part_numbers.append(res_number.number)

    print(sum(part_numbers))


def find_numbers(line: str) -> list[Number]:
    """Find and return a list of numbers from line if it exists.

    >>> find_numbers("467..114..")
    [Number(number=467, start=0, end=2), Number(number=114, start=5, end=7)]
    >>> find_numbers("..35...633")
    [Number(number=35, start=2, end=3), Number(number=633, start=7, end=9)]
    """

    numbers: list[Number] = []

    temp_num = ""
    start = end = -1
    for idx, char in enumerate(line):
        if char.isdigit():
            temp_num = "".join([temp_num, char])
            if start == -1:
                start = idx
            end = idx
        else:
            if temp_num:
                numbers.append(Number(int(temp_num), start, end))
                start = end = -1
                temp_num = ""
    if temp_num:
        numbers.append(Number(int(temp_num), start, end))

    return numbers


def find_adjacent(numbers: list[Number], idx: int) -> list[Number]:
    """
    Finds `Number` which satisfies any of the condition
    a. `idx` is between 'start' and 'stop'
    b. `idx`+1 = start or `idx`-1 = stop

    >>> find_adjacent([Number(number=467, start=0, end=2), Number(number=114, start=5, end=7)], 3)
    [Number(number=467, start=0, end=2)]
    """

    matches = []
    for number in numbers:
        if idx >= number.start and idx <= number.end:
            matches.append(number)
        elif number.start == idx + 1 or number.end == idx - 1:
            matches.append(number)

    return matches


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main()
