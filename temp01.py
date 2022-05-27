# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#dict1={'a':1,'b':2,'c':3}
#dict2={'d':4,'e':5,'f':6}

#dict1.update(dict2)

#dict3={**dict1,**dict2}

def prnPrice(name,**kwargs):
    print(f'{name}',kwargs)

def prnPrice01(name,colo1,colo2,colo3):
    print(f'{name}',colo1,colo2,colo3)
    
prnPrice('watame', red=3,green=4)
dict4={'red':3,'green':4,'bule':8}
prnPrice('wdwdwd',**dict4 )
prnPrice01('8787',*dict4 )
