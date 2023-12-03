RED = 12
GREEN = 13
BLUE = 14

score = 0

with open("input.txt", "r") as file:
    for line in file.readlines():
        game_id, rounds = line.split(":")
        valid = True
        for _round in rounds.split(";"):
            for cube in _round.split(","):
                num, color = cube.split()

                match color:
                    case "red":
                        if int(num) > RED:
                            valid = False
                    case "green":
                        if int(num) > GREEN:
                            valid = False
                    case "blue":
                        if int(num) > BLUE:
                            valid = False

        _id = game_id.split()[1]
        if valid:
            score += int(_id)

print(score)
