#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 16:31:49 2018

@author: aleksandradooley
"""

#Hello admin
#try it yourself ch.5
#for the if statement that checks if the list is empty> ask dad or look up on stackoverflow
#on line 15 look at what I changed it to do
#Not sure why this can't print the way I want it to
usernames = ['sasha', 'austin', 'admin']
if len(usernames) == 0:
    print "We need to find some users!"
for username in usernames:
    if username:
        if username == 'admin':
            print "Hello admin, would you like to see a status report?"
        else:
            print "Hello " + username.title() + ", thank you for logging in again."

        
name = "JOHN"
print name.title()

#need to finish pg. 93
#ordinal numbers
numbers = range(1,10)
for number in numbers:
    if number == 1:
        print "1st"
    elif number == 2:
        print "2nd"
    elif number == 3:
        print "3rd"
    else:
        print str(number) + "th"
        