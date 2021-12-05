
lines = open("data/day5.txt").read().splitlines()


def sign(n):
    if n == 0:
        return 0
    return 1 if n > 0 else -1


def get_crossings(count_diagonal=False):
    points = set()
    crossings = set()
    for line in lines:
        [fro, to] = line.split(" -> ")
        [from_x, from_y] = [int(i) for i in fro.split(",")]
        [to_x, to_y] = [int(i) for i in to.split(",")]
        if count_diagonal or from_x == to_x or from_y == to_y:
            dx = sign(to_x-from_x)
            dy = sign(to_y-from_y)
            n = max(abs(to_x-from_x), abs(to_y-from_y))+1
            for i in range(0, n):
                point = (from_x+dx*i, from_y+dy*i)
                if point in points:
                    crossings.add(point)
                else:
                    points.add(point)
    return crossings


print(len(get_crossings()))
print("part2")
print(len(get_crossings(True)))
