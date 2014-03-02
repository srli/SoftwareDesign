# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 15:37:08 2014

@author: sophie
"""
import re

E = [(1,2), (3,4), (5,6)]

def sentiment_average(source_sentiment):
    positivity_total = 0
    subjectivity_total = 0
    i = 0
    while i < len(source_sentiment):
        print i
        positivity_total = positivity_total + source_sentiment[i][0]
        subjectivity_total = subjectivity_total + source_sentiment[i][1]
        i += 1
    sentiment_average = [positivity_total/len(source_sentiment), subjectivity_total/len(source_sentiment)]
    return sentiment_average

print sentiment_average(E)

#str = 'hello /u45/u87/390 how are you'
#words = re.findall('[\w\.-]+',str)
#print words
#str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
#tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
#print tuples  ## [('alice', 'google.com'), ('bob', 'abc.com')]
#for tuple in tuples:
#    print tuple[0]  ## username
#    print tuple[1]  ## host


#A = ['hat','dog','bear','piano','sun']
#B = ['bunny','dogs']
#
#C = set(A) ^ set(B)
#D = list(C)
#print type(C)
#print type(D)
#print C
#print D
#
#def collapse(L):
#    """ Converts a list of strings to a string by concatenating all elements of the list """
#    
#    output = ""
#    for s in L:
#        output = output + ' ' + s
#    return output
#    
#print collapse(D)
#C = 'Today I had cake'
#words = C.split(' ')
#print words
#
#
#print len(A)
#def list_test():
#    bad_words = ['Sophie Li','wall']
#    D = ['Happy holidays from us to you', 'Sophie Li likes chocolate a lot', 'She also thinks homework sucks', 'this is on her wall']
#    E = []
#    i = 0
#    j = 0
#    while i < len(D):
#        print i
#        while j < len(bad_words):
#            if D[i] in bad_words[j]:
#                print j
#                j += 1
#            elif j == len(bad_words) - 1:
#                print j
#                E.append(D[i])
#                break
##                j = len(bad_words) + 1
#        i += 1
#        print i
#    print E
#
#list_test()