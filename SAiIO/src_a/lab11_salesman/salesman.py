import itertools
import random
import sys
from pprint import pprint


def get_subset_bits(subset):
    bits = 0
    for bit in subset:
        bits |= 1 << bit
    return bits


def exclude_bit(bits, k):
    return bits & ~(1 << k)


class HeldKarp:
    def __init__(self, dists):
        self.dists = dists
        self.n = len(dists)
        self.C = {}

    def __set_initial_state(self):
        for k in range(1, self.n):
            self.C[(1 << k, k)] = (self.dists[0][k], 0)

    def __calc_final_transition(self):
        # We're interested in all bits but the least significant (the start state)
        bits = (2**self.n - 1) - 1

        # Calculate optimal cost
        res = []
        for k in range(1, self.n):
            res.append((self.C[(bits, k)][0] + self.dists[k][0], k))

        return min(res)

    def __get_subset_to_vertex_distances(self, subset, prev, k):
        res = []
        for m in subset:
            if m == k:
                continue
            res.append((self.C[(prev, m)][0] + self.dists[m][k], m))

        return res

    def __restore_path(self, parent):
        bits = (2**self.n - 1) - 1
        path = []

        for _ in range(self.n - 1):
            print('parent:', parent)
            path.append(parent)
            new_bits = exclude_bit(bits, parent)
            _, parent = self.C[(bits, parent)]
            bits = new_bits

        path.append(0)

        return list(reversed(path))

    def solve(self):
        self.__set_initial_state()
        print(self.C)

        for subset_size in range(2, self.n):
            print('='*20)
            for subset in itertools.combinations(range(1, self.n), subset_size):
                bits = get_subset_bits(subset)
                print(subset, bits)

                # Find the lowest cost to get to this subset
                for k in subset:
                    prev = exclude_bit(bits, k)
                    res = self.__get_subset_to_vertex_distances(
                        subset, prev, k)
                    self.C[(bits, k)] = min(res)

                    print('prev:', prev)
                    print('k: {}, res: {}'.format(k, res))
                    pprint(self.C)

        opt, parent = self.__calc_final_transition()
        path = self.__restore_path(parent)

        return opt, path
