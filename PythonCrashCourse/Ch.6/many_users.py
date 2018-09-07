#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:18:00 2018

@author: aleksandradooley
"""
spc = "\n"
"""
#many_users pg 113
#how about a dictionary within a dictionary

users = {
        'aeinstein': {
                'first': 'albert',
                'last': 'einstein',
                'location': 'princeton',
                },
        'mcurie': {
                'first': 'marie',
                'last': 'curie',
                'location': 'paris',
                },
        }
        
    
for username, user_info in users.items():
    print "\nUsername: " + username
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    print "\tFullname: " + full_name.title()
    print "\tLocation: " + location.title()
"""

people = {
        'ajmx': {
                'first': 'Austin',
                'last': 'Jones-Madix',
                'age': 25,
                'location': 'Colorado Springs',
                },
        'ayd': {
                'first': 'Aleksandra',
                'last': 'Dooley',
                'age': 23,
                'location': 'Colorado Springs',
                },
        'nvd': {
                'first': 'Nina',
                'last': 'Dooley',
                'age': 16,
                'location': 'Larkspur'
                },
        'cbd': {
                'first': 'Camilla',
                'last': 'Dooley',
                'age': 19,
                'location': 'Larkspur'
                },
                }

for username, user_info in people.items():
    print "\nUsername: " + username
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    age = str(user_info['age'])
    
    print "\tFullname: " + full_name.title()
    print "\tLocation: " + location.title()
    print "\tAge: " + age