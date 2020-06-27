import unittest

import rsa
import rsa_crypto


class TestStringMethods(unittest.TestCase):

    def test_rsa(self):
        # 1. Generating key pair
        public_key, private_key = rsa.generate_rsa_key_pair(13, 17)

        # 2. Open file 'rsa_to_enc.txt' & read text
        file_to_enc = open('resources/lab_3/rsa_to_enc.txt', 'r')
        normal_text = file_to_enc.read()

        # 3. Encrypt read text
        encrypted_text = rsa.rsa_encrypt(public_key, normal_text)

        print(''.join(map(lambda x: str(x), encrypted_text)))

        # 4. Encrypt decrypted text
        decrypted_text = rsa.rsa_decrypt(private_key, encrypted_text)

        # 5. Save decrypted text to 'decrypted.txt'
        decrypted_file = open('resources/lab_3/rsa_decrypted.txt', 'w')
        decrypted_file.write(decrypted_text)

        self.assertEqual(normal_text, decrypted_text)

    def test_rsa_crypto(self):
        # 1. Generating key pair
        rsa_crypto.generate_rsa_key_pair()

        # 2. Open file 'rsa_to_enc.txt' & read text
        file_to_enc = open('resources/lab_3/rsa_crypto_to_enc.txt', 'r')
        normal_text = file_to_enc.read()

        # 3. Encrypt read text
        encrypted_text = rsa_crypto.rsa_encrypt(normal_text)

        print(''.join(map(lambda x: str(x), encrypted_text)))

        # 4. Encrypt decrypted text
        decrypted_text = rsa_crypto.rsa_decrypt()

        # 5. Save decrypted text to 'decrypted.txt'
        decrypted_file = open('resources/lab_3/rsa_crypto_decrypted.txt', 'w')
        decrypted_file.write(decrypted_text)

        self.assertEqual(normal_text, decrypted_text)


if __name__ == '__main__':
    unittest.main()
