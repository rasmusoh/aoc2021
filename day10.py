lines = open("data/day10.txt").read().splitlines()


matching = {"(": ")", "[": "]", "{": "}", "<": ">"}
completion_points = {")": 1, "]": 2, "}": 3, ">": 4}


def corrupted_score(line):
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


def completion_score(line):
    stack = [line[0:1]]
    for char in line[1:]:
        if char in ["(", "[", "{", "<"]:
            stack.append(char)
        else:
            stack.pop()
    completion = []
    while len(stack) > 0:
        completion.append(matching[stack.pop()])
    score = 0
    for ch in completion:
        score *= 5
        score += completion_points[ch]
    return score


print(sum([corrupted_score(line) for line in lines]))

"part 2"
completion_scores = [completion_score(
    line) for line in lines if corrupted_score(line) == 0]
completion_scores.sort()
print(completion_scores[len(completion_scores)//2])
