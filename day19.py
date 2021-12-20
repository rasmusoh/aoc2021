import itertools 

f = "data/day19.test.txt"
scans = [
    [tuple([int(c) for c in line.split(",")])
     for line in s.splitlines()[1:]]
    for s in open(f).read().split('\n\n')]
print(scans)

# for (a,b) in itertools.combinations(scans):
#     check_pair(a,b)

