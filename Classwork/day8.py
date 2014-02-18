# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:38:31 2014

@author: sophie
"""
from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001

#def making_sides(angle,sides):
def my_square(coordinate_x, coordinate_y, length):
    bob.x = coordinate_x
    bob.y = coordinate_y
    i = 0
#    angle_c = 60
    while i < 4:
        fd(bob, dist=length)
        lt(bob, angle=90)
        i += 1
    
#my_square(0,0,20)

def my_regular_polygon(coordinate_x, coordinate_y, length, sides):
    bob.x = coordinate_x
    bob.y = coordinate_y
    poly_angle = 360.0/sides
    i = 0
    while i < sides:
        fd(bob, dist=length)
        lt(bob, angle=poly_angle)
        i += 1

#my_regular_polygon(0,0,4,100)

def my_circle(coordinate_x, coordinate_y, radius):
    side_length = (2*pi*radius)/100
    my_regular_polygon(coordinate_x, coordinate_y, side_length, 100)

#my_circle(50,50,60)

def snow_flake_side(turtle, l, level):
    """ Draw a side of the snowflake curve with side length l and recursion depth of level """
    angle_c = 60
    if level == 0:
        print "Forward"
        print l
        fd(bob, dist = l)
        return
    #fd(bob, dist=l) 
    snow_flake_side(turtle,(1.0/3)*l,level-1)
    lt(bob, angle=-1 * angle_c)
    snow_flake_side(turtle,(1.0/3)*l,level-1)
    lt(bob, angle=2*angle_c)
    snow_flake_side(turtle,(1.0/3)*l,level-1)
    lt(bob, angle=-1 * angle_c)
    snow_flake_side(turtle,(1.0/3)*l,level-1)
    lt(bob, angle=-1 * 360/level)

#snow_flake_side(bob, 300,2)

def recursive_tree(turtle, branch_length, level):
    if level == 0:
        fd(turtle, dist = branch_length)
        return
    turtle.heading = 90
    fd(turtle, dist = branch_length*0.3)
    turtle1 = Turtle()
    turtle1.x = turtle.x
    turtle1.y = turtle.y
    lt(turtle1, angle=30)
    recursive_tree(turtle1, branch_length * 0.6, level-1)
    turtle1.undraw()
    fd(turtle, dist = branch_length*0.3)
    turtle2 = Turtle()
    turtle2.x = turtle.x
    turtle2.y = turtle.y
    rt(turtle2, angle = 40)
    recursive_tree(turtle2, branch_length * 0.64, level-1)
    turtle2.undraw()
    
recursive_tree(bob, 100,1)
wait_for_user()