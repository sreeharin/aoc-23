_total = 0

with open("input.txt", "r") as file:
    for line in file.readlines():
        game, rounds = line.split(":")

        red = green = blue = 0
        for _round in rounds.split(";"):
            for cube in _round.split(","):
                count, color = cube.split()
                count = int(count)

                match color:
                    case "red":
                        if count > red:
                            red = count
                    case "green":
                        if count > green:
                            green = count
                    case "blue":
                        if count > blue:
                            blue = count
        res = red * green * blue
        _total += res

print(_total)
