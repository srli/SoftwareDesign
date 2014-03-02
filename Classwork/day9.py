# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 14:34:53 2014

@author: sophie
"""
#def histogram(s):
#    d = dict()
#    for c in s:
#        if c not in d:
#            d[c] = 1
#        else:
#            d[c] += 1
#    return d
#
#def reverse_lookup(d,v):
#    r = []
#    for k in d:
#        if d[k] == v:
#            r.append(k)
#    return r
#
#h = histogram('banan')
#print h
#k = reverse_lookup(h,2)
#
#print k


known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

print fibonacci(9)

def ackermann(m,n):
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1,1)
    return ackermann(m-1,ackermann(m,n-1))

print ackermann(3,4)

#def ackermann(m, n):
#    if m == 0:
#        return n+1
#    if n == 0:
#        return ackermann(m-1, 1)
#    return ackermann(m-1, ackermann(m, n-1))
#
#print ackermann(3, 4)