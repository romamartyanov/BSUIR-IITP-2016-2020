PLAIN = 1
BLOCK = 2
GAMMING = 3
COUNTER = 4

H = [
    [177, 148, 186, 200, 10, 8, 245, 59, 54, 109, 0, 142, 88, 74, 93, 228],
    [133, 4, 250, 157, 27, 182, 199, 172, 37, 46, 114, 194, 2, 253, 206, 13],
    [91, 227, 214, 18, 23, 185, 97, 129, 254, 103, 134, 173, 113, 107, 137, 11],
    [92, 176, 192, 255, 51, 195, 86, 184, 53, 196, 5, 174, 216, 224, 127, 153],
    [225, 43, 220, 26, 226, 130, 87, 236, 112, 63, 204, 240, 149, 238, 141, 241],
    [193, 171, 118, 56, 159, 230, 120, 202, 247, 198, 248, 96, 213, 187, 156, 79],
    [243, 60, 101, 123, 99, 124, 48, 106, 221, 78, 167, 121, 158, 178, 61, 49],
    [62, 152, 181, 110, 39, 211, 188, 207, 89, 30, 24, 31, 76, 90, 183, 147],
    [233, 222, 231, 44, 143, 12, 15, 166, 45, 219, 73, 244, 111, 115, 150, 71],
    [6, 7, 83, 22, 237, 36, 122, 55, 57, 203, 163, 131, 3, 169, 139, 246],
    [146, 189, 155, 28, 229, 209, 65, 1, 84, 69, 251, 201, 94, 77, 14, 242],
    [104, 32, 128, 170, 34, 125, 100, 47, 38, 135, 249, 52, 144, 64, 85, 17],
    [190, 50, 151, 19, 67, 252, 154, 72, 160, 42, 136, 95, 25, 75, 9, 161],
    [126, 205, 164, 208, 21, 68, 175, 140, 165, 132, 80, 191, 102, 210, 232, 138],
    [162, 215, 70, 82, 66, 168, 223, 179, 105, 116, 197, 81, 235, 35, 41, 33],
    [212, 239, 217, 180, 58, 98, 40, 117, 145, 20, 16, 234, 119, 108, 218, 29]
]


