#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 15:46:30 2018

@author: aleksandradooley
"""

#cities
cities = {
        'colorado springs': {'state': 'colorado', 'country': 'United States of America'},
        'san francisco': {'state': 'california', 'country': 'USA'},
        'yekaturinburg': {'state': 'not applicable', 'country': 'Russia'},
        }
for city, info in cities.items():
    print city.title() + ": "
    for k, v in info.items():
        print v.title()
#lol damn.....
        