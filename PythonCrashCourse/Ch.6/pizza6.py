#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:04:39 2018

@author: aleksandradooley
"""
spc = "\n"
# Store information about a pizza being ordered.
pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese'],
        }
#Sumarize the order.
print "You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings: "

for topping in pizza['toppings']:
    print " \t" + topping