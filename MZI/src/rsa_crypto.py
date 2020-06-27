from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes


def generate_rsa_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    file_out = open("resources/lab_3/keys/private.pem", "wb")
    file_out.write(private_key)

    public_key = key.publickey().export_key()
    file_out = open("resources/lab_3/keys/receiver.pem", "wb")
    file_out.write(public_key)


#############
def rsa_encrypt(data):
    # data = "I met aliens in UFO. Here is the map.".encode("utf-8")
    file_out = open("resources/lab_3/rsa_crypto_encrypted_data.bin", "wb")

    recipient_key = RSA.import_key(open("resources/lab_3/keys/receiver.pem").read())
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data.encode("utf-8"))
    [file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]

    return ciphertext


#################

def rsa_decrypt():
    file_in = open("resources/lab_3/rsa_crypto_encrypted_data.bin", "rb")

    private_key = RSA.import_key(open("resources/lab_3/keys/private.pem").read())

    enc_session_key, nonce, tag, ciphertext = \
        [file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]

    # Decrypt the session key with the private RSA key
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    # Decrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    return data.decode("utf-8")
