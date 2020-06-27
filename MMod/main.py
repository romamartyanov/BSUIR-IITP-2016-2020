from statlib.rand.basic_rand import BasicRand
from statlib.rand.engine import JKissRandEngine, JLKiss64RandEngine


def main():
    gen = BasicRand(JLKiss64RandEngine())
    print(gen.next())


if __name__ == "__main__":
    main()
