# -*- coding: utf-8 -*-
"""
Created on Fri May 13 19:32:33 2022

@author: user
"""
def add(times):
    a=0
    for z in x:
        a=a+z        
    return a


def multiply (times):
    a=1
    for z in x:
        a=a*z        
    return a

def calcAll(value,func):
    return func(value)

x=[2,4,5,8,7]
funcs=[add,multiply]
for f in funcs:
    print(calcAll(x,f))