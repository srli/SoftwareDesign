# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:59:46 2014

@author: sophie
"""

x = raw_input ("Input x:  ")
y = raw_input ("Input y:  ")


x = int(float(x))
y = int(float(y))
   
if x > y:
    print '1'
elif x == y:
    print 'No, not right'
elif x < y:               # would have used else: 
    print '-1'

'''
Mostly the same comments as check_fermat.

I personally would have used an else: statement
for closure around the if statement.
'''