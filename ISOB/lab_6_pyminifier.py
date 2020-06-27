import subprocess
import os
from shutil import copyfile
from shutil import rmtree


def change_name(name, post):
    s = name.split('.')
    return s[0] + post + '.' + s[1]


# https://github.com/liftoff/pyminifier

file_name = "lab_1.py"
directory = "lab_6"
current = os.getcwd()

if not os.path.exists(os.path.join(current, directory)):
    os.makedirs(os.path.join(current, directory))

copyfile(os.path.join(current, file_name), os.path.join(current, directory, file_name))

os.system(
    'pyminifier ' + os.path.join(current, directory, file_name)
    + ' >> ' + os.path.join(current, directory, change_name(file_name, '_min')))
os.system(
    'pyminifier -O ' + os.path.join(current, directory, file_name)
    + ' >> ' + os.path.join(current, directory, change_name(file_name, '_min_obf')))
