'''

Flatten a nested list structure

- try to do so with the least amount of code


from itertools import chain
'''

#Solution 1
def flatten(lol):
    return list(chain(*lol))


# Solution 2 - Thanks Mike F and Robbie
def flatten2(items, seqtypes=(list, tuple)):
    for i, x in enumerate(items):
        while i < len(items) and isinstance(items[i], seqtypes):
            items[i:i+1] = items[i]
    return items

print flatten2([1, 2, [3, 4, [5],['hi']], [6, [[(7, 'hello')]]]])


#Solution 3 - Thanks Shahram
def unnest(A,Out):
   i=0
   for a in A:
       if (type(a)==list):
           unnest(a,Out)
           i=i+1
       else: 
           Out.append(a)
   if (i==0):
       print Out

[9:54]  
unnest([1,2,[3,[4,3,5]]],[])