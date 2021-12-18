import math


class Node:
    def __init__(self, parent=None, val=None):
        self.parent = parent
        self.value = val

    def root(self):
        root = self
        while root.parent != None:
            root = root.parent
        return root

    def valuenodes(self):
        if type(self.value) == tuple:
            yield from self.value[0].valuenodes()
            yield from self.value[1].valuenodes()
        else:
            yield self.value

    def __str__(self):
        if type(self.value) == tuple:
            return "({0},{0})".format(str(self.value[0]), str(self.value[1]))
        else:
            return str(self.value)


def parse(s, parent=None):
    if s[0] == "[":
        node = Node(parent)
        l, rest = parse(s[1:], node)
        r, rest = parse(rest[1:], node)
        node.value = (l, r)
        return node, rest[1:]
    return Node(parent, int(s[0])), s[1:]


def split(node):
    if type(node.value) == tuple:
        splitted = split(node.value[0])
        if splitted:
            return True
        return split(node.value[1])
    else:
        if node.value > 10:
            node.value = (Node(node, node.value//2),
                          Node(node, math.ceil(node.value/2)))


def explode(node, level=0):
    if type(node.value) == tuple:
        if level >= 4:
            vnodes = list(node.root().valuenodes())
            i = vnodes.index(node.value[0])
            if i > 0:
                vnodes[i-1].value += node.value[0]
            if i < len(vnodes)-1:
                vnodes[i+2].value += node.value[1]

            if node.parent.value[0] == node:
                node.parent.value[0] = Node(node.parent, 0)
            else:
                node.parent.value[1] = Node(node.parent, 0)
            return True
        else:
            if explode(node.value[0], level+1):
                return True
            return explode(node.value[1])
    return False


def reduce(node):
    while True:
        exploded = explode(node)
        if exploded:
            continue
        splitted = split(node)
        if not splitted:
            break


def add(exp1, exp2):
    added = (exp1, exp2)
    return reduce(added)


def magnitude(exp):
    pass


lines = open("data/day18.txt").read().splitlines()
for line in lines:
    p, _ = parse([c for c in line])
    for i in p.valuenodes():
        print(p)
    # reduce(p)
    # print(p)
    print()
