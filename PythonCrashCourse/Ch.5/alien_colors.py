#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 15:36:08 2018

@author: aleksandradooley
"""
#with no statement for other colors, other colors give no output

alien_color = "red"
if alien_color == "green":
    print "You have just earned 5 points."
elif alien_color == "yellow":
    print "You have just earned 10 points."
elif alien_color == "red":
    print "You have just earned 15 points."

#stages of life
age = 12
if age < 2:
    print "This person is a child."
elif age >= 2 and age < 4:
    print "This person is a toddler."
elif age >= 4 and age <13:
    print "This person is a kid."
elif age >=13 and age < 20:
    print "This person is a teenager."
elif age >= 20 and age <65:
    print "This person is an adult."
elif age >= 65:
    print "This person is an elder."
    
# favorite fruit notice how the if statements have to be within a for loop
# this is because it is a list. Just remember that this is how it has to written
    
favorite_fruits = ['apples', 'orange', 'strawberry']
for favorite_fruit in favorite_fruits:
    if favorite_fruit == 'strawberry':
        print "You really like strawberries!"
    if favorite_fruit == 'apples':
        print "You really like apples!"
    if favorite_fruit == 'orange':
        print "You really like oranges!"
    if favorite_fruit == 'bananas':
        print "You really like bananas!"
    if favorite_fruit == 'peach':
        print "You really like peaches!"
