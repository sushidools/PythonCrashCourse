#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 18:43:10 2018

@author: aleksandradooley
"""
spc = "\n"
#this is how to use slicing of lists
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print spc
print players[1:4]
print spc
print players[:4]
print spc
print players[2:]
#notice where it slices the list
#the first number slices before as well as the second
print spc
print players[-3:]
print spc
print "Here are the first three players on my team:"
for player in players[:3]:
    print player.title()
    
print spc
