# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 11:09:31 2014

@author: sophie
"""
from amino_acids import aa, codons


#mylist = range(0,21)

#values = dict(zip(mylist, codons))
codonlookup = dict(zip(aa, codons))
#print codonlookup
def reverse_codonlookup(d , v):
    for k in d:
        if v in d[k]:
            return k
    raise ValueError

print reverse_codonlookup(codonlookup,'TGG')

#index = 0
#while index < len(dna):
#    codon = dna[index:index+3]
#    if codon == codons[1]:
#        print aa[1]
#    elif codon == codons[2]:
#        print aa[2]
#    else:
#        print 'J'
#    index = index + 3

#
def testcoding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    index = 0
    while index < len(dna):
        codon = dna[index + 2]
        for k in codonlookup:
            if codon in codonlookup[k]:
                return k
        index = index + 3

print testcoding_strand_to_AA('TGGGAA')


#def histogram(s):
#    d = dict()
#    for c in s:
#        if c not in d:
#            d[c] = 1
#        else:
#            d[c] += 1
#    return d
#
#h = histogram('hello')
#print h

