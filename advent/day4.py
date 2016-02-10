#!/usr/bin/python

import hashlib

INPUT = "iwrupvqb" ## give your input

num = 0

def get_md5(i):
    h = hashlib.new('md5')
    h.update(i)
    return h.hexdigest()

while True:
    md5 = get_md5("%s%i" % (INPUT, num))
#    print(md5, num)
    if md5[:6] == "000000": ### for five zeroes please give md5[:5] == "00000"
        quit("The answer is %i" % num)
    else:
        num += 1
