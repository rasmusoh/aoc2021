lines = open("data/day11.txt").read().splitlines()


def neighbors(grid, x, y):
    return [(nx, ny) for nx in range(x-1, x+2)
            for ny in range(y-1, y+2)
            if nx >= 0 and nx < len(grid[0])
            and ny >= 0 and ny < len(grid)
            and not (ny == y and nx == x)]


def simulate_step(grid):
    flashcount = 0
    flashqueue = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] += 1
            if grid[y][x] > 9:
                flashqueue.append((x, y))
    flashes = set()
    while len(flashqueue) > 0:
        cell = flashqueue.pop()
        if cell not in flashes:
            flashes.add(cell)
            for (x, y) in neighbors(grid, cell[0], cell[1]):
                grid[y][x] += 1
                if grid[y][x] > 9:
                    flashqueue.append((x, y))
    for (x, y) in flashes:
        flashcount += 1
        grid[y][x] = 0
    return flashcount


grid = [[int(c) for c in line] for line in lines]
steps = 100
total_flashes = 0
for i in range(steps):
    total_flashes += simulate_step(grid)
print(total_flashes)
print("part 2")

grid = [[int(c) for c in line] for line in lines]
i = 0
last_flashcount = 0
while last_flashcount < len(grid)*len(grid[0]):
    i += 1
    last_flashcount = simulate_step(grid)
print(i)
