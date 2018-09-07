#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 15:26:01 2018

@author: aleksandradooley
"""

#toppings ch.5
requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']
if 'mushrooms' in requested_toppings:
    print "Adding mushrooms."
if 'pepperoni' in requested_toppings:
    print "Adding pepperoni."
if 'extra cheese' in requested_toppings:
    print "Adding extra cheese."

print "\nFinished making your pizza!"
# if elif had been used it would only notice the first
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print "Sorry, we are out of green peppers right now."
    else:
        print "Adding " + requested_topping + "."
print "\nFinished making your pizza!"
# how about check if a list is empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print "Adding " + requested_topping + "."
    print"\nFinished making your pizza!"
else:
    print "\nAre you sure you want a plain pizza?"

# what about working with multiple lists?
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
                      'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print "Adding " + requested_topping + "."
    else:
        print "Sorry, we don't have " + requested_topping + "."
print "\nFinished making your pizza."

