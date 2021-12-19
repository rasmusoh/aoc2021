import itertools
import math
import copy


class Node:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return self.to_string()

    def to_string(self):
        if type(self.val) == tuple:
            return "({},{})".format(
                self.val[0].to_string(), self.val[1].to_string())
        else:
            return str(self.val)

    def magnitude(self):
        if type(self.val) == tuple:
            return 3*self.val[0].magnitude()+2*self.val[1].magnitude()
        else:
            return self.val


def valuenodes(node):
    if type(node.val) == tuple:
        yield from valuenodes(node.val[0])
        yield from valuenodes(node.val[1])
    else:
        yield node


def parse(s):
    if s[0] == "[":
        l, rest = parse(s[1:])
        r, rest = parse(rest[1:])
        return Node((l, r)), rest[1:]
    return Node(int(s[0])), s[1:]


def split(node):
    if type(node.val) == tuple:
        splitted = split(node.val[0])
        if splitted:
            return True
        return split(node.val[1])
    else:
        if node.val > 9:
            node.val = (Node(node.val//2), Node(math.ceil(node.val/2)))
            return True
        return False


def explode(node, vnodes=None, level=0):
    if vnodes == None:
        vnodes = list(valuenodes(node))
    if type(node.val) == tuple:
        if level >= 4:
            i = vnodes.index(node.val[0])
            if i > 0:
                vnodes[i-1].val += node.val[0].val
            if i+2 < len(vnodes):
                vnodes[i+2].val += node.val[1].val
            node.val = 0
            return True
        else:
            if explode(node.val[0], vnodes, level+1):
                return True
            return explode(node.val[1], vnodes, level+1)
    return False


def add(exp1, exp2):
    node = Node((copy.deepcopy(exp1), copy.deepcopy(exp2)))
    while True:
        exploded = explode(node)
        if exploded:
            continue
        splitted = split(node)
        if not splitted:
            break
    return node


lines = open("data/day18.txt").read().splitlines()
nrs = [parse(line)[0] for line in lines]
total = nrs[0]
for nr in nrs[1:]:
    total = add(total, nr)
print(total.magnitude())
print("part 2")
print(max([add(a, b).magnitude()
      for (a, b) in itertools.permutations(nrs, 2)]))
