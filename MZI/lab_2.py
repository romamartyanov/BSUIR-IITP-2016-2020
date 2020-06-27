import unittest

from src.stb_34_101_31 import STB


class TestStringMethods(unittest.TestCase):

    def test_stb(self):
        key = 'key'
        block = 4
        synchro = 16

        stb = STB(key, block)

        # 1. Open file 'des3_to_enc.txt' & read text
        file_to_enc = open('resources/lab_2/stb_to_enc.txt', 'r')
        normal_text = file_to_enc.read()

        # 2. Encrypt read text
        encrypted_text = stb.encrypt(normal_text, S=synchro)

        print()
        print(''.join(map(lambda x: str(x), encrypted_text)))
        print()

        # 3. Encrypt decrypted text
        decrypted_text = stb.decrypt(encrypted_text, S=synchro)

        # 4. Save decrypted text to 'decrypted.txt'
        decrypted_file = open('resources/lab_2/stb_decrypted.txt', 'w')
        decrypted_file.write(decrypted_text)

        self.assertEqual(normal_text, decrypted_text)


if __name__ == '__main__':
    unittest.main()
