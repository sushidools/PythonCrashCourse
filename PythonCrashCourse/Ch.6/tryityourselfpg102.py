#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 13:16:26 2018

@author: aleksandradooley
"""

"""
This starts on page 102
"""
#SO! COME BACK TO THIS TO REWRITE. You aren't learning if you don't make a few mistakes to learn from.
spc = "\n"
person = {
       'first_name': 'Austin',
       'last_name': 'Jones-Madix',
       'age': '25',
       'city': 'Colorado Springs',
        }

for p in person.items():
    full_name = p['first'] + " " + p['last']
    location = p['city']
    age = str(p['age'])
    
    print "\tFullname: " + full_name.title()
    print "\tLocation: " + location.title()
    print "\tAge: " + age
print spc
favorite_numbers = {
        'Austin':'79',
        'Nina': '13',
        'Natasha': '9',
        }
print favorite_numbers
"""
glossary = {
        'print': 'This prints whatever is after to the console.',
        'for': 'This gives you a way to loop through a list or dictionary.',
        'key': 'This is part of the key-value pairs in a dictionary.',
        'value': 'This is the other part of the key-value pairs in a dictionary.',
        }
print "Print: \n" + glossary['print']
print "For: \n" + glossary['for']
print "Key: \n" + glossary['key']
print "Value: \n" + glossary['value']
"""
#now on page. 108 they ask to have glossary edited
glossary = {
        'print': 'This prints whatever is after to the console.',
        'for': 'This gives you a way to loop through a list or dictionary.',
        'key': 'This is part of the key-value pairs in a dictionary.',
        'value': 'This is the other part of the key-value pairs in a dictionary.',
        }
for x in glossary:
    print x, glossary[x]
#so above is how to print the key-value pairs
print spc
rivers = {
        'nile' : 'Egypt',
        'colorado' : 'USA',
        'russian' : 'california',
        }
for key, value in rivers.items():
    print "The " + key + " river runs through " + value + "."

print rivers.keys()
print rivers.values()


