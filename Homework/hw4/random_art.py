# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: sophie li wat is recursion how do i do it
omg why
why
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image
from math import *

#
#def snow_flake_side(turtle, l, level):
#    """ Draw a side of the snowflake curve with side length l and recursion depth of level """
#    angle_c = 60
#    if level == 0:
#        print "Forward"
#        print l
#        fd(bob, dist = l)
#        return
#    #fd(bob, dist=l) 
#    snow_flake_side(turtle,(1.0/3)*l,level-1)
#    lt(bob, angle=-1 * angle_c)
#    snow_flake_side(turtle,(1.0/3)*l,level-1)
#    lt(bob, angle=2*angle_c)
#    snow_flake_side(turtle,(1.0/3)*l,level-1)
#    lt(bob, angle=-1 * angle_c)
#    snow_flake_side(turtle,(1.0/3)*l,level-1)
#    lt(bob, angle=-1 * 360/level)

#snow_flake_side(bob, 300,2)

def build_random_function(min_depth, max_depth):
        # your doc string goes here
    hello = ['x','y']
    func = ['x','y','cos_pi','sin_pi','prod']
    if max_depth == 1:
        return hello[randint(0,1)]
    else:
        block = func[randint(2,4)]
        if block == 'prod':
            return [block, build_random_function(min_depth-1, max_depth-1), build_random_function(min_depth-1, max_depth-1)]
        elif not block == 'prod':
           return [block, build_random_function(min_depth-1, max_depth-1)] 
    
#print build_random_function(2,5)

def evaluate_random_function(f, x, y):
    
    func1 = f[0]
    
    if func1 == 'x':
        return x
    elif func1 == 'y':
        return y
        
    func2 = f[1]


    
    if func1 == 'prod':
        func3 = f[2]
     
        
    elif func1 == 'cos_pi':
        return cos(pi*evaluate_random_function(func2,x,y))
    elif func1 == 'sin_pi':
        return sin(pi*evaluate_random_function(func2,x,y))
    elif func1 == 'prod':
        return evaluate_random_function(func2,x,y)*evaluate_random_function(func3,x,y)

    

    # your code goes here

print evaluate_random_function(['sin_pi', ['cos_pi', ['cos_pi', ['sin_pi', ['y']]]]],0.1,0.9)
#def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
#    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
#        to the output interval [output_interval_start, output_interval_end].  The mapping
#        is an affine one (i.e. output = input*c + b).
#    
#        TODO: please fill out the rest of this docstring
#    """
#    # your code goes here
#    