
lines = open("data/day8.txt").read().splitlines()

segments = ["a", "b", "c", "d", "e", "f", "g"]
digit_segments = [
    set(["a", "b", "c", "e", "f", "g"]),
    set(["c", "f"]),
    set(["a", "c", "d", "e", "g"]),
    set(["a", "c", "d", "f", "g"]),
    set(["b", "c", "d", "f"]),
    set(["a", "b", "d", "f", "g"]),
    set(["a", "b", "d", "e", "f", "g"]),
    set(["a",  "c",  "f"]),
    set(["a", "b", "c", "d", "e", "f", "g"]),
    set(["a", "b", "c", "d", "f", "g"]),
]
len_to_segments = {2: digit_segments[1],
                   3: digit_segments[7], 4: digit_segments[4]}
n = len(segments)


def constraints_from_lengths(encoded_digits):
    constraints = [set(segments) for _ in segments]
    for digit in encoded_digits:
        if len(digit) in len_to_segments:
            for char in digit:
                i = segments.index(char)
                constraints[i] = len_to_segments[len(digit)]
    return constraints


def enumerate_encodings(constraints, determined=[]):
    i = len(determined)
    if i == n:
        yield {segments[i]: determined[i] for i in range(n)}
        return
    for seg in segments:
        if seg not in constraints[i] or seg in determined:
            continue
        yield from enumerate_encodings(constraints, determined+[seg])


def decode(encoding, digit):
    s = {encoding[letter] for letter in digit}
    for i in range(10):
        if digit_segments[i] == s:
            return i
    return None


def find_encoding(encoded_digits):
    constraints = constraints_from_lengths(encoded_digits)
    for encoding in enumerate_encodings(constraints):
        if all([decode(encoding, digit) != None for digit in encoded_digits]):
            return encoding
    return None


easy_digits = 0
tot = 0
for line in lines:
    [s, o] = line.split(" | ")
    all_digits = o.split()+s.split()
    output = o.split()

    easy_digits += len([d for d in output if len(d) in [2, 3, 4, 7]])

    encoding = find_encoding(all_digits)
    tot += int("".join([str(decode(encoding, digit))
               for digit in output]))

print(easy_digits)
print("part2")
print(tot)
