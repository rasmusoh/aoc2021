import copy

lines = open("data/day4.txt").read().splitlines()


def play(boards_left, numbers, nth=1):
    numbers = copy.copy(numbers)
    boards_left = copy.copy(boards_left)
    called_out = set()
    latest = -1
    i = 0
    while True:
        latest = numbers.pop(0)
        called_out.add(latest)
        bingos = check_bingo(boards_left, called_out)
        boards_left = [b for b in boards_left if b not in bingos]
        i += len(bingos)
        if i >= nth:
            left = [int(n) for row in bingos[0]
                    for n in row if n not in called_out]
            return sum(left)*int(latest)


def check_bingo(boards, called_out: set):
    bingos = []
    for board in boards:
        rowbingo = any([all([n in called_out for n in row]) for row in board])

        colbingo = any([all([n in called_out for n in column])
                       for column in zip(*board)])
        if rowbingo or colbingo:
            bingos.append(board)
    return bingos


numbers = lines[0].split(",")
n = 5
boards = []
for i in range(2, len(lines), n+1):
    boards.append([l.split() for l in lines[i:i + n]])


print("part 1")
print(play(boards, numbers))
print("part 2")
print(play(boards, numbers, len(boards)))
