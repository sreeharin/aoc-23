_sum = 0

with open('input.txt', 'r') as file:
    for line in file.readlines():
        first = last = -1
        for char in line:
            if char.isdigit():
                if first == -1:
                    first = int(char)
                last = int(char)
        res = first * 10 + last
        _sum += res

print(_sum)
