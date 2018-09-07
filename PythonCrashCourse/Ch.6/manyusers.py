#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:26:35 2018

@author: aleksandradooley
"""

#try it yourself pg 115
BooBoo = {'name': 'BooBoo', 'owner': 'Natasha Dooley', 'animal': 'dog', 'breed': 'labradoodle', 'age': 6}
Tommy = {'name': 'Tommy', ' owner': 'Austin Jones-Madix', 'animal': 'snake', 'breed': 'ball-python', 'age': 4}
Maeve = {'name': 'Maeve', 'owner': 'Brian Dooley', 'animal': 'dog', 'breed': 'airedale terrier', 'age': 3}
Geo = {'name': 'Geo', 'owner': 'Adam Screnci', 'animal': 'dog', 'breed': 'mutt', 'age': 3} 

pets = [BooBoo, Tommy, Maeve, Geo]

#only problem how to call the name of the list to print it before all of the information stored in each dictionary
#attempted below but what happened
for pet in pets:
    print pet
    
#Not sure yet how to print this in an organized fashion    
"""    
for pet in pets:
    name = pet['name'] 
    owner = pet['owner']
    species = pet['animal']
    breed = pet['breed']
    age = str(pet['age'])
    
    print "\tName: " + name
    print "\tOwner Name: " + owner
    print "\tAnimal: " + species
    print "\tBreed: " + breed
    print "\tAge: " + age
    """
    
    