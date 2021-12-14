import re

lines = open("data/day13.txt").read().splitlines()
br = lines.index("")
points = {tuple((int(c) for c in point.split(","))) for point in lines[:br]}
folds = [re.match('fold along (x|y)=(\d+)', line).groups()
         for line in lines[br+1:]]
folds = [(axis, int(val)) for (axis, val) in folds]


def fold(points, axis, at):
    return {((min(x, at)-max(0, x-at), y) if axis == 'x' else
             (x, min(y, at)-max(0, y-at))) for (x, y) in points}


(axis, at) = folds[0]
print(len(fold(points, axis, at)))

print("part 2")
print()

folded = points
for (axis, at) in folds:
    folded = fold(folded, axis, at)

for y in range(1+max(folded, key=lambda p: p[1])[1]):
    for x in range(1+max(folded, key=lambda p: p[0])[0]):
        print('█' if (x, y) in folded else ' ', end='')
    print()
    
