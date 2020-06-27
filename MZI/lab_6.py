import unittest

from src import digital_signature


class TestStringMethods(unittest.TestCase):
    def test_digital_signature(self):
        p = int(input("Enter a prime number (17, 19, 23, etc): "))
        q = int(input("Enter another prime number (Not one you entered above): "))

        print("Generating your public/private keypairs now . . .")
        public_key, private_key = digital_signature.generate_key_pair(p, q)

        print("Your public key is ", public_key, " and your private key is ", private_key)
        # message = input("Enter a message to encrypt with your private key: ")

        print("Reading text from file and hashing it")
        file_to_enc = open('resources/lab_6/digital_signature_to_enc.txt', 'r')
        normal_text = file_to_enc.read()
        print("")

        hashed = digital_signature.hash_function(normal_text)

        print("Encrypting message with private key . . .")
        encrypted_msg = digital_signature.encrypt(private_key, hashed)
        print("Your encrypted hashed message is: ", ''.join(map(lambda x: str(x), encrypted_msg)), '\n')
        print("")

        print("Decrypting message with public key . . .")
        decrypted_msg = digital_signature.decrypt(public_key, encrypted_msg)
        print("Your decrypted message is:")
        print(decrypted_msg)
        print("")

        decrypted_file = open('resources/lab_6/digital_signature_decrypted.txt', 'w')
        decrypted_file.write(decrypted_msg)

        print("Verification process . . .")
        status = digital_signature.verify(decrypted_msg, normal_text)

        self.assertTrue(status)


if __name__ == '__main__':
    unittest.main()
