# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:23:25 2020

@author: DELL1
"""


#1 milla americana = 1609.344 metros;
#1 galón americano = 3.785411784 litros.

def l100kmtompg(liters):
    mpg=(100000*3.785411784)/(liters*1609.344)
    return mpg

def mpgtol100km(miles):
    l100km=(100*3.785411784)/(miles*1.609344)
    return l100km
 
print(l100kmtompg(3.9))

print(l100kmtompg(7.5))

print(l100kmtompg(10.))

print(mpgtol100km(60.3))

print(mpgtol100km(31.4))

print(mpgtol100km(23.5))