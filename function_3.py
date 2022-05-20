# -*- coding: utf-8 -*-
"""
Created on Fri May 20 20:00:32 2022

@author: user
"""


def calc(w,*args):
    for arg in args:
        w=w*arg
    return w
y=calc(3,4,7,2)
print(y)

def prnPrice(name,**kwargs):
    print(name,kwargs)

prnPrice('物品', 胖胖品安體重=75,口非=10,陶樂比=3460,青蛙水煮麵=852)