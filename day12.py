lines = open("data/day12.txt").read().splitlines()
graph = {s: [] for line in lines for s in line.split("-")}
for line in lines:
    [fro, to] = line.split("-")
    graph[fro].append(to)
    graph[to].append(fro)

def get_paths(graph, current_path=["start"], one_double_visit=False):
    current = current_path[-1]
    if "end" == current:
        yield current_path
    else:
        for n in graph[current]:
            if n[0].isupper() or n not in current_path: 
                yield from get_paths(graph, current_path+[n], one_double_visit)
            elif n != "start" and one_double_visit:
                yield from get_paths(graph, current_path+[n], False)

print(len([p for p in get_paths(graph)]))
print("part2")
print(len([p for p in get_paths(graph,one_double_visit=True)]))
