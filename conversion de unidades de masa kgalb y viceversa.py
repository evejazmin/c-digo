# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:50:22 2020

@author: DELL1
"""


#conversion de unidades de masa kg a libras y viceversa
#1 kg es 2.20462262 libras
#1 libra es 1/2.20462262 kg

def kg_a_lb(kg):
    lb=kg*2.20462262 
    return lb

def lb_a_kg(lb):
    kg=lb*0.45259
    #kg=lb/2.20462262 
    return kg

def menu():
    print('1. pasar kg a lbs')
    print('2. pasar lbs a kg')
    opcion=input('-->')
    return opcion

op=menu()
if op=='1':
    kgs=float(input('ingrese kg'))
    conversion=kg_a_lb(kgs)
    print('son',conversion,'libras')
elif op=='2':
    lbs=float(input('ingrese libras'))
    conversion=lb_a_kg(lbs)
    print('son',conversion,'kilogramos')