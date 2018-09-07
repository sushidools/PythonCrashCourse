#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 19:52:11 2018

@author: aleksandradooley
"""
spc = "\n"
#tuples
dimensions = (200,50)
print dimensions[0]
print dimensions[1]
#dimensions[0] = 250
#so above values cannot be changed in tuples
for dimension in dimensions:
    print dimension
#another way to print values in a tuple is to loop through the values in the tuple
#to modify a tuple you have to completely write over it
print "Original dimensions:"
for dimension in dimensions:
    print dimension
print spc
dimensions = (400,100)
print "Modified dimensions:"
for dimension in dimensions:
    print dimension
    
#try it yourself buffet
buffet = ('chicken', 'steak', 'beans', 'rice', 'pineapple')
for food in buffet:
    print buffet
# this can't be done > buffet[0] = 'pork'
buffet = ('chicken', 'steak', 'apples', 'arugula', 'pineapple')
print "We now have these foods at our buffet:"
for food in buffet:
    print food
    