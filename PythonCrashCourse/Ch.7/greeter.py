#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 16:29:10 2018

@author: aleksandradooley
"""
"""
#greeter.py
name = raw_input("Please enter your name: ")
print "Hello, " + name + "!"
"""
"""
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = raw_input(prompt)
print "\nHello, " + name + "!"


#using int() to accept numerical input
age = raw_input("How old are you? ")
print age >= 18
#this is different than what the book asks for 
# to do what the book wants I think it needs to be done in a terminal
"""
"""
age = raw_input("How old are you? ")
print int(age)
print age >= 18
# so from the book it had to be edited so that it would print to the console.
"""

height = raw_input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print "\nYou're tall enough to ride!"
else:
    print "\nYou'll be able to ride when you're a little older."
#must be exactly as it is in the chapter
#height has to be set equal to the int(height)
    