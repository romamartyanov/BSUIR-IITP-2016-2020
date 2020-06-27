"""A program that encodes and decodes hidden messages in images through LSB steganography"""

from src import steganography

if __name__ == '__main__':
    mode = input('You want to "encode" or to "decode" image?: ')

    if mode == 'encode':
        normal_image_path = input('Enter the path to normal image: ')
        encoded_image_path = input('Enter the path to encoded (output) image: ')
        text_for_encoding = input('Enter the text for encoding: ')

        steganography.encode_image(text_for_encoding, normal_image_path, encoded_image_path)

    elif mode == 'decode':
        encoded_image_path = input('Enter the path to encoded (input) image: ')
        decoded_image_path = input('Enter the path to decoded (output) image: ')

        steganography.decode_image(encoded_image_path, decoded_image_path)
