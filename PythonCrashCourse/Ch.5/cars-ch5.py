#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 20:53:01 2018

@author: aleksandradooley
"""

#ch.5
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print car.upper()
    else:
        print car.title()
#tested these in terminal under python
car = 'audi'
car == 'bmw'

car = 'bmw'
car == 'bmw'

car = 'audi'
car == 'Audi'

car = 'Audi'
car.lower() == 'audi'

car = 'Audi'
car.lower() == 'audi'

car

age = 18
age == 18

answer = 17
if answer != 42:
    print "That is not the correct answer. Please try again!"

age = 19
age < 21

age <= 21

age > 21

age >= 21

age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21

requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
'pepperoni' in requested_toppings

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print user.title() + ", you can post a response if you wish."
    
#All of this above was run in the terminal
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print "Hold the anchovies"
    
#Below are some boolean expressions    
game_active = True
can_edit  = False
