import heapq
import numpy as np
from collections import namedtuple

lines = open("data/day15.txt").read().splitlines()

Point = namedtuple('Point', ('x', 'y'))
Node = namedtuple('Node', ('hcost', 'cost', 'pos'))


def neighbors(grid, x, y):
    if x > 0:
        yield Point(x-1, y)
    if x < len(grid[0])-1:
        yield Point(x+1, y)
    if y > 0:
        yield Point(x, y-1)
    if y < (len(grid)-1):
        yield Point(x, y+1)


def shortest_path(grid):
    goal = Point(len(grid[0])-1, len(grid)-1)
    q = []
    def h(p): return goal.x-p.x+goal.y-p.y
    mincost = {}
    start = Point(0, 0)
    heapq.heappush(q, Node(h(start), 0, start))
    mincost[start] = 0
    while len(q) > 0:
        node = heapq.heappop(q)
        if node.pos.x == goal.x and node.pos.y == goal.y:
            return node.cost
        (x, y) = node.pos
        for neighbor in neighbors(grid, x, y):
            cost = node.cost+grid[neighbor.y][neighbor.x]
            new_node = Node(h(neighbor)+cost, cost, neighbor)
            if new_node.pos not in mincost or mincost[new_node.pos] > new_node.cost:
                mincost[new_node.pos] = cost
                heapq.heappush(q, new_node)


def expand_grid(grid, n, m):
    a = np.array(grid)-1
    b = np.concatenate([a+i for i in range(n)])
    c = np.concatenate([b+i for i in range(m)], 1)
    return np.mod(c, 9)+1

grid = [[int(c) for c in line] for line in lines]
print(shortest_path(grid))
print("part 2")
print(shortest_path(expand_grid(grid, 5, 5)))
