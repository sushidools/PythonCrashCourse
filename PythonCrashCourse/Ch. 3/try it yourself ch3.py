#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 12:08:08 2018

@author: aleksandradooley
"""

#try it yourself pg 50
spc = "******************************************"
destinations = ["Bali", "Caribbean", "Paris", "Panama", "Mexico"]
print destinations
print sorted(destinations)
print destinations
print spc
#I had to look up how to format this below so be sure to remember this!
print sorted(destinations, reverse=True)
print spc
print destinations
print spc
destinations.reverse()
print destinations
destinations.reverse()
print destinations
print spc
#This is how to use .sort for permanently changing it to alphabetical order
destinations.sort()
print destinations
print spc
destinations.sort(reverse=True)
print destinations
print spc
print spc
print spc
#every function and my own list
dog_breeds = ["french bulldog", "labradoodle", "labrador", "golden retriever", "english bulldog"]
print dog_breeds
print dog_breeds[0]
print dog_breeds[0].title()
print dog_breeds[1]
print dog_breeds[2]
print dog_breeds[-1]
print spc
message = "My favorite breed is the " + dog_breeds[0].title() + "!"
print message
dog_breeds[-1] = 'chinese chin'
print dog_breeds
print spc
dog_breeds.append('boston terrier')
print dog_breeds
print spc
dog_breeds.insert(1, 'airedale terrier')
print dog_breeds
print spc
del dog_breeds[4]
print dog_breeds
print spc
popped_dog_breed = dog_breeds.pop()
print dog_breeds
print popped_dog_breed
dog_breeds.remove('labrador')
print dog_breeds
dog_breeds.append('pitbull')
print dog_breeds
print spc
too_cute = 'pitbull'
dog_breeds.remove(too_cute)
print dog_breeds
print "\nA " + too_cute.title() + " is too cute for me."
print spc
dog_breeds.sort()
print dog_breeds
print spc
dog_breeds.sort(reverse=True)
print dog_breeds
print spc
print "Here is the sorted list:"
print sorted(dog_breeds)
print spc
print "Here is the original list:"
print dog_breeds
print spc
dog_breeds.reverse()
print dog_breeds
print len(dog_breeds)
print spc
#avoid index errors by not asking for things that do not exist in a list
#this is an index error
print dog_breeds[4]