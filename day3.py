lines = open("data/day3.txt", "r").read().splitlines()


def part1():
    counts = [0]*len(lines[0])
    for line in lines:
        for i, c in enumerate(line):
            counts[i] += 1 if c == "1" else -1
    gamma = int("".join(["1" if c > 0 else "0" for c in counts]),2)
    epsilon = int("".join(["0" if c > 0 else "1" for c in counts]),2)
    print(gamma* epsilon)


def part2():
    oxygen = find(lines, sieve_oxygen)
    co2 = find(lines, sieve_co2)
    print(oxygen*co2)


def sieve_oxygen(nrs, digit):
    count = 0
    for line in nrs:
        count += 1 if line[digit] == "1" else -1
    common = "1" if count >= 0 else "0"
    return [l for l in nrs if l[digit] == common]


def sieve_co2(nrs, digit):
    count = 0
    for line in nrs:
        count += 1 if line[digit] == "1" else -1
    least = "0" if count >= 0 else "1"
    return [l for l in nrs if l[digit] == least]


def find(l, sieve):
    i = 0
    while len(l) > 1:
        l = sieve(l, i)
        i += 1
    return int(l[0], 2)


print("part1")
part1()

print("part2")
part2()
