import os

from src.elliptic_curve_diffie_hellman.elliptic import *
from src.elliptic_curve_diffie_hellman.finitefield.finitefield import FiniteField


def generate_secret_key(num_bits):
    return int.from_bytes(os.urandom(num_bits // 8), byteorder='big')


def send_dh(private_key, generator, send_function):
    return send_function(private_key * generator)


def receive_dh(private_key, receive_function):
    return private_key * receive_function()


def slow_order(point):
    Q = point
    i = 1
    while True:
        if type(Q) is Ideal:
            return i
        else:
            Q = Q + point
            i += 1


if __name__ == "__main__":
    F = FiniteField(3851, 1)

    # Totally insecure curve: y^2 = x^3 + 324x + 1287
    curve = EllipticCurve(a=F(324), b=F(1287))

    # order is 1964
    basePoint = Point(curve, F(920), F(303))

    aliceSecretKey = generate_secret_key(8)
    bobSecretKey = generate_secret_key(8)

    print('Secret keys are %d, %d' % (aliceSecretKey, bobSecretKey))

    alicePublicKey = send_dh(aliceSecretKey, basePoint, lambda x: x)
    bobPublicKey = send_dh(bobSecretKey, basePoint, lambda x: x)

    sharedSecret1 = receive_dh(bobSecretKey, lambda: alicePublicKey)
    sharedSecret2 = receive_dh(aliceSecretKey, lambda: bobPublicKey)
    print('Shared secret is %s == %s' % (sharedSecret1, sharedSecret2))

    print('extracing x-coordinate to get an integer shared secret: %d' % sharedSecret1.x.n)
