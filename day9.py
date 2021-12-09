import math
lines = open("data/day9.txt").read().rstrip().splitlines()
heightmap = [[int(c) for c in line] for line in lines]


def neighbors(hmap, x, y):
    n = []
    if x > 0:
        n.append((x-1, y))
    if x < len(hmap[0])-1:
        n.append((x+1, y))
    if y > 0:
        n.append((x, y-1))
    if y < (len(hmap)-1):
        n.append((x, y+1))
    return n


def get_low_points(hmap):
    low_points = []
    for y, row in enumerate(hmap):
        for x, value in enumerate(row):
            ns = neighbors(hmap, x, y)
            if all([hmap[ny][nx] > value for (nx, ny) in ns]):
                low_points.append((x, y))
    return low_points


def get_basin(hmap, x, y, low_points):
    if hmap[y][x] == 9:
        return None
    q = [(x, y)]
    while len(q) > 0:
        p = q.pop()
        if p in low_points:
            return p
        (x, y) = p
        ns = neighbors(hmap, x, y)
        for (nx, ny) in ns:
            if hmap[ny][nx] < hmap[y][x]:
                q.append((nx, ny))


def get_basins(hmap, low_points):
    basins = {p: [] for p in low_points}
    for y, row in enumerate(hmap):
        for x in range(len(row)):
            basin = get_basin(hmap, x, y, low_points)
            if basin:
                basins[basin].append((x, y))
    return basins.values()


low_points = get_low_points(heightmap)
print(sum([heightmap[y][x]+1 for (x, y) in low_points]))
print("part2")
basins = get_basins(heightmap, low_points)
lens = [len(b) for b in basins]
lens.sort(reverse=True)
print(math.prod(lens[0:3]))
