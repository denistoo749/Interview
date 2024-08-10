#!/usr/bin/python3
"""UTF-8 Validation"""
from itertools import takewhile


NUMBER_OF_BITS_PER_BLOCK = 8
MAX_NUMBER_OF_ONES = 4


def to_bits(bytes):
    """Changes a number to a list of bits"""
    for byte in bytes:
        num = []
        exp = 1 << NUMBER_OF_BITS_PER_BLOCK
        while exp:
            exp >>= 1
            num.append(bool(byte & exp))
        yield num


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    bits = to_bits(data)
    for byte in bits:
        if byte[0] == 0:
            continue
        amount = sum(takewhile(bool, byte))
        if amount <= 1:
            return (False)
        if amount > MAX_NUMBER_OF_ONES:
            return (False)
        for _ in range(amount - 1):
            try:
                byte = next(bits)
            except StopIteration:
                return (False)
            if byte[0:2] != [1, 0]:
                return (False)
    return (True)
