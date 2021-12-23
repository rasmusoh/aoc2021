

def start_ranges(pixels):
    xs = [x for (x, _) in pixels]
    ys = [y for (_, y) in pixels]
    min_x = min(xs)
    max_x = max(xs)+1
    min_y = min(ys)
    max_y = max(ys)+1
    return min_x, max_x, min_y, max_y


def enhance(dots, algo, n):
    min_x, max_x, min_y, max_y = start_ranges(dots)
    outside_lit = False
    for _ in range(n):
        min_x -= 1
        max_x += 1
        min_y -= 1
        max_y += 1

        def is_outside(x, y):
            return x <= min_x or x >= max_x or y <= min_y or y >= max_y
        next_dots = set()
        for y in range(min_y-1, max_y+1):
            for x in range(min_x-1, max_x+1):
                v = 0
                for i in reversed(range(3)):
                    for j in reversed(range(3)):
                        px, py = x+1-i, y+1-j
                        if (px, py) in dots or (outside_lit and is_outside(px, py)):
                            exp = (i+3*j)
                            v |= (1 << exp)
                val = algo[v]
                if val:
                    next_dots.add((x, y))
                    # print("#", end="")
                # else:
                    # print(".", end="")
            # print()
        # print()
        outside_lit = algo[-1] if outside_lit else algo[0]
        dots = next_dots
    return dots


algostring, imagestring = open("data/day20.txt").read().split("\n\n")
dots = set()
for y, row in enumerate(imagestring.splitlines()):
    for x, char in enumerate(row):
        if char == "#":
            dots.add((x, y))
algo = [c == "#" for c in algostring]

print(len(enhance(dots, algo, 2)))
print("day 2")
print(len(enhance(dots, algo, 50)))
