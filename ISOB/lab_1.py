import os
import argparse
from lab_1_caesar import Caesar
from lab_1_vigener import Vigener


def parse_args():
    """
    Parsing arguments

    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--code',
        type=str,
        default='caesar',
        help="'caesar' or 'vigener'")

    parser.add_argument(
        '--mode',
        type=str,
        default='encode',
        help="'decode' or 'encode'")

    parser.add_argument(
        '--input_file',
        type=str,
        default='',
        help='Input file path')

    parser.add_argument(
        '--export_file',
        type=str,
        default='',
        help='Export file path (not existing file)')

    return parser.parse_known_args()


def check_args_errors(FLAGS):
    """
    Checking errors in arguments

    :param FLAGS:
    :return:
    """
    if FLAGS.input_file != '':
        if not os.path.exists(FLAGS.input_file):
            raise IOError("File don't exist")
    else:
        raise IOError("File don't exist")

    if FLAGS.export_file != '':
        # if os.path.exists(FLAGS.export_file):
        #     raise IOError("File is exist")
        pass
    else:
        raise IOError("File is exist")

    if FLAGS.code == 'caesar' or FLAGS.code == 'vigener':
        pass
    else:
        raise IOError("Incorrect mode")

    if FLAGS.mode == 'encode' or FLAGS.mode == 'decode':
        pass
    else:
        raise IOError("Incorrect mode")


if __name__ == '__main__':
    FLAGS, _ = parse_args()
    check_args_errors(FLAGS)

    if FLAGS.code == 'caesar':
        caesar = Caesar()
        caesar.input_file = FLAGS.input_file
        caesar.output_file = FLAGS.export_file

        key = int(input("Enter the key: "))

        if FLAGS.mode == 'encode':
            caesar.encode(key)
        else:
            caesar.decode(key)

    elif FLAGS.code == 'vigener':
        vigener = Vigener()
        vigener.input_file = FLAGS.input_file
        vigener.output_file = FLAGS.export_file

        key = input("Enter the key: ")

        if FLAGS.mode == 'encode':
            vigener.encode(key)
        else:
            vigener.decode(key)
