#-*- coding: utf-8 -*-
from sys import argv

script, first, second, third = argv

print "how old are you?"
# read input
age = raw_input()
print "you are %s years old, live in Taipei for %s years" %(age, age)

print "the script is:", script
print "the first one is:", first
print "the second one is:", second
print "the third one is:", third

# execute with four parameters: python ex13.py first 2nd 3rd
