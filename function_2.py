# -*- coding: utf-8 -*-
"""
Created on Fri May 20 18:48:09 2022

@author: user
"""
def zz(a=1,b=1):
    print(f'a={a},b={b}')
zz('品安','好奘')

s=[(3,4),(2,2),(5,4)]
def calc(w,h):
    return w*h,'正方形' if w==h else '長方形'
def calcAll(conta,func):
    for r in conta:
        print(func(r[0],r[1]))
calcAll(s,calc)

