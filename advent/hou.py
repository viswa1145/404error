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
	
for line in tmp:
	x, y = get_code(line, x, y)
	print x, y
	vi.append((x, y))

print len(set(vi))


