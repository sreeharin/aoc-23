_sum = 0
with open("input.txt", "r") as file:
    for line in file.readlines():
        points = 0
        card, numbers = line.split(":")
        winning, in_hand = numbers.split("|")
        for num in in_hand.split():
            if num in winning.split():
                if not points:
                    points = 1
                else:
                    points *= 2
        _sum += points
print(_sum)
