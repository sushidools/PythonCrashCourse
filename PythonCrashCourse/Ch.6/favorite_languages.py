#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 13:55:01 2018

@author: aleksandradooley
"""
spc = "\n"

favorite_languages = {
        'jen': ['python', 'ruby'],
        'sarah' : ['c'],
        'edward' : ['ruby', 'go'],
        'phil' : ['python', 'haskell'],
        }
"""
print ("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")
"""
print spc
#for the above the entire print statement must be within parathenses when on multiple lines
for name, languages in favorite_languages.items():
    print "\n" + name.title() + "'s favorite languages are: " 
    for language in languages:
        print "\t" + language.title()

print spc
#here the way to just pull the keys is not needed but its to show that it can be done
#looping through the keys is actually the default behavior
"""
for name in favorite_languages.keys():
    print name.title()
print spc
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print name.title()
    
    if name in friends:
        print "  Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!"
print spc  
if 'erin' not in favorite_languages.keys():
    print "Erin, please take our poll!"
    
for name in sorted(favorite_languages.keys()):
    print name.title() + ", thank you for taking the poll."

print spc
print "The following languages have been mentioned:"
for language in favorite_languages.values():
    print language.title()
    
print spc
#to not get duplicates  do the above this way:
print "The following languages have been mentioned:"
for language in set(favorite_languages.values()):
    print language.title()
    
print spc

need_poll = ['jen', 'pete', 'tilly', 'addison', 'meredith', 'sarah', 'phil']

for names in need_poll:
    if names in favorite_languages.keys():
        print names.title() + " has already done the poll!"
    if names not in favorite_languages.keys():
        print names.title() + ", you still need to do the poll!"

#And finally figured out how to phrase the above without searching
#now both if statements are finished without stopping at a name!
 """        
