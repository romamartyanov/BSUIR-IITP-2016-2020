from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import DES, DES3
from Crypto import Random


def des_encrypt(key, msg, pad_block_size=8):
    cipher = DES.new(key, DES.MODE_ECB)
    msg = cipher.encrypt(pad(msg.encode('utf-8'), pad_block_size))
    return msg


def des_decrypt(key, msg, pad_block_size=8):
    decipher = DES.new(key, DES.MODE_ECB)
    msg = decipher.decrypt(msg)
    msg = unpad(msg, pad_block_size).decode('utf-8')
    return msg


def prepare_des_key(key, pad_block_size=8):
    return pad(key.encode('utf-8'), pad_block_size)


def des3_encrypt(key, iv, msg, pad_block_size=8):
    encipher = DES3.new(key, DES3.MODE_OFB, iv)
    msg = encipher.encrypt(pad(msg.encode('utf-8'), pad_block_size))
    return msg


def des3_decrypt(key, iv, msg, pad_block_size=8):
    decipher = DES3.new(key, DES3.MODE_OFB, iv)
    msg = decipher.decrypt(msg)
    msg = unpad(msg, pad_block_size).decode('utf-8')
    return msg


def prepare_des3_key(key, pad_key_size=16):
    return pad(key.encode('utf-8'), pad_key_size)


def prepare_iv(pad_block_size=8):
    return Random.new().read(pad_block_size)  # DES3.block_size==8
