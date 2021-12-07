crabs = [int(c)
         for c in open("data/day7.txt").read().rstrip().split(",")]


def fuel_cost_p2(dist):
    return sum(range(abs(dist)+1))

print(min([sum([abs(c-i) for c in crabs])
      for i in range(min(crabs), max(crabs))]))

print("part 2")

print(min([sum([fuel_cost_p2(c-i) for c in crabs])
      for i in range(min(crabs), max(crabs))]))
