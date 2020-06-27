# lab 1
import os
import subprocess

paths = [line[2:] for line in subprocess.check_output("find . -iname '*.txt'", shell=True).splitlines()]

with open('output.txt', 'a') as out_file:
    for path in paths:
        path = path.decode("utf-8")
        out_file.write(path + '\n')

# lab 2


max_size = 0
for dirpath, dirnames, filenames in os.walk(os.path.dirname(os.path.abspath(__file__))):
    for f in filenames:
        fp = os.path.join(dirpath, f)
        try:
            cur_size = os.path.getsize(fp)
        except:
            continue
        if cur_size > max_size:
            max_size = cur_size
print(max_size)
print()


# lab 3

class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


d = Deque()
print(d.is_empty())

d.add_rear(4)
d.add_rear('dog')
d.add_front('cat')
d.add_front(True)
print(d.size())
print(d.is_empty())

d.add_rear(8.4)
print(d.remove_rear())
print(d.remove_front())

print(d.items)
