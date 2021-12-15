import heapq
import numpy as np
from collections import namedtuple

lines = open("data/day15.txt").read().splitlines()

Point = namedtuple('Point', ('x', 'y'))
Node = namedtuple('Node', ('hcost', 'cost', 'pos'))  # , 'visited'))

def neighbors(hmap, x, y):
    if x > 0:
        yield Point(x-1, y)
    if x < len(hmap[0])-1:
        yield Point(x+1, y)
    if y > 0:
        yield Point(x, y-1)
    if y < (len(hmap)-1):
        yield Point(x, y+1)

def shortest_path(grid):
    goal = Point(len(grid[0])-1, len(grid)-1)
    q = []
    def h(p): return goal.x-p.x+goal.y-p.y
    mincost = {}
    start = Point(0, 0)
    heapq.heappush(q, Node(h(start), 0, start))  # , {start}))
    mincost[start] = 0
    while len(q) > 0:
        node = heapq.heappop(q)
        if node.pos.x == goal.x and node.pos.y == goal.y:
            return node.cost
        (x, y) = node.pos
        for neighbor in neighbors(grid, x, y):
            # if neighbor in node.visited:
            #     continue
            cost = node.cost+grid[neighbor.y][neighbor.x]
            neighbor_node = Node(h(neighbor)+cost, cost, neighbor)
            # , node.visited | {neighbor})
            if neighbor_node.pos not in mincost or mincost[neighbor_node.pos] > neighbor_node.cost:
                mincost[neighbor_node.pos] = cost
                heapq.heappush(q, neighbor_node)


grid = [[int(c) for c in line] for line in lines]
print(shortest_path(grid))
print("part 2")
a = np.array(grid)-1
b = np.concatenate([a+i for i in range(5)])
c = np.concatenate([b+i for i in range(5)], 1)
c = np.mod(c, 9)+1
print(shortest_path(c))
