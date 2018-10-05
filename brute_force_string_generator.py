import string


class BruteForceStringGenerator(object):

    def __init__(self, initial_sequence=[], chars=string.ascii_lowercase, min_length=1, max_length=0):
        self.sequence = list(initial_sequence)
        self.chars = chars
        self.min_length = max(0, min_length)
        self.max_length = max(0, max_length)
        self.number_of_chars = len(self.chars)

    def next_string(self):
        self.sequence = self._next(self.sequence)
        return "".join(self.sequence)

    def _next(self, curr_string):
        if len(curr_string) <= 0:
            if not self.sequence:
                return list(self.chars[0]*self.min_length)
            else:
                if self.max_length and len(self.sequence) >= self.max_length:
                    raise ValueError("Max length")
                return list(self.chars[0])
        else:
            curr_string[0] = self.chars[((self.chars.index(curr_string[0]) + 1) % self.number_of_chars)]
            if self.chars.index(curr_string[0]) is 0:
                return list(curr_string[0]) + self._next(curr_string[1:])
        return curr_string


