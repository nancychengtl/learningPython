#-*- coding: utf-8 -*-
def print_two(*args):
    #That tells Python to take all the arguments to the function and then put them in args as a list.
    #we do not use it usually, instead, we use arg1, arg2 in the parenthesis
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" %(arg1, arg2)
print_two("happyy", "rrrrr")

#指數函數
def power(base, exponent):
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)
power(37,4)

#函數互相呼叫
def one_good_turn(n):
    return n + 1

def deserves_another(m):
    return one_good_turn(m) + 2
#沒有參數時，仍然需要保留()


import math

print math.sqrt(25) #取平方根

#function import
#只從module裡引入特定function
#from module import function
#就可以把上面的引入改為

from math import sqrt
print sqrt(5)

#也可以引入所有function
from math import *
#就都不需要打math.
#找出module中所有function
import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!

# 數字函數介紹
def biggest_number(*args):
    print max(args)
    return max(args)

def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)
#告訴你變數的型別
print type(42)
print type(4.2)
print type('abc')

print "************ functional programming ************"
# 可以pass functions如同參數或值一樣
lambda x: x % 3 == 0
'''
等同於
def by_three(x):
    return x % 3 == 0
'''

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)