#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 13:34:19 2021

@author: andreas
"""
# Lesson 2: Python Functions 25th January 2021

def say_hello():
    #code block belonging to the function
    print('hello world')
    
#call the function
say_hello()

# functions allow you to divide your task into bitesize pieces
# allows you to reuse code
# code is more readable (easier to spot errors)

def print_max(a, b ):
    if a > b:
        print (a, "is greater")
    elif a == b:
        print (a, 'is equal to', b)
    else:
        print(a, "is lesser")
        
#call the function
print_max(13, 14)

#Returning data from a function
# ie: use the function to do maths

def maximum(x, y):
    if x > y:
        return x
        print (x, "is maximum")
    elif x == y:
        return'the numbers are equal'
        print (x, 'is equal to', y)
    else:
        return y
        print(y, "is maximum")
        
maximum(22, 17)

#Biological example

#find the complementary DNA strand

def complementary_base(base):
    output = None
    if base == 'A':
        output == 'T'
    elif base == 'G':
        output == 'C'
    elif base == 'C':
        output == 'G'   
    elif base == 'T':
        output == 'A'
    else:
        print ('unknown base')
    return output()

sequence = 'AACA'
complement = ''

for base in sequence:
    complement += complement_base(base)   
complementary_base(sequence)

# Variable Scope

# what's a module?
# python file containing a set of functions with a common theme
# module do not contain the *main* function

