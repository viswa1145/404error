#!/bin/usr/env python

n = 0
d = 0
with open ("/home/viswanatha/python/dd.py") as tmp:
	text = tmp.read().splitlines()
	for s in text: ## part 1
		if 'ab' in s or 'cd' in s or 'pq' in s or 'xy' in s:
			continue
		if (s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')) < 3:
			continue
		for i in range(0, len(s)-1):
			if s[i] == s[i+1]:
				n += 1
				break

	print(n)

	for s in text: ## Part 2
        	for i in range(0, len(s)-2):
            		if s[i] == s[i+2]:
                		break
        	else:
            		continue

        	for i in range(0, len(s)-1):
            		if s.count(s[i] + s[i+1]) > 1:
                		d += 1
                		break
        	else:
            		continue
	print (d)


