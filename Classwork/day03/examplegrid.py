# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:04:00 2014

@author: sophie"""

# raw_input() reads every input as a string
# then it's up to you to process the string
str1 = raw_input("Enter anything:")
print "raw_input =", str1
# input() actually uses raw_input() and then tries to
# convert the input data to a number using eval()
# hence you could enter a math expression
# gives an error if input is not numeric eg. $34.95
x = input("Enter a number:")
print "input =", x