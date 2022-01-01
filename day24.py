def is_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def compile_line(line):
    ins = line.split()
    if ins[0] == "inp":
        def exInput(reg, inp):
            reg[ins[1]] = next(inp)
        return exInput
    elif ins[0] == "add":
        if is_int(ins[2]):
            def exAddLit(reg, _):
                reg[ins[1]] += int(ins[2])
            return exAddLit
        else:
            def exAddVar(reg, _):
                reg[ins[1]] += reg[ins[2]]
            return exAddVar
    elif ins[0] == "mul":
        if is_int(ins[2]):
            def exMulLit(reg, _):
                reg[ins[1]] *= int(ins[2])
            return exMulLit
        else:
            def exMulVar(reg, _):
                reg[ins[1]] *= reg[ins[2]]
            return exMulVar
    elif ins[0] == "div":
        if is_int(ins[2]):
            def exDivLit(reg, _):
                reg[ins[1]] //= int(ins[2])
            return exDivLit
        else:
            def exDivVar(reg, _):
                reg[ins[1]] //= reg[ins[2]]
            return exDivVar
    elif ins[0] == "mod":
        if is_int(ins[2]):
            def exModLit(reg, _):
                reg[ins[1]] %= int(ins[2])
            return exModLit
        else:
            def exModVar(reg, _):
                reg[ins[1]] %= reg[ins[2]]
            return exModVar
    elif ins[0] == "eql":
        if is_int(ins[2]):
            def exEqlLit(reg, _):
                reg[ins[1]] = 1 if reg[ins[1]] == int(ins[2]) else 0
            return exEqlLit
        else:
            def exEqlVar(reg, _):
                reg[ins[1]] = 1 if reg[ins[1]] == reg[ins[2]] else 0
            return exEqlVar
    else:
        raise ValueError("invalid input line")


def compile(lines):
    return [compile_line(line) for line in lines]


def run(program, inputstring, z_override=None):
    reg = {"w": 0, "x": 0, "y": 0, "z": 0}
    if z_override != None:
        reg["z"] = z_override

    def inp():
        for i in inputstring:
            yield int(i)
    input_iterator = inp()
    for instruction in program:
        instruction(reg, input_iterator)
    return reg


def compile_blocks(source):
    d = "inp w"
    return [compile((d+e).splitlines()) for e in source.split(d) if e]


blocks = compile_blocks(open("data/day24.txt").read())
result_blocks = [{}]*len(blocks)
span = 1000
for i, block in reversed(list(enumerate(blocks))):
    result = result_blocks[i] = {}
    for z in range(-span, span):
        for inp in range(1, 10):
            res = run(block, str(inp), z)
            if res["z"] in result:
                result[res["z"]].append((str(inp), z))
            else:
                result[res["z"]] = [(str(inp), z)]
valids = result_blocks[11][0]
for i in reversed(range(11)):
    nex = []
    for inp,z in valids:
        if z not in result_blocks[i]:
            continue
        for inp2,z2 in result_blocks[i][z]:
            nex.append((inp2+inp,z2))
    valids = nex
    print(valids)
# test2 = ["inp z",
# "inp x",
# "mul z 3",
# "eql z x"]
# print(run(compile(["inp x", "mul x -1"]), "2"))
# print()
# print(run(compile(test2), "39"))
# print()
