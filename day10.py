lines = open("data/day10.txt").read().splitlines()


matching = {"(": ")", "[": "]", "{": "}", "<": ">"}
corruption_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
completion_points = {")": 1, "]": 2, "}": 3, ">": 4}


def corrupted_score(line):
    stack = [line[0:1]]
    for char in line[1:]:
        if char in matching.keys():
            stack.append(char)
        elif char != matching[stack.pop()]:
            return corruption_points[char]
    return 0


def completion_score(line):
    stack = [line[0:1]]
    for char in line[1:]:
        if char in matching.keys():
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
