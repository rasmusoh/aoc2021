from collections import deque
test_input = (4, 8)
real_input = (7, 3)


class Die:
    count = 0
    rollcount = 0

    def roll(self):
        self.rollcount += 1
        self.count = 1+(self.count % 100)
        return self.count


def play(pos):
    scores = [0, 0]
    pos = list(pos)
    die = Die()
    while True:
        for p in range(2):
            roll = die.roll()+die.roll()+die.roll()
            pos[p] = 1+(roll+pos[p]-1) % 10
            scores[p] += pos[p]
            if scores[p] >= 1000:
                return scores[(p+1) % 2]*die.rollcount


def generate_rolls():
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                yield i+j+k


def get_next_state(state, roll):
    turn, s1, s2, p1, p2 = state
    if turn % 2 == 0:
        pos = 1+(roll+p1-1) % 10
        return (turn+1, s1+pos, s2, pos, p2)
    else:
        pos = 1+(roll+p2-1) % 10
        return (turn+1, s1, s2+pos, p1, pos)


def count_wins_p2(start):
    start = (int(0), 0, 0, start[0], start[1])
    q = deque([start])
    paths = {start: 1}
    rolls = list(generate_rolls())
    while len(q) > 0:
        state = q.popleft()
        if state[1] < 21 and state[2] < 21:
            for roll in rolls:
                next_state = get_next_state(state, roll)
                if next_state in paths:
                    paths[next_state] += paths[state]
                else:
                    paths[next_state] = paths[state]
                    q.append(next_state)
    return (sum([ps for (_, s1, _, _, _), ps in paths.items() if s1 >= 21]),
            sum([ps for (_, _, s2, _, _), ps in paths.items() if s2 >= 21]))


print(play(real_input))
print("part 2")
print(count_wins_p2(test_input))
print(count_wins_p2(real_input))
# 75823864479001 too low
