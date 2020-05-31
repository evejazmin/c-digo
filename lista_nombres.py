# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:51:54 2020

@author: EstAnthonyFabricioSa
"""

def hola3(mylist):
    for a in mylist:
        print("Hola !", a)
    return mylist
hola3(["Juan", "Carlos", "Pedro"])
hola3(["Juan", "Carlos", "Pedro", "Sandra", "Monica"])
hola3(["Juan"])

print(hola3(["Juan", "Carlos", "Pedro", "Sandra", "Monica"]))