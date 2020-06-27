import random


class BasicRand:
    def __init__(self, gen):
        self.gen = gen

    def next(self):
        return self.gen.next() / self.max_val()

    def max_val(self):
        return self.gen.max_val()

    def reseed(self, seed):
        self.gen.reseed(seed)


class Discrete:
    def __init__(self, possibilities, gen):
        self.gen = gen
        self.ranges = []
        
        cur_p = 0
        for c_x, c_p in possibilities:
            cur_p += c_p
            self.ranges.append((cur_p, c_x))

    def next(self):
        next_val = self.gen.next()
        
        if next_val <= self.ranges[0][0]:
            return self.ranges[0][1]
        
        for i in range(len(self.ranges) - 1):
            if self.ranges[i][0] < next_val <= self.ranges[i + 1][0]:
                return self.ranges[i + 1][1]
