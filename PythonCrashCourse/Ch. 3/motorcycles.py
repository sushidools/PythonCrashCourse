#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 16:35:58 2018

@author: aleksandradooley
"""

spc = "************************************"

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#below is how you change a value in a list
motorcycles[0] = 'ducati'
print motorcycles
#how to add to a list?
motorcycles.append('ducati')
print motorcycles
#inserting an element into a list
motorcycles.insert(0, 'ducati')
print motorcycles
#notice how it prints because of how items were added to the list
#now to remove an item from the list using delete or del
del motorcycles[0]
print motorcycles
#now to pop one from the list of motorcycles
motorcycles = ['ducati', 'honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print motorcycles
print popped_motorcycle
last_owned = motorcycles.pop()
print("The last motcycle I owned was a " + last_owned.title() + ".")
#if you know you won't use the deleted value again use del 
#if you want to use the value you are removing as you remove it. use .pop()
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print motorcycles
print "\nA " + too_expensive.title() + " is too expensive for me."
