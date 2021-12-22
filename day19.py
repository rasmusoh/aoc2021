import numpy as np
import itertools


def get_rotations(scan):
    # x, y, z = scan[:, 0], scan[:, 1], scan[:, 2]
    # for first in [x, -x, y, -y, z, -z]:
    # rotm = np.array([[1 s
    # b = np.matmul(scan
    yield scan


f = "data/day19.test.txt"
scans = [
    np.array([[int(c) for c in line.split(",")]
              for line in s.splitlines()[1:]], dtype=np.int32)
    for s in open(f).read().split('\n\n')]


solved = scans[0]
solved_set = set([tuple(row) for row in solved])
free = [list(get_rotations(scan)) for scan in scans[1:]]
for i, scan in enumerate(free):
    for rotation in scan:
        pairs = [(a, b) for a in solved for b in rotation]
        for a, b in pairs:
            offset = b-a
            b_set = set([tuple(row-offset) for row in solved])
            count = len(solved_set & b_set)
            if count >= 12:
                print(i)
