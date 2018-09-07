#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 18:55:33 2018

@author: aleksandradooley
"""
spc = "\n"

my_foods = ['pizza', 'falafel', 'carrot cake', 'sushi', 'steak']
#below is the wrong way
#friend_foods = my_foods
#below is the correct way to make one list equal to another
#this way above would put all foods in both lists
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print "My favorite foods are:"
print my_foods
print spc
print "My friend's favorite foods are:"
print friend_foods
print spc
print "The first three items in the list are:"
print my_foods[0:3]
print spc
print "Three items fom the middle of the list:"
print my_foods[1:4]
print spc
print "The last three items in the list are:"
print my_foods[-3:]
print spc
