'''
Monday Morning Exercise 

A number is simply made up of digits.

The number 1256 is made up of the digits 1, 2, 5, and 6.

For 1256 there are 24 distinct permuations of the digits:
	1256, 1265, 1625, 1652, 1562, 1526, 2156, 2165, 2615, 2651, 2561, 2516,
	5126, 5162, 5216, 5261, 5621, 5612, 6125, 6152, 6251, 6215, 6521, 6512.

Your goal is to write a program that takes a number, n, and returns the average 
value of all distinct permutations of the digits in n. 
- Your answer should be rounded to the nearest integer. 
- For the example above the return value would be 3889.
- n will never be negative
- Your program should be able to handle numbers up to 6 digits long
- Tip: It is fine to write helper functions
- Tip 2: Yes use additional packages to help with calculations

More tips will be provided at 15 and 20 minutes markers.

Examples:

permutation_average(2) == 2

permutation_average(25) == 39
	>>> 25 + 52 = 77
	>>> 77 / 2 = 38.5
	return 39

permutation_average(20) == 11
	>>> 20 + 02 = 22
	>>> 22 / 2 = 11
	return 11

permutation_average(737) == 629
	>>> 737 + 377 + 773 = 1887
	>>> 1887 / 3 = 629
	return 629
'''

#Solutions 1 - Thanks Mike F!

import numpy as np
from itertools import permutations

def get_permutations(number):
    number = str(number)
    numlist = list(number)
    perm_list = permutations(numlist)
    perm_list = list(perm_list)
    # print perm_list
    pl2 = []
    for i in perm_list:
        pl2.append(''.join(i))
    # print pl2
    # print perm_list
    return [float(i) for i in pl2]

# get_permutations(1234)

def get_mean(number):
    print np.mean(get_permutations(number))
    return np.mean(get_permutations(number))

get_mean(1256)

#Solution 2

import itertools 
import numpy as np

def decompose_digits(a):
    return list(map(int, str(a)))

def get_perms(num_list):
    return list(itertools.permutations(num_list))

def digitlist_to_num(digit_list):
    s = ''.join(map(str, digit_list))
    return int(s)

def permutation_average(n):
    s = decompose_digits(n)
    perm_list = get_perms(s)

    return int(round(np.mean(list(map(digitlist_to_num, perm_list)))))
