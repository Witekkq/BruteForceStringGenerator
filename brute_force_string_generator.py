import string


class BruteForceStringGenerator(object):

    def __init__(self, chars=string.ascii_lowercase, min_length=1, max_length=0, initial_sequence=[]):
        self.sequence = list(initial_sequence)
        self.chars = chars
        self.min_length = min_length
	self.max_length = max_length
        self.number_of_chars = len(self.chars)

    def character_to_index(self, char):
        return self.chars.index(char)

    def index_to_character(self, index):
        if self.number_of_chars <= index:
            raise ValueError("Index out of range.")
        else:
            return self.chars[index]

    def next_string(self):
        self.sequence = self._next(self.sequence)
        return "".join(self.sequence)

    def _next(self, curr_string):
        if len(curr_string) <= 0:
            if not self.sequence:
                return list(self.chars[0]*self.min_length)
            else:
		if len(self.sequence) >= self.max_length:
			raise ValueError("Max length")
                return list(self.index_to_character(0))
        else:
            curr_string[0] = self.index_to_character((self.character_to_index(curr_string[0]) + 1) % self.number_of_chars)
            if self.character_to_index(curr_string[0]) is 0:
                return list(curr_string[0]) + self._next(curr_string[1:])
        return curr_string
