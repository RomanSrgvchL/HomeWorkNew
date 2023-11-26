class Counter:

    def __init__(self, initial_value):
        self.value = initial_value

    def inc(self):
        self.value = self.value + 1
        return self.value

    def dec(self):
        self.value = self.value - 1
        return self.value


class ReverseCounter(Counter):

    def inc(self):
        self.value = self.value - 1
        return self.value

    def dec(self):
        self.value = self.value + 1
        return self.value


def get_counter(number):
    if number >= 0:
        counter = Counter(number)
        return counter
    else:
        counter = ReverseCounter(number)
        return counter
