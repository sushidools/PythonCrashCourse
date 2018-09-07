#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 16:25:56 2018

@author: aleksandradooley
"""

#making numerical lists
for value in range(1,5):
    print value
# to print through number 5 the range must be 6
for value in range(1,6):
    print value
#using range() to make a list of numbers
number = list(range(1,6))
print number
#to make a list of even numbers
even_numbers = list(range(2,11))
print even_numbers
#what about square numbers
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print squares
#min and max
digits = [1,2,3,4,5,6,7,8,9,0]
print min(digits)
print max(digits)
print sum(digits)
