lines = open("data/day12.txt").read().splitlines()
graph = {s: [] for line in lines for s in line.split("-")}
for line in lines:
    [fro, to] = line.split("-")
    graph[fro].append(to)
    graph[to].append(fro)


def get_paths(graph, path=["start"], one_double_visit=False):
    current = path[-1]
    if "end" == current:
        yield path
        return
    for node in graph[current]:
        if node[0].isupper() or node not in path:
            yield from get_paths(graph, path+[node], one_double_visit)
        elif node != "start" and one_double_visit:
            yield from get_paths(graph, path+[node], False)


print(len([p for p in get_paths(graph)]))
print("part2")
print(len([p for p in get_paths(graph, one_double_visit=True)]))
