#-*- coding: utf-8 -*-
#list 用append
# n.pop(index) will remove the item at index from the list
# n.remove(item) will remove the actual item if it finds it
# del(n[1]) is like .pop in that it will remove the item at the given index, but it won't return it

n = [1, 3, 5]
n.pop(0)
print n
n.append(6)
print n
n.remove(3)
print n

# list也可以直接當做function中的一個參數
def list_extender(x):
    x.append(9)
    #如果是兩個list合併，直接用+
    return x
print list_extender(n)

#print 所有list中的element
def print_list(x):
    for i in range(0, len(x)):
    #或者用for item in list: 也可以，但用本來的方法才可以修改list
        print x[i]
print_list(n)

#range可以自動產生list
'''
range(stop)
range(start, stop)
range(start, stop, step)
range(6) # => [0,1,2,3,4,5]
range(1,6) # => [1,2,3,4,5]
range(1,6,3) # => [1,4]
'''

# list comprehension
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

even_squares = [x**2 for x in range(1,12) if x % 2 == 0]
print even_squares

print "*********** List slicing ***********"
#[start:end:stride]
'''
The default starting index is 0.
The default ending index is the end of the list.
The default stride is 1.
'''
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2] #[9, 25, 49, 81]

to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:]
#start count start from 0
# prints ['D', 'E']

print to_five[:2]
#end count start from 1
# prints ['A', 'B']

print to_five[::2]
# print ['A', 'C', 'E']

#Reversing a List
letters = ['A', 'B', 'C', 'D', 'E']
print letters[::-1]
['E', 'D', 'C', 'B', 'A']
