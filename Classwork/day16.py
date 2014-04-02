# -*- coding: utf-8 -*-
""" 
Created on Wed Mar 26 23:07:27 2014

@author: pruvolo is awesome! hi paul! :)
"""

import pygame
from pygame.locals import *
import time

class Polygon(object):
    def __init__(self,vertices):
        self.vertices = vertices
        
    def draw(self, screen):
        for i in range(len(self.vertices)):
            j = (i+1)%len(self.vertices)
            pygame.draw.line(screen, pygame.Color(0,0,0),(self.vertices[i][0], self.vertices[i][1]),(self.vertices[j][0],self.vertices[j][1]))

class Quadrilateral(Polygon):
    """ Represents a quadrilateral that can draw itself to a Pygame window """
    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
        super(Quadrilateral,self).__init__([(x1,y1),(x2,y2),(x3,y3),(x4,y4)])

class Rectangle(Quadrilateral):
    def __init__(self,x_ul,y_ul,width,height):
        super(Rectangle, self).__init__(x_ul, y_ul, x_ul +width, y_ul, x_ul + width, y_ul+height, x_ul, y_ul+height)

class Square(Rectangle):
    def __init__(self,x_ul,y_ul,side_length):
        super(Square, self).__init__(x_ul,y_ul, side_length,side_length)
        
if __name__ == '__main__':
    pygame.init()
    

    size = (640,480)
    screen = pygame.display.set_mode(size)

    quad = Quadrilateral(100,100,200,90,200,300,100,300)
    rect = Rectangle(300,300,100,50)
    square = Square(400,100,20)
    triangle = Polygon([(250,250),(300,200),(350,250)])
    running = True

    while running:
        screen.fill(pygame.Color(255,255,255))
        quad.draw(screen)
        rect.draw(screen)
        square.draw(screen)
        triangle.draw(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        time.sleep(.01)
        pygame.display.update()

    pygame.quit()