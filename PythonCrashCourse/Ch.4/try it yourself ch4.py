#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 15:55:17 2018

@author: aleksandradooley
"""
spc = "\n"

pizzas = ['Hawaiin', 'BBQ chickcen', 'pepperoni']
friend_pizzas = pizzas[:]
for pizza in pizzas:
    print "I like " + pizza + " pizza."
print "I really love pizza!"
pizzas.append('cheese')
print "My favorite pizzas are:"
print pizzas
print spc
print "My friend's favorite pizzas are:"
print friend_pizzas
print spc
for pizza in friend_pizzas:
    print "I love " + pizza + " pizza."
print spc
# 4-2
animals = ['cat', 'dog', 'rabbit']
for animal in animals:
    print "A " + animal + " would make a great pet."
print "Any of these animals would make a great pet!"

#Try it yourself pg 64
numbers = range(1,21)
print numbers
# use a for loop this time
for value in range(1,21):
    print value
#look at how it printed the values. the for loop gives a new number on each new line
#the other one will print a list instead
#for value in range(1,100000000):
#    print value
#you have to be careful doing whats above only because it takes time
numbers = range(1,100000001)
print min(numbers)
print max(numbers)
print sum(numbers)  
print spc
  
odd_numbers = range(1,20,2)
print odd_numbers
print spc
numbers = range(3,31)
for number in numbers:
    print number * 3
print spc
numbers = range(1,11)
for number in numbers:
    print number ** 3
print spc
cubes = [value**3 for value in range(1,11)]
print cubes