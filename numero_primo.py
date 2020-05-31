# -*- coding: utf-8 -*-
"""
Created on Mon May 11 18:56:55 2020

@author: DELL1
"""


def isPrime(num):
    for i in range (2,num):
        if num%i==0:
            return False
    return True

for i in range(1, 20):
                if isPrime(i+1):
                   print(i+1, end=" ")
print()