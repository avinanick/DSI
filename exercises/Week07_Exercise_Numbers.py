'''
Monday Morning Challenge: 

For every positive integer N, there exists a unique sequence 
starting with 1 and ending with N and such that every number in 
the sequence is either the double of the preceeding number or 
the double plus 1.

For example, given N = 13, the sequence is [1, 3, 6, 13], 
because . . . :
 
 3 =  2*1 +1
 6 =  2*3
 13 = 2*6 +1

Write a function that returns this sequence given a number N. 
Try generating the elements of the resulting list in ascending 
order, i.e., without resorting to a list reversal or prependig 
the elements to a list.

Write Assert Statements for input and outputs that will test your code 

'''
#Solution 1 - Thanks Sharam!
import numpy as np

def NSeq(N):
    out=[N]
    temp=N
    while (temp>1):
        out.append(temp/2)
        temp=temp/2
    return out[::-1] 

#Solution 2 - while statement with iterators
def climb(n):
    a, b, c = n, 1, 0
    while b <= n: b <<= 1
    res = []
    while b > 1:
        b >>= 1
        c <<= 1
        if b <= a:
            c +=1
            a -= b
        res.append(c)
    return res

#Solution 3 -- binary
def climb(n):
    result = [1]
    for x in "{:b}".format(n)[1:]:
        result.append(result[-1]*2 + (x =='1'))
    return result


# Solution 3 -- currying
def climb(n):
    return [1] if n == 1 else climb(int(n/2)) + [n]

# Solution 4
# If we write the decision tree for the problem we can see
# that we can traverse upwards from any node simply by
# dividing by two and taking the floor. This would require
# a reversal of the list generated since we're building it
# backwards.
# 
# If we examine the successor function (x -> {2x, 2x + 1})
# we can deduce that the binary representation of any number
# gives us the steps to follow to generate it: if the n-th (LTR)
# bit is set, we use 2x + 1 for the next element, otherwise we
# choose 2x. This allows us to build the sequence in order.

def climb(n):
    res = []
    cur = 1
    mask = 1 << max(0, n.bit_length() - 2)

    while cur <= n:
        res.append(cur)
        cur = 2*cur + (1 if (n & mask) != 0 else 0)
        mask >>= 1

    return res
