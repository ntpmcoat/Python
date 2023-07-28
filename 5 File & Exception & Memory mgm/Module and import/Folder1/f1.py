import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from Folder2 import f2

f2.name()

def age() : 
     print("19")

age()
