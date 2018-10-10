import string

from enum import IntEnum


class Direction(IntEnum):
    LEFT = 0
    RIGHT = -1


class BruteForceStringGenerator(object):

    def __init__(self, sequence='', chars=string.ascii_lowercase, dir=Direction.RIGHT, min_length=1, max_length=0):
        self.sequence = sequence
        self._sequence_list = list(sequence)
        self.chars = chars
        self.dir = dir
        self.min_length = max(0, min_length)
        self.max_length = max(0, max_length)
        self.chars_num = len(self.chars)

    def __iter__(self):
        return self

    def __next__(self):
        self.next_string()
        if self.max_length and len(self) > self.max_length:
            raise StopIteration
        return self.sequence

    def __len__(self):
        return len(self._sequence_list)

    @property
    def sequence(self):
        return "".join(self._sequence_list)

    @sequence.setter
    def sequence(self, sequence):
        self._sequence_list = list(sequence)

    def next_string(self):
        self._sequence_list = self._next(self._sequence_list)

    def _next(self, current):
        if len(current) <= 0:
            if not self._sequence_list:
                return list(self.chars[0] * self.min_length)
            else:
                return list(self.chars[0])
        else:
            current[self.dir] = self.chars[((self.chars.index(current[self.dir]) + 1) % self.chars_num)]
            if self.chars.index(current[self.dir]) == 0:
                if self.dir == Direction.LEFT:
                    return list(current[0]) + self._next(current[1:])
                else:
                    return self._next(current[:-1]) + list(current[-1])
        return current


class BruteForceListGenerator(BruteForceStringGenerator):

    def __init__(self, sequence, **kwargs):

        BruteForceStringGenerator.__init__(self, sequence=sequence)
        self.end_string = None
        self.number = None
        self.iterator = 0
        for key, value in kwargs.items():
            if key == 'end':
                self.end_string = value

            elif key == 'num':
                self.number = value
            else:
                raise ValueError("Missing params")

    def to_number(self):
        self.next_string()
        self.iterator += 1
        if self.sequence and self.iterator > self.number:
            raise StopIteration
        return self.sequence

    def to_string(self):
        if self.sequence and self.sequence == self.end_string:
            raise StopIteration
        self.next_string()
        return self.sequence

    def __next__(self):
        if self.end_string:
            return self.to_string()
        else:
            return self.to_number()

    @staticmethod
    def create(sequence, **kwargs):
        gen = BruteForceListGenerator(sequence=sequence, **kwargs)
        return [element for element in gen]
