from operator import xor, add
from itertools import permutations
import time

start = time.clock()

f = open("Problem59.txt")
f = f.readline()
f = f.split(",")

def apply_password(chars, passwd):
    currpswd = 0
    decrypted = []
    for i in chars:
        if currpswd == len(passwd):
            currpswd = 0
        decrypted.append(xor(int(i), ord(passwd[currpswd])))
        currpswd += 1
    return decrypted

for i in permutations('abcdefghijklmnopqrstuvwxyz', 3):
    phrase = ''.join([chr(j) for j in apply_password(f, i)])
    words = phrase.split(" ")
    if "the" in words:
        print reduce(add, [ord(j) for j in list(phrase)])
        break

print time.clock() - start
