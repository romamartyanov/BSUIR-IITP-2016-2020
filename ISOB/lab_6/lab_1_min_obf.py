import os
U=str
e=IOError
o=int
S=input
H=os.path
import argparse
y=argparse.ArgumentParser
from lab_1_caesar import Caesar
from lab_1_vigener import Vigener
def f():
 h=y()
 h.add_argument('--code',type=U,default='caesar',help="'caesar' or 'vigener'")
 h.add_argument('--mode',type=U,default='encode',help="'decode' or 'encode'")
 h.add_argument('--input_file',type=U,default='',help='Input file path')
 h.add_argument('--export_file',type=U,default='',help='Export file path (not existing file)')
 return h.parse_known_args()
def D(s):
 if s.input_file!='':
  if not H.exists(s.input_file):
   raise e("File don't exist")
 else:
  raise e("File don't exist")
 if s.export_file!='':
  pass
 else:
  raise e("File is exist")
 if s.code=='caesar' or s.code=='vigener':
  pass
 else:
  raise e("Incorrect mode")
 if s.mode=='encode' or s.mode=='decode':
  pass
 else:
  raise e("Incorrect mode")
if __name__=='__main__':
 s,_=f()
 D(s)
 if s.code=='caesar':
  b=Caesar()
  b.input_file=s.input_file
  b.output_file=s.export_file
  l=o(S("Enter the key: "))
  if s.mode=='encode':
   b.encode(l)
  else:
   b.decode(l)
 elif s.code=='vigener':
  J=Vigener()
  J.input_file=s.input_file
  J.output_file=s.export_file
  l=S("Enter the key: ")
  if s.mode=='encode':
   J.encode(l)
  else:
   J.decode(l)
# Created by pyminifier (https://github.com/liftoff/pyminifier)

