import heapq
from collections import namedtuple

Pod = namedtuple('Pod', ('kind', 'x', 'y', 'done'))
Node = namedtuple('Node', ('hcost', 'cost', 'state'))

unit_costs = {"A": 1, "B": 10, "C": 100, "D": 1000}
goal_room = {"A": 3, "B": 5, "C": 7, "D": 9}
allowed = [1, 2, 4, 6, 8, 10, 11]
width = 12


def room_free(grid, kind, depth):
    free = True
    room_x = goal_room[kind]
    for i in range(1, depth+1):
        free = free and (grid[i][room_x] == '.' or grid[i][room_x] == kind)
    return free


def hallway_free(grid, from_x, to_x):
    if from_x > to_x:
        return all([x == '.' for x in grid[0][to_x:from_x]])
    else:
        return all([x == '.' for x in grid[0][from_x+1:to_x+1]])


def way_out(pod, grid):
    return all([grid[i][pod.x] == '.' for i in range(pod.y)])


def move_cost(pod, to_x, to_y):
    dist = abs(pod.y-to_y) + abs(pod.x-to_x)
    return unit_costs[pod.kind] * dist


def neighbors(state, grid, depth):
    for i, pod in enumerate(state):
        if pod.done:
            continue
        if pod.y == 0:
            goal_x = goal_room[pod.kind]
            if hallway_free(grid, pod.x, goal_x) and room_free(grid, pod.kind, depth):
                newstate = list(state)
                new_y = depth
                while grid[new_y][goal_x] != '.':
                    new_y -= 1
                newstate[i] = Pod(pod.kind, goal_x, new_y, True)
                yield newstate, move_cost(pod, goal_x, new_y)
        elif way_out(pod, grid):
            for x in allowed:
                if hallway_free(grid, pod.x, x):
                    newstate = list(state)
                    new_y = 0
                    newstate[i] = Pod(pod.kind, x, new_y, False)
                    yield newstate, move_cost(pod, x, new_y)


def h(state):
    total = 0
    for pod in state:
        if goal_room[pod.kind] != pod.x:
            dist = pod.y+1 + abs(pod.x-goal_room[pod.kind])
            total += unit_costs[pod.kind] * dist
    return total


def get_grid(state, depth):
    grid = [['.']*width for _ in range(1+depth)]
    for pod in state:
        grid[pod.y][pod.x] = pod.kind

    return grid


def shortest_path(start, depth):
    mincost = {}
    q = []
    heapq.heappush(q, Node(h(start), 0, start))
    while len(q) > 0:
        node = heapq.heappop(q)
        if all([goal_room[pod.kind] == pod.x for pod in node.state]):
            return node.cost
        grid = get_grid(node.state, depth)
        for neighbor, cost in neighbors(node.state, grid, depth):
            totcost = node.cost+cost
            new_node = Node(h(neighbor) +
                            totcost, totcost, neighbor)
            new_node_set = tuple(new_node.state)
            if new_node_set not in mincost or mincost[new_node_set] > new_node.cost:
                mincost[new_node_set] = cost
                heapq.heappush(q, new_node)


def parse(lines, depth):
    start_state = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in unit_costs.keys():
                done = (goal_room[c] == x and y == depth)
                start_state.append(Pod(c, x, y, done))
    return start_state


lines = open("data/day23.txt").read().splitlines()[1:]

print(shortest_path(parse(lines, 2), 2))
print("part 2")
start = parse(lines[:2] + ["  #D#C#B#A#", "  #D#B#A#C#"]+lines[2:], 4)
print(shortest_path(start, 4))
