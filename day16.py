from collections import namedtuple
import math
import numpy as np

Packet = namedtuple('Packet', ('version', 'type', 'value'))


def to_int(b):
    return b.dot(1 << np.arange(b.size)[::-1])


def versions_sum(packet):
    if packet.type == 4:
        return packet.version
    return packet.version + sum([versions_sum(p) for p in packet.value])


def eval_packet(packet):
    if packet.type == 0:
        return sum([eval_packet(p) for p in packet.value])
    elif packet.type == 1:
        return math.prod([eval_packet(p) for p in packet.value])
    elif packet.type == 2:
        return min([eval_packet(p) for p in packet.value])
    elif packet.type == 3:
        return max([eval_packet(p) for p in packet.value])
    elif packet.type == 4:
        return packet.value
    elif packet.type == 5:
        a = eval_packet(packet.value[0])
        b = eval_packet(packet.value[1])
        return 1 if a > b else 0
    elif packet.type == 6:
        a = eval_packet(packet.value[0])
        b = eval_packet(packet.value[1])
        return 1 if a < b else 0
    elif packet.type == 7:
        a = eval_packet(packet.value[0])
        b = eval_packet(packet.value[1])
        return 1 if a == b else 0
    else:
        raise ValueError("unexpected packet.type",packet.type)


class Buffer:
    def __init__(self, data):
        self.data = data
        self.ptr = 0

    def read(self, n):
        oldptr = self.ptr
        self.ptr += n
        return self.data[oldptr:buf.ptr]

    def read_packet(self):
        version = to_int(self.read(3))
        packet_id = to_int(self.read(3))
        if packet_id == 4:
            literal = []
            while self.ptr < len(self.data):
                cont = self.read(1)
                literal.append(self.read(4))
                if cont == 0:
                    break
            value = to_int(np.concatenate(literal))
            return Packet(version, packet_id, value)
        length_type = self.read(1)
        if length_type == 0:
            sub_packets = []
            length = to_int(self.read(15))
            end = self.ptr+length
            while self.ptr < end:
                sub_packets.append(self.read_packet())
            return Packet(version, packet_id, sub_packets)
        else:
            sub_packets = []
            nr_packets = to_int(self.read(11))
            for _ in range(nr_packets):
                sub_packets.append(self.read_packet())
            return Packet(version, packet_id, sub_packets)


lines = open("data/day16.txt").read().rstrip()
buf = Buffer(np.unpackbits(bytearray.fromhex(lines)))
packet = buf.read_packet()
print(versions_sum(packet))
print("part 2")
print(eval_packet(packet))
