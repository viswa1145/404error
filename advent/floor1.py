#!/bin/usr/env python

import subprocess
s = subprocess.check_output(['cat', '/home/viswanatha/python/start.py'])

sub = '('
k = ')'
a = 0
for j,i in enumerate(s):
	if a == -1:
		print a
		print j
	        break
	elif sub == i:
		a = a + 1
	elif k == i:
		 a = a - 1 
v = s.count(sub, 0)
b = s.count(k, 0)
k = v - b
print k
