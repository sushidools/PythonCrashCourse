#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:35:28 2018

@author: aleksandradooley
"""

message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

mesage = "Hello Python Crash Course reader!"
print(mesage)

message = "This should be fun, 'is what she said'"
print message

first_name = 'ada'
last_name = 'lovelace'
#concatenation below
full_name = first_name + ' ' + last_name
print(full_name)
#notice that the \t created a space before the print
message = "\tHello, " + full_name.title() + "!"
print(message)

#So below notice that each \n adds a new line to the string
print("Languages:\nPython\nC\nJavaScript")

favorite_language = 'python '
print(favorite_language)
#rstrip() gets ride of any whitespace at the right end of the string
print(favorite_language.rstrip())
#to store the string as permanently without the white space you must store it back into the variable
favorite_language = favorite_language.rstrip()
#to get rid of white space to the left of the string you use .lstrip()
#to get rid of all the white space on both sides at once you use .strip()