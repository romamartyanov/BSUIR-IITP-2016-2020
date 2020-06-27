import string
import numpy as np


class Vigener:
    @staticmethod
    def __create_table():
        alp_lower = [i for i in string.ascii_lowercase]
        alp_upper = [i for i in string.ascii_uppercase]
        symbols = [i for i in (string.digits + ".,!?")]
        rus_upper = [chr(i) for i in range(1040, 1072)]
        rus_lower = [chr(i) for i in range(1072, 1104)]

        alpha = alp_lower + alp_upper + rus_lower + rus_upper + symbols

        n = len(alpha)
        table = [[""] * n] * n

        for i in range(n):
            table[i] = alpha
            alpha = alpha[1:] + alpha[:1]

        return table

    def __init__(self):
        self.input_file = None
        self.output_file = None
        self.__result = ''

        self.__table = Vigener.__create_table()

    def encode(self, key):
        k_i = 0
        with open(self.input_file) as f:
            lines = f.readlines()
            key *= len("".join(lines)) // len(key) + 1

            for s in lines:
                for c in s:
                    if c not in self.__table[0]:
                        self.__result += c
                        continue

                    k_pos = self.__table[0].index(key[k_i])
                    k_i += 1

                    t_pos = self.__table[0].index(c)
                    self.__result += self.__table[t_pos][k_pos]

        with open(self.output_file, 'w') as f:
            for c in self.__result:
                if c == '\n':
                    f.write('\n')
                    continue
                f.write(c)

        self.__result = None

    def decode(self, key):
        k_i = 0
        with open(self.input_file) as f:
            lines = f.readlines()
            key *= len("".join(lines)) // len(key) + 1

            for s in lines:
                for c in s:
                    if c not in self.__table[0]:
                        self.__result += c
                        continue
                    k_pos = self.__table[0].index(key[k_i])
                    k_i += 1

                    t_pos = list(np.array(self.__table)[:, k_pos]).index(c)
                    self.__result += self.__table[0][t_pos]

        with open(self.output_file, 'w') as f:
            for c in self.__result:
                if c == '\n':
                    f.write('\n')
                    continue
                f.write(c)

        self.__result = None
