# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 13:32:00 2014

@author: sophie
"""

def exclusive_or_dict(d1,d2):
    diff_key = set(d1)^set(d2)
    d3 = dict(d1.items() + d2.items())
    d4 = {}
    for i in diff_key:
        d4[i] = d3[i]
    return d4
   
print exclusive_or_dict({'a':5, 'b':3}, {'a':7, 'c':3})