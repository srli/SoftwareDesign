# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:08:15 2014

@author: sophie
"""



#def check_fermat(a,b,c,n):

a = raw_input ("Input A:  ")
b = raw_input ("Input B:  ")
c = raw_input ("Input C:  ")
n = raw_input ("Input N greater than 2:  ")    

a = int(float(a))         # redundant cast
b = int(float(b))
c = int(float(c))
n = int(float(n))

x=(a**n) + (b**n)         # you could mitigate
y=(c**n)                  # these lines
    
if x == y:
    print 'Holy smokes, Fermat was wrong!'
else:
        print 'No, not right'

'''
Excellent logic; it does exactly what the prompt
asks for!

A few things:
  1. you should get in the habit of writing these
     things as functions, not pure scripts
  2. when casting int, you don't have to cast
     to float first. So doing something like:
     a = int(a) would have worked perfectly
  3. you could simply to a**n + b**n == c**n 
     in the conditional to mitigate those lines.
     However, the extra lines to make it more
     readable, so it's an issue of tradeoffs.
'''