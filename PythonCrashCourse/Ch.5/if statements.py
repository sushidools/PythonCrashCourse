#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 23:23:38 2018

@author: aleksandradooley
"""
#this below is a simple if statement
#if conditional_test:
#    do something
age = 17
if age >= 18:
    print "You are old enough to vote!"
    print "Have you registered to vote yet?"

# if else statements
else:
    print "Sorry, you are too young to vote."
    print "Please register to vote as soon as you turn 18!"
    
# amusementpark pg. 84

age = 12
if age < 4:
    print "Your admission cost is $0."
elif age < 18:
    print "Your admission cost is $5."
else:
    print "Your admission cost is $10."

#another way to do the same thing is below

age = 3
if age <4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print "Your admission cost is $" + str(price) + "."
# the else block is not needed so it can be replaced with the below code
#elif age >= 65:
#   price = 5
