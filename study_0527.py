# -*- coding: utf-8 -*-
"""
Created on Fri May 27 19:51:40 2022

@author: user
"""

x=lambda x:list(range(1,x+1))
def callcAll(val,fuc):
    return fuc(val)
print(callcAll(3,x))

s=[(2,2),(4,7),(8,1),(6,4)]
s1=sorted(s)
s2=(sorted(s, key=lambda e:e[1]))

a=b=c=1
def test(b):
    a=2
    print(a,b,c)
test(3)
print(a,b,c)

z=[1,2,3]
q=[4,5,6]
def test1(a):
    a[0]='aaa'
    q[0]='www'
    z=[7,8,9]
    z[0]='zzzqqq'
    print(a,q)
test1(z)
print(z,q)
    