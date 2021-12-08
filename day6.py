
fishes = open("data/day6.txt").read().rstrip().split(",")

maxage = 8
cycle = 6

def fishes_at_day(day):
    fishstates = [0]*(maxage+1)
    for fish in fishes:
        fishstates[int(fish)] += 1

    for day in range(day):
        new = fishstates[0]
        for i in range(0, maxage):
            fishstates[i] = fishstates[i+1]
        fishstates[maxage] = new
        fishstates[cycle] += new
    return sum(fishstates)

print(fishes_at_day(80))
print("part 2")
print(fishes_at_day(256))
