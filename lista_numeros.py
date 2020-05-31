# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:57:15 2020

@author: EstAnthonyFabricioSa
"""

def createlist(n):
    mylist=[]
    for i in range(1,n+1,3):
        mylist.append(i)
    return mylist
print(createlist(100))
