import re
from collections import namedtuple

Step = namedtuple("Step", ("on", "bounds"))
Cuboid = namedtuple("Cuboid", ("x1", "x2", "y1", "y2", "z1", "z2"))
# oint = namedtuple("Step", ("x", "y", "z"))
Node = namedtuple("Node", ("bounds", "children"))


def parse(line):
    m = re.match(
        r"(\S+) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)", line)
    if m == None:
        raise ValueError("invalid line")
    groups = m.groups()
    return Step(groups[0] == 'on', Cuboid(*[int(d) for d in groups[1:]]))


def within(cube1, cube2):
    return (cube2.x1 <= cube1.x1 <= cube2.x2 and
            cube2.x1 <= cube1.x2 <= cube2.x2 and
            cube2.y1 <= cube1.y1 <= cube2.y2 and
            cube2.y1 <= cube1.y2 <= cube2.y2 and
            cube2.z1 <= cube1.z1 <= cube2.z2 and
            cube2.z1 <= cube1.z2 <= cube2.z2)


def apart(cube1, cube2):
    return (cube1.x1 > cube2.x2 or cube2.x1 > cube1.x2 or
            cube1.y1 > cube2.y2 or cube2.y1 > cube1.y2 or
            cube1.z1 > cube2.z2 or cube2.z1 > cube1.z2)


def volume(cube):
    x1, x2, y1, y2, z1, z2 = cube
    return (x2-x1+1) * (y2-y1+1) * (z2-z1+1)


def intersect(cube1, cube2):
    x1, x2, y1, y2, z1, z2 = cube1
    rest = []
    if cube2.x1 > x1:
        rest.append(Cuboid(x1, cube2.x1-1, y1, y2, z1, z2))
    if cube2.x2 < x2:
        rest.append(Cuboid(cube2.x2+1, x2, y1, y2, z1, z2))
    ix1, ix2 = max(cube2.x1, x1), min(cube2.x2, x2)
    if cube2.y1 > y1:
        rest.append(Cuboid(ix1, ix2, y1, cube2.y1-1, z1, z2))
    if cube2.y2 < y2:
        rest.append(Cuboid(ix1, ix2, cube2.y2+1, y2, z1, z2))
    iy1, iy2 = max(cube2.y1, y1), min(cube2.y2, y2)
    if cube2.z1 > z1:
        rest.append(Cuboid(ix1, ix2, iy1, iy2, z1, cube2.z1-1))
    if cube2.z2 < z2:
        rest.append(Cuboid(ix1, ix2, iy1, iy2, cube2.z2+1, z2))
    iz1, iz2 = max(cube2.z1, z1), min(cube2.z2, z2)
    return Cuboid(ix1, ix2, iy1, iy2, iz1, iz2), rest


def insert(node, cube, flip):
    inserts = [cube]
    while len(inserts) > 0:
        cube = inserts.pop()
        split = False
        for i in reversed(range(len(node.children))):
            child = node.children[i]
            if apart(cube, child.bounds):
                continue
            elif within(child.bounds, cube):
                del node.children[i]
            else:
                intersection, rest = intersect(cube, child.bounds)
                insert(child, intersection, not flip)
                for new_cube in rest:
                    inserts.append(new_cube)
                split = True
                break 
        if flip and not split:
            node.children.append(Node(cube, []))


def count(node):
    return volume(node.bounds) - sum([count(child) for child in node.children])


lines = open("data/day22.txt").read().splitlines()
steps = [parse(line) for line in lines]
root = Node(Cuboid(0, -1, 0, -1, 0, -1), [])
init_bounds = Cuboid(-50, 50, -50, 50, -50, 50)
for step in steps:
    if apart(step.bounds, init_bounds):
        continue
    bounds = intersect(step.bounds,init_bounds)[0]
    insert(root, bounds, step.on)
print(count(root))
print("part 2")
root = Node(Cuboid(0, -1, 0, -1, 0, -1), [])
init_bounds = Cuboid(-50, 50, -50, 50, -50, 50)
for step in steps:
    insert(root, step.bounds, step.on)
print(count(root))
