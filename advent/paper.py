viswanatha@viswanatha-3446:~/python$ python
Python 2.7.3 (default, Jun 22 2015, 19:33:41) 
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> input = "4x23x21"
>>> myinput = input.split("x")
>>> myinput
['4', '23', '21']
>>> area = 2*(myinput[0]*myinput[1] + myinput[1]*myinput[2] + myinput[2]*myinput[0])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>> myinput = map( lambda x: int(x) input.split("x"))
  File "<stdin>", line 1
    myinput = map( lambda x: int(x) input.split("x"))
                                        ^
SyntaxError: invalid syntax
>>> myinput = map( lambda x: int(x) ,input.split("x"))
>>> myinput
[4, 23, 21]
>>> area = 2*(myinput[0]*myinput[1] + myinput[1]*myinput[2] + myinput[2]*myinput[0])
>>> area
1318
>>> myinput.sort()
>>> myinput
[4, 21, 23]
>>> sides = [myinput[0]*myinput[1] ,myinput[1]*myinput[2] ,myinput[2]*myinput[0]]
>>> sides       
[84, 483, 92]
>>> area = 2*(sides[0] + sides[1] + sides[2])
>>> area
1318
>>> sides.sort()
>>> sides
[84, 92, 483]
>>> total_paper = area + sides[0]
>>> total_paper
1402
>>> 



sed ':a;$!{N;s/\n/ /;ba;}' 
