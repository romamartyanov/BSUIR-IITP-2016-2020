import random
import unittest

from src.el_gamal import gen_key, power, encrypt, decrypt


class TestStringMethods(unittest.TestCase):

    def test_el_gamal(self):
        # 1. Open file 'des3_to_enc.txt' & read text
        file_to_enc = open('resources/lab_4/el_gamal_to_enc.txt', 'r')
        normal_text = file_to_enc.read()

        # 2. Encrypt read text
        q = random.randint(pow(10, 20), pow(10, 50))
        g = random.randint(2, q)

        key = gen_key(q)  # Private key for receiver
        h = power(g, key, q)
        print("g used : ", g)
        print("g^a used : ", h)

        # encrypted_text = stb.encrypt(normal_text, S=synchro)
        encrypted_text, p = encrypt(normal_text, q, h, g)

        print()
        print(''.join(map(lambda x: str(x), encrypted_text)))
        print()

        # 3. Encrypt decrypted text
        # decrypted_text = stb.decrypt(encrypted_text, S=synchro)
        decrypted_text = decrypt(encrypted_text, p, key, q)
        decrypted_text = ''.join(decrypted_text)

        # 4. Save decrypted text to 'decrypted.txt'
        decrypted_file = open('resources/lab_4/el_gamal_decrypted.txt', 'w')
        decrypted_file.write(decrypted_text)

        self.assertEqual(normal_text, decrypted_text)


if __name__ == '__main__':
    unittest.main()
