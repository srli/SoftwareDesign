# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: sophie li wat is recursion how do i do it
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image

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
    
    depth = randint(min_depth, max_depth)
    x = build_random_function(min_depth, max_depth-1)
    y = build_random_function(min_depth, max_depth-1)
    hello = ['x','y']
    f = []
    if depth == 0:
        return hello
    blocks = [x,y,['cos_pi', x],['sin_pi', x],['prod',x,y]]
    return f = f[blocks[randint(0,4)]]

print build_random_function(2,5)

#def evaluate_random_function(f, x, y):
#    # your doc string goes here
#
#    # your code goes here
#
#def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
#    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
#        to the output interval [output_interval_start, output_interval_end].  The mapping
#        is an affine one (i.e. output = input*c + b).
#    
#        TODO: please fill out the rest of this docstring
#    """
#    # your code goes here
#    