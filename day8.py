import copy

lines = open("data/day8.test.txt").read().splitlines()


easy_digits = 0
patterns = []
for line in lines:
    [signal, output] = line.split(" | ")
    patterns.append({"signal": signal.split(), "output": output.split()})

print(len([d for pattern in patterns for d in pattern["output"]
      if len(d) in [2, 3, 4, 7]]))

print("part2")

segments_by_digit = {
    0: set(["a", "b", "c", "e", "f", "g"]),
    1: set(["c", "f"]),
    2: set(["a", "c", "d", "e", "g"]),
    3: set(["a", "c", "d", "f", "g"]),
    4: set(["b", "c", "d", "f"]),
    5: set(["a", "b", "d", "f", "g"]),
    6: set(["a", "b", "d", "e", "f", "g"]),
    7: set(["a",  "c",  "f"]),
    8: set(["a", "b", "c", "d", "e", "f", "g"]),
    9: set(["a", "b", "c", "d", "f", "g"]),
}

# digits_by_nr_segments = {2: set([1]), 3: set([7]), 4: set([
#     4]), 5: set([2, 3, 5]), 6: set([6, 9]), 7: set([8])},
possible_by_nr_segments = [set() for _ in range(10)]
for digit in segments_by_digit:
    possible_by_nr_segments[len(segments_by_digit[digit])
                            ] |= segments_by_digit[digit]

segments = ["a", "b", "c", "d", "e", "f", "g"]


def generate_hypotheticals(encoding):
    hyps = []
    [letter, possiblevals] = min(
        [(k, v) for (k, v) in encoding.items() if len(v) > 1], key=lambda x: len(x[1]))
    for val in possiblevals:
        hyp = copy.deepcopy(encoding)
        hyp[letter] = set(val)
        hyps.append(hyp)
    return hyps


def propagate_contstraints(encoding):
    while True:
        propagated = 0
        determined = [(k, next(iter(v)))
                      for (k, v) in encoding.items() if len(v) == 1]
        for letter in encoding:
            for (k, v) in determined:

                if k != letter and v in encoding[letter]:
                    encoding[letter].remove(v)
                    propagated += 1
        if propagated == 0:
            return


def find_encoding(pattern):
    encoding = {}
    for seg in segments:
        encoding[seg] = set(segments)
    for digit in (pattern["signal"]+pattern["output"]):
        for letter in digit:
            encoding[letter] &= possible_by_nr_segments[len(digit)]
    queue = [encoding]
    while len(queue) > 0:
        hyps = generate_hypotheticals(queue.pop())
        for hyp in hyps:
            print(hyp)
            propagate_contstraints(hyp)
            print(hyp)
            if all([len(v) == 1 for v in hyp.values()]):
                return [(k, next(iter(v))) for (k, v) in hyp]
            elif not any([len(v) == 0 for v in hyp.values()]):
                queue.append(hyp)

    raise copy.Error("nothing found")


def decode(encoding, digit):
    decoded=[encoding[letter] for letter in digit]
    for i in range(10):
        if len(decoded) == len(segments_by_digit[i]) and all([s in segments_by_digit[i] for s in decoded]):
            return i


for pattern in patterns:
    encoding=find_encoding(pattern)
    for digit in pattern["output"]:
        print(decode(encoding, digit))
