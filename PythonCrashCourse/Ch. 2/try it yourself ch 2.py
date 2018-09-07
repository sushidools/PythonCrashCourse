#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 12:58:18 2018

@author: aleksandradooley
"""
spc = "**********************"
dinner_list = ['David Bowie', 'Prince', 'Deadpool']
message = "Hi " + dinner_list[0] + ", I would like to invite you to dinner at my humble home!"
print message
message = "Hi " + dinner_list[1] + ", I would like to invite you to dinner at my humble home!"
print message
message = "Hi " + dinner_list[2] + ", I would like to invite you to dinner at my humble home!"
print message
print spc
#changing the guest list 3.5
print dinner_list.pop(2) + ", I am sorry you cannot make it."
dinner_list.append("Brian Dooley")
print "Here is the new guest list: " + str(dinner_list)
print spc
#more guests 3.6
print "I found a bigger table!"
dinner_list.insert(0, "Austin Jones-Madix")
print dinner_list
print spc
dinner_list.insert(2, "Nina Dooley")
print dinner_list
print spc
dinner_list.append("Natasha Dooley")
print dinner_list
print spc
message = "Hi " + dinner_list[0] + ", I would like to invite you to dinner at my humble home!"
print message
message = "Hi " + dinner_list[1] + ", I would like to invite you to dinner at my humble home!"
print message
message = "Hi " + dinner_list[2] + ", I would like to invite you to dinner at my humble home!"
print message
message = "Hi " + dinner_list[3] + ", I would like to invite you to dinner at my humble home!"
print message
message = "Hi " + dinner_list[4] + ", I would like to invite you to dinner at my humble home!"
print message
message = "Hi " + dinner_list[-1] + ", I would like to invite you to dinner at my humble home!"
print message
print spc
print "I am sorry to say I can now only have two guests."
print dinner_list.pop(-1) + ", I appologize for any inconvenience, but I will no longer be able to have you for dinner."
print dinner_list.pop(-1) + ", I appologize for any inconvenience, but I will no longer be able to have you for dinner."
print dinner_list.pop(-1) + ", I appologize for any inconvenience, but I will no longer be able to have you for dinner."
print dinner_list.pop(-1) + ", I appologize for any inconvenience, but I will no longer be able to have you for dinner."
print spc
print dinner_list[0] + ", you are still invited to have dinner with me at my home. Hope you can make it!"
print dinner_list[-1] + ", you are still invited to have dinner with me at my home. Hope you can make it!"
print spc
del dinner_list[0]
del dinner_list[0]
print dinner_list
print "I am inviting " +  str(len(dinner_list)) + " people to dinner."
