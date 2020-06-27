from statlib.rand.constants import ULM, ULLM
from datetime import datetime

SEED = 42

class LCG:
    def __init__(self, seed=SEED):
        self.a = 1103515245
        self.c = 12345
        self.m = 1 << 31
        self.reseed(seed)

    def reseed(self, seed=SEED):
        self._next = seed

    def next(self):
        self._next = (self.a * self._next + self.c) % self.m
        return self._next
    
    def max_val(self):
        return self.m - 1
