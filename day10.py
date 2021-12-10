lines = open("data/day10.txt").read().splitlines()

matching = {"(": ")", "[": "]", "{": "}", "<": ">"}


def points_line(line):
    stack = [line[0:1]]
    for char in line[1:]:
        if char in ["(", "[", "{", "<"]:
            stack.append(char)
        elif char == ")":
            if stack.pop() != "(":
                return 3
        elif char == "]":
            if stack.pop() != "[":
                return 57
        elif char == "}":
            if stack.pop() != "{":
                return 1197
        elif char == ">":
            if stack.pop() != "<":
                return 25137
    return 0


def completion(line):
    stack = [line[0:1]]
    for char in line[1:]:
        if char in ["(", "[", "{", "<"]:
            stack.append(char)
        else:
            stack.pop()
    completion = []
    while len(stack) > 0:
        completion.append(matching[stack.pop()])
    # print(line," ", completion)
    score = 0
    completion_points = {")": 1, "]": 2, "}": 3, ">": 4}
    for ch in completion:
        score *= 5
        score += completion_points[ch]
    return score


points = 0
for line in lines:
    points += points_line(line)
print(points)
"part 2"

incomplete = [line for line in lines if points_line(line) == 0]
points = []
for line in incomplete:
    points.append(completion(line))
points.sort()
print(points[len(points)//2])
