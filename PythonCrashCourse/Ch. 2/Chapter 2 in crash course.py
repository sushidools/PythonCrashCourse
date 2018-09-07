#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:08:05 2018

@author: aleksandradooley
"""

message = "One of Python's strengths is its diverse community."
print message


#message = 'Once of Python's strengths is its diverse community.'
# you can see why the above would give an error

#Try it yourself pg 29
bff_name = 'Austin'
print "Hello "  + bff_name + ", would you like to learn some Python today?"
print bff_name.upper()
print bff_name.lower()
print 'Perks of Being a Wallflower, "We accept the love we think we deserve."'

movie = "Perks of Being a Wallflower"
message = movie + ', "We accept the love we think we deserve."'
print message

#below this is just an example of stripping white space
name = " Austin  "
print name
print name.strip()
print name.lstrip()
print name.rstrip()

austins_age = 25
#putting a few lessons together below
#how to put make an integer a string
#to do the opposite would be the same
message = "Happy " + str(austins_age) + "th birthday " + name.strip() + "."
print message

# to get integers to print as floats be sure to have at least one with a decimal
# to make the string print with the empty line below it must be formatted as it is on 44
print 3 / 2
print str(3.0 / 2) + "\n"

# math examples below
print "\t" + str(3 + 5)

space = "*********************"

print 4 * 2
print space
print 2 ** 3
print 12 - 4
print 16 / 2

favorite_number = 95
message = "My favorite number is " + str(favorite_number) + "!"
print message


#this contains the Python philosophy
import this
