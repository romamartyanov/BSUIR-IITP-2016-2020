import random
from hashlib import sha256


def co_prime(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


# Euclid's extended algorithm for finding the multiplicative inverse of two numbers
def mod_inv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % m


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


def generate_key_pair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q

    # Phi is the totient of n
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = co_prime(e, phi)

    while g != 1:
        e = random.randrange(1, phi)
        g = co_prime(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = mod_inv(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return (e, n), (d, n)


def encrypt(private_key, plain_text):
    # Unpack the key into it's components
    key, n = private_key

    # Convert each letter in the plaintext to numbers based on the character using a^b mod m

    number_repr = [ord(char) for char in plain_text]
    print("Number representation before encryption: ", number_repr)
    cipher = [pow(ord(char), key, n) for char in plain_text]

    # Return the array of bytes
    return cipher


def decrypt(public_key, cipher_text):
    # Unpack the key into its components
    key, n = public_key

    # Generate the plaintext based on the ciphertext and key using a^b mod m
    number_repr = [pow(char, key, n) for char in cipher_text]
    plain = [chr(pow(char, key, n)) for char in cipher_text]

    print("Decrypted number representation is: ", number_repr)

    # Return the array of bytes as a string
    return ''.join(plain)


def hash_function(message):
    hashed = sha256(message.encode("UTF-8")).hexdigest()
    return hashed


def verify(received_hashed, message):
    our_hashed = hash_function(message)
    if received_hashed == our_hashed:
        print("Verification successful!")
        return True

    else:
        print("Verification failed!")
        return False
