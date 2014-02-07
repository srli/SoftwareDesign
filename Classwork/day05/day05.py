# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 13:33:08 2014

@author: sophie
"""

def sum_list(N):
    index = 0
    while index < len(N):
        total = sum(N[0:index+1])
        print total
        index = index + 1
        
sum_list([1, 2, 3])


#
#import unum
#from unum import Unum
#from unum.units import *
#unit = Unum.unit
#
#mower = (100.0 * m * m) / (300.0 * s)
#
#print mower.asUnit((mile*mile)/h)
#
#def hinge(n):
#    if n < 0:
#        return 0
#    else:
#        return n
#
#print "When n = -4 hinge returns",
#print hinge(-4)
#print "When n = 5 hinge returns",
#print hinge(5)
#
#
#def print_number_of_days(n):
#    if n == 1:
#        print "Input is 1 day."
#    else:
#        print "Input is",
#        print n ,
#        print "days"
#        
#print print_number_of_days(1)
#print print_number_of_days(3)