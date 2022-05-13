# -*- coding: utf-8 -*-
"""
Created on Fri May 13 19:32:33 2022

@author: user
"""
def add(times):
    a=1
    for z in range(1,times+1):
        a=a*z        
    return a
a=add(10)
print(a)

def multiply (times):
    a=0
    for z in range(1,times+1):
        a=a+z        
    return a
a=multiply (10)
print(a)
        