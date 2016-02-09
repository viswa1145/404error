import sys

def get_code(c, x, y):
	if c == '^':
		y += 1
	elif c == 'v':
		y -= 1
	elif c == '<':
		x += 1
	elif c == '>':
		x -= 1
	return (x, y)


with open ("/home/viswanatha/python/ls.py") as s :
	tmp = s.read()



vi = []
x = 0
y = 0
a = 0
b = 0
 
	
for j, line in enumerate(tmp):
	if j % 2 ==0:
		x, y = get_code(line, x, y)
#		print x, y
		vi.append((x, y))
	else:
		a, b = get_code(line, a, b)
		vi.append((a, b))

print len(set(vi))


