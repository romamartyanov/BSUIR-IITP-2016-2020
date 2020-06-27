K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]


def rotate_right(num, shift, size=32):
    return (num >> shift) | (num << size - shift)


def sha256(sha256_text):
    sha256_text = bytearray(sha256_text)
    length = len(sha256_text) * 8
    sha256_text.append(0x80)

    while (len(sha256_text) * 8 + 64) % 512 != 0:
        sha256_text.append(0x00)

    sha256_text += length.to_bytes(8, 'big')

    blocks = []
    for i in range(0, len(sha256_text), 64):
        blocks.append(sha256_text[i:i + 64])

    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h5 = 0x9b05688c
    h4 = 0x510e527f
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19

    for message_block in blocks:
        message_schedule = []
        for t in range(0, 64):
            if t <= 15:
                message_schedule.append(bytes(message_block[t * 4:(t * 4) + 4]))
            else:
                term1 = (rotate_right((int.from_bytes(message_schedule[t - 2], 'big')), 17)
                         ^ rotate_right((int.from_bytes(message_schedule[t - 2], 'big')), 19)
                         ^ ((int.from_bytes(message_schedule[t - 2], 'big')) >> 10))

                term2 = int.from_bytes(message_schedule[t - 7], 'big')

                term3 = (rotate_right((int.from_bytes(message_schedule[t - 15], 'big')), 7)
                         ^ rotate_right((int.from_bytes(message_schedule[t - 15], 'big')), 18)
                         ^ ((int.from_bytes(message_schedule[t - 15], 'big')) >> 3))

                term4 = int.from_bytes(message_schedule[t - 16], 'big')

                schedule = ((term1 + term2 + term3 + term4) % 2 ** 32).to_bytes(4, 'big')
                message_schedule.append(schedule)

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        f = h5
        g = h6
        h = h7

        for t in range(64):
            t1 = ((h + (rotate_right(e, 6) ^ rotate_right(e, 11) ^ rotate_right(e, 25))
                   + ((e & f) ^ (~e & g)) + K[t] +
                   int.from_bytes(message_schedule[t], 'big')) % 2 ** 32)

            t2 = ((rotate_right(a, 2) ^ rotate_right(a, 13) ^ rotate_right(a, 22))
                  + ((a & b) ^ (a & c) ^ (b & c))) % 2 ** 32
            h = g
            g = f
            f = e
            e = (d + t1) % 2 ** 32
            d = c
            c = b
            b = a
            a = (t1 + t2) % 2 ** 32

        h0 = (h0 + a) % 2 ** 32
        h1 = (h1 + b) % 2 ** 32
        h2 = (h2 + c) % 2 ** 32
        h3 = (h3 + d) % 2 ** 32
        h4 = (h4 + e) % 2 ** 32
        h5 = (h5 + f) % 2 ** 32
        h6 = (h6 + g) % 2 ** 32
        h7 = (h7 + h) % 2 ** 32

    return ((h0).to_bytes(4, 'big') + (h1).to_bytes(4, 'big') +
            (h2).to_bytes(4, 'big') + (h3).to_bytes(4, 'big') +
            (h4).to_bytes(4, 'big') + (h5).to_bytes(4, 'big') +
            (h6).to_bytes(4, 'big') + (h7).to_bytes(4, 'big'))


def hmac(hmac_key, hmac_text):
    i_key = bytearray()
    o_key = bytearray()

    hmac_key = hmac_key.encode()
    hmac_text = hmac_text.encode()
    block_size = 64

    if len(hmac_key) > block_size:
        hmac_key = bytearray(sha256(hmac_key))
    elif len(hmac_key) < block_size:
        i = len(hmac_key)
        while i < block_size:
            hmac_key += b"\x00"
            i += 1

    for i in range(block_size):
        i_key.append(0x36 ^ hmac_key[i])
        o_key.append(0x5C ^ hmac_key[i])
    hmac_text = bytes(o_key) + sha256(bytes(i_key) + hmac_text)
    return sha256(hmac_text).hex()


if __name__ == "__main__":
    key = "key_mzi_5"
    text = "Lab 5, MZI"

    print("Raw message: ", text)
    print("Key: ", key)

    h_key = hmac(key, text)
    print("Hash key: ", h_key)
