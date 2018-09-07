#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 13:57:28 2018

@author: aleksandradooley
"""
spc = "*******************************************"

#pg 47 in crash course
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print cars
#now that they are in alphabetical order the original order cannot be reverted
#below we print in reverse but again this is permanent
cars.sort(reverse=True)
print cars
print spc
# to sort a list temporarily us sorted() 
#also notice the format of  how these statements print
cars = ['bmw', 'audi', 'toyota', 'subaru']
print ("Here is the original list:")
print cars
print ("\nHere is the sorted list:")
print(sorted(cars))
print ("\nHere is the original list again:")
print cars
#now how about just print a list in reverse?
cars = ['bmw', 'audi', 'toyota', 'subaru']
print "\n" 
print cars
print spc
cars.reverse()
print cars
print spc
print len(cars)