# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:32:51 2014

@author: sophie
"""

def sum_of_squares(N):
    res = []
    i = 1
    while i <= N:
        res.append(i**2)
        i = i + 1
    return sum(res)

print sum_of_squares(4)

def filter_out_negative_numbers(N):
    res = []
    i = 0
    while i < len(N):
        if N[i] > 0:
            res.append(N[i])
            i += 1
        else:
            i += 1
    return res

print filter_out_negative_numbers([-2,5,10,-100,5])