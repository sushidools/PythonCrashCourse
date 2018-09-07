#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 15:38:09 2018

@author: aleksandradooley
"""

spc = "*********************\n"

#chapter 3
#introducing lists
# square brackets indicate a list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# below papa gave an example of a for loop and bikes as an iterator
#the point of using bikes is that the iterator could be anything
#all the iterator really means is for items in list: do whatever the loop says
for bikes in bicycles:
    print bikes
#this below prints a certain item from the list by using the indeces
    # index starts at 0
print(bicycles[0])
print spc
#below this prints the same as above except capitalized
print(bicycles[0].title())
print spc
#to print the last item in a list
print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title() + "."
print message