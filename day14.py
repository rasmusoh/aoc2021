from collections import defaultdict

lines = open("data/day14.test.txt").read().splitlines()
start = lines[0]
rules = {}
for line in lines[2:]:
    [pair, inserted] = line.split(" -> ")
    [a, b] = pair
    rules[pair] = a+inserted+b

print(rules)
def process(polymer):
    if len(polymer) < 2:
        return ""
    if polymer in rules:
        return rules[polymer]
    elif len(polymer) % 2== 0:
        mid = len(polymer)//2
        p1 = process(polymer[:mid])
        p2 = rules[polymer[mid-1:mid+1]]
        p3 = process(polymer[mid:])
        res = p1+p2[1]+p3
        rules[polymer]=res
        return res
    else:
        mid = len(polymer)//2
        p1 = process(polymer[:mid+1])
        p2 = process(polymer[mid:])
        res = p1[:-1]+p2
        rules[polymer]=res
        return res


def get_hash(polymer):
    occurrences = defaultdict(lambda: 0)
    for c in polymer:
        occurrences[c] += 1
    most_common = max(occurrences.items(), key=lambda o: o[1])
    least_common = min(occurrences.items(), key=lambda o: o[1])
    return most_common[1]-least_common[1]


polymer = start
l = 4
for i in range(40):
    l= l*2-1
    # print(i)
    # print(len(rules))
    # print(len(polymer))
    # polymer = process(polymer)

print(l)
