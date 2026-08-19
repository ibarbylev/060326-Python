import sys
print("sys.path[0]:", sys.path[0])

from library import greet1, greet2

greet1()
greet2()
print("main.py видит все пакеты на своём уровне.")