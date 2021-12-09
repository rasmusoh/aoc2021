import copy
import math

lines = open("data/day8.txt").read().splitlines()


easy_digits = 0
patterns = []
for line in lines:
    [signal, output] = line.split(" | ")
    patterns.append({"all": output.split()+signal.split(),
                    "output": output.split()})

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
all_segments = ["a", "b", "c", "d", "e", "f", "g"]
len_to_digit = {2: 1, 3: 7, 4: 4}
n = len(all_segments)


def enumerate_encodings(constraints, determined=[]):
    i = len(determined)
    if i == n:
        yield {all_segments[i]: determined[i] for i in range(n)}
        return
    for seg in all_segments:
        if seg not in constraints[i] or seg in determined:
            continue
        yield from enumerate_encodings(constraints, determined+[seg])


def decode(encoding, digit):
    s = {encoding[letter] for letter in digit}
    for i in range(10):
        if segments_by_digit[i] == s:
            return i
    return None


def find_encoding(encoded_digits):
    constraints = [set(all_segments) for _ in all_segments]
    for nr in encoded_digits:
        if len(nr) in len_to_digit:
            for c in nr:
                i = all_segments.index(c)
                constraints[i] = segments_by_digit[len_to_digit[len(
                    nr)]].copy()
    for encoding in enumerate_encodings(constraints):
        if all([decode(encoding, digit) != None for digit in encoded_digits]):
            return encoding
    return None


tot=0
for pattern in patterns:
    encoding = find_encoding(pattern["all"])
    tot+=int("".join([str(decode(encoding, digit)) for digit in pattern["output"]]))
print(tot)