class STB:
    def __init__(self, key, mode=COUNTER):
        key = int(''.join(str(ord(c)) for c in key))

        count = self.get_key_chunks_counts(key)
        self.tmp_keys = []

        # key partition
        for i in range(count):
            self.tmp_keys.append(key & 0xFFFF)
            key >>= 32

        if count == 4:
            self.tmp_keys.extend(self.tmp_keys[:])
        elif count == 6:
            self.tmp_keys.extend([
                self.tmp_keys[0] ^ self.tmp_keys[1] ^ self.tmp_keys[2],
                self.tmp_keys[3] ^ self.tmp_keys[4] ^ self.tmp_keys[5]
            ])

        self.K = []
        for _ in range(8):
            self.K.extend(self.tmp_keys[:])

        self.mode = mode

    def get_key_chunks_counts(self, key):
        l = len(bin(key)[2:])
        l &= (1 << 256) - 1
        if 256 >= l > 192:
            return 8
        elif 192 >= l > 128:
            return 6
        elif l <= 128:
            return 4

    def rot_hi(self, u):
        if u < 1 << 31:
            return (2 * u) % (1 << 32)
        else:
            return (2 * u + 1) % (1 << 32)

    def rot_hi_r(self, u, r):
        result = u
        for i in range(r):
            result = self.rot_hi(result)
        return result

    def square_plus(self, u, v):
        return (u + v) % (1 << 32)

    def square_minus(self, u, v):
        return (u - v) % (1 << 32)

    def L(self, X, Y):
        l = len(bin(X)) - 2
        res = int(bin(Y)[2:l + 2], base=2)
        return Y

    def G(self, r, word):
        mask = (1 << 8) - 1
        final = 0
        for i in range(4):
            part = word & mask
            word >>= 8
            r = part & 0x0F
            l = (part & 0xF0) >> 4
            result = H[l][r]
            result <<= 8 * i
            final += result
        return self.rot_hi_r(final, r)

    def encrypt_block(self, X):
        if self.get_key_chunks_counts(X) != 4:
            raise ValueError()
        d = X & 0xFFFFFFFF
        X >>= 32
        c = X & 0xFFFFFFFF
        X >>= 32
        b = X & 0xFFFFFFFF
        X >>= 32
        a = X

        for i in range(1, 9):
            b = b ^ self.G(5, self.square_plus(a, self.K[7 * i - 7]))
            c = c ^ self.G(21, self.square_plus(d, self.K[7 * i - 6]))
            a = self.square_minus(a, self.G(13, self.square_plus(b, self.K[7 * i - 5])))
            e = self.G(21, self.square_plus(self.square_plus(b, c), self.K[7 * i - 4])) ^ (i % (2 ** 32))
            b = self.square_plus(b, e)
            c = self.square_minus(c, e)
            d = self.square_plus(d, self.G(13, self.square_plus(c, self.K[7 * i - 3])))
            b = b ^ self.G(21, self.square_plus(a, self.K[7 * i - 2]))
            c = c ^ self.G(5, self.square_plus(d, self.K[7 * i - 1]))
            a, b = b, a
            c, d = d, c
            b, c = c, b

        return (b << 96) + (d << 64) + (a << 32) + c

    def decrypt_block(self, X):
        if self.get_key_chunks_counts(X) != 4:
            raise ValueError()
        d = X & 0xFFFFFFFF
        X >>= 32
        c = X & 0xFFFFFFFF
        X >>= 32
        b = X & 0xFFFFFFFF
        X >>= 32
        a = X

        for i in range(8, 0, -1):
            b = b ^ self.G(5, self.square_plus(a, self.K[7 * i - 1]))
            c = c ^ self.G(21, self.square_plus(d, self.K[7 * i - 2]))
            a = self.square_minus(a, self.G(13, self.square_plus(b, self.K[7 * i - 3])))
            e = self.G(21, self.square_plus(self.square_plus(b, c), self.K[7 * i - 4])) ^ (i % (2 ** 32))
            b = self.square_plus(b, e)
            c = self.square_minus(c, e)
            d = self.square_plus(d, self.G(13, self.square_plus(c, self.K[7 * i - 5])))
            b = b ^ self.G(21, self.square_plus(a, self.K[7 * i - 6]))
            c = c ^ self.G(5, self.square_plus(d, self.K[7 * i - 7]))
            a, b = b, a
            c, d = d, c
            a, d = d, a

        return (c << 96) + (a << 64) + (d << 32) + b

    def split_message(self, message):
        chunks = []
        chunk = 0
        while message:
            chunk = message & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
            chunks.append(chunk)
            message >>= 128
        return chunks

    def join_message(self, chunks):
        answer = 0
        for chunk in chunks:
            answer <<= 128
            answer += chunk
        return answer

    ############################################
    #                 Plain                    #
    ############################################
    def encrypt_block_plain(self, chunks):
        results = []

        for X in chunks:
            Y = self.encrypt_block(X)
            results.append(Y)

        return results

    def decrypt_block_plain(self, chunks):
        results = []

        for X in chunks:
            Y = self.decrypt_block(X)
            results.append(Y)

        return results

    ##############################################
    #                 Coupled                    #
    ##############################################
    def encrypt_block_coupled(self, chunks, S):
        results = []

        for X in chunks:
            Y = self.encrypt_block(X ^ S)
            results.append(Y)
            S = Y

        return results

    def decrypt_block_coupled(self, chunks, S):
        results = []

        for X in chunks:
            Y = self.decrypt_block(X) ^ S
            results.append(Y)
            S = X

        return results

    ##############################################
    #                 Gamming                    #
    ##############################################
    def encrypt_block_gamming(self, chunks, S):
        results = []

        for X in chunks:
            Y = X ^ self.L(X, self.encrypt_block(S))
            results.append(Y)
            S = Y

        return results

    def decrypt_block_gamming(self, chunks, S):
        results = []

        for X in chunks:
            Y = X ^ self.L(X, self.encrypt_block(S))
            results.append(Y)
            S = X

        return results

    ##############################################
    #                 Counter                    #
    ##############################################
    def encrypt_counter(self, chunks, S):
        results = []

        s = self.encrypt_block(S)
        for X in chunks:
            s = self.square_plus(s, 1)
            Y = X ^ self.L(X, self.encrypt_block(s))
            results.append(Y)

        return results

    def decrypt_counter(self, chunks, S):
        return self.encrypt_counter(chunks, S)

    def encrypt(self, message: str, **kwargs):
        plain_msg = int.from_bytes(message.encode(), 'big')
        chunks = self.split_message(plain_msg)

        synchro = kwargs['S']

        if self.mode == BLOCK:
            results = self.encrypt_block_coupled(chunks, synchro)
        elif self.mode == PLAIN:
            results = self.encrypt_block_plain(chunks)
        elif self.mode == GAMMING:
            results = self.encrypt_block_gamming(chunks, synchro)
        elif self.mode == COUNTER:
            results = self.encrypt_counter(chunks, synchro)

        answer = self.join_message(results)

        return answer.to_bytes((answer.bit_length() + 7) // 8, 'big')

    def decrypt(self, message: bytes, **kwargs):
        plain_msg = int.from_bytes(message, 'big')
        chunks = reversed(self.split_message(plain_msg))

        synchro = kwargs['S']

        if self.mode == BLOCK:
            results = self.decrypt_block_coupled(chunks, synchro)
        elif self.mode == PLAIN:
            results = self.decrypt_block_plain(chunks)

        elif self.mode == GAMMING:
            results = self.decrypt_block_gamming(chunks, synchro)

        elif self.mode == COUNTER:
            results = self.decrypt_counter(chunks, synchro)

        answer = self.join_message(reversed(results))
        return answer.to_bytes((answer.bit_length() + 7) // 8, 'big').decode()
