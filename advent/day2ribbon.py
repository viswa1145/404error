#!/bin/usr/env python


import subprocess
import sys

lap = 0
app = 0
#s = subprocess.check_output(['cat', '/home/viswanatha/python/la.py'])
with open ("/home/viswanatha/python/la2.py") as s:

#s = open ("/home/viswanatha/python/la2.py")
        temp = s.read().splitlines()
        for i in temp:
                myinput = map( lambda x: int(x) , i.split("x"))
		myinput.sort();
		print myinput
                rib = myinput[0] + myinput[0] + myinput[1] + myinput[1]
		print rib
                bir = myinput[0]*myinput[1]*myinput[2]
		print bir
                lib = rib + bir
                print lib
                app = app + lib
                print app
