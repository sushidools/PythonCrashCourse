#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 14:54:43 2018

@author: aleksandradooley
"""
spc = "\n"
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print magician.title()
print spc
#don't forget to indent the second line in a for loop and every line included in the for loop after
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print magician.title() + ", that was a great trick!"
    print "I can't wait to see your next trick, " + magician.title() + ".\n"
print "Thank you, everyone. That was a great magic show!"    
#The indentation above is important to determine how many times a print statement is done!
