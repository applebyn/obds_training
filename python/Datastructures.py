#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 09:36:25 2021
Python data structures 
@author: andreas
"""

shoplist =['apple', 'banana', 'carrot']
items = len(shoplist)
print('these items are')

    
shoplist.append('rice')
print('my list is', shoplist)

shoplist.sort()

# to delete an item in order
del shoplist [1]

# to take a subset of items from a list
my_list = ['n', 'i', 'a', 'm', 'h']
print(my_list[2:5])
# from the start : to the 3rd from the end
print(my_list[:-3])
# from the start to the 2nd item
print(my_list[:2])
#print from 4th tothe end
print(my_list[3:])
# print the whole list
print(my_list[:])

# this should reverse the order
my_list[::-1]

# nesting to make a list of lists
# list can contain different types of variable eg stpring, integer

help(print)

# make a copy by doing a full splice
mylist= shoplist[:]
#this function makes a copy of the direction to the list. not a full memory copy of the file

del mylist[0]
print(mylist)
print(shoplist)

#tupels are a type of list. You can't add or delete elements of a tupels
#dictionaries - think of them like an address book. Also immutable. 

#two ways to make a 'shallow copy' of the dictionary
dict()
ab.copy()

# to copy everything (memory intensive)
deep.copy()

#Strings are objects and sequences
#Strings are sliceable like lists
name = "WIMM"
if name.startswith("W")
    print("starts with")
    
if "M" in name:
    print()

if name.find('IMM')!=-1:
    print('name contains the string')



    