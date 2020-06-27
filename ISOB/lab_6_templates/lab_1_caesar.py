class Caesar:
    def __init__(self):
        self.input_file = None
        self.output_file = None

        self.__alpha = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !"#$%&\()*+,-./:;<=>?@[]^_`{' \
                       '|}~абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.__result = ''

    def encode(self, key):
        with open(self.input_file) as f:
            lines = f.readlines()
            for s in lines:
                for c in s:
                    if c == '\n':
                        self.__result += '\n'
                        continue

                    self.__result += self.__alpha[(self.__alpha.index(c) + key) % len(self.__alpha)]

        with open(self.output_file, 'w') as f:
            for c in self.__result:
                if c == '\n':
                    f.write('\n')
                    continue
                f.write(c)

        self.__result = None

    def decode(self, key):
        with open(self.input_file) as f:
            lines = f.readlines()
            for s in lines:
                for c in s:
                    if c == '\n':
                        self.__result += '\n'
                        continue

                    self.__result += self.__alpha[(self.__alpha.index(c) - key) % len(self.__alpha)]

        with open(self.output_file, 'w') as f:
            for c in self.__result:
                if c == '\n':
                    f.write('\n')
                    continue
                f.write(c)

        self.__result = None
