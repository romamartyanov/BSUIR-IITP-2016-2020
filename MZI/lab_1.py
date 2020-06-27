import unittest
from src.des import des_decrypt, des_encrypt, prepare_des_key
from src.des import des3_decrypt, des3_encrypt, prepare_des3_key, prepare_iv


class TestStringMethods(unittest.TestCase):

    def test_des(self):
        key = 'key'
        block_size = 8
        key = prepare_des_key(key, block_size)

        # 1. Open file 'des3_to_enc.txt' & read text
        file_to_enc = open('resources/lab_1/des_to_enc.txt', 'r')
        normal_text = file_to_enc.read()

        # 2. Encrypt read text
        encrypted_text = des_encrypt(key, normal_text, block_size)

        print()
        print(''.join(map(lambda x: str(x), encrypted_text)))
        print()

        # 3. Encrypt decrypted text
        decrypted_text = des_decrypt(key, encrypted_text, block_size)

        # 4. Save decrypted text to 'decrypted.txt'
        decrypted_file = open('resources/lab_1/des_decrypted.txt', 'w')
        decrypted_file.write(decrypted_text)

        self.assertEqual(normal_text, decrypted_text)

    def test_des3(self):
        key = 'key'
        key_size = 16
        block_size = 8

        key = prepare_des3_key(key, key_size)
        iv = prepare_iv(block_size)

        # 1. Open file 'des3_to_enc.txt' & read text
        file_to_enc = open('resources/lab_1/des3_to_enc.txt', 'r')
        normal_text = file_to_enc.read()

        # 2. Encrypt read text
        encrypted_text = des3_encrypt(key, iv, normal_text)

        print()
        print(encrypted_text)
        print()

        # 3. Encrypt decrypted text
        decrypted_text = des3_decrypt(key, iv, encrypted_text)

        # 4. Save decrypted text to 'decrypted.txt'
        decrypted_file = open('resources/lab_1/des3_decrypted.txt', 'w')
        decrypted_file.write(decrypted_text)

        self.assertEqual(normal_text, decrypted_text)


if __name__ == '__main__':
    unittest.main()
