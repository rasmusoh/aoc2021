import numpy as np
from collections import defaultdict
import itertools
import math


def get_rot_matrices():
    def cos(d): return int(round(math.cos(d*math.pi/2)))
    def sin(d): return int(round(math.sin(d*math.pi/2)))
    r1s = []
    for i in range(4):
        r1s.append(np.array([[cos(i), 0, sin(i)], [0, 1, 0],
                   [-sin(i), 0, cos(i)]], dtype=np.int32))
    r1s.append(np.array(
        [[cos(1), -sin(1), 0], [sin(1), cos(1), 0], [0, 0, 1]], dtype=np.int32))
    r1s.append(np.array([[cos(-1), -sin(-1), 0],
               [sin(-1), cos(-1), 0], [0, 0, 1]], dtype=np.int32))
    r2s = []
    for i in range(4):
        r2s.append(np.array([[1, 0, 0], [0, cos(i), -sin(i)],
                   [0, sin(i), cos(i)]], dtype=np.int32))
    return [np.matmul(r1, r2) for r1, r2 in itertools.product(r1s, r2s)]


rotation_matrices = get_rot_matrices()


def get_rotations(scan):
    for rot in rotation_matrices:
        yield np.matmul(scan, rot)


def find_offset(solved, scan):
    for rotation in scan:
        pairs = [(a, b) for a in solved for b in rotation]
        offsets = defaultdict(lambda: 0)
        for a, b in pairs:
            offset = tuple(b-a)
            offsets[offset] += 1
            if offsets[offset] >= 12:
                return np.asarray(offset), rotation-offset
    return None


def solve(scans):
    solved = [scans[0]]
    free = [list(get_rotations(scan)) for scan in scans[1:]]
    s = 0
    offsets = []
    while len(free) > 0:
        for f in reversed(range(len(free))):
            result = find_offset(solved[s], free[f])
            if result is not None:
                offset, from_perspective = result
                solved.append(from_perspective)
                offsets.append(offset)
                del free[f]
        s += 1
    pointset = set()
    for scan in solved:
        for point in scan:
            pointset.add(tuple(point))
    print(len(pointset))
    print("part 2")
    print(max([np.sum(np.abs(a-b))
          for a, b in itertools.combinations(offsets, 2)]))


def parse(contents):
    return [
        np.array([[int(c) for c in line.split(",")]
                  for line in s.splitlines()[1:]], dtype=np.int32)
        for s in contents.split('\n\n')]


a = np.array([[-1, -1, 1],
              [-2, -2, 2],
              [-3, -3, 3],
              [-2, -3, 1],
              [5, 6, -4],
              [8, 0, 7]])
scans = parse(open("data/day19.test.txt").read())
solve(scans)
