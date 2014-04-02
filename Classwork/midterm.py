# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 13:32:19 2014

@author: sophie
"""

def sum_of_squares(N):
    res = []
    i = 0
    while i <= N:
        res.append(i**2)
        i = i + 2
    return sum(res)

print sum_of_squares(5)

def pair_list_to_dictionary(listvalues):
    mydict = {}
    i = 0
    while i <= len(listvalues):      
        if i+1 < len(listvalues):
            key = listvalues[i]
            mydict[key] = listvalues[i+1]
        i += 2
    return mydict
    
print pair_list_to_dictionary(['hello','a','test','b'])

def split_dictionary(inputdictionary):
    upperdict = {}
    lowerdict = {}
    i = 0
    while i <= len(inputdictionary):
        for k in inputdictionary:
            if k.islower():
                lowerdict[k] = inputdictionary[k]
            else:
                upperdict[k] = inputdictionary[k]
        i += 1
    dictreturn = [upperdict, lowerdict]
    return dictreturn

print split_dictionary({'a':2, 'B':'hello', 'c':'t'})

#def in_language(string):
#    i = 0
#    counter_a = 0
#    counter_b = 0
#    while i+1 <= len(string):
#        if 'a' in string[i] and string[i+1]:
#            counter_a += 1
#        else:
#            if 'b' in string[-i] and string[-i-1]:
#                counter_b += 1
#        i += 1
#    print counter_a
#    print counter_b
#    if counter_a == counter_b:
#        return True
#    else:
#        return False
#        
#        
def in_language2(string):
    i = 0
    counter_a = 0
    counter_b = 0
    string_backwards = string[::-1]
        
    while i+2 <= len(string):
        if 'a' in string[i] and string[i+1]:
            counter_a += 1
        if 'b' in string_backwards[i] and string[i+1]:
            counter_b += 1
        i += 1
        
    print counter_a
    print counter_b
    if counter_a == counter_b:
        return True
    else:
        return False

print in_language2('')


class DNASequence:
    def __init__(self, nucleotides):
        self.nucleotides = nucleotides
    
    def get_reverse_complement(self):
        string = list(self.nucleotides)
        index = 0
        reverse = []
        while index < len(string):
            N = string[index]
            if N == 'A':
                reverse.append('T')            
            elif N == 'T':
                reverse.append('A')
            elif N == 'G':
                reverse.append('C')
            elif N == 'C':
                reverse.append('G')
            index += 1
        complement = ''.join(reverse)
        self.reverse_complement = complement[::-1]
    
    def get_proportion_ACGT(self):
        self.proportion = {}
        i = 0
        for k in (self.nucleotides):
            if k in self.proportion:
                self.proportion[k] += 1
            else:
                self.proportion[k] = 1
        values = self.proportion.values()
        length = len(self.nucleotides)
        proportional = [k/length for k in values]
        while i < len(proportional):
            for k in self.proportion:
                self.proportion[k] = proportional[i]
                i += 1
             
       
        return self.proportion
        
    
def get_proportion_ACGT(nucleotides):
    print nucleotides
    proportion = {}
    i = 0
    for k in (nucleotides):
        if k in proportion:
            proportion[k] += 1
        else:
            proportion[k] = 1
    print proportion
    values = proportion.values()
    print values
    length = len(nucleotides)
    proportional = [float(k/length) for k in values]
    print proportional
    while i < len(proportional):
        for k in proportion:
            proportion[k] = proportional[i]
            i += 1
    return proportion

#print get_proportion_ACGT('AATTGCCG')
