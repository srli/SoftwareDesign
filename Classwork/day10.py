# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:32:00 2014

@author: sophie
"""
import re
#def flatten(L):
#    """ Converts a list of lists to a list by concatenating all elements of the list """  
#    M = []
#    for n in range(len(L)):
#        if type(L[n]) != list:
#            M.append(L[n])
#        else:
#            print flatten(L[n])
#            M = M + flatten(L[n])
#    return M
#                        
#print flatten([1,2,[3,4],5])
f = open('mary.txt','r')
re.findall("[a-z]",mary.txt)
fulltext = f.read()
fulltext = re.findall("[a-z]",mary.txt)
def get_words_from_book(text):
    res = []
#    print text
    i = 0
    while i < len(text):
        if text[i] == '':
            i += 1
        else:
            res.append(text[i])
            i += 1
    return res

print get_words_from_book(fulltext)
    
f.close()