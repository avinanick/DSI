'''
Wednesday Morning Exercise

Create a function add(n) which returns a function 
that always adds n to any number. You cannot use global 
variables.

Example outputs: 

	addOne = add(1)
	addOne(3) # 4

	addThree = add(3)
	addThree(3) # 6

	addThree = partial(adder, x=3)
	addThree(3) # 6

'''

#Solution
from functools import partial

def adder(x, y):
    return x+y

def add(x):
    return partial(adder, x)



'''
Additional explanation of functools partial:

	What functools.partial does is:

	Makes a new version of a function with one or more arguments
	already filled in.
	New version of a function documents itself.

Use in scenarios where you may know only one argument of many

Another exercise to reinforce the problem: 
	>>> from functools import partial

	>>> def fnx(a, b, c):
	      return a + b + c

	>>> fnx(3, 4, 5)
	      12

Answer: 
you have to choose, explicit or positional. 
both will not work

>>> pfnx = partial(fnx, a=12, b=4)

>>> pfnx(c=5)
     21


'''







