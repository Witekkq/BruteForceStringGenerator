import string

from enum import Enum, auto


class Direction(Enum):
    LEFT = 0
    RIGHT = -1

    def __int__(self):
        return self.value


class BruteForceStringGenerator(object):

    def __init__(self, sequence=[], chars=string.ascii_lowercase, dir=Direction.RIGHT, min_length=1, max_length=0):
        self.sequence = list(sequence)
        self.chars = chars
        self.dir = dir
        self.min_length = max(0, min_length)
        self.max_length = max(0, max_length)
        self.chars_num = len(self.chars)

    def next_string(self):
        self.sequence = self._next(self.sequence)
        return "".join(self.sequence)

    def _next(self, current):
        if len(current) <= 0:
            if not self.sequence:
                return list(self.chars[0] * self.min_length)
            else:
                if self.max_length and len(self.sequence) >= self.max_length:
                    raise ValueError("Max length")
                return list(self.chars[0])
        else:
            current[int(self.dir)] = self.chars[((self.chars.index(current[int(self.dir)]) + 1) % self.chars_num)]
            if self.chars.index(current[int(self.dir)]) == 0:
                if self.dir == Direction.LEFT:
                    return list(current[0]) + self._next(current[1:])
                else:
                    return self._next(current[:-1]) + list(current[-1])
        return current

