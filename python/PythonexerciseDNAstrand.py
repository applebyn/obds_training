#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:12:15 2021
Find the complementary DNA strand
@author: andreas
"""

#find the complementary DNA strand

def complementarynucleotide(nucleotide):
    #input is nucleotide A, T, C or G
    #output is nucleotide A, T, C or G
    output = None
    #can get rid of this print(nucleotide)
    if nucleotide == 'A':
        output ='T'
    elif nucleotide == 'T':
        output = 'A'
    elif nucleotide == 'G':
        output = 'C'
    elif nucleotide == 'C':
        output = 'G'
    #if the nucleotide is undetermined, the screen prints N
    else:
        output = "N"
    # this print is not needed for now print(output)
    return output


nucleotide= 'ATGHCCT'
complementarynucleotide(nucleotide)

# this is expecting an individual nucleotide, not a sequence


# to do a sequence
sequence = 'ATGCCT'
print(sequence)
def complementaryDNAstrand(strand):
    #input is a strand of nucleotides A, T, C or G
    #output is the complementary strand of nucleotides A, T, C or G
    #output = None
    # print the input strand
    # take out the input print(strand)
    # create a complementary strand
    complementarystrand = ""
    # use a "for" loop to recycle the earlier function 
    for n in strand:
        # make a new variable for the complementary nucleotide
         x = complementarynucleotide(n)
         # if I take out this print(x)
         complementarystrand = complementarystrand + x
    print(complementarystrand)
    #put the return indented to the left of the return() 
    #to allow the function to run through multiple loops
    return (complementarystrand)

complementaryDNAstrand(sequence)


# if I want to put this output somewhere
complementary_strand = complementaryDNAstrand(sequence)
print(complementary_strand)

# write a script to return the reverse complement of a user supplied sequence
complementary_strand = complementaryDNAstrand(sequence)
# this will be a string variable
# how do you reverse a string on python? this is the key question

#google says
#txt = "hello"[::-1]
#print(txt)

#reverse_strand = complementary_strand[::-1]
#print(reverse_strand)   

# do it as a new function
def reversestring (string):
    return string[::-1]
print(reversestring ('abcde'))

print(reversestring (complementary_strand))
