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
		sides = [myinput[0]*myinput[1] ,myinput[1]*myinput[2] ,myinput[2]*myinput[0]]
#		sides.sort();
		area = 2*(sides[0] + sides[1] + sides[2])
		per = area + sides[0]
		lap = lap + per
#		print lap
		rib = myinput[0] + myinput[0] + myinput[1] + myinput[1]
		bir = myinput[0]*myinput[1]*myinput[2]
		lib = rib + bir
#		print lib
		app = app + lib
		print app
