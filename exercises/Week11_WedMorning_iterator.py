"""
Wednesday Morning Exercise

Let's look at the following generator:

def gen():
    for i in range(2):
        for j in range(3):
            yield (i, j)

If we print all yielded values, we'll get

(0, 0)
(0, 1)
(0, 2)
(1, 0)
(1, 1)
(1, 2)

For a given parameter list N you must return an iterator, 
which goes through all possible tuples A, where Ai changes from 0 to Ni.
"""

#Solution 1

from itertools import product

def multiiter(*values):
    return product(*(range(val) for val in values))

#Solution 2 - Thanks Mike F!

def product(*args):
	pools = [tuple(range(pool)) for pool in args] 

	result = [[]]
	for pool in pools:
		result = [x+[y] for x in result for y in pool]
	for prod in result:
		yield tuple(prod)

# print len([i for i in product(1,2,3,5)])
print [i for i in product(1,2,3)]
print product(1,2,3)
